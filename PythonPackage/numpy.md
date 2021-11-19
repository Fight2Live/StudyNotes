# numpy





## 创建np对象

```python
# 读取文本，CSV文件
np.genfromtxt(fpath, delimiter, dtype)

np.loadtxt(fpath, delimiter ,dtype, skiprows=0)
"""
skiprows=1 表示跳过首行
"""
```







## 数据转换



```ptython
n2 = n1.astype(type)  # 将n1中的元素都转换为type类型
```





## 合并



```python
np.append


np.concatenate


np.stack


np.vstack


np.hstack

```



