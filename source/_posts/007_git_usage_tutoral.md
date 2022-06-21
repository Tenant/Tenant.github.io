---
title: Git使用详解
categories:
  - Git
tags:
  - Git
description: 本文介绍了Git常用的命令。
---

## 1. 常用操作

**设置默认编辑器为vim**

```bash
git config --global core.editor "vim"
```

**终端显示中文乱码**

```bash
git config --global core.quotepath false
```

**Convert remote's URL from `https` to `ssh`**:

```bash
# To check if remote's URL is ssh or https
git remote -v
# To switch from https to ssh
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

**Untrack files and don't change working directory**:

```bash
git rm --cached [filename]# untrack specified file
git reset HEAD file
git reset HEAD . # untrack all files
```

**Reset**

```bash
# reset staging area and reset working directory to match last commit
git reset --hard
# move the current brach tip backward to <commit>, reset the staging area to match, but leave the working directory alone
git reset <commit>
# same as precious, but resets both the staging area and working directory
git reset --hard <commit>
```

**Clean files**:

```bash
# Show which files would be removed from working directory
git clean -n
# Execute the clean
git clean -f
```

**Append changes to last commit**:

```bash
git commit --amend
```

**Display `commits` concerned with the specific file**:

```bash
git log -- <file>
```

**Diff**

```bash
# show difference between working directory and last commit
git diff
# show difference between changes and last commit
git diff --cached
git diff --name-only
git diff --name-status
```

**Stash**

```bash
git stash
git stash -- file_01 file_02
git stash -p
git stash list
git stash show -p stash@{0}
git stash drop stash@{0}
```

**Patch**

```
git format-patch <commit-id-head>
git am --abort
git am *.patch
git am *.patch --reject
```

**Reflog**

```bash
git reflog
```

**Tag**

```bash
git tag -a v0.1 -m ""
git tag -a v0.2 9fceb028
git push origin tag_name
git push origin --tags
```

**CherryPick**

```bash
git cherry-pick A^...B
```

**Checkout**

```bash
git checkout branch_name/commit_id/tag_name -- file_name
```

## 2. 常见问题

### 部分仓库下载缓慢/失败问题

**方法一**

对于不包含submodule的仓库，出现这种问题后，从网页版GitHub中下载源码即可。

**方法二**

对于包含submodule的仓库，一般是主仓库可以下载，但是其submodule下载失败。此时，可以在clone主仓库后，分别clone每个子仓库，再将其放置到父仓库对应的目录下，然后通过`git reset --hard commit_id`将子仓库切换到对应版本。

```bash
git clone xxx.git repo-a --recursive # failed
git clone xxx.git repo-a # success
cd repo-a/third_parth
git clone xxxx.git repo-b --recursive # success or fail
cd repo-b
git reset --hard commit_id
```

**方法三**

除了上述两种方法外，可以借助[我的工作台 - Gitee.com](https://gitee.com/)解决该问题。操作时首先将需要clone的仓库从GitHub中fork到Gitee中，然后从Gitee clone即可。对于包含submodule的仓库，可以将其submodule均fork到Gitee，并修改`.submodule`中对应仓库的路径为Gitee下的路径（注意此处路径结尾不包含`.git`字段）.
