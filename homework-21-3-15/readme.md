#######################################  
数据库创建  
···
create database class;
use class;
drop table `cucnews`;
CREATE TABLE `cucnews` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL DEFAULT '' COMMENT 'title',
  `newsurl` varchar(50) NOT NULL DEFAULT '' COMMENT 'newsurl',
  `department` varchar(100) NOT NULL DEFAULT '' COMMENT 'department',
  `date` varchar(30) NOT NULL DEFAULT '' COMMENT 'date',
  `count` int NOT NULL DEFAULT '0' COMMENT 'count',
  `content` varchar(1000) NOT NULL DEFAULT '' COMMENT 'content',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='cucnews';
···