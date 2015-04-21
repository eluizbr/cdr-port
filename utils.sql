# UPDATES

UPDATE nao_portados  SET operadora = 'VIVO' WHERE operadora = 'TELEFONICA';
UPDATE nao_portados  SET tipo = 'MOVEL' WHERE tipo = 'MÓVEL';
UPDATE nao_portados  SET tipo = 'RADIO' WHERE tipo = 'RÁDIO';

###


# Cria %

CREATE VIEW vw_disposition AS
		SELECT id, disposition, count(disposition) AS Total
		FROM cdr_cdr
		GROUP BY disposition ORDER BY Total DESC;


REPLACE INTO cdr_DispositionPercent (disposition, valor, perc)	
	SELECT lista.disposition, total valor , 
	        ((total / total.total_geral) * 100) perc
		FROM
	(
	SELECT disposition, total
		FROM vw_disposition) lista,
	(
	SELECT sum(total) total_geral
		FROM vw_disposition
	) total

####

# Cria Stats

REPLACE INTO cdr_stats_answered (d_total,s_total,m_total)
	SELECT(
		SELECT count(src) FROM cdr_cdr
		WHERE disposition = 'ANSWERED' AND DAY(calldate)=DAY(CURDATE()) AND YEAR(calldate)=YEAR(CURDATE())
		)  AS DIA,
		(
		SELECT count(src) FROM cdr_cdr
		WHERE disposition = 'ANSWERED' AND WEEK(calldate)=WEEK(CURDATE()) AND YEAR(calldate)=YEAR(CURDATE())
		) AS SEMANA,
		(
		SELECT count(src)  FROM cdr_cdr
		WHERE disposition = 'ANSWERED' AND MONTH(calldate)=MONTH(CURDATE()) AND YEAR(calldate)=YEAR(CURDATE())
		)AS MES


REPLACE INTO cdr_stats_noanswer (d_total,s_total,m_total)
	SELECT(
		SELECT count(src) FROM cdr_cdr
		WHERE disposition = 'NO ANSWER' AND DAY(calldate)=DAY(CURDATE()) AND YEAR(calldate)=YEAR(CURDATE())
		)  AS DIA,
		(
		SELECT count(src) FROM cdr_cdr
		WHERE disposition = 'NO ANSWER' AND WEEK(calldate)=WEEK(CURDATE()) AND YEAR(calldate)=YEAR(CURDATE())
		) AS SEMANA,
		(
		SELECT count(src)  FROM cdr_cdr
		WHERE disposition = 'NO ANSWER' AND MONTH(calldate)=MONTH(CURDATE()) AND YEAR(calldate)=YEAR(CURDATE())
		)AS MES


REPLACE INTO cdr_stats_busy (d_total,s_total,m_total)
	SELECT(
		SELECT count(src) FROM cdr_cdr
		WHERE disposition = 'BUSY' AND DAY(calldate)=DAY(CURDATE()) AND YEAR(calldate)=YEAR(CURDATE())
		)  AS DIA,
		(
		SELECT count(src) FROM cdr_cdr
		WHERE disposition = 'BUSY' AND WEEK(calldate)=WEEK(CURDATE()) AND YEAR(calldate)=YEAR(CURDATE())
		) AS SEMANA,
		(
		SELECT count(src)  FROM cdr_cdr
		WHERE disposition = 'BUSY' AND MONTH(calldate)=MONTH(CURDATE()) AND YEAR(calldate)=YEAR(CURDATE())
		)AS MES
###

# Cria STATS By DAY / MONTH

CREATE VIEW vw_day_stats AS 
	SELECT date(calldate) AS dia, MONTH(date(calldate)) AS mes, count(*) AS total 
	FROM cdr_cdr
	WHERE calldate BETWEEN CURDATE() - INTERVAL 6 MONTH AND CURDATE()
	GROUP BY dia ORDER BY dia ASC;

CREATE VIEW vw_month_stats AS
SELECT MONTHNAME(date(calldate)) AS mes, count(*) AS total 
		FROM cdr_cdr
		WHERE disposition = 'ANSWERED'
		GROUP BY mes ORDER BY mes ASC;		

###

# Ultimos 10 numeros atendidos
CREATE VIEW vw_last_10 AS SELECT dst, calldate, SEC_TO_TIME(billsec) AS billsec
	FROM cdr_cdr
	WHERE disposition = 'ANSWERED'
	GROUP BY dst  ORDER BY calldate DESC  LIMIT 8;
###


# TRIGGERS

DELIMITER $$
CREATE TRIGGER tr_stats BEFORE INSERT ON cdr_cdr
		FOR EACH ROW
BEGIN

	REPLACE INTO cdr_DispositionPercent (disposition, valor, perc)	
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

END$$
DELIMITER$$

# TRIGGERS 

CREATE VIEW vw_stats_answered AS 	SELECT(
		SELECT count(src) FROM cdr_cdr
		WHERE disposition = 'ANSWERED' AND DAY(calldate)=DAY(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		)  AS dia,
		(
		SELECT count(src) FROM cdr_cdr
		WHERE disposition = 'ANSWERED' AND WEEK(calldate)=WEEK(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		) AS semana,
		(
		SELECT count(src)  FROM cdr_cdr
		WHERE disposition = 'ANSWERED' AND MONTH(calldate)=MONTH(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		)AS mes;


CREATE VIEW vw_stats_noanswer AS SELECT(
		SELECT count(src) FROM cdr_cdr
		WHERE disposition = 'NO ANSWER' AND DAY(calldate)=DAY(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		)  AS dia,
		(
		SELECT count(src) FROM cdr_cdr
		WHERE disposition = 'NO ANSWER' AND WEEK(calldate)=WEEK(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		) AS semana,
		(
		SELECT count(src)  FROM cdr_cdr
		WHERE disposition = 'NO ANSWER' AND MONTH(calldate)=MONTH(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		)AS mes;

CREATE VIEW vw_stats_busy AS 	SELECT(
		SELECT count(src) FROM cdr_cdr
		WHERE disposition = 'BUSY' AND DAY(calldate)=DAY(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		)  AS dia,
		(
		SELECT count(src) FROM cdr_cdr
		WHERE disposition = 'BUSY' AND WEEK(calldate)=WEEK(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		) AS semana,
		(
		SELECT count(src)  FROM cdr_cdr
		WHERE disposition = 'BUSY' AND MONTH(calldate)=MONTH(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		)AS mes;


SELECT nao_portados.operadora, nao_portados.tipo 
	FROM nao_portados
	WHERE prefixo IN (SELECT SUBSTRING(dst,1,6) AS prefixo
	FROM cdr_cdr
	WHERE disposition = 'ANSWERED')
	GROUP BY prefixo ORDER BY operadora LIMIT 20


CREATE VIEW vw_last_10 AS SELECT dst, calldate 
	FROM cdr_cdr
	WHERE disposition = 'ANSWERED'
	GROUP BY dst  ORDER BY calldate DESC  LIMIT 8;

CREATE VIEW vw_last_10 AS; SELECT dst, operadora, tipo, rn1, calldate, disposition, cidade, estado
	FROM vw_cdr
	WHERE disposition = 'ANSWERED'
	GROUP BY dst  ORDER BY calldate DESC  LIMIT 8;


CREATE VIEW vw_prefix AS 
	SELECT SUBSTRING(dst,1,2) AS ddd,  SUBSTRING(dst,1,6) AS prefixo, dst AS numero, src, disposition,calldate, 
	SEC_TO_TIME(duration) AS duration, SEC_TO_TIME(billsec) AS billsec
	FROM cdr_cdr;

CREATE VIEW vw_prefix AS 
	SELECT id, SUBSTRING(dst,1,2) AS ddd,  SUBSTRING(dst,1,6) AS prefixo, SUBSTRING(dst,7,9) AS sufixo, dst AS numero, src, disposition,calldate, 
	SEC_TO_TIME(duration) AS duration, SEC_TO_TIME(billsec) AS billsec
	FROM cdr_cdr;
		CASE
			WHEN character_length(dst)='10'
				THEN SUBSTRING(dst,7,9)
			WHEN character_length(dst)='11'
				THEN SUBSTRING(dst,8,9)			
		END AS sufixo,
			dst AS numero, src, disposition,calldate, 
			SEC_TO_TIME(duration) AS duration, SEC_TO_TIME(billsec) AS billsec
		FROM cdr_cdr LIMIT 2000;


CREATE VIEW vw_prefixo AS 
	SELECT nao_portados.id, nao_portados.operadora, nao_portados.tipo, nao_portados.rn1,
	vw_prefix.prefixo, vw_prefix.numero, vw_prefix.src, vw_prefix.disposition, vw_prefix.calldate, vw_prefix.duration, vw_prefix.billsec
	FROM nao_portados, vw_prefix
	WHERE nao_portados.prefixo = vw_prefix.prefixo;


CREATE VIEW vw_cdr AS SELECT cdr_cdr.id,calldate,src,dst,SEC_TO_TIME(duration) AS duration, SEC_TO_TIME(billsec) AS billsec,disposition,prefixo.ddd,
		prefixo.prefixo,prefixo.cidade,prefixo.estado,prefixo.operadora,prefixo.tipo, prefixo.rn1, portado 
	FROM cdr_cdr,prefixo
	WHERE cdr_cdr.prefix = prefixo.prefixo ;
		
CREATE VIEW vw_operadoras AS SELECT id, operadora, count(operadora) AS total 
	FROM vw_cdr
	GROUP BY operadora ORDER BY total DESC;


### Views para CDR

CREATE VIEW vw_ramais AS SELECT id, src AS ramais, count(src) AS total FROM cdr_cdr 
		WHERE disposition = 'ANSWERED' AND MONTH(calldate)=MONTH(CURDATE()) AND YEAR(calldate)=YEAR(CURDATE())
		GROUP BY src ORDER BY total DESC;


CREATE VIEW vw_cidades AS SELECT id, cidade, count(cidade) AS total 
	FROM vw_cdr
	GROUP BY cidade ORDER BY cidade ASC;

CREATE VIEW vw_estados AS SELECT id, estado, count(estado) AS total 
	FROM vw_cdr
	GROUP BY estado ORDER BY estado ASC;

### FIM Views para CDR

### Gera difernca entre meses

SELECT
  @total1:= COUNT( IF( MONTH( calldate ) = MONTH( CURDATE() ), 1, NULL ) ) AS atual,
  @total2:= COUNT( IF( MONTH( calldate ) = MONTH( CURRENT_DATE - INTERVAL 1 MONTH ), 1, NULL ) ) AS anterior,
  ( @total1 - @total2 ) / @total1 * 100 AS percentual
FROM cdr_cdr
WHERE
  disposition = 'ANSWERED'
  AND (
    MONTH( calldate ) = MONTH( CURDATE() )
    OR
    MONTH( calldate ) = MONTH( CURRENT_DATE - INTERVAL 1 MONTH )
  )

 ### FIM Gera difernca entre meses

### Cria tabelas cidades
REPLACE INTO cidades (cidade,estado,ddd,regiao)
SELECT city.cidade, state.letter AS estado ,city.iso_ddd AS ddd, region.title AS regiao
	FROM city, state, region
	WHERE city.id_state = state.id AND state.id_region = region.id
	ORDER BY cidade;
###

### Cira PREFIXOS
	#FIXO

INSERT INTO prefixo (ddd,prefixo,inicial,final,cidade,estado, operadora, tipo, rn1)
SELECT DISTINCT fixo.Codigo_Nacional AS ddd, CONCAT(fixo.Codigo_Nacional,fixo.prefixo) AS prefixo, fixo.FaixaInicial, fixo.FaixaFinal, NomedaLocalidade AS cidade, cidades.estado, nao_portados.operadora, nao_portados.tipo, nao_portados.rn1
	FROM fixo, cidades, nao_portados
	WHERE cidades.cidade = fixo.NomedaLocalidade 
	AND fixo.Codigo_Nacional = cidades.ddd
	AND nao_portados.prefixo = CONCAT(fixo.Codigo_Nacional,fixo.prefixo);
	
	#MOVEL



INSERT INTO prefixo (ddd,prefixo,inicial,final,cidade,estado, operadora, tipo, rn1)
	SELECT DISTINCT movel.Codigo_Nacional AS ddd, CONCAT(movel.Codigo_Nacional,movel.prefixo) AS prefixo, movel.FaixaInicial, movel.FaixaFinal, NomedaLocalidade AS cidade, cidades.estado, nao_portados.operadora, nao_portados.tipo, nao_portados.rn1
	FROM movel, cidades, nao_portados
	WHERE movel.Codigo_Nacional = cidades.ddd
	AND nao_portados.prefixo = CONCAT(movel.Codigo_Nacional,movel.prefixo);


###

### VIEW CDR OK
	SELECT nao_portados.id, nao_portados.operadora, nao_portados.tipo, nao_portados.rn1, prefixo.cidade, prefixo.estado,
			vw_prefix.ddd, vw_prefix.prefixo, vw_prefix.numero, vw_prefix.src, vw_prefix.disposition, vw_prefix.calldate, 
			vw_prefix.duration, vw_prefix.billsec
		FROM nao_portados, vw_prefix, prefixo
		WHERE nao_portados.prefixo = vw_prefix.prefixo 
		AND prefixo.prefixo = nao_portados.prefixo
		LIMIT 100;
###


SELECT id, src, MIN(billsec) AS min, MAX(billsec) AS max, COUNT(src) AS chamdas, SEC_TO_TIME(SUM(billsec)) As tempo_total, 
	SEC_TO_TIME(AVG(billsec)) As tempo_medio
	FROM vw_cdr
	WHERE disposition = 'ANSWERED' AND calldate BETWEEN ('2015-04-16T00:00:00') AND ('2015-04-17T23:59:59')
	GROUP BY src ORDER BY min;
	
### Update localidade MOVEL
UPDATE movel
	SET    NomedaLocalidade = 'MOVEL';
###

 
SELECT
@prefixo:= (SELECT SUBSTRING(dst,1,6) FROM cdr_cdr LIMIT 1) AS prefixo,
@ddd:= (SELECT SUBSTRING(prefixo,1,2) FROM nao_portados WHERE prefixo = @prefixo) AS ddd,
@cidade:= (SELECT  concat(NomedaLocalidade) FROM Anatel where concat(Codigo_Nacional,'',Prefixo)  = @prefixo LIMIT 1) As cidade,
@estado:= (SELECT state.letter FROM state INNER JOIN city ON (city.id_state = state.id) AND (city.iso_ddd = @ddd)  WHERE cidade = @cidade) AS estado;

SELECT 
	dst, src, calldate, disposition, duration, billsec,
@prefixo:= (SELECT SUBSTRING(dst,1,6)) AS prefixo,
@ddd:= (SELECT ddd FROM prefixo WHERE prefixo = @prefixo) AS ddd,
@cidade:= (SELECT cidade FROM prefixo WHERE prefixo = @prefixo) As cidade,
@estado:= (SELECT estado FROM prefixo WHERE prefixo = @prefixo) As estado,
@tipo:= (SELECT operadora FROM prefixo WHERE prefixo = @prefixo) As operadora,
@tipo:= (SELECT tipo FROM prefixo WHERE prefixo = @prefixo) As tipo

FROM cdr_cdr
ORDER BY dst LIMIT 100;

INSERT INTO cdrport (dst,src,calldate,disposition,duration,billsec,prefixo,ddd,cidade,estado,operadora,tipo);
SELECT dst, src, calldate, disposition, SEC_TO_TIME(duration) AS duration, SEC_TO_TIME(billsec) AS billsec,
@prefixo:= (SELECT SUBSTRING(dst,1,6)) AS prefixo,
@ddd:= (SELECT ddd FROM prefixo WHERE prefixo = @prefixo) AS ddd,
@cidade:= (SELECT cidade FROM prefixo WHERE prefixo = @prefixo) As cidade,
@estado:= (SELECT estado FROM prefixo WHERE prefixo = @prefixo) As estado,
@tipo:= (SELECT operadora FROM prefixo WHERE prefixo = @prefixo) As operadora,
@tipo:= (SELECT tipo FROM prefixo WHERE prefixo = @prefixo) As tipo
FROM cdr_cdr
ORDER BY dst LIMIT 50;

	CREATE TABLE `cdrport` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `dst` bigint(20) DEFAULT NULL,
  `src` bigint(11) DEFAULT NULL,
  `calldate` datetime DEFAULT NULL,
  `disposition` varchar(20) DEFAULT NULL,
  `duration` time DEFAULT NULL,
  `billsec` time DEFAULT NULL,
  `prefixo` int(8) DEFAULT NULL,
  `ddd` int(2) DEFAULT NULL,
  `cidade` varchar(50) DEFAULT NULL,
  `estado` varchar(2) DEFAULT NULL,
  `operadora` varchar(50) DEFAULT NULL,
  `tipo` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `cdrport` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `calldate` datetime DEFAULT NULL,
  `src` int(20) DEFAULT NULL,
  `dst` bigint(20) DEFAULT NULL,
  `duration` time DEFAULT NULL,
  `billsec` time DEFAULT NULL,
  `disposition` varchar(20) DEFAULT NULL,
  `ddd` int(2) DEFAULT NULL,
  `prefixo` int(8) DEFAULT NULL,
  `cidade` varchar(50) DEFAULT NULL,
  `estado` varchar(2) DEFAULT NULL,
  `tipo` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


	SELECT nao_portados.id, nao_portados.operadora, nao_portados.tipo, nao_portados.rn1,
	vw_prefix.ddd, vw_prefix.prefixo, vw_prefix.numero, vw_prefix.src, vw_prefix.disposition, vw_prefix.calldate, vw_prefix.duration, 
	vw_prefix.billsec, city.cidade
	FROM nao_portados, vw_prefix, city, state
	WHERE nao_portados.prefixo = vw_prefix.prefixo 
	AND state.id = city.cidade
	AND vw_prefix.prefixo = 373274 
	LIMIT 10;

CREATE VIEW vw_cdr_new AS 	SELECT nao_portados.id, nao_portados.operadora, nao_portados.tipo, nao_portados.rn1, prefixo.cidade, prefixo.estado,
			vw_prefix.ddd, vw_prefix.prefixo, vw_prefix.numero, vw_prefix.src, vw_prefix.disposition, vw_prefix.calldate, 
			vw_prefix.duration, vw_prefix.billsec
		FROM nao_portados, vw_prefix, prefixo
		WHERE nao_portados.prefixo = vw_prefix.prefixo;

SELECT prefixo.id, prefixo.operadora, prefixo.tipo, prefixo.rn1, prefixo.cidade, prefixo.estado,
			vw_prefix.ddd, vw_prefix.prefixo, vw_prefix.numero, vw_prefix.src, vw_prefix.disposition, vw_prefix.calldate, 
			vw_prefix.duration, vw_prefix.billsec
		FROM prefixo, vw_prefix
		WHERE prefixo.prefixo = vw_prefix.prefixo;

	CREATE VIEW vw_cdr AS SELECT cdr_cdr.id,calldate,src,dst,SEC_TO_TIME(duration) AS duration, SEC_TO_TIME(billsec) AS billsec,disposition,prefixo.ddd,
		prefixo.prefixo,prefixo.cidade,prefixo.estado,prefixo.operadora,prefixo.tipo, prefixo.rn1, portado 
	FROM cdr_cdr,prefixo
	WHERE cdr_cdr.prefix = prefixo.prefixo ;
	

CREATE VIEW vw_prefix AS 
	SELECT id, SUBSTRING(dst,1,2) AS ddd,
		CASE
			WHEN character_length(dst)='10'
				THEN SUBSTRING(dst,1,6)
			WHEN character_length(dst)='11'
				THEN SUBSTRING(dst,1,7)
			WHEN character_length(dst)<'9'
				THEN dst	
		END AS prefixo,
	dst AS numero, src, disposition,calldate, 
	SEC_TO_TIME(duration) AS duration, SEC_TO_TIME(billsec) AS billsec
		FROM cdr_cdr;
		LIMIT 2000;


SELECT cdr_cdr.calldate, cdr_cdr.src, cdr_cdr.dst, cdr_cdr.duration, cdr_cdr.billsec, cdr_cdr.disposition, cdr_cdr.uniqueid,
			prefixo.ddd, prefixo.prefixo, prefixo.cidade, prefixo.estado, prefixo.operadora, prefixo.tipo
	FROM cdr_cdr, prefixo
	WHERE prefixo.prefixo = (SELECT SUBSTRING(cdr_cdr.dst,1,6))
	
	LIMIT 100;

INSERT INTO cdr_cdr_new(id,calldate,clid,src,dst,dcontext,channel,dstchannel,lastapp,lastdata,duration,billsec,disposition,amaflags,accountcode,uniqueid,userfield,prefix) 
SELECT 
	*,
@prefixo:= (SELECT SUBSTRING(dst,1,6)) AS prefix
FROM cdr_cdr
ORDER BY dst LIMIT 10;

UPDATE cdr_cdr SET prefix = 
		CASE
			WHEN dst LIKE '%s-%'
				THEN src
			WHEN character_length(dst)='10'
				THEN SUBSTRING(dst,1,6)
			WHEN character_length(dst)='11'
				THEN SUBSTRING(dst,1,7)
			WHEN character_length(dst)<'9'
				THEN src
		END;
		
UPDATE cdr_cdr SET sufix = 
		CASE
			WHEN dst LIKE '%s-%'
				THEN src
			WHEN character_length(dst)='10'
				THEN SUBSTRING(dst,7,9)
			WHEN character_length(dst)='11'
				THEN SUBSTRING(dst,8,9)
			WHEN character_length(dst)<'9'
				THEN src
		END;
	
DELIMITER $$
CREATE TRIGGER tr_cdr BEFORE INSERT ON cdr_cdr
		FOR EACH ROW
BEGIN

UPDATE cdr_cdr SET prefix = 
		CASE
			WHEN dst LIKE '%s-%'
				THEN src
			WHEN character_length(dst)='10'
				THEN SUBSTRING(dst,1,6)
			WHEN character_length(dst)='11'
				THEN SUBSTRING(dst,1,7)
			WHEN character_length(dst)<'9'
				THEN src
		END;
		
END$$
DELIMITER$$


DELIMITER $$
CREATE TRIGGER tr_cdr BEFORE INSERT ON cdr_cdr
		FOR EACH ROW
BEGIN
		INSERT INTO cdr_cdr_new(id,calldate,clid,src,dst,dcontext,channel,dstchannel,lastapp,lastdata,duration,billsec,disposition,amaflags,accountcode,uniqueid,userfield,prefix) 
		SELECT 
			*,
		@prefixo:= (SELECT SUBSTRING(dst,1,6)) AS prefix
		FROM cdr_cdr
		ORDER BY dst;
		
END$$
DELIMITER$$


#### UPDATE CRON
SHOW PROCESSLIST;
SET GLOBAL event_scheduler = OFF;

DELIMITER $$		
CREATE EVENT atualiza_base
ON SCHEDULE EVERY 1 MINUTE
ON COMPLETION PRESERVE
DO BEGIN
	UPDATE cdr_cdr SET prefix = 
		CASE
			WHEN dst LIKE '%s-%'
				THEN src
			WHEN dst LIKE '%-%'
				THEN src
			WHEN character_length(dst)='10'
				THEN SUBSTRING(dst,1,6)
			WHEN character_length(dst)='11'
				THEN SUBSTRING(dst,1,7)
			WHEN character_length(dst)<'9'
				THEN src
		END;

END $$
DELIMITER ;
###

### UODATE portados

UPDATE cdr_cdr
	INNER JOIN portados
		ON cdr_cdr.dst = portados.numero
	SET portado = 
		CASE
			WHEN cdr_cdr.dst = portados.numero
				THEN 'Sim'
		END;

###

INSERT INTO cdrport (calldate,src,dst,duration,billsec,disposition,ddd,prefixo,cidade,estado,operadora,tipo)
SELECT calldate,src,dst,SEC_TO_TIME(duration) AS duration, SEC_TO_TIME(billsec) AS billsec,disposition,prefixo.ddd,prefixo.prefixo,prefixo.cidade,prefixo.estado,prefixo.operadora,prefixo.tipo  
	FROM cdr_cdr,prefixo
	WHERE cdr_cdr.prefix = prefixo.prefixo ;

INSERT INTO cdrport (calldate,src,dst,duration,billsec,disposition,ddd,prefixo,cidade,estado,operadora,tipo)
SELECT calldate,src,dst,SEC_TO_TIME(duration) AS duration, SEC_TO_TIME(billsec) AS billsec,disposition,prefixo.ddd,prefixo.prefixo,prefixo.cidade,prefixo.estado,prefixo.operadora,prefixo.tipo  
	FROM cdr_cdr,prefixo
	WHERE cdr_cdr.prefix = prefixo.prefixo AND prefixo.tipo = 'fixo';
	
	LIMIT 50;



