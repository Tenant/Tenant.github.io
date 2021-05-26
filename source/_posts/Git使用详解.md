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

**Transfer codes from `GitLab` to`GitHub`**:

- create an empty repo on GitHub

  ```c++
  git remote add githubhttps://yourLogin@github.com/yourLogin/yourRepoName.git
  git push --mirror github
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

对于不包含submodule的仓库，出现这种问题后，从网页版GitHub中下载源码即可。而对于包含submodule的仓库，一般是主仓库可以下载，但是其submodule下载失败。此时，可以在clone主仓库后，分别clone每个子仓库，再将其放置到父仓库对应的目录下。如对于spconv仓库而言，可以通过如下操作解决问题。

```bash
git clone ... --recursive
cd spconv/third_party
git clone ... --recursive
```

