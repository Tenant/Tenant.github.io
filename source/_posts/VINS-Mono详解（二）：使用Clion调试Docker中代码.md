---
title: VINS-Mono详解（二）：使用Clion调试Docker中代码
date: 2021-01-09 15:41:43
categories:
  - SLAM
  - vSLAM
  - VINS
tags:
  - SLAM
  - vSLAM
  - VINS
description: 本节详述了如何在Docker中配置VINS-Mono的环境并使用本地的Clion进行调试开发。
---

本节内容参考[链接](https://blog.jetbrains.com/clion/2020/01/using-docker-with-clion/)。

## 1. 构建Docker

为了构建支持远程调试的Docker，需要在`Docker`文件中添加如下命令：

```bash
RUN apt-get update && apt-get install -y openssh-server rsync gdb gdbserver && \
    mkdir /var/run/sshd && \
    echo 'root:root' | chpasswd && \
    sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
    sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd && \
    sed -i 's/\(^Port\)/#\1/' /etc/ssh/sshd_config && echo Port 2233 >> /etc/ssh/sshd_config

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 2233 7777 # 22 for ssh server. 7777 for gdb server

# RUN useradd -ms /bin/bash debugger
# RUN echo 'debugger:pwd' | chpasswd
```

注意，上面的命令中，为了防止`Docker`和`Host`的SSH端口发生冲突，将`Docke`的`SSH`端口重定向到了`2233`

端口。

然后运行如下命令，构建镜像：

```bash
docker build -t ros:vins-mono-screen .
```

## 2. 实例化镜像

```bash
docker run -it --name vins-mono-screen --network host ros:vins-mono-screen
```

示例化镜像后通过以下命令测试`ssh`配置是否成功：

```bash
ssh -p 2233 root@localhost
```

若提示密码设置不成功，可以通过以下命令重设密码：

```bash
passwd root
```

若`Docker`中SSH服务没有启动，或手工更改了`\etc\ssh\sshd_config`中的参数，可以通过以下命令操作：

```bash
/etc/init.d/ssh restart
/etc/init.d/ssh start
```

## 3. 配置Clion

### 3.1 配置Toolchains

<img src = "http://qmt3iojod.hn-bkt.clouddn.com/FoyKTY1LxsYpFCEwtE3zlbWjckQ-" width="600px"/>



### 3.2 配置Deployment

<img src = "http://qmt3iojod.hn-bkt.clouddn.com/FvB7rmC9FnuaTiQIKIQwOan1NXMd" width="600px"/>

<img src = "http://qmt3iojod.hn-bkt.clouddn.com/FkJf3pZQw4NiCYVWV6lKVeAxmbjV" width="600px"/>

`Local Path`的文件会上传到`Deployment Path`，然后在远程编译，完成配置后记得Resync代码。

### 4. 打开项目

完成以上配置后，打开工程项目。此时注意因为Clion通过SSH连接到Container时，是没有`source`ROS的安装路径的，所以此时`CMakelists.txt`中`find_package(catkin)`将报错，此时，需要在`CMakelists.txt`中`find_package(catkin)`前添加如下命令：

```cmake
set(CMAKE_PREFIX_PATH /opt/ros/kinetic /root/catkin_ws/devel)
```

另外，需要在Clion的Run/Debug Configurations中，增加相应的环境变量：

```bash
ROS_MASTER_URI=http://localhost:11311 # ros master
```



