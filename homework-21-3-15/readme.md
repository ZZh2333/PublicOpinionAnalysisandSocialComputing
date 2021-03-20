#########################################  
  
# 作业：爬虫爬取中传要闻题目、url、部门、时间、浏览量、正文  
...  
homework.jpynb为最终作业版本  
该版本保证了稳定的连接，具有良好的准确率  
截止到2021/3/20  
中传要闻共3490条记录，共582页  
爬取记录3383条，其中三条数据丢失  
...  

# 数据库创建  
···  
适用于homework.jpynb  
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

===========================================

适用于homeworkV1.jpynb  
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
  
=============================================  
  
# 关于headers  
...  
USER_AGENTS = [  
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",  
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",  
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",  
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",  
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",  
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",  
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",  
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",  
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",  
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",  
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",  
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",  
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",  
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",  
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",  
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",  
]  

经测试Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52该项不可用，会导致爬虫数据丢失。  
...  
#########################################  