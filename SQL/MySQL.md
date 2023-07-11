# MySQL







# 存储过程

​		即数据库的可编程函数。

## 优缺点

优点：

- 在生产环境下，可以通过直接修改存储过程的方式修改业务逻辑或BUG，而不用重启服务器。
- 执行速度快，存储过程经过编译后会比单独一条执行快
- 减少网络传输开销
- 方便优化



缺点：

- 复杂业务处理的维护成本高
- 调试不便
- 不同数据库之间可移植性差

## 语法

``` SQL
DELIMITER //
CREATE PROCEDURE myproc([OUT|IN|INOUT name type,])
	begin
	-- 函数体
	end
//
		
```

**局部变量**

```sql
-- 自定义变量，在函数体中有效
-- declare name type [default value_1]

create procedure t_1()
begin
	-- set 赋值
	declare v1 varchar(32) default 'unkown';
	set v1 = 'str';
	select v1
	-- into 赋值
	declare t_name varchar(32) defaulut 'none';
	declare t_age int default 0;
	select name, age into t_name, t_age from user where id=1;
	select t_name, t_age;
end
```



**用户变量**

```sql
-- 自定义变量，在当前会话，连接中都有效
-- @var_name
```



会话变量 与 全局变量 是系统设定好的

### 判断

```sql
if
```



```sql
case
```





### 循环

```sql
-- loop死循环，需要使用leave退出循环，同样的可以用iterate来开始跳过下面的语句进入下一次循环
[begin_label:] LOOP
	if i >= 10;
	then leave [begin_label];
	end if;
	
	set i = i + 1
end loop [begin_label];
```



```SQL
-- repeat循环，直到statement为True时跳出
[begin_label:] repeat
	code;
until statement
end repeat [begin_label]
```

