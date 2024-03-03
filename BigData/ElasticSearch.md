# ElasticSearch

# 概念

​    ElasticSearch是**面向文档**的

> 关系型数据库与ES一些概念的对比

| Relational DB | ElasticSearch |
| ------------- | ------------- |
| databse       | index         |
| table         | type          |
| row           | document      |
| column        | field         |

elasticSearch（集群）中可以包含多个索引（数据库），每个索引中可以包含多个类型（表），每个类型下又包含多个文档（行），每个文档中又包含多个字段（列）

**物理设计：**

elasticSearch在后台把每个**索引划分成多个分片**，每份分片可以在集群中的不同服务器间迁移

## 索引 _index

### 索引别名_alias

​        索引别名API允许使用一个名字来作为一个索引的别名，所有API会自动将别名转换为实际的索引名称。 别名也可以映射到多个索引，别名不能与索引具有相同的名称。别名可以用来做索引迁移和多个索引的查询统一，还可以用来实现视图的功能

```json
# 查看所有别名
GET /_aliases

# 查看某个别名下的索引
GET /_alias/alias_name

#查看别名以2017开头的下的索引
GET /_alias/2017

# 查看某个索引的别名
GET /index_name/_alias

# 添加并删除别名
POST /_aliases
{
    "actions" : [
        { "remove" : { "index" : "test1", "alias" : "alias1" } },
        { "add" : { "index" : "test2", "alias" : "alias1" } }
    ]
}
```

将别名与多个索引相关联只是几个添加操作：

```json
POST /_aliases
{
    "actions" : [
        { "add" : { "index" : "test1", "alias" : "alias1" } },
        { "add" : { "index" : "test2", "alias" : "alias1" } }
    ]
}

# 也可以使用数组的形式
POST /_aliases
{
    "actions" : [
        { "add" : { "indices" : ["test1", "test2"], "alias" : "alias1" } }
    ]
}

# 还可以使用通配符*
POST /_aliases
{
    "actions" : [
        { "add" : { "index" : "test*", "alias" : "all_test_indices" } }
    ]
}
```

```json
# 还可以使用别名实现类似视图的功能

PUT /test1
{
  "mappings": {
    "type1": {
      "properties": {
        "user" : {
          "type": "keyword"
        }
      }
    }
  }
}

# 创建一个user等于kimchy的视图
POST /_aliases
{
    "actions" : [
        {
            "add" : {
                 "index" : "test1",
                 "alias" : "alias2",
                 "filter" : { "term" : { "user" : "kimchy" } }
            }
        }
    ]
}
```

**filter**

如my_index有个字段是team，team字段记录了该数据是那个team的。team之间的数据是不可见的

```json
POST /_aliases
{
  "actions": [
    {
      "add": {
        "index": "my_index",
        "alias": "my_index__teamA_alias",
        "filter":{
            "term":{
                "team":"teamA"
            }
        }
      }
    },
    {
      "add": {
        "index": "my_index",
        "alias": "my_index__teamB_alias",
        "filter":{
            "term":{
                "team":"teamB"
            }
        }
      }
    },
    {
      "add": {
        "index": "my_index",
        "alias": "my_index__team_alias"
      }
    }
  ]
}

GET /my_index__teamA_alias/_search 只能看到teamA的数据
GET /my_index__teamB_alias/_search 只能看到teamB的数据
GET /my_index__team_alias/_search 既能看到teamA的，也能看到teamB的数据
```

创建索引时也可以指定别名

```
PUT /logs_20162801
{
    "mappings" : {
        "type" : {
            "properties" : {
                "year" : {"type" : "integer"}
            }
        }
    },
    "aliases" : {
        "current_day" : {},
        "2016" : {
            "filter" : {
                "term" : {"year" : 2016 }
            }
        }
    }
}
```

删除别名

```
DELETE /{index}/_alias/{name}
index * | _all | glob pattern | name1, name2, …
name * | _all | glob pattern | name1, name2, …

DELETE /logs_20162801/_alias/current_day
```

### 优化索引

1.拆分索引

2.缩小索引

3.滚动索引

4.手动清除缓存

5.手动刷新内存缓冲区

6.手动刷新到硬盘

7.同步刷新

8.强制合并分段

## 字段类型_mapping

- 字符串类型
  
  text， keyword（不可分词），string(5.0版本后移除)

- 整数
  
  long，integer，short，byte

- 浮点
  
  double，float，half_float，scaled_float

- 日期
  
  date（可以是“2021-12-13”、“2021-05-21 12:10:30”、long类型的毫秒级时间戳，或integer类型的秒级时间戳）

- 布尔值

- 二进制

- 范围
  
  范围类型要求字段值描述的是一个**数值、日期或IP地址的范围**， 在添加文档时可以使用： gte、gt、lt、lte分别表示 >=、 > 、< 、<= 。
  
  integer_range，float_range，long_range，double_range，date_range，ip_range

- 复合
  
  数组类型 array 
  对象类型 object ：JSON格式对象数据
  嵌套类型 nested 
  地理类型 地理坐标类型 geo_point 
  地理地图 geo_shape 
  特殊类型 IP类型 ip 
  范围类型 completion 
  令牌计数类型 token_count 
  附件类型 attachment 
  抽取类型 percolator

- 多数据
  
  有些字段可能会以不同的方式进行检索， 如果文档字段只以一种方式编入索引， 检索性能就会受到影响。所以针对字段类型text 和 keyword , es 专门提供了一个配置字段多数据类型的参数fields， 它可以让一个字段同时具备两种数据类型的特征：
  
  ```
  PUT articles{
      "mappings"{
          "properties":{
              "title":{
                  "type":"text",
                  "fields":{
                      "raw":{"type":"keyword"},
                      "length":{"type":"token_count", "analyzer":"standard"}
                  }
              }
          }
      }
  }
  ```
  
  上面的示例中， title字段被设置为text， 同时通过fields参数又为该字段添加了两个子字段 raw和 length， 且分别为keyword类型和token_count 类型。使用fields设置的子字段， 在添加文档时不需要不需要单独设置字段值， 他们与title共享相同的字段值， 只是会以不同的方式处理字段值， 且在查询时不会展现出来。

## 文档

## 分片

### 倒排索引

采用Lucence倒排索引作为底层，适用于快速的全文检索

通俗点说就是索引的转置，比如原数据是这样

| ID  | label        |
| --- | ------------ |
| 1   | python       |
| 2   | python       |
| 3   | linux,python |
| 4   | linux        |

倒排后的索引为这样：

| labe   | ID    |
| ------ | ----- |
| python | 1,2,3 |
| linux  | 3,4   |

# IK分词器

​        **如果使用中文，则建议使用IK分词器**        

​        即把一段文字划分成一个个的关键字，在搜索时会把自己的信息进行分词，会把数据库或者索引库中的数据进行分词，然后进行一个匹配操作，默认的中文分词是将每个字看成一个词，这显然不符合实际要求，而中文分词器IK能有效解决这个问题

​        它提供了两个分词算法：ik_smart（最少切分）和 ik_max_word（最细粒度划分）

## 安装

git下载安装包，解压进elasticSearch插件文件夹中，然后重启es

## 使用

**ik_smart**

最少切分，返回最少的分词结果

```json
GET _analyze
{
    "analyzer": "ik_smart",
    "text": "中国共产党"
}
/*
{
    "tokens" :[
        {
            "token" : "中国共产党",
            "start_offset": 0,
            "end_offset": 5,
            "type": "CN_WORD"
            "position": 0
        }
    ]
}
*/
```

**ik_max_word**

最细粒度划分，穷尽所有可能

```json
GET _analyze
{
    "analyzer": "ik_max_word",
    "text": "中国共产党"
}
/*
{
    "tokens" :[
        {
            "token" : "中国共产党",
            "start_offset": 0,
            "end_offset": 5,
            "type": "CN_WORD"
            "position": 0
        },
        {
            "token" : "中国",
            "start_offset": 0,
            "end_offset": 2,
            "type": "CN_WORD"
            "position": 0
        }，
        {
            "token" : "国共",
            "start_offset": 1,
            "end_offset": 3,
            "type": "CN_WORD"
            "position": 0
        }，
        {
            "token" : "共产党",
            "start_offset": 3,
            "end_offset": 5,
            "type": "CN_WORD"
            "position": 0
        }
    ]
}
*/
```

# 一、安装

elasticSearch

> 运行状态：http://localhost:9200

elasticSearch-head

> http://localhost:9100

kibana

> http://localhost:5601

如果需要从外部机器访问，则需要修改相应模块的conf文件夹中的yml配置文件，将其中的network改为0.0.0.0

```PYTHON
# python 
pip install elasticsearch
pip isntall elasticsearch[async]  # 支持异步
```

# 二、ES的普通操作

| method | url                           | describe   |
| ------ | ----------------------------- | ---------- |
| PUT    | url/index/type/doc_id         | 创建文档（指定ID） |
| POST   | url/index/type                | 创建文档（随机ID） |
| POST   | url/index/type/doc_id/_update | 修改文档       |
| DELETE | url/index/type/doc_id         | 通过id删除文档   |
| GET    | url/index/type/doc_id         | 查询指定id文档   |
| POST   | url/index/type/_search        | 查询         |

## 创建

```
# _index是索引名称，使用PUT来创建文档时，需要在最后指定一个id
PUT (_index)/_doc/(_id)
{
    key1: value1,
    key2: value2,
}

# 若不指定id，则使用POST可以自动生成
POST (_index)/_doc
{
    key1: value1,
    key2: value2,
}
```

​        在创建文档时，如果建立的是**该索引的第一个文档**，而在事先没有创建对应的scheme，那么ES会根据输入的字段自动划分数据类型，并创建相应的schema，这种方式称为schema on write。而一个索引的某个字段的数据类型被确定下来之后，**后续新增的文档的这个字段类型必须要符合**，否则会报错。

​        但是同样的，在上面这种情况中，字段类型可能不是我们想要的，我们可以事先创建一个索引的shema。

**index的创建**包括三部分：

> 索引名不允许有大写字母

​    **settings**:索引的基本配置，包括分片数，每个分片对应的复制数量，分词器等
​    **mapping**:属性的类型及其相关定义
​    **aliases**:索引别名的定义    

```
# 创建索引，并规定字段类型
PUT /(_index)
{
    "mappings": {

        "properties": {
               field_1: {
                   "type": type1,
                   "index": "false" # 默认为true，true时会建立字段索引
                   "null_value": "null" # 设置空值的值，设置后会参与倒排索引
               },
               field_2: {
                   "type": type2
               },
        }
    }
}
```

> 可通过GET _cat/来获取es更多的信息

## 修改

### 1.POST和PUT

​        在修改文档时，我们需要指定一个id来进行，所以通常使用PUT，可使用PUT时，我们需要把**所有字段都写出来**，否则没写出来的字段会被删除，所以有时候也并不方便。

​        而使用POST则可以做到修改哪个字段就提供哪个字段的键值对，来进行**部分字段的修改**

```json
PUT (_index)/_doc/(_id)
{
key1: new_value1,
new_key2: value2,
old_key3: old_value3,
}

POST (_index)/_doc/(_id)
{
key1: new_value1,
new_key2: value2,
}
```

​        在我们不知道文档的id时，需要通过查询的方式来进行修改

```json
POST (_index)/_update_by_query
{
    # 查询要修改的文档
  "query": {
    "match": {
      "user": "GB"
    }
  },
      # 修改语句
  "script": {
      # source中的是要修改的字段与规则
    "source": "ctx._source.city = params.city;ctx._source.province = params.province;ctx._source.country = params.country",
    "lang": "painless",
    "params": {
      "city": "上海",
      "province": "上海",
      "country": "中国"
    }
  }
}
```

### 2./_UPDATE

```json
PUT test/_doc/1
{
    "counter" : 1,
    "tags" : ["red"]
}

POST test/_doc/1/_update
{
    "doc" : {
        key : new_value
    },
    # 如果doc和script都指定，那么doc会被忽视掉。
    "script" : {
        # counter值增加 
        "source": "ctx._source.counter += params.count",
        # 列表增加元素    
        "source": "ctx._source.tags.add(params.tag)",
        # 增加新字段        
        "script" : "ctx._source.new_field = 'value_of_new_field'"
        # 移除字段
        "script" : "ctx._source.remove('new_field')"
        # 逻辑判断做删除
        "source": "if (ctx._source.tags.contains(params.tag)) 
                    { ctx.op = 'delete' } 
                   else { ctx.op = 'none' }"

        "lang": "painless",
        "params" : {
            "count" : 4,
            "tag" : "blue"
        }
    }
}
```

### 3.upsert

​        当文档不存在时，会创建新文档，存在时则为更新。

```
POST (_index)/_update/(_id)
{
  "script": {
    "source": "ctx._source.key=params.field",
    "params": {field: field_value}
  },
  "upsert": {
    key: key_value
  }
}
```

### 4.doc_as_upsert

​    与upsert类似，当指定id的文档不存在时，会将doc内容插入新文档；若存在，则与目标文档合并

```
POST (_index)/_update/(_id)
{
     "doc": {
       "author": "Albert Paro",
       "title": "Elasticsearch 5.0 Cookbook",
       "description": "Elasticsearch 5.0 Cookbook Third Edition",
       "price": "54.99"
      },
     "doc_as_upsert": true
}
```

## 删除

```
# 删除指定id的文档
delete /(_index)/_doc/(_id)

# 删除满足条件的所有文档
POST (_index)/_delete_by_query
{
  "query": {
    "match": {
      field: value
    }
  }
}

# 删除索引
delete (_index)
```

## 查询

​    检查索引是否存在

```
HEAD (_index)
```

​    检查文档是否存在

```
HEAD /(_index)/_doc/(_id)
```

### 

```PYTHON
# 查看指定索引的信息
GET (_index)
# 获取指定ID的文档
GET (_index)/_doc/(id)
```

​    

# 三、复杂搜索

```json
# 查询所有索引的文档
GET _search
GET /_all/_search

# 查询特定索引
GET (_index)/_search

# 查询多个索引
POST /index1,index2,index3/_search

# 查询多个index开头的索引，但排除index3
POST /index*,-index3/_search

# 获取第2页的5个文档
GET _search?size=5&from=2

# 通过_source定义要搜索的字段
# 而如果 _source是空列表[]，则返回所有字段
GET twitter/_search
{
  "_source": ["user", "city"],
  "query": {
    "match_all": {
    }
  }
}
# 使用fields而不是用_source的话，这样更高效
GET twitter/_search
{
  "_source": false,
  "fields": ["user", "city"],
  "query": {
    "match_all": {
    }
  }
}
```

```json
GET index/type/_search
{
    "query":{
        "match":{    # 匹配条件，这里支持模糊匹配
            "field_1":"value_1"
        },
    },
    "sort":[
        {    # 排序字段
           "field_1":{
            "order":"asc"
            } 
        } 
    ],
    "from": 0,    # 从第几个数据开始
    "size": 1    # 返回的数据条数
}
```

```json
# 多条件匹配与过滤
# must：满足每个match条件，即and
# must_not
# should则可以理解为or
GET index/type/_search
{
    "query":{
        "bool":{    
            "must":[    
                {
                    "match":
                    {    
                        "field_1":"value_1"
                    },
                        "match":
                    {    
                        "field_2":"value_2"
                    },
                }
            ],
            # 过滤
            # range  满足范围条件的字段
            # gt     大于
            # gte     大于等于
            # lt     小于
            "filter":{
                "range":{
                    "field_1":{
                        "gte":"value_1",
                        "lt":"value_2",
                    }
                }
            }
        }
    }
}
```

term 查询是直接通过倒排索引指定的词条进行精确查找的

### 几个搜索语句的区别

1、**term**不会对value进行分词处理，输入的什么就匹配的什么，并且若key是能被分词的类型，则value必须是分词结果中的一个

2、而**match**会对条件value进行分词。

## 1、full text query 全文查询

### match

​    标准匹配查询以匹配提供的文本、数字、日期或布尔值。对查询字符串进行分析，并获取词汇单元，然后将各个词汇单元根据参数operator（默认为or）进行匹配及布尔运算，获得最终匹配结果。

​    会对提供的查询条件进行分词。

```json
{
    "query":{
        "match":{
            "field_1": {
                "query": "value_1",
                // 可配合query参数同时使用的常用参数
                "lenient": true, // 忽略基于格式的错误，例如数字字段提供文本查询值，默认为false
                "operator": "AND", // 对于词汇单元的匹配模式，默认为“OR”,
                "minimum_should_match": 1, // 对词汇单元的最小匹配个数
                "zero_term_query": "all", // 如果查询字符串通过分析器后没有产生词汇单元，那应该如何返回查询结果。默认为none，不返回数据

                "analyzer": "对查询字符串指定分析器", 
                "fuzziness": 1 , // 用模糊匹配来查询分词过后的单元词汇
                "prefix_length": 1,  // 模糊匹配时，对于查询字符串所产生的词汇单元，需要固定开始字符数的个数，默认为0
                "fuzzy_transpositions": false, // 模糊匹配时，对于字符串所产生的词汇单元，允许相邻两个字符换位匹配，默认为true
                "max_expansions": 2, // 模糊匹配时，对于字符串所产生的词汇单元最大个数，默认为50    
            } 
        }
    }
}
```

#### match_bool_prefix

​        会对查询字符串使用analyzer分词器处理为多个term，然后基于这些个term进行bool query，除了最后一个term使用前缀查询 其它都是term query。

```json
{
    "query": {
        "match_bool_prefix" : {
            "message" : "quick brown f"
        }
    }
}

/* 等价于 */
{
    "query": {
        "bool" : {
            "should": [
                { "term": { "message": "quick" }},
                { "term": { "message": "brown" }},
                { "prefix": { "message": "f"}}
            ]
        }
    }
}

// 可用参数
{
    "operator": "AND",// 对于词汇单元的匹配模式，默认为“OR”,
    "minimum_should_match": 1, // 对词汇单元的最小匹配个数
    "analyzer": "对查询字符串指定分析器"
}
```

#### match_phrase

​        对查询字符串使用analyzer分词器处理为多个term，然后将各个term连接生成一个新的string来匹配搜索文本字段。

​        或者说用输入的原查询字符串来匹配

```json
/* 
可以使用参数slop（默认为0）来允许匹配项的字符之间的间隔差，这个字符是指匹配项经分词器之后的term。
比如查询字符串 query = "5ETF"，目标字符串是 "5G50ETF",该目标字符串的terms=["5", "G", "50", "ETF"]，其中"5"和"ETF"间隔2，所以当slop=0或者1时，无法匹配到，当slop=2时可以匹配 
*/

// 可用参数
{
    "minimum_should_match": 1, // 对词汇单元的最小匹配个数
    "analyzer": "对查询字符串指定分析器"
}
```

#### match_phrase_prefix

#### mutli_match

```json
// 可用参数
{
    "type": "best_fields"
    /*
    best_fields           根据得分对结果进行降序排序
    most_fields           按总得分排序
    cross_fields           匹配多个term的文本查询结果时，必须存在至少一个字段才算文档为匹配
    phrase                  同best_fields,但查询方式为 match_phrase
    phrase_prefix         同best_fields,但查询方式为 match_phrase_prefix
    bool_prefix              同best_fields,但查询方式为 match_bool_prefix
    */
}
```

### query string query

​        可以细分为两种子类型：query_sring 和 simple_query_sring。她们使用不同的analyzer来处理查询字符串。当查询字符串不符合analyzer语法时，query_string会引发异常，而simple_query_string会丢弃无效部分继续执行。

#### query_sring

#### simple_query_sring

### interval query

​        与span query类似，根据定义的匹配规则返回结果。根据所用的查询规则或对象，可分为五个类型

```json
{
    "query": {
        "intervals": {
            "field_1": {
                // 1.match，可根据对查询文本单词的ordered（顺序）和max_gaps（间隔）返回
                "match": {
                    "query": "value1",
                    "analyzer": "",
                    "max_gaps": 1, // 匹配时词之间允许的最大间隔、偏移量，默认为-1没有限制。
                    "ordered": false, // 匹配字词必须按单元词汇的顺序，默认为false
                    "use_field": "field_2" // 如果指定此参数值，则匹配该值的字段，而不是匹配intervals的字段field_1
                },

                // 2.prefix，查询的字符串不再分词，完全匹配，可以在文本最多产生128个匹配。如果超过则算作错误.
                // prefix的参数只对英文和数字有效，对汉字无效
                "prefix": {
                    "prefix": "value1",
                    "analyzer": "",
                    "use_field": "field_2" // 如果指定此参数值，则匹配该值的字段，而不是匹配intervals的字段field_1
                },

                // 3.wildcard，使用通配符规则匹配，可以在文本最多产生128个匹配。如果超过则算作错误.
                "wildcard": {
                    "pattern": "value1",
                    "analyzer": "",
                    "use_field": "field_2" // 如果指定此参数值，则匹配该值的字段，而不是匹配intervals的字段field_1
                },

                // 4.all_of

                // 5.any_of

            }
        }
    }
}
```

## 2、term query 词条级别搜索

## 3、compound query 复合查询

​        用于组合多个子句以构建复杂的查询。

### bool

```json
/*
bool query使用
must(and)，should(or), must_not(not)
组合查询子句
*/
{
    "query":{
        "bool":{
            "must":{
                "range":{
                    "field_1":{
                        "gte":0.1,
                        "lte":0.2
                    }
                }
            },
            "must_not":{
                "range":{
                    "field_2":{

                    }
                }
            }
        }
    }
}
```

**高亮查询**

```JSON
GET index/_doc/_search
{    
    "query":{    
        "match":{
            "field_1": "value"
        }
    },
    "highlight":{    # 设置高亮字段
        # pre/post_tags可以自定义高亮的html格式，否则默认<em>
        "pre_tags": "<p class='key' style='color:red'>",
        "post_tags": "<\p>"
        "fields":{
            "field_1":{}
        }
    }
}
```

### 

# 四、聚合

​        聚合框架有助于根据搜索查询提供聚合数据。聚合查询是数据库中重要的功能特性，ES作为搜索引擎兼数据库，同样提供了强大的聚合分析能力。它基于查询条件来对数据进行分桶、计算的方法。有点类似于 SQL 中的 group by 再加一些函数方法的操作。聚合可以嵌套，由此可以组成复杂的操作（Bucketing聚合可以包含sub-aggregation）

## 语法

```Json
"aggregations" : {                        //也可简写为 aggs
    "<aggregation_name>" : {      // 聚合的名字
        "<aggregation_type>" : {     //聚合的类型
            <aggregation_body>      //聚合体：对哪些字段进行聚合
        }
        [,"meta" : {  [<meta_data_body>] } ]?                 //元
        [,"aggregations" : { [<sub_aggregation>]+ } ]?   //在聚合里面在定义子聚合
    }
    [,"<aggregation_name_2>" : { ... } ]*                      //聚合的名字
}
```

## aggregation_type

### 1、矩阵统计：matrix_stats

​            返回字段：

| field       | 中文名 |
| ----------- | --- |
| count       | 计数  |
| mean        | 均值  |
| variance    | 方差  |
| skewness    | 偏度  |
| kurtosis    | 峰度  |
| covariance  | 协方差 |
| correlation | 相关性 |

### 2、常见度量指标

```python
"""
1.最大值            max
2.最小值            min
3.总和            sum
4.值计数            value_count    
5.平均值            avg
6.加权平均值           weighted_avg
7.基数             cardinality
8.统计             stats
9.扩展统计            extended_stats
10.中位数绝对偏差      median_absolute_deviation
11.百分位             percentiles
12.百分位等级        percentile_ranks
13.地理重心            gep_centroid
14.地理边界            geo_bounds
15.最热点             top_hits
16.脚本时度量指标       scripted_metric
"""
```

### 3、bucket聚合
