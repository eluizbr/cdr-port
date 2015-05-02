### INICIO VIEWS

CREATE VIEW vw_disposition AS
		SELECT id, disposition, count(disposition) AS Total
		FROM cdr_cdrport
		GROUP BY disposition ORDER BY Total DESC;


CREATE VIEW vw_day_stats AS 
	SELECT date(calldate) AS dia, MONTH(date(calldate)) AS mes, count(*) AS total 
	FROM cdr_cdrport
	WHERE calldate BETWEEN CURDATE() - INTERVAL 6 MONTH AND CURDATE()
	GROUP BY dia ORDER BY dia ASC;


CREATE VIEW vw_last_10 AS SELECT dst, operadora, tipo, rn1, calldate, disposition, cidade, estado, portado
	FROM vw_cdr
	WHERE disposition = 'ANSWERED'
	ORDER BY calldate DESC  LIMIT 8;

CREATE VIEW vw_operadoras AS SELECT id, operadora, count(operadora) AS total 
	FROM vw_cdr
	GROUP BY operadora ORDER BY total DESC;

CREATE VIEW vw_ramais AS SELECT id, src AS ramais, count(src) AS total FROM cdr_cdrport 
		WHERE disposition = 'ANSWERED' AND MONTH(calldate)=MONTH(CURDATE()) AND YEAR(calldate)=YEAR(CURDATE())
		GROUP BY src ORDER BY total DESC;

CREATE VIEW vw_cidades AS SELECT id, cidade, count(cidade) AS total 
	FROM vw_cdr
	GROUP BY cidade ORDER BY cidade ASC;

CREATE VIEW vw_estados AS SELECT id, estado, count(estado) AS total 
	FROM vw_cdr
	GROUP BY estado ORDER BY estado ASC;

CREATE VIEW vw_month_stats AS
SELECT MONTHNAME(date(calldate)) AS mes, count(*) AS total 
		FROM cdr_cdrport
		WHERE disposition = 'ANSWERED'
		GROUP BY mes ORDER BY mes ASC;	

CREATE VIEW vw_stats_answered AS 	SELECT(
		SELECT count(src) FROM cdr_cdrport
		WHERE disposition = 'ANSWERED' AND DAY(calldate)=DAY(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		)  AS dia,
		(
		SELECT count(src) FROM cdr_cdrport
		WHERE disposition = 'ANSWERED' AND WEEK(calldate)=WEEK(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		) AS semana,
		(
		SELECT count(src)  FROM cdr_cdrport
		WHERE disposition = 'ANSWERED' AND MONTH(calldate)=MONTH(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		)AS mes;


CREATE VIEW vw_stats_noanswer AS SELECT(
		SELECT count(src) FROM cdr_cdrport
		WHERE disposition = 'NO ANSWER' AND DAY(calldate)=DAY(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		)  AS dia,
		(
		SELECT count(src) FROM cdr_cdrport
		WHERE disposition = 'NO ANSWER' AND WEEK(calldate)=WEEK(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		) AS semana,
		(
		SELECT count(src)  FROM cdr_cdrport
		WHERE disposition = 'NO ANSWER' AND MONTH(calldate)=MONTH(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		)AS mes;

CREATE VIEW vw_stats_busy AS 	SELECT(
		SELECT count(src) FROM cdr_cdrport
		WHERE disposition = 'BUSY' AND DAY(calldate)=DAY(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		)  AS dia,
		(
		SELECT count(src) FROM cdr_cdrport
		WHERE disposition = 'BUSY' AND WEEK(calldate)=WEEK(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		) AS semana,
		(
		SELECT count(src)  FROM cdr_cdrport
		WHERE disposition = 'BUSY' AND MONTH(calldate)=MONTH(CURDATE()) AND MONTH(calldate)=MONTH(CURDATE())  AND YEAR(calldate)=YEAR(CURDATE())
		)AS mes;

CREATE VIEW vw_cdr AS
SELECT cdr_cdrport.id,calldate,src,dst, duration,billsec,disposition,cdr_prefixo.ddd,
		cdr_prefixo.prefixo,cdr_prefixo.cidade,cdr_prefixo.estado,cdr_cdrport.operadora_id AS operadora,cdr_prefixo.tipo, cdr_cdrport.rn1_id AS rn1, portado,
		CASE
			WHEN cdr_cdrport.tipo = 'FIXO' AND cdr_cdrport.cidade = cdr_prefixo.cidade AND cdr_cdrport.estado = cdr_config_local.estado_id
					THEN FORMAT(cdr_cdrport.billsec*cdr_config_local.custo_local/60, 3)
			WHEN cdr_cdrport.tipo = 'MOVEL' AND cdr_cdrport.cidade = cdr_prefixo.cidade AND cdr_cdrport.estado = cdr_config_local.estado_id
					THEN FORMAT(cdr_cdrport.billsec*cdr_config_local.custo_movel_local/60, 3)
			WHEN cdr_cdrport.tipo = 'FIXO'
					THEN FORMAT(cdr_cdrport.billsec*cdr_config_local.custo_ldn/60, 3)
			WHEN cdr_cdrport.tipo = 'MOVEL'
					THEN FORMAT(cdr_cdrport.billsec*cdr_config_local.custo_ldn/60, 3)
			WHEN cdr_cdrport.tipo = 'FIXON'
					THEN FORMAT(cdr_cdrport.billsec*0, 3)
			WHEN cdr_cdrport.tipo = 'RAMAL'
					THEN FORMAT(cdr_cdrport.billsec*0, 3)
			ELSE FORMAT(cdr_cdrport.billsec*cdr_config_local.custo_movel_ldn/60, 3)
		END AS preco, userfield	 
	FROM cdr_cdrport, cdr_prefixo, cdr_config_local
	WHERE cdr_cdrport.prefixo = cdr_prefixo.prefixo;



### FIM VIEWS