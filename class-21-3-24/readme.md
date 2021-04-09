# 系统运行方法  

进入class-21-3-24目录，终端输入：cd class-21-3-24  
终端输入：python manager,py run  
所需库文件请查阅requirments.txt  
即可在[127.0.0.1:5000]访问该系统  
[127.0.0.1:5000/wordcloud/]为本次作业内容  

## 目录结构  

本系统采用MVC框架  
  
···  
  
···  
  
########################################  
service firewalld stop--关闭防火墙  

## 报错解决  

vscode中/web/controllers/static.py报错  
修改.vscode文件为  
···  
{  
    "python.pythonPath": "/home/apr/anaconda3/envs/api_misuse/bin/python",  
    // "terminal.integrated.env.osx": {"PYTHONPATH": "${workspaceFolder}"},  
    "python.linting.pylintArgs": [  
        // "--disable=F0401"  
        "--disable=E0401"  
    ]  
}  
···  
  
## flask-sqlacodegen  
  
    flask-sqlacodegen 'mysql+pymysql://name:password@127.0.0.1/table' --outfile "common/models/model.py" --flask
    flask-sqlacodegen 'mysql+pymysql://root:123456@127.0.0.1/table' --tables user --outfile "common/models/user.py"  
    
    
use class;  
drop table if exists `douban`;  
CREATE TABLE `douban` (  
  `id` int unsigned NOT NULL AUTO_INCREMENT,  
  `title` varchar(100) NOT NULL DEFAULT '' COMMENT ' 书名',  
  `bookurl` varchar(11) NOT NULL DEFAULT '' COMMENT 'url',  
  `score` float(11) NOT NULL DEFAULT '0.0' COMMENT '得分',  
  `score_people` int NOT NULL DEFAULT '' COMMENT '评分人数',  
  `price` float(11) NOT NULL DEFAULT '' COMMENT '价格',  
  `publishtime` varchar(100) NOT NULL DEFAULT '' COMMENT '出版日期',  
  `publishcompany` varchar(100) NOT NULL DEFAULT '' COMMENT '出版社',  
  `author` varchar(100) NOT NULL DEFAULT '' COMMENT '作者',  
  `comment` varchar(100) NOT NULL DEFAULT '' COMMENT '总结',  
  `bookintro` varchar(5000) NOT NULL DEFAULT '' COMMENT '简介',  
  PRIMARY KEY (`id`)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='豆瓣top250';  
##########################################  
