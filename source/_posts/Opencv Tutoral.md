---
title: 三方库安装指南
date: 2021-04-09 21:29:21
categories:
  - 编程
  - C++
tags:
  - 编程
  - C++
description: 本文记录C++常用三方库的安装指南。
---

# 三方库安装指南

## OpenCV

```bash
# Install minimal prerequisites (Ubuntu 18.04 as reference)
sudo apt update && sudo apt install -y cmake g++ wget unzip
# Download and unpack sources
wget -O opencv.zip https://github.com/opencv/opencv/archive/master.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/master.zip
unzip opencv.zip
unzip opencv_contrib.zip
# Create build directory and switch into it
mkdir -p build && cd build
# Configure
cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-master/modules ../opencv-master
# Build
cmake --build .
```

## Protoc

从官网下载预编译好的版本放置在自己的安装目录下即可。

## Eigen

1. 从官网下载最新版本代码

2. 解压后进行如下操作

   ```bash
   mkdir -p 3rd/eigen/build
   cd 3rd/eigen/build
   cmake -DCMAKE_INSTALL_PREFIX=../install ..
   make install
   ```

   



