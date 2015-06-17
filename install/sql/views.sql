# ************************************************************
# Sequel Pro SQL dump
# Version 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: localhost (MySQL 5.6.23)
# Database: cdrport
# Generation Time: 2015-06-17 15:53:06 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table nao_portados
# ------------------------------------------------------------

DROP VIEW IF EXISTS `nao_portados`;

CREATE TABLE `nao_portados` (
   `id` INT(10) NOT NULL DEFAULT '0',
   `operadora` VARCHAR(64) NOT NULL,
   `tipo` VARCHAR(64) NOT NULL,
   `prefixo` BIGINT(7) NOT NULL,
   `rn1` INT(64) NOT NULL
) ENGINE=MyISAM;



# Dump of table portados
# ------------------------------------------------------------

DROP VIEW IF EXISTS `portados`;

CREATE TABLE `portados` (
   `numero` BIGINT(11) NOT NULL,
   `rn1` INT(11) NOT NULL,
   `data_hora` DATETIME NOT NULL,
   `op` INT(11) NOT NULL
) ENGINE=MyISAM;



# Dump of table vw_cdr
# ------------------------------------------------------------

DROP VIEW IF EXISTS `vw_cdr`;

CREATE TABLE `vw_cdr` (
   `id` INT(11) NOT NULL DEFAULT '0',
   `calldate` DATETIME NULL DEFAULT NULL,
   `src` BIGINT(20) NULL DEFAULT NULL,
   `dst` BIGINT(20) NULL DEFAULT NULL,
   `duration` TIME NULL DEFAULT NULL,
   `billsec` TIME NULL DEFAULT NULL,
   `disposition` VARCHAR(20) NOT NULL,
   `ddd` INT(11) NULL DEFAULT NULL,
   `prefixo` INT(11) NULL DEFAULT NULL,
   `cidade` VARCHAR(100) NOT NULL,
   `estado` VARCHAR(2) NOT NULL,
   `operadora` VARCHAR(50) NOT NULL,
   `tipo` VARCHAR(20) NOT NULL DEFAULT '',
   `rn1` INT(11) NULL DEFAULT NULL,
   `portado` VARCHAR(5) NOT NULL,
   `preco` VARCHAR(63) NULL DEFAULT NULL,
   `userfield` VARCHAR(255) NULL DEFAULT NULL
) ENGINE=MyISAM;



# Dump of table vw_cidades
# ------------------------------------------------------------

DROP VIEW IF EXISTS `vw_cidades`;

CREATE TABLE `vw_cidades` (
   `id` INT(11) NOT NULL DEFAULT '0',
   `cidade` VARCHAR(100) NOT NULL,
   `total` BIGINT(21) NOT NULL DEFAULT '0'
) ENGINE=MyISAM;



# Dump of table vw_day_stats
# ------------------------------------------------------------

DROP VIEW IF EXISTS `vw_day_stats`;

CREATE TABLE `vw_day_stats` (
   `dia` DATE NULL DEFAULT NULL,
   `mes` INT(2) NULL DEFAULT NULL,
   `total` BIGINT(21) NOT NULL DEFAULT '0'
) ENGINE=MyISAM;



# Dump of table vw_disposition
# ------------------------------------------------------------

DROP VIEW IF EXISTS `vw_disposition`;

CREATE TABLE `vw_disposition` (
   `id` INT(11) NOT NULL DEFAULT '0',
   `disposition` VARCHAR(20) NOT NULL,
   `Total` BIGINT(21) NOT NULL DEFAULT '0'
) ENGINE=MyISAM;



# Dump of table vw_estados
# ------------------------------------------------------------

DROP VIEW IF EXISTS `vw_estados`;

CREATE TABLE `vw_estados` (
   `id` INT(11) NOT NULL DEFAULT '0',
   `estado` VARCHAR(2) NOT NULL,
   `total` BIGINT(21) NOT NULL DEFAULT '0'
) ENGINE=MyISAM;



# Dump of table vw_last_10
# ------------------------------------------------------------

DROP VIEW IF EXISTS `vw_last_10`;

CREATE TABLE `vw_last_10` (
   `dst` BIGINT(20) NULL DEFAULT NULL,
   `operadora` VARCHAR(50) NOT NULL,
   `tipo` VARCHAR(20) NOT NULL DEFAULT '',
   `rn1` INT(11) NULL DEFAULT NULL,
   `calldate` DATETIME NULL DEFAULT NULL,
   `disposition` VARCHAR(20) NOT NULL,
   `cidade` VARCHAR(100) NOT NULL,
   `estado` VARCHAR(2) NOT NULL,
   `portado` VARCHAR(5) NOT NULL
) ENGINE=MyISAM;



# Dump of table vw_month_stats
# ------------------------------------------------------------

DROP VIEW IF EXISTS `vw_month_stats`;

CREATE TABLE `vw_month_stats` (
   `mes` VARCHAR(9) NULL DEFAULT NULL,
   `total` BIGINT(21) NOT NULL DEFAULT '0'
) ENGINE=MyISAM;



# Dump of table vw_operadoras
# ------------------------------------------------------------

DROP VIEW IF EXISTS `vw_operadoras`;

CREATE TABLE `vw_operadoras` (
   `id` INT(11) NOT NULL DEFAULT '0',
   `operadora` VARCHAR(50) NOT NULL,
   `tipo` VARCHAR(20) NOT NULL DEFAULT '',
   `total` BIGINT(21) NOT NULL DEFAULT '0'
) ENGINE=MyISAM;



# Dump of table vw_ramais
# ------------------------------------------------------------

DROP VIEW IF EXISTS `vw_ramais`;

CREATE TABLE `vw_ramais` (
   `id` INT(11) NOT NULL DEFAULT '0',
   `ramais` BIGINT(20) NULL DEFAULT NULL,
   `total` BIGINT(21) NOT NULL DEFAULT '0'
) ENGINE=MyISAM;



# Dump of table vw_stats_answered
# ------------------------------------------------------------

DROP VIEW IF EXISTS `vw_stats_answered`;

CREATE TABLE `vw_stats_answered` (
   `dia` BIGINT(21) NULL DEFAULT NULL,
   `semana` BIGINT(21) NULL DEFAULT NULL,
   `mes` BIGINT(21) NULL DEFAULT NULL
) ENGINE=MyISAM;



# Dump of table vw_stats_busy
# ------------------------------------------------------------

DROP VIEW IF EXISTS `vw_stats_busy`;

CREATE TABLE `vw_stats_busy` (
   `dia` BIGINT(21) NULL DEFAULT NULL,
   `semana` BIGINT(21) NULL DEFAULT NULL,
   `mes` BIGINT(21) NULL DEFAULT NULL
) ENGINE=MyISAM;



# Dump of table vw_stats_noanswer
# ------------------------------------------------------------

DROP VIEW IF EXISTS `vw_stats_noanswer`;

CREATE TABLE `vw_stats_noanswer` (
   `dia` BIGINT(21) NULL DEFAULT NULL,
   `semana` BIGINT(21) NULL DEFAULT NULL,
   `mes` BIGINT(21) NULL DEFAULT NULL
) ENGINE=MyISAM;





# Replace placeholder table for vw_stats_noanswer with correct view syntax
# ------------------------------------------------------------

DROP TABLE `vw_stats_noanswer`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_stats_noanswer`
AS SELECT
   (select count(`cdr_cdrport`.`src`)
FROM `cdr_cdrport` where ((`cdr_cdrport`.`disposition` = 'NO ANSWER') and (dayofmonth(`cdr_cdrport`.`calldate`) = dayofmonth(curdate())) and (month(`cdr_cdrport`.`calldate`) = month(curdate())) and (year(`cdr_cdrport`.`calldate`) = year(curdate())))) AS `dia`,(select count(`cdr_cdrport`.`src`) from `cdr_cdrport` where ((`cdr_cdrport`.`disposition` = 'NO ANSWER') and (week(`cdr_cdrport`.`calldate`,0) = week(curdate(),0)) and (month(`cdr_cdrport`.`calldate`) = month(curdate())) and (year(`cdr_cdrport`.`calldate`) = year(curdate())))) AS `semana`,(select count(`cdr_cdrport`.`src`) from `cdr_cdrport` where ((`cdr_cdrport`.`disposition` = 'NO ANSWER') and (month(`cdr_cdrport`.`calldate`) = month(curdate())) and (month(`cdr_cdrport`.`calldate`) = month(curdate())) and (year(`cdr_cdrport`.`calldate`) = year(curdate())))) AS `mes`;


# Replace placeholder table for vw_last_10 with correct view syntax
# ------------------------------------------------------------

DROP TABLE `vw_last_10`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_last_10`
AS SELECT
   `vw_cdr`.`dst` AS `dst`,
   `vw_cdr`.`operadora` AS `operadora`,
   `vw_cdr`.`tipo` AS `tipo`,
   `vw_cdr`.`rn1` AS `rn1`,
   `vw_cdr`.`calldate` AS `calldate`,
   `vw_cdr`.`disposition` AS `disposition`,
   `vw_cdr`.`cidade` AS `cidade`,
   `vw_cdr`.`estado` AS `estado`,
   `vw_cdr`.`portado` AS `portado`
FROM `vw_cdr` where (`vw_cdr`.`disposition` = 'ANSWERED') order by `vw_cdr`.`calldate` desc limit 8;


# Replace placeholder table for nao_portados with correct view syntax
# ------------------------------------------------------------

DROP TABLE `nao_portados`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `nao_portados`
AS SELECT
   `portabilidade`.`nao_portados`.`id` AS `id`,
   `portabilidade`.`nao_portados`.`operadora` AS `operadora`,
   `portabilidade`.`nao_portados`.`tipo` AS `tipo`,
   `portabilidade`.`nao_portados`.`prefixo` AS `prefixo`,
   `portabilidade`.`nao_portados`.`rn1` AS `rn1`
FROM `portabilidade`.`nao_portados`;


# Replace placeholder table for vw_ramais with correct view syntax
# ------------------------------------------------------------

DROP TABLE `vw_ramais`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_ramais`
AS SELECT
   `cdr_cdrport`.`id` AS `id`,
   `cdr_cdrport`.`src` AS `ramais`,count(`cdr_cdrport`.`src`) AS `total`
FROM `cdr_cdrport` where ((`cdr_cdrport`.`disposition` = 'ANSWERED') and (month(`cdr_cdrport`.`calldate`) = month(curdate())) and (year(`cdr_cdrport`.`calldate`) = year(curdate()))) group by `cdr_cdrport`.`src` order by `total` desc;


# Replace placeholder table for vw_month_stats with correct view syntax
# ------------------------------------------------------------

DROP TABLE `vw_month_stats`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_month_stats`
AS SELECT
   monthname(cast(`cdr_cdrport`.`calldate` as date)) AS `mes`,count(0) AS `total`
FROM `cdr_cdrport` where (`cdr_cdrport`.`disposition` = 'ANSWERED') group by `mes` order by `mes`;


# Replace placeholder table for vw_stats_answered with correct view syntax
# ------------------------------------------------------------

DROP TABLE `vw_stats_answered`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_stats_answered`
AS SELECT
   (select count(`cdr_cdrport`.`src`)
FROM `cdr_cdrport` where ((`cdr_cdrport`.`disposition` = 'ANSWERED') and (dayofmonth(`cdr_cdrport`.`calldate`) = dayofmonth(curdate())) and (month(`cdr_cdrport`.`calldate`) = month(curdate())) and (year(`cdr_cdrport`.`calldate`) = year(curdate())))) AS `dia`,(select count(`cdr_cdrport`.`src`) from `cdr_cdrport` where ((`cdr_cdrport`.`disposition` = 'ANSWERED') and (week(`cdr_cdrport`.`calldate`,0) = week(curdate(),0)) and (month(`cdr_cdrport`.`calldate`) = month(curdate())) and (year(`cdr_cdrport`.`calldate`) = year(curdate())))) AS `semana`,(select count(`cdr_cdrport`.`src`) from `cdr_cdrport` where ((`cdr_cdrport`.`disposition` = 'ANSWERED') and (month(`cdr_cdrport`.`calldate`) = month(curdate())) and (month(`cdr_cdrport`.`calldate`) = month(curdate())) and (year(`cdr_cdrport`.`calldate`) = year(curdate())))) AS `mes`;


# Replace placeholder table for vw_day_stats with correct view syntax
# ------------------------------------------------------------

DROP TABLE `vw_day_stats`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_day_stats`
AS SELECT
   cast(`cdr_cdrport`.`calldate` as date) AS `dia`,month(cast(`cdr_cdrport`.`calldate` as date)) AS `mes`,count(0) AS `total`
FROM `cdr_cdrport` where (`cdr_cdrport`.`calldate` between (curdate() - interval 6 month) and curdate()) group by `dia` order by `dia`;


# Replace placeholder table for vw_cdr with correct view syntax
# ------------------------------------------------------------

DROP TABLE `vw_cdr`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_cdr`
AS SELECT
   `cdr_cdrport`.`id` AS `id`,
   `cdr_cdrport`.`calldate` AS `calldate`,
   `cdr_cdrport`.`src` AS `src`,
   `cdr_cdrport`.`dst` AS `dst`,
   `cdr_cdrport`.`duration` AS `duration`,
   `cdr_cdrport`.`billsec` AS `billsec`,
   `cdr_cdrport`.`disposition` AS `disposition`,
   `cdr_prefixo`.`ddd` AS `ddd`,
   `cdr_prefixo`.`prefixo` AS `prefixo`,
   `cdr_prefixo`.`cidade` AS `cidade`,
   `cdr_prefixo`.`estado` AS `estado`,
   `cdr_cdrport`.`operadora_id` AS `operadora`,
   `cdr_prefixo`.`tipo` AS `tipo`,
   `cdr_cdrport`.`rn1_id` AS `rn1`,
   `cdr_cdrport`.`portado` AS `portado`,(case when ((`cdr_cdrport`.`tipo` = 'FIXO') and (`cdr_cdrport`.`cidade` = `cdr_prefixo`.`cidade`) and (`cdr_cdrport`.`estado` = `cdr_config_local`.`estado_id`)) then format(((`cdr_cdrport`.`billsec` * `cdr_config_local`.`custo_local`) / 60),3) when ((`cdr_cdrport`.`tipo` = 'MOVEL') and (`cdr_cdrport`.`cidade` = `cdr_prefixo`.`cidade`) and (`cdr_cdrport`.`estado` = `cdr_config_local`.`estado_id`)) then format(((`cdr_cdrport`.`billsec` * `cdr_config_local`.`custo_movel_local`) / 60),3) when (`cdr_cdrport`.`tipo` = 'FIXO') then format(((`cdr_cdrport`.`billsec` * `cdr_config_local`.`custo_ldn`) / 60),3) when (`cdr_cdrport`.`tipo` = 'MOVEL') then format(((`cdr_cdrport`.`billsec` * `cdr_config_local`.`custo_ldn`) / 60),3) when (`cdr_cdrport`.`tipo` = 'NACIONAL') then format((`cdr_cdrport`.`billsec` * 0),3) when (`cdr_cdrport`.`tipo` = 'RAMAL') then format((`cdr_cdrport`.`billsec` * 0),3) else format(((`cdr_cdrport`.`billsec` * `cdr_config_local`.`custo_movel_ldn`) / 60),3) end) AS `preco`,
   `cdr_cdrport`.`userfield` AS `userfield`
FROM ((`cdr_cdrport` join `cdr_prefixo`) join `cdr_config_local`) where (`cdr_cdrport`.`prefixo` = `cdr_prefixo`.`prefixo`);


# Replace placeholder table for portados with correct view syntax
# ------------------------------------------------------------

DROP TABLE `portados`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `portados`
AS SELECT
   `portabilidade`.`portados`.`numero` AS `numero`,
   `portabilidade`.`portados`.`rn1` AS `rn1`,
   `portabilidade`.`portados`.`data_hora` AS `data_hora`,
   `portabilidade`.`portados`.`op` AS `op`
FROM `portabilidade`.`portados`;


# Replace placeholder table for vw_estados with correct view syntax
# ------------------------------------------------------------

DROP TABLE `vw_estados`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_estados`
AS SELECT
   `vw_cdr`.`id` AS `id`,
   `vw_cdr`.`estado` AS `estado`,count(`vw_cdr`.`estado`) AS `total`
FROM `vw_cdr` group by `vw_cdr`.`estado` order by `vw_cdr`.`estado`;


# Replace placeholder table for vw_disposition with correct view syntax
# ------------------------------------------------------------

DROP TABLE `vw_disposition`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_disposition`
AS SELECT
   `cdr_cdrport`.`id` AS `id`,
   `cdr_cdrport`.`disposition` AS `disposition`,count(`cdr_cdrport`.`disposition`) AS `Total`
FROM `cdr_cdrport` group by `cdr_cdrport`.`disposition` order by `Total` desc;


# Replace placeholder table for vw_operadoras with correct view syntax
# ------------------------------------------------------------

DROP TABLE `vw_operadoras`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_operadoras`
AS SELECT
   `vw_cdr`.`id` AS `id`,
   `vw_cdr`.`operadora` AS `operadora`,
   `vw_cdr`.`tipo` AS `tipo`,count(`vw_cdr`.`operadora`) AS `total`
FROM `vw_cdr` group by `vw_cdr`.`operadora`,`vw_cdr`.`tipo` order by count(`vw_cdr`.`operadora`) desc;


# Replace placeholder table for vw_cidades with correct view syntax
# ------------------------------------------------------------

DROP TABLE `vw_cidades`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_cidades`
AS SELECT
   `vw_cdr`.`id` AS `id`,
   `vw_cdr`.`cidade` AS `cidade`,count(`vw_cdr`.`cidade`) AS `total`
FROM `vw_cdr` group by `vw_cdr`.`cidade` order by `vw_cdr`.`cidade`;


# Replace placeholder table for vw_stats_busy with correct view syntax
# ------------------------------------------------------------

DROP TABLE `vw_stats_busy`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_stats_busy`
AS SELECT
   (select count(`cdr_cdrport`.`src`)
FROM `cdr_cdrport` where ((`cdr_cdrport`.`disposition` = 'BUSY') and (dayofmonth(`cdr_cdrport`.`calldate`) = dayofmonth(curdate())) and (month(`cdr_cdrport`.`calldate`) = month(curdate())) and (year(`cdr_cdrport`.`calldate`) = year(curdate())))) AS `dia`,(select count(`cdr_cdrport`.`src`) from `cdr_cdrport` where ((`cdr_cdrport`.`disposition` = 'BUSY') and (week(`cdr_cdrport`.`calldate`,0) = week(curdate(),0)) and (month(`cdr_cdrport`.`calldate`) = month(curdate())) and (year(`cdr_cdrport`.`calldate`) = year(curdate())))) AS `semana`,(select count(`cdr_cdrport`.`src`) from `cdr_cdrport` where ((`cdr_cdrport`.`disposition` = 'BUSY') and (month(`cdr_cdrport`.`calldate`) = month(curdate())) and (month(`cdr_cdrport`.`calldate`) = month(curdate())) and (year(`cdr_cdrport`.`calldate`) = year(curdate())))) AS `mes`;

/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
