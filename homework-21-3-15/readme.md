#######################################  
数据库创建  
···  
create database class;
use class;
drop table if exists `cucnews`;
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
drop table if exists `cucnewsv1`;
CREATE TABLE `cucnewsv1` (
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

作业：爬虫爬取中传要闻题目、url、部门、时间、浏览量、正文  
最终作业为homeworkV1.jpynb  