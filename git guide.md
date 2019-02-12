Git & GitHub 指南
-----------------

- 新建文件： `touch newfile`
- 列出当前路径下所有文件名称： `ls`
- 转到相应路径： `cd 路径名称`
- 用vim编辑文件： `vim 文件名称`
- 直接编辑文件： echo "# test again!" >> "test.md"
- 显示文件内容：　cat 文件名称

# 安装git 
1. [下载地址](https://gitforwindows.org/)
2. 配置用户名和邮箱地址
	```git
	git -config --global user.name 'glc jasper'
	git -config --global user.email 'glc_luck@outlook.com'
	```

# git常用命令
1. 创建仓库
   `git init <文件夹名称>`
   git init 命令来初始化一个 Git仓库
   Git 仓库会生成一个.git目录，该目录包含了资源的所有元数据，其他的项目目录保持不变 
   当你执行 git init 的时候，缺省情况下 Git 就会为你创建"master"分支。
   for example:
   ```git
   mkdir runoob
   cd runoob/
   git init
   ```
   等价于 `git init runoob`

2. clone
	`git clone <repo> <directory>`
	使用 git clone 从现有 Git 仓库中拷贝项目
	其中repo表示git仓库 directory是本地目录
	for example: `git clone git://github.com/schacon/grit.git mygrit`

3. git status
	`git status -s`
	查看项目的当前状态,会显示每个文件的状态，-s表示显示简短内容，含义如下：
	??: 未放入缓存区
	A: 该文件已放入缓存区且**未被修改**
	git branch (branchname)
	AM: 该文件已放入缓存区,但**随后被修改** 可以使用git add重新放入缓存区
3. git add & git commit
	```
	git add <文件名称/.>  # .表示全部文件
	git commit -m "你想写的注释"
	```
	git add 命令可将该文件添加到缓存（索引区，暂存区）
	执行 git commit 将缓存区内容添加到仓库中
	如果你觉得修改文件后，先add再commit很麻烦，可以用如下命令： `git commit -am '修改 hello.php 文件'`

4. git rm
	`git rm <file>` 
	如果要删除的文件已经add，则必须加入强制删除选项 `-f`
	`git rm -f <file>`
	如果把文件从暂存区域中移除，但仍然希望保留在当前工作目录中，换句话说，仅是从跟踪清单中删除:
	`git rm --cached <file>`


# git 分支管理
几乎每一种版本控制系统都以某种形式支持分支。使用分支意味着你可以从开发主线上分离开来，然后在不影响主线的同时继续工作。 
- 创建分支 
	`git branch (branchname)` 省略branchname表示列出你在本地的分支
	`git checkout -b (branchname)` 创建新分支并立即切换到该分支下，从而在该分支中操作

- 切换分支 `git checkout (branchname)` 
当你切换分支的时候，Git 会用该分支的最后提交的快照替换你的工作目录的内容， 所以多个分支不需要多个目录。
- 合并分支 
	`git merge　（分支名称）` 　将（分支名称）合并到当前分支
	你可以多次合并到统一分支， 也可以选择在合并之后直接删除被并入的分支。 

- 删除分支　｀git branch -d <branchname> 
```
git branch # list all local branches/ only master
git branch testing # creating new branch named 'testing'
git branch # master and testing
git checkout testing # switch to branch 'testing'
ls # list all files in current branch
echo 'runoob.com' > test.txt  # create a file in 'testing' branch
git add.
git commit -m "add test.txt"
git checkout master # switchc to 'master' branch
git merge testing
```

# git查看提交历史
- `git log`
- `git log --oneline` 
- `git log --oneline --graph`
- `git log --author=jasperGui --oneline -5` # -5表示最近修改的５条
如果想看 Git 项目中三周前且在四月十八日之后的所有提交，可以用如下命令：
- `git log --oneline --before={3.weeks.ago} --after={2010-04-18} --no-merges`
如果想查看标签等装饰的记录，可以用如下命令：
- `git log --oneline --decorate --graph`

# git标签
如果你达到一个重要的阶段，并希望永远记住那个特别的提交快照，你可以使用 git tag 给它打上标签
比如说，我们想为我们的 runoob 项目发布一个"1.0"版本。 我们可以用 `git tag -a v1.0` 命令给最新一次提交打上（HEAD）"v1.0"的标签。

如果我们忘了给某个提交打标签，又将它发布了，我们可以给它追加标签。首先通过如下命令查看提交历史：
`git log --oneline --decorate --graph`
然后找到需要打标签的提交所对应的编码(比如是85fc7e7)，执行如下命令：
`git tag -a v0.9 85fc7e7`

可以使用`git tag`查看所有标签


# git远程仓库
本例使用了 Github 作为远程仓库

## 配置git连接到github远程仓库： 
1. 在bash命令窗口键入： `ssh-keygen -t rsa -C "glc_luck@outlook.com" `
2. 一路enter，注意千万不要设置密码（这里是ssh文件的密码，不是github密码），否则以后每次和远程进行沟通时都要输入密码
3. 成功后会在屏幕上显示.ssh文件的生成位置，打开该文件夹，找到id_rsa.pub文件，用记事本打开，复制所有内容
4. 登录github，在setting中找到SSH and GPG keys选项，点击New SSH key，在key中输入复制内容，title可以随便填
5. 在bash命令窗口键入：`ssh -T git@github.com` 来确认是否成功配置

## 添加一个远程仓库
` git remote add origin git@github.com:glcLucky/finance_plan.git`
其中origin为别名，可随便取　git@github.com:glcLucky/finance_plan.git为远程仓库地址（https or ssh)

## 常用命令
- ` git remote add origin git@github.com:glcLucky/finance_plan.git` 添加一个远程仓库

- `git remote -v` 查看当前连接的远程仓库别名及地址

- `git push [alias] [branch]` 将你的 [branch] 分支推送成为 [alias] 远程仓库上的 [branch] 分支

- ```
  git fetch origin master:tmp //从远程仓库master分支获取最新，在本地建立tmp分支
  git diff tmp //將當前分支和tmp進行對比
  git merge tmp //合并tmp分支到当前分支
  ```

或者，也有另一种方法

-
 ```
 git fetch orgin master //将远程仓库的master分支下载到本地当前branch中
 git log -p master  ..origin/master //比较本地的master分支和origin/master分支的差别
 git merge origin/master //进行合并
 ``` 

也可以使用git pull 相当于是从远程获取最新版本并merge到本地
`git pull origin master`