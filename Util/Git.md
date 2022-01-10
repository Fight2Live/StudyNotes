#  GitLab使用介绍and笔记

从一篇Git.pdf上得到的教程，我将其转移到这备用

和使用过程中的记录

## 提交新文件夹到远程仓库中：

   

```PYTHON
 # 新建本地仓库
 $ git init
 
 # 从远程的git仓库pull项目
 $ git pull 链接
 $ git add -A
 $ git commit -m '备注'
 $ git push 链接 分支
```


## 删除项目中的文件夹

```python
# 拉取远程的Repo到本地（如果已存在可略过）  

$ git clone [ssh链接]

# 在本地仓库删除文件

$ git rm my_file

# 在本地仓库删除文件夹，此处 -r 表示递归所有子目录。

$ git rm -r my_folder/

# 提交代码

$ git commit -m [msg]

# 推送到远程仓库

$ git push origin warehouse
```





## 新建代码库

```PYTHON
# 进入文件夹
$ cd "目标文件夹"

# 在当前文件夹新建Git代码库
$ git init

# 新建一个目录并初始化为Git代码库
$ git init "project-name"

# 下载一整个项目
$ git clone [ssh链接]
```

  


## 配置

```PYTHON
# 显示当前Git配置
$ git config --list
    
# 编辑Git配置
$ git config -e [--global]

# 设置提交代码时的用户信息
$ git config [--global] user.name "name"
$ git config [--global] user.email "email address"
```

## 添加文件到暂存区

```PYTHON
# 添加指定文件到暂存区
$ git add [file1] [file2] ...

# 添加指定目录到暂存区，包括子目录
$ git add [dir]

# 添加当前目录的所有文件夹到暂存区
$ git add .
```

## 代码提交到本地仓库

```PYTHON
# 提交暂存区到本地仓库区
$ git commit -m "操作备注"

# 提交暂存区的指定文件到仓库
$ git commit [file1] [file2] ... -m "操作备注"
```

## 撤销提交

```PYTHON
# HEAD^的意思是上一个版本，也可以写成HEAD~1
# --mixed是指既撤销commit，也撤销add，不删除工作空间改动代码
# --soft是指只撤销commit，不撤销add，不删除工作空间改动代码
# --hard是既撤销commit，也撤销add，删除工作空间改动代码
git reset --soft HEAD^ 
git reset --hard HEAD^ 
```



## 分支

  

```PYTHON
# 列出所有本地分支
$ git branch

# 列出所有远程分支
$ git branch -r

# 列出所有本地分支和远程分支
$ git branch -a

# 新建一个分支，但依然停留在当前分支
$ git branch "branch-name"

# 新建一个分支并切换到该分支
$ git checkout -b "branch-name"

# 删除分支
$ git branch -d "branch-name"
```

## 查看信息


​    

```PYTHON
# 显示所有变更文件
$ git status

# 显示当前分支的版本历史
$ git log

# 显示暂存区和工作区的差异
$ git diff

# 显示工作区与当前分支最新commit之间的差异
$ git diff HEAD
```

## 远程同步


```PYTHON
# 下载远程仓库所有变动
$ git fetch

# 显示所有远程仓库
$ git remote -v

# 显示某个远程仓库的信息
$ git remote show [remote]

# 取回远程仓库的变化，并与本地分支合并
$ git pull [remote] [branch]

# 上传本地指定分支到远程仓库
$ git push [remote] [branch]

# 强行推送当前分支到远程仓库，即使有冲突
$ git push [remote] --force

# 推送所有分支到远程仓库
$ git push [remote] -all
```



## .gitignore



```PYTHON
# 创建git_ignore配置文件
tourch .gitignore
# 里面写入add时跳过的文件名，运行通配符
```

