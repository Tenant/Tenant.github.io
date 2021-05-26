---
title: CMake用法详解
date: 2021-01-05 12:24:12
categories:
  - C++
  - CMakelist
tags: 
description: 本文对CMake的常见用法进行了总结归纳。
---

## 安装

使用源码安装CMAKE可以对版本进行指定。

首先从官网下载对应平台的源码，并进行解压。解压后执行如下命令：

```bash
./bootstrap
make
make install
```



## 常用命令

### Interface Changing

`CMake 3.12`中将`add_definitions`修改为``add_compile_definitions()` 。

```cmake
add_definitions(-DQURL_NO_CAST_FROM_STRING) # < 3.12
add_compile_definitions(QURL_NO_CAST_FROM_STRING) # >= 3.12
```



## 示例

```cmake
cmake_minimum_required(VERSION 3.5)
project(LOAM)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_BUILD_TYPE Debug)

find_package(OpenCV REQUIRED)
find_package(PCL REQUIRED)
find_package(Boost 1.6 REQUIRED)

include_directories(${OpenCV_INCLUDE_DIRS})
        ${PCL_INCLUDE_DIRS}
        ${Boost_INCLUDE_DIRS}
        .
        ./DsvLoading
        ./ScanRegistration
        ./LaserOdometry
        ./LaserMapping)
link_directories(${PCL_LIBRARY_DIRS})

AUX_SOURCE_DIRECTORY(. DIR_SRCS)
AUX_SOURCE_DIRECTORY(./DsvLoading DIR_DL_SRCS)
AUX_SOURCE_DIRECTORY(./ScanRegistration DIR_SR_SRCS)
AUX_SOURCE_DIRECTORY(./LaserOdometry DIR_LO_SRCS)
AUX_SOURCE_DIRECTORY(./LaserMapping DIR_LM_SRCS)

add_executable(LOAM
        ${DIR_SRCS}
        ${DIR_DL_SRCS}
        ${DIR_SR_SRCS}
        ${DIR_LO_SRCS}
        ${DIR_LM_SRCS})
target_link_libraries(LOAM
        ${PCL_LIBRARIES}
        ${OpenCV_LIBS}
        ${Boost_LIBRARIES})
```