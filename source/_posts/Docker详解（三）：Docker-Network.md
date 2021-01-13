---
title: Docker详解（三）：Docker-Network
date: 2021-01-08 12:46:54
categories:
  - 操作系统
  - Docker
tags: 
  - 操作系统
  - Docker
description: 本节内容对Docker中Network的使用进行了详解。
---

更多内容参考[链接](https://docs.docker.com/network/)。

Docker的一大优势在于Docker支持不同Docker间以及Docker和Host间的网络通信，因此使用Docker可以允许不同环境、平台协同工作，这在开发涉及依赖较为复杂的项目时很有用处。

Docker通过`driver`实现网络通讯。



## 1. 使用Bridge Network

本节内容参考[链接](https://docs.docker.com/network/bridge/)。`Bridge`允许连接到同一`bridge`的`docker`间进行网络通讯。

### 1.1 创建User-defined Bridge

```bash
docker network create my-net # 更多用法通过docker network create --help获得
```

### 1.2 删除User-defined Bridge

```bash
docker network rm my-net
```

### 1.3 将Container连接到User-defined Bridge

下述命令创建一个名为`my-ros`的`container`，将`container`连接到名为`my-net`的Bridge网络桥，并将`container`的`80`端口映射到Host的`8080`端口。

```bash
docker run -it --name my-ros \
  --network my-net \
  --publish 8080:80 \
  ros:kinetic-ros-core
```

下述命令将当前正在运行的`container`连接到名为`my-net`的Bridge网络桥。

```bash
docker network connect my-net my-nginx
```

### 1.4  将Container从User-defined Bridge断开

```bash
docker network disconnect my-net my-nginx
```

## 2. 使用Host Network

本节内容参考[链接](https://docs.docker.com/network/host/)。使用Host network的container的网络不会和Host隔绝，此时`container`也不会有自己的`IP`地址。Host network只能用于Host系统为Linux的情况。

Container只能在创建时被连接到Host Bridge，命令如下：

下述命令创建一个名为`my-ros的`container`，将`container`连接到`Host`网络桥：

```bash
docker run -it --name my-ros \
  --network host \
  ros:kinetic-ros-core
```



## 3. 使用Overlay Network

本节更多内容可以参考[链接](https://docs.docker.com/network/overlay/)。