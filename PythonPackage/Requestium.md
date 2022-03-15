# Requestium

​		Requestium是集Requests和Selenium于一体的WEB自动化工具。Requestium可以看作是在Requests为主体的基础上增加了Selenium的部分功能

## Session

​		在requests的session基础上增加了一些selenium的功能模块，如web_driver。它允许我们在有需要的时候来回切换session与web_driver

```python
__init__(self, 
         webdriver_path, 		# webdriver_path
         browser, 				# browser_name， 'phantomjs','chrome'
         default_timeout=5, 
         webdriver_options={})	# webdriver_options { binary_location:, arguments:{}, }
```

​		在session和driver间的转换，似乎是通过transfer cookie来实现