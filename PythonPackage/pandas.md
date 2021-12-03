# Pandas

Pandas 的主要数据结构是 Series （一维数据）与 DataFrame（二维数据）



## 数据结构

**Series** 是一种类似于一维数组的对象，它由一组数据（各种Numpy数据类型）以及一组与之相关的数据标签（即索引）组成。

**DataFrame** 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。**DataFrame** 既有行索引也有列索引，它可以被看做由 **Series** 组成的字典（共同用一个索引）。

**DataFrame**有四个重要的属性： 
	**index**：		行索引。 
	**columns**：  列索引。 
	**values**：	  值的二维数组。 
	**name**：	   名字。





## 操作

```python
import pandas as pd
```



### 创建对象

#### 从外部文件读取

```python
df = pd.read_csv( file_name, [encoding, ] )   # 从csv文件中读取数据，默认将第一行作为列名
df = pd.read_excel( file_name, [encoding, ] ) # 从excel文件中读取
df = pd.read_xxx()

```



#### 由内部数据转换

```python
pd.DataFrame(data, [index, columns, ])
# data:		要转换的数据，可以是list，ndarray，dict，arrays或者Series对象
# index:	list，行号
# columns:	list，列名

pd.DataFrame.from_items(data， [columns, ])
# data:		[( column1: [v1, v2,]),]
# columns:	list,data中要转化为DF的列名列表column_list

pd.DataFrame.from_records(data)

pd.DataFrame.from_dict(data)
```



比如我要创建这样的DF对象：

|      | name  | sex   | age  |
| ---- | ----- | ----- | ---- |
| 0    | Blue  | man   | 20   |
| 1    | Red   | man   | 19   |
| 2    | Green | woman | 18   |



##### 由list转换：

```python
"""
1、默认的DataFrame
"""
list1 = [ ['Blue', 'man', '20'], ['Red', 'man', 19], ['Green', 'woman', 18] ]
column1 = ['name', 'sex', 'age']
df = pd.DataFrame(list1, columns=column1)

"""
2、from_items
"""
list2 = [('name', ['Blue', 'Red', 'Green']), ('sex', ['man', 'man', 'woman']), ('age', [20, 18, 18])]
df2 = pd.DataFrame.from_items(l2)

```





##### 由dict转换：

```python
"""
1、默认的DataFrame
"""
dict1 = {'name': ['Blue', 'Red', 'Green'], 'sex': ['man', 'man', 'woman'], 'age':[20, 18, 18]}
df3 = pd.DataFrame(dict1)

dict2 = [{'name':'Blue', 'sex':'man', 'age':20},
         {'name':'Red', 'sex':'man', 'age':19},
         {'name':'Green', 'sex':'woman', 'age':18}]
df4 = pd.DataFrame(dict2)

"""
2、from_dict
"""
dict3 = {'name': ['Blue', 'Red', 'Green'], 'sex': ['man', 'man', 'woman'], 'age':[20, 18, 18]}
df5 = pd.DataFrame.from_dict(dict1)




```





### 判空







### 计数

```PYTHON
# 得到非空数据的计数
data.count()
data['字段名'].count()

# 该列名下各个值的计数
data[字段名].value_counts()
```



### 选择与切片

#### .iloc

基于整数的下标来进行数据定位/选择

```python
df.iloc[row, column]

df.iloc[100]		#  series，第100行的数据
df.iloc[[100]]		#  dataframe，第100行的数据
df.iloc[2:10]		#  dataframe，第2行至第9行的数据，[2, 10)
df.iloc[2:10, 1]	#  series，第二行至第九行中，第一列的值
df.iloc[2:10, 1:3]	#  dataframe，第2行至第9行[2, 10)的中，第一列到第二列的值[1, 3)
df.iloc[2:10,[1]]	#  dataframe，第二行至第九行中，第一列的值
```





#### .loc

1. 基于标签名进行查找

2. 使用布尔值，或条件语句来进行查找

3. 基于行或列的整数下标进行差找（与iloc一致）

   





##### **.iloc和.loc的区别：**

**iloc**主要使用数字来索引数据，而不能使用字符型的标签来索引数据。

而**loc**则刚好相反，只能使用字符型标签来索引数据，不能使用数字来索引数据，不过有特殊情况，当数据框dataframe的行标签或者列标签为数字，loc就可以来其来索引。



iloc可以用来取指定位置[x,y]的元素，比如df.iloc[0,1]，而loc会报错

loc可以[x:y, [name] ]，来获得‘name’列的[x,y]区间内的元素

loc可以[ [x1,x2,], [name] ]来获得x1行，x2行等name列的数据

以[x:y]的形式时，iloc的区间为[x,y)，loc的区间为[x,y]

 

**总结：**

1. **loc:**

   通过行标签索引行数据

   例：

   loc[n]表示索引的是第n行（index 是整数）

   loc[‘d’]表示索引的是第’d’行（index 是字符）

   有行索引可以没有字段取值，但有字段取值前必须得有行索引，

   而且行索引只能为标签索引形式来取，不能按切片形式来取。

   单取切片形式可以，只是索引为左闭右闭。

2. **iloc**：

   通过行索引获取行数据，不能是字符，取索引必须按切片形式来取，不能按标签，这是与loc的不同。索引为左闭右开。iloc也可以取指定行列，只不过得按切片形式索引，不能直接拿标签索引来做。



当用行索引的时候, 尽量用 iloc 来进行索引; 而用标签索引的时候用 loc 。

 

df[ df[column]==x ]可以取得column列为x的所有行



### 筛选

```PYTHON
df = df[(df['column_name1' <!=> 条件1] & df['column_name2' <!=> 条件2])]  # df = dataFrame
```





### 新加列

```PYTHON
#1.apply
def get_hour(s:pd.Series):
    return int(((s['date'].split(' '))[-2].split(':'))[0])

df1.loc[:, 新列名] = df1.apply(get_hour, axis=1)
```







### 合并

#### concat

```python
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)
```

1. **axis**
   axis=0：竖方向（index）合并，合并方向index作列表相加，非合并方向columns取并集
   axis=1：横方向（columns）合并，合并方向columns作列表相加，非合并方向index取并集
2. .**join**
   默认值：join=‘outer’非合并方向的行/列名称：取交集（inner），取并集（outer）。
3. **join_axes**
   默认值：join_axes=None，取并集
   合并后，可以设置非合并方向的行/列名称，使用某个df的行/列名称
4. **ignore_index**
   默认值：ignore_index=False
   合并方向是否忽略原行/列名称，而采用系统默认的索引，即从0开始的int。
5. **keys**
   默认值：keys=None
   可以加一层标签，标识行/列名称属于原来哪个df。



#### append

```python
append(self, other, ignore_index=False, verify_integrity=False)
```

竖方向合并df，没有axis属性

不会就地修改，而是会创建副本



#### merge

```python
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)
```

默认合并后只保留有共同列项并且值相等行（即交集）。如果没有共同列就会报错

 

##### **how**

​	how取值范围：'inner', 'outer', 'left', 'right'

​	默认值：how='inner'

​	‘**inner**’：共同列的值必须完全相等：

​	‘**outer**’：共同列的值都会保留，left或right在共同列上的差集，会对它们的缺失列项的值赋上NaN

​	‘**left**’：根据左边的DataFrame确定共同列的保留值，右边缺失列项的值赋上NaN

​	‘**right**’：根据右边的DataFrame确定共同列的保留值，左边缺失列项的值赋上NaN



### 聚合

```PYTHON
df_groupby = df.groupby("字段名")
```





## 数据库相关

### 保存

```python
df.to_sql(table_name, con, schema, if_exists, index)

# 其中con接受sqlalchemy.engine.connect
from sqlalchemy import create_engine
engine_connect = create_engine('mysql+pymysql://{帐户}:{密码}@{主机地址}:{端口号}/{数据库名}').connect()

```

> to_sql保存时，需要df与表中的列一一对应，若表不存在，会自动建表，并且每一个字段类型都是text
>
> 如果列不一一对应，会保存失败，这个限制很麻烦，常常自定义sql去执行



### 读取

```PY
data = pd.read_sql(sql ,con)
```







