---
title: Windows常用命令
date: 2021-04-09 21:33:53
categories:
  - 操作系统
tags:
  - 操作系统
  - Windows
description: 本文记录了Windows平台下用的命令。
---

## 1. 系统和文件

### 1.1 文件硬链接

```powershell
mklink \H destination_file source_file # 在destination_file路径下创建指向source_file的硬链接
fsutil hardlink list filename.txt # 查找所有和filename.txt指向同一文件的硬链接
```

### 1.2 强制重新加载环境变量

```bash
set PATH=C:
echo %PATH%
```

打开磁盘管理器为U盘重新建立分区。

### 1.3 在CMD中计算文件MD5值

```bash
certutil -hashfile filename MD5
certutil -hashfile filename SHA1
certutil -hashfile filename SHA256
```

### 1.4 用U盘制作启动盘后空间变小的恢复方法

在命令行窗口执行如下命令:

```bash
diskpart
```

在弹出窗口运行如下命令:

```bash
list disk
select disk 1
clean
```

## 2. 软件程序

从CMD中打开回收站

```bash
explorer.exe ::{645FF040-5081-101B-9F08-00AA002F954E}
```

