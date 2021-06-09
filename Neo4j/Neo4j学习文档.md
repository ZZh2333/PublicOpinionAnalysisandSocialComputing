# 一、Neo4j学习笔记

## 1、首先清空数据库，确保在一个空白的环境操作：

```cypher
MATCH (n) DETACH DELETE n
```

MATCH为匹配操作，小括号（）代表一个节点node，括号里的n为标识符。

``` Cypher
MATCH (n) RETURN n
```

查看图数据库。

## 2、创建一个人物节点

```cypher
CREATE (n:Person {name:'John'}) RETURN n
```

CREATE是创建操作，Person是标签，代表节点的类型，花括号{}代表节点的属性，属性类似Python的字典，该语句的含义就是创建一个标签为Person的节点，该节点具有一个那么属性，属性值为John。

## 3、继续创建更多的人物节点

```cypher
CREATE (n:Person {name:'Sally'}) RETURN n;
CREATE (n:Person {name:'Steve'}) RETURN n;
CREATE (n:Person {name:'Mike'}) RETURN n;
CREATE (n:Person {name:'Liz'}) RETURN n;
CREATE (n:Person {name:'Shawn'}) RETURN n;
```

## 4、创建地区节点

```cypher
CREATE (n:Location {city:'Miami', state:'FL'});
CREATE (n:Location {city:'Boston', state:'MA'});
CREATE (n:Location {city:'Lynn', state:'MA'});
CREATE (n:Location {city:'Portland', state:'ME'});
CREATE (n:Location {city:'San Francisco', state:'CA'});
```

地区节点类型为Location，属性包括city和state。

## 5、创建关系

```Cypher
MATCH (a:Person {name:'Liz'}),(b:Person {name:'Mike'}) Merge (a)-[:FRIENDS]->(b)
```

该语句中方括号[]即为关系，FRIENDS为关系的类型。注意这里的箭头-->是有方向的，表示是a到b的关系。

## 6、给关系增加属性值

```Cypher
MATCH (a:Person {name:'Shawn'}),(b:Person {name:'Sally'}) MERGE (a)-[:FRIENDS {since:2001}]->(b)
```

在关系中，同样使用花括号{}来增加关系的属性，也是类似于Python的字典，这里给FRIENDS关系增加了since属性，属性值为2001，表示他们建立朋友关系的时间。

## 7、增加更多的关系

```Cypher
MATCH (a:Person {name:'Shawn'}), (b:Person {name:'John'}) MERGE (a)-[:FRIENDS {since:2012}]->(b);
MATCH (a:Person {name:'Mike'}), (b:Person {name:'Shawn'}) MERGE (a)-[:FRIENDS {since:2006}]->(b);
MATCH (a:Person {name:'Sally'}), (b:Person {name:'Steve'}) MERGE (a)-[:FRIENDS {since:2006}]->(b);
MATCH (a:Person {name:'Liz'}), (b:Person {name:'John'}) MERGE (a)-[:MARRIED {since:1998}]->(b);
```

## 8、建立不同类型节点之间的关系——人物和地点的关系

```Cypher
MATCH (a:Person {name:'John'}),(b:Location {city:'Boston'}) MERGE (a)-[:BORN_IN {year:1978}]->(b)
```

这里的关系是BORN_IN，表示出生地，同样有一个属性year，表示出生年份。

## 9、建立更多的出生地关系

```Cypher
MATCH (a:Person {name:'Liz'}), (b:Location {city:'Boston'}) MERGE (a)-[:BORN_IN {year:1981}]->(b);
MATCH (a:Person {name:'Mike'}), (b:Location {city:'San Francisco'}) MERGE (a)-[:BORN_IN {year:1960}]->(b);
MATCH (a:Person {name:'Shawn'}), (b:Location {city:'Miami'}) MERGE (a)-[:BORN_IN {year:1960}]->(b);
MATCH (a:Person {name:'Steve'}), (b:Location {city:'Lynn'}) MERGE (a)-[:BORN_IN {year:1970}]->(b);
```

至此，知识图谱的数据已经插入完毕，可以开始做查询了。

## 10、查询

查询所有在Boston出生的人物。

```Cypher
MATCH (a:Person)-[:BORN_IN]->(b:Location {city:'Boston'}) RETURN a,b
```

## 11、查询所有对外有关系的节点

```Cypher
MATCH (a)-->() RETURN a
```

## 12、查询所有有关系的节点

```Cypher
MATCH (a)--() RETURN a
```

## 13、查询所有对外有关系的节点，以及关系类型

```Cypher
MATCH (a)-[r]->() RETURN a.name,type(r)
```
查询结果如下：
```markdown
╒════════╤═════════╕
│"a.name"│"type(r)"│
╞════════╪═════════╡
│"John"  │"BORN_IN"│
├────────┼─────────┤
│"Sally" │"FRIENDS"│
├────────┼─────────┤
│"Steve" │"BORN_IN"│
├────────┼─────────┤
│"Mike"  │"BORN_IN"│
├────────┼─────────┤
│"Mike"  │"FRIENDS"│
├────────┼─────────┤
│"Liz"   │"BORN_IN"│
├────────┼─────────┤
│"Liz"   │"MARRIED"│
├────────┼─────────┤
│"Liz"   │"FRIENDS"│
├────────┼─────────┤
│"Shawn" │"BORN_IN"│
├────────┼─────────┤
│"Shawn" │"FRIENDS"│
├────────┼─────────┤
│"Shawn" │"FRIENDS"│
└────────┴─────────┘
```

## 14、查询所有有结婚关系的节点

```Cypher
MATCH (n)-[:MARRIED]-() RETURN n
```

## 15、创建节点的同时创建关系

```Cypher
CREATE (a:Person {name:'Todd'})-[r:FRIENDS]->(b:Person {name:'Carlos'})
```

## 16、查找某人朋友的朋友

```Cypher
MATCH (a:Person {name:'Mike'})-[r1:FRIENDS]-()-[r2:FRIENDS]-(friend_of_friend) RETURN friend_of_friend.name AS fofName
```

查询结果如下：

```markdown
╒═════════╕
│"fofName"│
╞═════════╡
│"John"   │
├─────────┤
│"Sally"  │
└─────────┘
```

Mike朋友的朋友为John和Sally。

## 17、增加/修改节点的属性

```Cypher
MATCH (a:Person {name:'Liz'}) SET a.age=34;
MATCH (a:Person {name:'Shawn'}) SET a.age=32;
MATCH (a:Person {name:'John'}) SET a.age=44;
MATCH (a:Person {name:'Mike'}) SET a.age=25;
```

这里的SET表示修改操作。

## 18、删除节点的属性

```cypher
MATCH (a:Person {name:'Mike'}) SET a.test='test';
MATCH (a:Person {name:'Mike'}) REMOVE a.test;
```

删除属性操作主要通过REMOVE命令。

## 19、删除节点

```Cypher
MATCH (a:Location {city:'Portland'}) DELETE a
```

删除节点的操作是DELETE

## 20、删除有关系的节点

```Cypher
MATCH (a:Person {name:'Todd'})-[rel]-(b:Person) DELETE a,b,rel
```

