# PowerBI

是一个实时的数据可视化看板。它本身没有数据存储的能力，需要从外部引用数据



## 数据结构

#### 列表

#### 记录

#### 表



## QUERY





### 常用函数

##### **ALL**



#### 数字

##### **CALCULATE**



##### **AVERAGE**







#### 文本

##### Text.BetweenDelimiters( 列名，符号1，符号2， 返回类型 )

​	将【列名】下的每一行文本中，"符号1"和"符号2"中间的数据提取出来





#### 时间

##### previousmonth

时间点：根据所选时间点获取上一个完整月的数值统计

时间段：后点没有影响，以时间前点为基准获取前点上一个完整月的数值统计



##### DATEADD

返回一个表，此表包含一列日期，日期从当前上下文中的日期开始按指定的间隔数向未来或过去推移

###### dateadd -1 month

时间点：根据所选日期获取上月对应日期的数值统计，若遇上月底，则匹配上月月底
时间段：同时受到时间前点和时间后点的影响，获取此时间区间上个月对应区间的数值统计，若包含月末则以上月末日期为准



##### PARALLELPERIOD

类似DATEADD，但它



##### totalmtd



## DAX







### 常用函数



##### SWITCH





#### 
