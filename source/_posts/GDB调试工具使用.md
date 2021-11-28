---
title: GDB调试工具使用
date: 2021-10-24 21:29:21
categories:
  - 编程
  - C++
tags:
  - 编程
  - C++
description: 本文记录了使用GDB进行调试的一些经验。
---

## 常用命令

### 流程控制

```bash
gdb --args executable_program arg1 arg2 arg3
> show args
> start
> step
> continue
> return
> return # or `r`
> quit # or `q`
> b function_name
> b lidar/lib/main.cc:60
> bt
```

### 查看变量和代码

```bash
> info variables # list all static and global variables
> info locals # list all local variables
> info args # list all args
```

