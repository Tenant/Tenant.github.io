---
title: Docker详解（一）：安装和常见操作
date: 2021-01-05 12:19:28
categories:
  - 操作系统
  - Docker
tags: 
  - 操作系统
  - Docker
description: 本文对常用的Docker指令进行了详细的归纳总结。
---

## 1. Docker Install

完整Docker安装过程参考[链接](https://docs.docker.com/get-docker/)。下面的安装以Ubuntu系统为例。

### 1.1 卸载原有安装

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

### 1.2 添加Docker源仓库

```bash
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=arm64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

### 1.3 安装Docker Engine

安装最新版本：

```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

安装指定版本：

```bash
apt-cache madison docker-ce
# select from the all available versions
sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
```

### 1.4 验证安装(Optional)

```bash
sudo docker run hello-world # This command downloads a test image and runs it in a container
```

### 1.5 卸载Docker

使用以下命令卸载安装：

```bash
sudo apt-get purge docker-ce docker-ce-cli containerd.io
```

如需彻底删除Docker产生的文件，执行以下命令：

```bash
sudo rm -rf /var/lib/docker
```

## 2. Docker配置

本节内容不影响Docker的正常使用，但恰当的配置可以改善Docker使用体验。

### 2.1 允许非root用户使用docker

因Docker使用Unix socket进行通讯，而在Linux系统中仅root用户可以访问Unix socket，所以通常使用Docker时需要添加`sudo`命令。为了解决这个问题，需要为系统添加一个名为`docker`的组，设置该组拥有和`root`相同的权限，并令当前用户属于该组。

```bash
sudo groupadd docker # create a group named `docker`
sudo usermod -aG docker $USER # add current user to the group `docker`
newgrp docker # force re-evaluate the group membership
docker run hello-world # verify docker can be runned without sudo
```

若系统之前运行过Docker，修改后可能出现以下错误：

```bash
WARNING: Error loading config file: /home/user/.docker/config.json -
stat /home/user/.docker/config.json: permission denied
```

使用下述命令修复：

```bash
sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
sudo chmod g+rwx "$HOME/.docker" -R
```

本部分内容完整版见[链接](https://docs.docker.com/engine/install/linux-postinstall/)。

## 3. Docker使用

### 3.1 获取Image

List all `image`:

```bash
docker images ls
```

产出指定`Image`：

```bash
docker image rm {imageName}
```



### 3.2 创建Container

Create `container` from `image`:

```bash
docker run -d --name={containerName} {imageName} tail -f /dev/null
```

Create `container` with `X11` from `image`:

```bash
xhost +
sudo docker run -d -v /etc/localtime:/etc/localtime:ro -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY -e GDK_SCALE -e GDK_DPI_SCALE --name {containerName} {imageName}
```

显示当前所有运行中的`container`：

```bash
docker container ls
```

显示当前已创建的所有`container`：

```bash
docker container ls -a
```

删除指定`container`：

```bash
docker container rm  {containerName}
```

### 3.3 Container的运行与停止

Start or stop `container`:

```bash
sudo docker start/stop {containerName}
```

Open a running `container` in `bash`:

```bash
sudo docker exec -it {containerName} bash
```

### 3.4 Container和Host间操作

Copy files between `host` and `container`:

```bash
sudo docker cp ~/code/notepanda  {containerId}:/code
```

### 3.5 保存Container

Save `container` as `image`:

```bash
sudo docker commit {containerId} {savedImageName}
```



### 3.2 Update Image

Update `image` with `container`:

```bash
sudo docker commit {containerId} {savedImageName}
```



### 3.3 Pull and Push

Login

```bash
sudo docker login
```

Push local`image` to remote:

```bash
sudo docker push {userName}/{imageName}
```