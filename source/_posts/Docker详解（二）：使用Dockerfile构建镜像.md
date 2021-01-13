---
title: Docker详解（二）：使用Dockerfile构建镜像
date: 2021-01-08 14:48:22
categories:
  - 操作系统
  - Docker
tags: 
  - 操作系统
  - Docker
description: 本文对使用Dockerfile进行镜像构建进行了详解。
---

Dockerfile 是一个用来构建镜像的文本文件，文本内容包含了一条条构建镜像所需的指令和说明。本节内容参考[链接](https://www.runoob.com/docker/docker-dockerfile.html)。

下面所示是一个基本的Dockerfile示例：

```html
FROM ros:kinetic-perception

ENV CATKIN_WS=/root/catkin_ws
RUN git clone https://github.com/ceres-solver/ceres-solver.git
```

`FROM`指令用于指定构建的镜像所依赖的基础镜像文件，实例中设置为`ros:kinetic-perception`

`RUN`指令用于执行后面跟着的命令行命令

`ENV`指令用于设置环境变量，定义了环境变量，那么在后续的指令中，就可以使用这个环境变量

`COPY`指令用于从上下文目录中复制文件或者目录到容器里指定路径

`WORKDIR`指令用于指定工作目录。用 WORKDIR 指定的工作目录，会在构建镜像的每一层中都存在。`WORKDIR` 指定的工作目录，必须是提前创建好的。docker build 构建镜像过程中的，每一个 RUN 命令都是新建的一层。只有通过 `WORKDIR` 创建的目录才会一直存在。

**注意**：Dockerfile 的指令每执行一次都会在 docker 上新建一层。所以过多无意义的层，会造成镜像膨胀过大。例如：

```bash
FROM centos
RUN yum install wget
RUN wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz"
RUN tar -xvf redis.tar.gz
以上执行会创建 3 层镜像。可简化为以下格式：
FROM centos
RUN yum install wget \
    && wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz" \
    && tar -xvf redis.tar.gz
```

使用以下命令，根据当前路径下的Dockerfile构建名为`my-ros`的镜像：

```bash
docker build -t my-ros .
```

