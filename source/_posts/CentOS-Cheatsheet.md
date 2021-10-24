---
title: CentOS Cookbook
date: 2021-10-24 21:29:21
categories:
  - 操作系统
tags:
  - 操作系统
  - CentOS
description: 本文记录了CentOS安装及使用的一些经验。
---

## 简介

首先我们需要清楚Linux内核和Linux发行版本不是一个概念。

Linux内核：是系统的心脏，是运行程序和管理像磁盘和打印机等硬件设备的核心程序，它提供了一个在裸设备与应用程序间的抽象层。Linux发行版：它是一个可以高效使用Linux 内核的操作系统，即它涵盖了Linux内核，此外还包含一些GNU程序库和工具，命令行shell，图形界面和相应的桌面环境，如KDE或GNOME，并包含数千种从办公套件，编译器，文本编辑器到科学工具的应用软件。典型的有CentOS、Ubuntu、RedHat、SUSE等。

CentOS与内核版本对应关系见[链接1](https://blog.csdn.net/t1506376703/article/details/97618900)和[链接2](https://access.redhat.com/articles/3078#RHEL8).

## 安装CentOS

首先从[官网](https://wiki.centos.org/Download)下载CentOS镜像下载，然后按照[教程](https://www.jianshu.com/p/9d5b9757a1ef)在虚拟机中安装CentOS。

对于CentOS 6.x，官方不再进行维护，需要修改yum软件源，以能够联网安装环境。一键更换yum源为CentOS的Vault源的操作如下：

```bash
wget -O /etc/yum.repos.d/CentOS-Base.repo http://file.kangle.odata.cc/repo/Centos-6.repo
wget -O /etc/yum.repos.d/epel.repo http://file.kangle.odata.cc/repo/epel-6.repo
yum makecache
```

## 内核编译

当使用了指定发行版本后，有时需要将内核版本升级到指定版本，这里有两种方法，第一种是使用`elrepo`进行在线更新，操作简单，但是对于有些指定版本，在上面可能找不到；第二种方法是编译内核版本的源码，这种方法的操作比骄傲复杂，但是灵活性比较高，可以安装任意版本的内核，且可以自己对内核进行再开发。

### 使用elrepo

1. 安装elrepo软件库的key

   ```bash
   rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
   ```

2. 将软件库添加到源

   ```bash
   rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-3.el7.elrepo.noarch.rpm # centos-7
   ```

3. 查看可用的软件源

   ```bash
   yum --disablerepo="*" --enablerepo="elrepo-kernel" list available
   ```

4. 安装内核

   ```bash
   yum --enablerepo=elrepo-kernel install kernel-ml
   ```

### 从源码编译内核

1. 从官方网站下载指定版本的内核，网址如下：https://www.kernel.org/，例如linux-4.14.1.tar.xz

2. 安装开发工具包，包括内核源码编译所需要的一些环境：

   ```bash
   yum groupinstall "Development Tools" -y
   ```

3. 安装常用工具软件

   ```bash
   yum install -y elfutils-libelf-devel bc openssl-devel ncurses-devel wget ntpdate vim net-tools
   ```

4. 同步时间，时间错误可能导致编译失败

   ```bash
   ntpdate -u times.aliyun.com
   ```

5. 解压内核源码

   ```bash
   tar xf linux-4.14.1.tar.xz -C /usr/src
   ```

6. 进行刚刚解压的内核源码的目录

   ```bash
   cd /usr/src/linux-4.14.1/
   ```

7. 将之前的内核版本的配置文件，拷贝一份到当前目录

   ```bash]
   cp /boot/config-3.10.0-1127.el7.x86_64 .config
   ```

8. 修改配置文件

   ```bash
   sh -c 'yes "" | make oldconfig'
   ```

9. 进行编辑

   ```bash
   make -j2 bzImage
   make -j2 modules
   make -j2 modules_install
   make install
   ```

10. 查看编译是否成功

    ```bash
    awk -F\' '$1=="menuentry " {print $2}' /etc/grub2.cfg
    ```

11. 将内核设置为默认启动，并重新启动

    ```bash
    grub2-set-default 0 && init 6
    ```

12. 重启成功后，检查内核是否安装成功

    ```bash
    uname -r
    ```

    

## 常用命令

查看发行版本

```bash
cat /etc/issue
```

查看系统内核

```bash
uname -r
```

