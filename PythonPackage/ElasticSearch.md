# ElasticSearch-py

> 测试环境
>
> ElasticSearch：v 7.16.2
>
> python包版本：v 7.16.2

```python
from elasticsearch import Elasticsearch
from elasticsearch import AsyncElasticsearch

es = Elasticsearch(hosts='https://localhost:9200')
```



# 索引_index

## 新增

```python
# 新增索引
index_mapping = {
    "settings": {
		"number_of_shards": 4,	# 分片数
		"number_of_replicas": 2	# 副本数
	},
    "mappings": {
        "properties": {
            "id":                   {"type": "keyword", "index": True},
            "patch_id":             {"type": "keyword", "index": True},
            "departure":            {"type": "text"},
            "arrival":              {"type": "text"},
            "container_type":       {"type": "text"},
            "container_weight":     {"type": "integer"},
            "vessel":               {"type": "text"},
            "ocean_freight":        {"type": "float"},
            "surcharges_freight":   {"type": "float"},
            "total_freight":        {"type": "float"},
            "voyage":               {"type": "text"},
            "service":              {"type": "text"},
            "etd":                  {"type": "date"},
            "eta":                  {"type": "date"},
            "days":                 {"type": "integer"},
            "charges_information":  {"type": "text"},
            "surcharges_details":   {"type": "text"},
            "err_msg":              {"type": "text"},
            "create_time":          {"type": "date", "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"},
        }
    },
    "_default_": {
            "dynamic": "strict"  # 限定不能多增加或减少字段，如果多增加或减少字段就会抛出异常；dynamic是处理遇到未知字段情况的，设置为“strict”是说当遇到未知字段时抛出异常
        }
}

es.indices.create(index='index_name', body='body')

```



## 查看

```python
# 查看index的mapping
map = es.indices.get_mapping(index='index_name')
print(map)
```



## 修改

```PYTHON
# 修改索引映射
es.indices.mapping(index='index_name', body='index_mapping')
```



## 删除

```PYTHON
# 删除索引
es.indices.delete(index='index_name')
```







# 文档_doc

## 新增

```python
query = {
    'name': '李四',
    'addr': '黑龙江'
}
# id非必填，会自动生成，PUT
es.index(index='index_name', document=query)

# 必须指定id，不会自动生成，POST
es.create(index='index_name', document=query, id='1')

# 批量插入，如果不指定_id，就会自动生成，而id是对文档内的字段id赋值，不是文档属性id
bulk = [{
	'_index':'test',
	'_type':'_doc',
	'_id':4,
	'name':'找钱',
    'addr':'中国',
},{
	'_index':'test',
	'name':'孙李', 
    'field':'value',
},]
from elasticsearch import helpers
helpers.bulk(es, actions=bulk)
```



## 查询

```PYTHON
# 根据id进行搜索
res = es.get(index='index_name', id='id')
'''
res = {
    '_index': 'spot_quote', 
    '_type': '_doc', 
    '_id': '1', 
    '_version': 4, 
    '_seq_no': 4, 
    '_primary_term': 1, 
    'found': True, 
    '_source': {
        'name': '张三', 
        'addr': '上海'
    }
}
'''

# 根据查询语句进行搜索，若不指定body则默认是match_all
# 其他参数：
# size：返回的数据量，默认是10
# from_：从第几个数据开始，多用于分页
query = {
    "query": {
        "match_all": {}
    }
}
r1 = es.search(index='index_name', body=query)
for i in r1['hits']['hits']:
    # 打印搜索结果
    # i['_source'] = {'name': '张三', 'addr': '上海'}
    print(i['_source'])

    
```





## 修改

```python
# 修改指定id的文档，若修改的字段不存在会自动新增
query = {
    'doc':{
        "name": '张三（alter）'
    }
}
update_1 = es.update(index=index_name, body=query, id='1')

# 批量修改，与上面批量插入一样，若_id数据存在，则会对其进行修改操作
bulk = [{
	'_index':'test',
	'_type':'_doc',
	'_id':4,
	'name':'赵钱（alter）',
    'addr':'中国',
    'age':85
},{
	'_index':'test',
	'name':'孙李', 
    'field':'value',
},]
from elasticsearch import helpers
helpers.bulk(es, actions=bulk)
```





## 删除

```PYTHON
es.delete(index=index_name, id='1')
```

