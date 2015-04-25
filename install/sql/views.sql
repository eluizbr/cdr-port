-- Create syntax for VIEW 'vw_cdr'
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_cdr`
AS SELECT
   `cdr_cdrport`.`id` AS `id`,
   `cdr_cdrport`.`calldate` AS `calldate`,
   `cdr_cdrport`.`src` AS `src`,
   `cdr_cdrport`.`dst` AS `dst`,sec_to_time(`cdr_cdrport`.`duration`) AS `duration`,sec_to_time(`cdr_cdrport`.`billsec`) AS `billsec`,
   `cdr_cdrport`.`disposition` AS `disposition`,
   `cdr_prefixo`.`ddd` AS `ddd`,
   `cdr_prefixo`.`prefixo` AS `prefixo`,
   `cdr_prefixo`.`cidade` AS `cidade`,
   `cdr_prefixo`.`estado` AS `estado`,
   `cdr_prefixo`.`operadora` AS `operadora`,
   `cdr_prefixo`.`tipo` AS `tipo`,
   `cdr_prefixo`.`rn1` AS `rn1`,
   `cdr_cdrport`.`portado` AS `portado`
FROM (`cdr_cdrport` join `cdr_prefixo`) where (`cdr_cdrport`.`prefixo` = `cdr_prefixo`.`prefixo`);

-- Create syntax for VIEW 'vw_cidades'
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_cidades`
AS SELECT
   `vw_cdr`.`id` AS `id`,
   `vw_cdr`.`cidade` AS `cidade`
FROM `vw_cdr` group by `vw_cdr`.`cidade` order by `vw_cdr`.`cidade`;

-- Create syntax for VIEW 'vw_day_stats'
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_day_stats`
AS SELECT
   cast(`cdr_cdr`.`calldate` as date) AS `dia`,month(cast(`cdr_cdr`.`calldate` as date)) AS `mes`,count(0) AS `total`
FROM `cdr_cdr` where ((`cdr_cdr`.`calldate` > (curdate() - interval 6 month)) and curdate()) group by `dia` order by `dia`;

-- Create syntax for VIEW 'vw_disposition'
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_disposition`
AS SELECT
   `cdr_cdr`.`id` AS `id`,
   `cdr_cdr`.`disposition` AS `disposition`,count(`cdr_cdr`.`disposition`) AS `Total`
FROM `cdr_cdr` group by `cdr_cdr`.`disposition` order by `Total` desc;

-- Create syntax for VIEW 'vw_estados'
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_estados`
AS SELECT
   `vw_cdr`.`id` AS `id`,
   `vw_cdr`.`estado` AS `estado`,count(`vw_cdr`.`estado`) AS `total`
FROM `vw_cdr` group by `vw_cdr`.`estado` order by `vw_cdr`.`estado`;

-- Create syntax for VIEW 'vw_last_10'
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
FROM `vw_cdr` where (`vw_cdr`.`disposition` = 'ANSWERED') group by `vw_cdr`.`dst` order by `vw_cdr`.`calldate` desc limit 9;

-- Create syntax for VIEW 'vw_month_stats'
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_month_stats`
AS SELECT
   monthname(cast(`cdr_cdr`.`calldate` as date)) AS `mes`,count(0) AS `total`
FROM `cdr_cdr` where (`cdr_cdr`.`disposition` = 'ANSWERED') group by `mes` order by `mes`;

-- Create syntax for VIEW 'vw_operadoras'
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_operadoras`
AS SELECT
   `vw_cdr`.`id` AS `id`,
   `vw_cdr`.`operadora` AS `operadora`,count(`vw_cdr`.`operadora`) AS `total`
FROM `vw_cdr` group by `vw_cdr`.`operadora` order by `total` desc;

-- Create syntax for VIEW 'vw_ramais'
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_ramais`
AS SELECT
   `cdr_cdr`.`id` AS `id`,
   `cdr_cdr`.`src` AS `ramais`
FROM `cdr_cdr` where ((`cdr_cdr`.`disposition` = 'ANSWERED') and (month(`cdr_cdr`.`calldate`) = month(curdate())) and (year(`cdr_cdr`.`calldate`) = year(curdate()))) group by `cdr_cdr`.`src` order by `cdr_cdr`.`src` desc;

-- Create syntax for VIEW 'vw_stats_answered'
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_stats_answered`
AS SELECT
   (select count(`cdr_cdr`.`src`)
FROM `cdr_cdr` where ((`cdr_cdr`.`disposition` = 'ANSWERED') and (dayofmonth(`cdr_cdr`.`calldate`) = dayofmonth(curdate())) and (month(`cdr_cdr`.`calldate`) = month(curdate())) and (year(`cdr_cdr`.`calldate`) = year(curdate())))) AS `dia`,(select count(`cdr_cdr`.`src`) from `cdr_cdr` where ((`cdr_cdr`.`disposition` = 'ANSWERED') and (week(`cdr_cdr`.`calldate`,0) = week(curdate(),0)) and (month(`cdr_cdr`.`calldate`) = month(curdate())) and (year(`cdr_cdr`.`calldate`) = year(curdate())))) AS `semana`,(select count(`cdr_cdr`.`src`) from `cdr_cdr` where ((`cdr_cdr`.`disposition` = 'ANSWERED') and (month(`cdr_cdr`.`calldate`) = month(curdate())) and (month(`cdr_cdr`.`calldate`) = month(curdate())) and (year(`cdr_cdr`.`calldate`) = year(curdate())))) AS `mes`;

-- Create syntax for VIEW 'vw_stats_busy'
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_stats_busy`
AS SELECT
   (select count(`cdr_cdr`.`src`)
FROM `cdr_cdr` where ((`cdr_cdr`.`disposition` = 'BUSY') and (dayofmonth(`cdr_cdr`.`calldate`) = dayofmonth(curdate())) and (month(`cdr_cdr`.`calldate`) = month(curdate())) and (year(`cdr_cdr`.`calldate`) = year(curdate())))) AS `dia`,(select count(`cdr_cdr`.`src`) from `cdr_cdr` where ((`cdr_cdr`.`disposition` = 'BUSY') and (week(`cdr_cdr`.`calldate`,0) = week(curdate(),0)) and (month(`cdr_cdr`.`calldate`) = month(curdate())) and (year(`cdr_cdr`.`calldate`) = year(curdate())))) AS `semana`,(select count(`cdr_cdr`.`src`) from `cdr_cdr` where ((`cdr_cdr`.`disposition` = 'BUSY') and (month(`cdr_cdr`.`calldate`) = month(curdate())) and (month(`cdr_cdr`.`calldate`) = month(curdate())) and (year(`cdr_cdr`.`calldate`) = year(curdate())))) AS `mes`;

-- Create syntax for VIEW 'vw_stats_noanswer'
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_stats_noanswer`
AS SELECT
   (select count(`cdr_cdr`.`src`)
FROM `cdr_cdr` where ((`cdr_cdr`.`disposition` = 'NO ANSWER') and (dayofmonth(`cdr_cdr`.`calldate`) = dayofmonth(curdate())) and (month(`cdr_cdr`.`calldate`) = month(curdate())) and (year(`cdr_cdr`.`calldate`) = year(curdate())))) AS `dia`,(select count(`cdr_cdr`.`src`) from `cdr_cdr` where ((`cdr_cdr`.`disposition` = 'NO ANSWER') and (week(`cdr_cdr`.`calldate`,0) = week(curdate(),0)) and (month(`cdr_cdr`.`calldate`) = month(curdate())) and (year(`cdr_cdr`.`calldate`) = year(curdate())))) AS `semana`,(select count(`cdr_cdr`.`src`) from `cdr_cdr` where ((`cdr_cdr`.`disposition` = 'NO ANSWER') and (month(`cdr_cdr`.`calldate`) = month(curdate())) and (month(`cdr_cdr`.`calldate`) = month(curdate())) and (year(`cdr_cdr`.`calldate`) = year(curdate())))) AS `mes`;