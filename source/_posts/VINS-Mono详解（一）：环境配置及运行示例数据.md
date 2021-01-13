---
title: VINS-Mono详解（一）：环境配置及运行示例数据
date: 2021-01-08 16:02:24
categories:
  - SLAM
  - vSLAM
  - VINS
tags:
  - SLAM
  - vSLAM
  - VINS
description: 本节详述了如何在本地配置VINS-Mono的环境并运行示例数据。
---

本教程使用Docker环境配置VINS-Mono的运行环境。

## 1. Docker安装

关于Docker的安装和基本操作，参考[Docker使用入门：安装和基本操作](https://tenant.github.io/2021/01/05/Docker%E4%BD%BF%E7%94%A8%E5%85%A5%E9%97%A8_%E5%AE%89%E8%A3%85%E5%92%8C%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C/)。

## 2. 构造镜像

首先从GitHub上下载官方源码：

```bash
git clone https://github.com/HKUST-Aerial-Robotics/VINS-Mono.git
```

设下载后的源码的根目录为`$VINS_MONO`，执行如下命令切换目录：

```bash
cd $VINS_MONO/docker
```

打开目录下的`Dockerfile`，将其修改为：

```bash
FROM ros:kinetic-perception
  
ENV CERES_VERSION="1.12.0"
ENV CATKIN_WS=/root/catkin_ws

      # set up thread number for building
RUN   if [ "x$(nproc)" = "x1" ] ; then export USE_PROC=1 ; \
      else export USE_PROC=$(($(nproc)/2)) ; fi && \
      apt-get update && apt-get install -y \
      cmake \
      libatlas-base-dev \
      libeigen3-dev \
      libgoogle-glog-dev \
      libsuitesparse-dev \
      python-catkin-tools \
      ros-${ROS_DISTRO}-cv-bridge \
      ros-${ROS_DISTRO}-image-transport \
      ros-${ROS_DISTRO}-message-filters \
      ros-${ROS_DISTRO}-tf && \
      rm -rf /var/lib/apt/lists/* && \
      # Build and install Ceres
      git clone https://github.com/ceres-solver/ceres-solver.git && \
      cd ceres-solver && \
      git checkout tags/${CERES_VERSION} && \
      mkdir build && cd build && \
      cmake .. && \
      make -j$(USE_PROC) install && \
      rm -rf ../../ceres-solver && \
      mkdir -p $CATKIN_WS/src/VINS-Mono/

# Copy VINS-Mono
COPY ../ $CATKIN_WS/src/VINS-Mono/

# use the following line if you only have this dockerfile
# RUN git clone https://github.com/HKUST-Aerial-Robotics/VINS-Mono.git
# Build VINS-Mono
WORKDIR $CATKIN_WS
ENV TERM xterm
ENV PYTHONIOENCODING UTF-8
RUN catkin config \
      --extend /opt/ros/$ROS_DISTRO \
      --cmake-args \
        -DCMAKE_BUILD_TYPE=Release && \
    catkin build && \
    sed -i '/exec "$@"/i \
            source "/root/catkin_ws/devel/setup.bash"' /ros_entrypoint.sh

```

然后运行如下命令构造镜像：

```bash
docker build -t ros:vins-mono .
```

## 3. 运行程序

基于前面构造的镜像，生成`container`：

```bash
docker run -it --name vins-mono \
  --network host \
  ros:vins-mono
```

进入生成的`container`后，通过以下命令启动程序：

```bash
roslaunch vins_estimator euroc.launch 
```

同时，在Host电脑上，使用以下命令回放示例数据：

```bash
rosbag play YOUR_PATH_TO_DATASET/MH_01_easy.bag
```

示例数据可以从[链接](http://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets)下载。

另外，再在Host电脑上打开窗口运行`rviz`：

```
rviz -d $VINS_MONO/config/vins_rviz_config.rviz
```



至此，成功完成环境配置和示例数据回放。