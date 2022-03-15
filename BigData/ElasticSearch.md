# ElasticSearch

# 概念

​	ElasticSearch是**面向文档**的

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





## 字段类型_mapping

- 字符串类型

  text， keyword（不可分词），string

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

| ID   | label        |
| ---- | ------------ |
| 1    | python       |
| 2    | python       |
| 3    | linux,python |
| 4    | linux        |

倒排后的索引为这样：

| labe   | ID    |
| ------ | ----- |
| python | 1,2,3 |
| linux  | 3,4   |



# IK分词器

​		**如果使用中文，则建议使用IK分词器**		

​		即把一段文字划分成一个个的关键字，在搜索时会把自己的信息进行分词，会把数据库或者索引库中的数据进行分词，然后进行一个匹配操作，默认的中文分词是将每个字看成一个词，这显然不符合实际要求，而中文分词器IK能有效解决这个问题

​		它提供了两个分词算法：ik_smart（最少切分）和 ik_max_word（最细粒度划分）

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
>
> 首页：http://localhost:5601





elasticSearch-head

> http://localhost:9100



kibana



```PYTHON
# python 
pip install elasticsearch
pip isntall elasticsearch[async]  # 支持异步
```



# 二、ES的普通操作

| method | url                           | describe           |
| ------ | ----------------------------- | ------------------ |
| PUT    | url/index/type/doc_id         | 创建文档（指定ID） |
| POST   | url/index/type                | 创建文档（随机ID） |
| POST   | url/index/type/doc_id/_update | 修改文档           |
| DELETE | url/index/type/doc_id         | 通过id删除文档     |
| GET    | url/index/type/doc_id         | 查询指定id文档     |
| POST   | url/index/type/_search        | 查询               |



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

​		在创建文档时，如果建立的是**该索引的第一个文档**，而在事先没有创建对应的scheme，那么ES会根据输入的字段自动划分数据类型，并创建相应的schema，这种方式称为schema on write。而一个索引的某个字段的数据类型被确定下来之后，**后续新增的文档的这个字段类型必须要符合**，否则会报错。

​		但是同样的，在上面这种情况中，字段类型可能不是我们想要的，我们可以事先创建一个索引的shema。

**index的创建**包括三部分：

> 索引名不允许有大写字母

​	**settings**:索引的基本配置，包括分片数，每个分片对应的复制数量，分词器等
​	**mapping**:属性的类型及其相关定义
​	**aliases**:索引别名的定义	

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

​		在修改文档时，我们需要指定一个id来进行，所以通常使用PUT，可使用PUT时，我们需要把**所有字段都写出来**，否则没写出来的字段会被删除，所以有时候也并不方便。

​		而使用POST则可以做到修改哪个字段就提供哪个字段的键值对，来进行**部分字段的修改**

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

​		在我们不知道文档的id时，需要通过查询的方式来进行修改

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

​		当文档不存在时，会创建新文档，存在时则为更新。

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

​	与upsert类似，当指定id的文档不存在时，会将doc内容插入新文档；若存在，则与目标文档合并

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

​	检查索引是否存在

```
HEAD (_index)
```



​	检查文档是否存在

```
HEAD /(_index)/_doc/(_id)
```

### 1.直接查询

```PYTHON
# 查看指定索引的信息
GET (_index)
# 获取指定ID的文档
GET (_index)/_doc/(id)


```



### 2._search

​	

```
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



#### script_fields

​		有时候我们需要的字段在_source中没有时，可以使用script_field来生成

​	

# 复杂搜索



```json
GET index/type/_search
{
    "query":{
        "match":{	# 匹配条件，这里支持模糊匹配
            "field_1":"value_1"
        },
    },
    "sort":[
        {	# 排序字段
           "field_1":{
        	"order":"asc"
        	} 
        } 
    ],
	"from": 0,	# 从第几个数据开始
	"size": 1	# 返回的数据条数
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
            # gt	 大于
            # gte	 大于等于
            # lt	 小于
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



**term和match的区别**





**高亮查询**

```JSON
GET index/_doc/_search
{	
    "query":{	
        "match":{
            "field_1": "value"
        }
    },
    "highlight":{	# 设置高亮字段
        # pre/post_tags可以自定义高亮的html格式，否则默认<em>
        "pre_tags": "<p class='key' style='color:red'>",
        "post_tags": "<\p>"
        "fields":{
            "field_1":{}
        }
    }
}
```











