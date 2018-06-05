### 快速运行开发
#### 准备 git 环境
1. 安装git
```
# Linux
$ sudo yum install git
$ git --version

# Windows
# 下载gitbash

# MAC
# 参考：https://code.google.com/archive/p/git-osx-installer/
```
2. 通过ssh连接到github
这一步遇到问题直接参考 [github 文档](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-mac)
生成新的 ssh key
```
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
在 ssh-agent 中添加 ssh key
```
# 确保 ssh-agent 在后台运行
$ eval $(ssh-agent -s)
Agent pid 15044
```
添加 ssh private key 到 ssh-agent
```
$ ssh-add ~/.ssh/id_rsa

# MAC 方式
$ ssh-add -K ~/.ssh/id_rsa
```

3. 在 github 上设置添加 ssh public key
主要是把公钥复制到剪切板，然后去粘贴添加就好了，可以参考 [github 文档](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
```
# Linux 复制到剪切板的方式
$ sudo apt-get install xclip
$ xclip -sel clip < ~/.ssh/id_rsa.pub

# windows 复制到剪切板的方式
$ clip < ~/.ssh/id_rsa.pub

# MAC  复制到剪切板的方式
$ pbcopy < ~/.ssh/id_rsa.pub
```

#### 把项目拉到本地
1. 初始化 git 环境并拉取文件
```
$ git init
$ git config --global user.name "Your Name"
$ git config --global user.email "email@email.com"
$ git remote add origin git@github.com:gitname/repositoryname.git
$ git remote -v
$ git pull origin master --allow-unrelated-histories
$ git clone https://github.com/gitname/repositoryname.git
```
2. 准备 Python 
此项目依赖的是 python3 的环境，自行搜索 python 环境安装过程。如果需要虚拟环境，也自行搜索。 命令记录
```
$ virtualenv blogproject_env

# windows
$ blogproject_env\Scripts\activate

# linux
$ source blogproject_env/bin/activate
```
3. 安装项目依赖
```
$ pip install -r requirements.txt
```
4. 迁移数据库
```
$ python manage.py migrate
```
5. 命令行运行
```
$ python manage.py runserver
```
6. 浏览器打开 127.0.0.1:8000 查看效果
#### 修改代码远程提交简单说明
```
$ git status # 查看状态
$ git diff filename  # 查看文件改动
$ git add filename # 把改动的文件添加到缓存区
$ git commit -m "注释" # 提交改动的文件
$ git push -u origin master # 提交到远程 master 不建议直接操作线上环境
```
跟多 git 说明参考 [git 笔记](https://github.com/xiao201208/gitlearner/blob/master/gitnote.txt)