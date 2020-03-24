# TFtestgit
git下载自己项目到本地:
假如外出工作，需要在另一台电脑上面pull自己的某个git远程项目到本地；

 git init
 
 git pull https://github.com/TTyb/54qjLogin   （远程仓库url）
下载的这个项目更改后需要push的会出现：
$ git push
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using
 
    git remote add <name> <url>
 
and then push using the remote name
 
    git push <name>
此时：git remote用法
这个时候第一次push需要网址：
 
$ git add --all
$ git commit -m "提交信息"
$ git remote add origin '远程仓库url'
$ git push -u origin 对应远程分支名
 
 
 
然后下一次就不用那么麻烦了，直接：
 
$ git add --all
$ git commit -m "信息"
$ git push
————————————————
版权声明：本文为CSDN博主「COCOLI_BK」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/COCOLI_BK/article/details/97921497
