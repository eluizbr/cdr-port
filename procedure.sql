DELIMITER ;;

CREATE TRIGGER tr_stats AFTER INSERT ON cdr_cdr
		FOR EACH ROW
BEGIN

DROP TEMPORARY TABLE IF EXISTS TMP_cdr_cdr;

CREATE TEMPORARY TABLE `TMP_cdr_cdr` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `calldate` datetime NOT NULL,
  `clid` varchar(80) NOT NULL,
  `src` varchar(80) NOT NULL,
  `dst` varchar(80) NOT NULL,
  `dcontext` varchar(80) NOT NULL,
  `channel` varchar(80) NOT NULL,
  `dstchannel` varchar(80) NOT NULL,
  `lastapp` varchar(80) NOT NULL,
  `lastdata` varchar(80) NOT NULL,
  `duration` int(11) NOT NULL,
  `billsec` int(11) NOT NULL,
  `disposition` varchar(45) NOT NULL,
  `amaflags` int(11) NOT NULL,
  `accountcode` varchar(20) NOT NULL,
  `uniqueid` varchar(32) NOT NULL,
  `userfield` varchar(255) NOT NULL,
  `prefix` varchar(80) DEFAULT NULL,
  `portado` varchar(3) DEFAULT 'Nao',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;

INSERT INTO TMP_cdr_cdr (calldate,clid,src,dst,dcontext,channel,dstchannel,lastapp,lastdata,duration,billsec,disposition,amaflags,accountcode,uniqueid,userfield,prefix,portado)
SELECT calldate,clid,src,
		CASE
			WHEN character_length(dst)='10'
			THEN dst
			WHEN character_length(dst)='11'
			THEN dst
			WHEN character_length(dst)='9'
			THEN dst
			WHEN character_length(dst)='8'
			THEN dst
			WHEN character_length(dst)='11'
				THEN SUBSTRING(dst,cdr_config_local.cortar+1)
			WHEN character_length(dst)='12'
				THEN SUBSTRING(dst,cdr_config_local.cortar+1)
		END AS dst,
dcontext,channel,dstchannel,lastapp,lastdata,duration,billsec,disposition,amaflags,accountcode,uniqueid,userfield,prefix,portado
FROM cdr_config_local,cdr_cdr;

SET @cortar:=(SELECT cortar FROM cdr_config_local);
SET @ddd:=(SELECT ddd FROM cdr_config_local);
	UPDATE TMP_cdr_cdr SET prefix = 
		CASE
			WHEN dst LIKE '%s-%'
				THEN src
			WHEN dst LIKE '%-%'
				THEN src
			WHEN dst LIKE '0800%'
				THEN SUBSTRING(dst,@cortar,4)
			WHEN dst LIKE '300%'
				THEN SUBSTRING(dst,@cortar,4)
			WHEN dst LIKE '4004%'
				THEN SUBSTRING(dst,@cortar,4)
			WHEN character_length(dst)='11'
				THEN SUBSTRING(dst,@cortar,7)
			WHEN character_length(dst)='10'
				THEN SUBSTRING(dst,@cortar,6)
			WHEN character_length(dst)='9'
				THEN CONCAT(@ddd,SUBSTRING(dst,1,5))
			WHEN character_length(dst)='8'
				THEN CONCAT(@ddd,SUBSTRING(dst,1,4))
			WHEN character_length(dst)<'7'
				THEN src
		END;

UPDATE TMP_cdr_cdr
	INNER JOIN portados
		ON TMP_cdr_cdr.dst = portados.numero
	SET portado = 
		CASE
			WHEN TMP_cdr_cdr.dst = portados.numero
				THEN 'Sim'
		END;

UPDATE TMP_cdr_cdr SET dst = 
	CASE
		WHEN character_length(dst)='8'
			THEN CONCAT(@ddd,SUBSTRING(dst,1))  
	END
	WHERE  character_length(dst)='8';

UPDATE TMP_cdr_cdr SET dst = 
	CASE
		WHEN character_length(dst)='9'
			THEN CONCAT(@ddd,SUBSTRING(dst,1))  
	END
	WHERE  character_length(dst)='9';

INSERT INTO cdr_cdrport (calldate,src,dst,duration,billsec,disposition,ddd,prefixo,cidade,estado,operadora_id,tipo,rn1_id,portado,uniqueid,userfield)
SELECT calldate,src,dst,SEC_TO_TIME(duration) AS duration, SEC_TO_TIME(billsec) AS billsec,disposition,cdr_prefixo.ddd,
		cdr_prefixo.prefixo,cdr_prefixo.cidade,cdr_prefixo.estado,cdr_prefixo.operadora,cdr_prefixo.tipo, cdr_prefixo.rn1, portado, uniqueid,userfield 
	FROM TMP_cdr_cdr,cdr_prefixo
	WHERE TMP_cdr_cdr.prefix = cdr_prefixo.prefixo
	ON DUPLICATE KEY UPDATE uniqueid = cdr_cdrport.uniqueid;

UPDATE cdr_cdrport rt, 
				(SELECT numero, rn1
				FROM portados, cdr_cdrport 
				WHERE portados.numero = cdr_cdrport.dst
				) rs
				SET
				rt.rn1_id = rs.rn1
				WHERE rt.dst = rs.numero;


UPDATE cdr_cdrport rt,
				(select operadora,rn1_id
				FROM cdr_cdrport,cdr_prefixo
				WHERE cdr_prefixo.rn1 = cdr_cdrport.rn1_id
				AND cdr_cdrport.portado = 'Sim'
				GROUP BY cdr_prefixo.rn1) rs
				SET 
				rt.operadora_id = rs.operadora
				WHERE rt.rn1_id = rs.rn1_id;		

REPLACE INTO cdr_dispositionpercent (disposition, valor, perc)	
	SELECT lista.disposition, total valor , 
	        ((total / total.total_geral) * 100) perc
		FROM
		(
		SELECT disposition, total
			FROM vw_disposition) lista,
		(
		SELECT sum(total) total_geral
			FROM vw_disposition
		) total;

END;;
DELIMITER ;