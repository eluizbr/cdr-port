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

# Cria STATS By DAY

CREATE VIEW vw_day_stats AS 
	SELECT DAY(date(calldate)) AS dia, MONTH(date(calldate)) AS mes, count(*) AS total 
	FROM cdr_cdr
	WHERE disposition = 'ANSWERED'
	GROUP BY dia ORDER BY dia ASC;

		

###

