---
title: Git使用详解
date: 2021-01-14 13:24:00
categories:
  - Git
tags:
  - Git
description: 本文介绍了Git常用的命令。
---



## 常用命令

**Convert remote's URL from `https` to `ssh`**:

```bash
# To check if remote's URL is ssh or https
git remote -v
# To switch from https to ssh
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

**Untrack files and don't change working directory**:

```bash
git rm --cached [filename]
```

**Reset `git add` operations**:

```bash
# reset staging area, but leave the working directory unchanged
git reset HEAD .
git reset

# Remove <file> from the staging area, but leave the working directory unchanged
git reset <file>

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

**Git diff**:

```bash
# show difference between working directory and last commit
git diff HEAD

# show difference between changes and last commit
git diff --cached
```

## 常见问题

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