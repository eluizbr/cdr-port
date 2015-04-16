# UPDATES

UPDATE nao_portados  SET operadora = 'VIVO' WHERE operadora = 'TELEFONICA';
UPDATE nao_portados  SET tipo = 'MOVEL' WHERE tipo = 'MÓVEL';
UPDATE nao_portados  SET tipo = 'RADIO' WHERE tipo = 'RÁDIO';

###


# Cria %

CREATE VIEW vw_disposition AS
		SELECT disposition, count(disposition) AS Total
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

CREATE VIEW vw_last_10 AS SELECT numero, operadora, tipo, rn1, calldate, disposition
	FROM vw_prefixo
	WHERE disposition = 'ANSWERED'
	GROUP BY numero  ORDER BY calldate DESC  LIMIT 8;


CREATE VIEW vw_prefix AS SELECT SUBSTRING(dst,1,6) AS prefixo, dst AS numero, disposition,calldate
	FROM cdr_cdr;

CREATE VIEW vw_prefixo AS SELECT nao_portados.id, nao_portados.operadora, nao_portados.tipo, nao_portados.rn1,
	vw_prefix.prefixo, vw_prefix.numero, vw_prefix.disposition, vw_prefix.calldate, vw_prefix.billsec
	FROM nao_portados, vw_prefix
	WHERE nao_portados.prefixo = vw_prefix.prefixo;
	
	
CREATE VIEW vw_operadoras AS SELECT operadora, count(operadora) AS total 
	FROM vw_prefixo
	GROUP BY operadora ORDER BY total DESC;


### Views para CDR

CREATE VIEW vw_ramais AS SELECT id, src AS ramais, count(src) AS total FROM cdr_cdr 
		WHERE disposition = 'ANSWERED' AND MONTH(calldate)=MONTH(CURDATE()) AND YEAR(calldate)=YEAR(CURDATE())
		GROUP BY src ORDER BY total DESC;

### FIM Views para CDR
