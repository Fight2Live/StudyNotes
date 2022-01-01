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



## 索引 



## 倒排索引

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



## 字段类型（mapping）

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



# 一、安装

elasticSearch



elasticSearch-head



kibana



```PYTHON
# python 
pip install elasticsearch
pip isntall elasticsearch[async]  # 支持异步
```



# 二、ES的普通操作

## 创建

```
# _index是索引名称，使用PUT来创建文档时，需要在最后指定一个id
PUT (_index)/_doc/(_id)
{
key1: value1,
key2: value2,
}

# 若不指定id，则使用POST可以自动生成
POSET (_index)/_doc
{
key1: value1,
key2: value2,
}
```

​		在创建文档时，如果建立的是**该索引的第一个文档**，而在事先没有创建对应的scheme，那么ES会根据输入的字段自动划分数据类型，并创建相应的schema，这种方式称为schema on write。而一个索引的某个字段的数据类型被确定下来之后，**后续新增的文档的这个字段类型必须要符合**，否则会报错。

​		但是同样的，在上面这种情况中，字段类型可能不是我们想要的，我们可以事先创建一个索引的shema。

index的创建包括三部分：

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





## 修改

### 1.POST和PUT

​		在修改文档时，我们需要指定一个id来进行，所以通常使用PUT，可使用PUT时，我们需要把**所有字段都写出来**，否则没写出来的字段会被删除，所以有时候也并不方便。

​		而使用POST则可以做到修改哪个字段就提供哪个字段的键值对，来进行**部分字段的修改**

```
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

```
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

```
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





