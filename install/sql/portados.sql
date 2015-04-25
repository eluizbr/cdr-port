# ************************************************************
# Sequel Pro SQL dump
# Version 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 192.168.2.230 (MySQL 5.5.43-0ubuntu0.14.04.1)
# Database: cdrport
# Generation Time: 2015-04-24 17:27:07 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table portados
# ------------------------------------------------------------

DROP TABLE IF EXISTS `portados`;

CREATE TABLE `portados` (
  `numero` bigint(11) DEFAULT NULL,
  `rn1` int(11) DEFAULT NULL,
  `data_hora` datetime DEFAULT NULL,
  `op` int(11) DEFAULT NULL,
  KEY `numero` (`numero`),
  KEY `rn1` (`rn1`),
  KEY `op` (`op`),
  KEY `data_hora` (`data_hora`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

LOCK TABLES `portados` WRITE;
/*!40000 ALTER TABLE `portados` DISABLE KEYS */;

INSERT INTO `portados` (`numero`, `rn1`, `data_hora`, `op`)
VALUES
	(3000010300,55115,'2012-11-26 22:02:08',1);

/*!40000 ALTER TABLE `portados` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
