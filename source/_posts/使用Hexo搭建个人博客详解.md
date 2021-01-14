---
title: 使用Hexo搭建个人博客详解
date: 2021-01-03 21:51:55
categories:
  - 网站搭建
tags: Hexo
description: 本文简单介绍了使用Hexo搭建个人博客的方法。
---

## 1. 环境配置

搭建个人网站前，首先从[链接](http://nodejs.cn/download/)下载`nodejs`安装包并进行安装，建议安装最新版本。安装后需确认将`node.js`安装路径添加到了系统环境变量中，例如：

```bash
D:\Program\nodejs\
```

## 2. Hexo安装及操作

### 2.1 安装Hexo

输入如下命令安装`Hexo`:

```bash
npm i hexo-cli -g
```

安装完成后输入以下指令验证是否安装成功：

```bash
hexo -v
```

运行上述指令时可能弹出“在此系统上禁止运行脚本”错误，其原因是Windows系统处于安全考虑，默认禁止脚本文件运行，可以通过在以管理员身份运行的`Powershell`中执行以下命令并选择`Y`选项解决：

```bash
set-executionpolicy remotesigned
```

之后输入如下命令安装其他依赖项：

```bash
npm install
```

### 2.2 初始化博客文件夹

创建用于存放博客内容的文件夹，并在该文件夹内打开`Powershell`输入如下命令，初始化文件夹：

```bash
hexo init 
```

### 2.3 常用操作

创建新的`post：

```bash
hexo new "文件名"
```

从当前`Markdown`文档生成网页：

```bash
hexo generate
hexo g
```

本地预览生成的网站：

```bash
hexo static
hexo s
```

将网站布置到云端：

```bash
hexo deploy
hexo d                                                              
```

## 3. 主题选择



## 4. 图床选择

### 4.1 Github图床

我们可以选择Github仓库作为图床。

#### 4.1.1 创建Github Repository

创建用于保存图片的仓库，将访问权限设置为公开。

#### 4.1.2 创建Token

点击Github网页版右上角头像，进入`设置`，在页面最下找到`Developer settings`点击进入，然后依次点击`Personal access token `，`创建token`，创建时设置如下：

![img](https://raw.githubusercontent.com/Tenant/Tenant.github.io/assets/images/aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3llZmNpb24vUGljRGF0YS9tYXN0ZXIvaW1nLzE1NTIzMTQ5MDc3OTQucG5n)

Token description根据实际情况填写，`repo`下项必须勾选，其他项随意，创建成功后会生成一团字符token。

#### 4.1.3 PicGo安装和配置

PicGo是一个开源的图床工具，非常优秀。从[官网](https://github.com/Molunerfinn/PicGo)下载安装后，打开软件，在图床设置中选择`Github图床`，根据实际情况填写相应项目。

#### 4.1.4 Typora配置

Typora可以和PicGo联动，实现从剪切板复制到Typora的图片自动通过PicGo上传图床并在Typora中引用。配置时依次打开Typora的Preference->Image，然后按照下图进行配置。

![image-20210114005827658](https://raw.githubusercontent.com/Tenant/Tenant.github.io/assets/images/image-20210114005827658.png)

配置完成后将剪切板中的图片复制到Typora，然后右键选择“上传图片”即可。

#### 4.1.5 其它问题

将Github作为图床有时候会出现图片加载失败的现象，这多半是由于DNS污染引起的，通过在`C:\Windows\System32\drivers\etc`内的`hosts`文件中添加如下内容直接对相关IP地址进行解析即可。

```bash
192.30.253.112    github.com 
192.30.253.119    gist.github.com
151.101.184.133    assets-cdn.github.com
151.101.184.133    raw.githubusercontent.com
151.101.184.133    gist.githubusercontent.com
151.101.184.133    cloud.githubusercontent.com
151.101.184.133    camo.githubusercontent.com
151.101.184.133    avatars0.githubusercontent.com
151.101.184.133    avatars1.githubusercontent.com
151.101.184.133    avatars2.githubusercontent.com
151.101.184.133    avatars3.githubusercontent.com
151.101.184.133    avatars4.githubusercontent.com
151.101.184.133    avatars5.githubusercontent.com
151.101.184.133    avatars6.githubusercontent.com
151.101.184.133    avatars7.githubusercontent.com
151.101.184.133    avatars8.githubusercontent.com
```

### 4.2 七牛云

七牛云的免费域名只有一个月的使用期，到期将被回收，所以暂时不使用。