---
title: OpenCV详解（一）：编译与安装
date: 2021-01-03 21:15:12
categories: 
  - C++
  - OpenCV
tags: 
  - OpenCV
---

本文总结了编译OpenCV时常用的参数设置方式。

<!--more-->

## 1. Ubuntu环境

### 1.1 Without CUDA

OpenCV编译命令

```bash
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D OPENCV_EXTRA_MODULES_PATH=../contrib/modules \
-D PYTHON3_EXCUTABLE=/usr/bin/python \
-D WITH_CUDA=OFF \
-D WITH_TBB=ON \
-D WITH_V4L=ON \
-D WITH_GTK=ON \
-D WITH_OPENGL=ON \
-D WITH_VTK=ON \
-D WITH_QT=ON \
-D WITH_FFMPEG=ON \
-D BUILD_EXAMPLES=ON ..
```

### 1.2 With CUDA

带CUDA的OpenCV编译

```bash
###这是带cuda的，下面带颜色的数值要自己查###查询网址：查看cuda型号网址
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D OPENCV_EXTRA_MODULES_PATH=../contrib/modules \
-D PYTHON_EXCUTABLE=/usr/bin/python \
-D WITH_CUDA=ON \
-D WITH_CUBLAS=ON \
-D DCUDA_NVCC_FLAGS="-D_FORCE_INLINES" \
#-D CUDA_ARCH_BIN="5.2" \
#-D CUDA_ARCH_PTX="" \
-D ENABLE_FAST_MATH=1 \
-D CUDA_FAST_MATH=ON \
-D WITH_CUFFT=ON \
-D WITH_NVCUVID=ON \
-D WITH_TBB=ON \
-D WITH_V4L=ON \
-D WITH_GTK=ON \
-D WITH_OPENGL=ON \
-D WITH_VTK=ON \
-D WITH_QT=ON \
-D WITH_FFMPEG=ON \
-D BUILD_EXAMPLES=ON ..
```

```bash
# cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_IPP=OFF -DWITH_FFMPEG=OFF -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.3.1/modules/ -D BUILD_opencv_dnn=ON ..

cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D FORCE_VTK=ON -D WITH_TBB=ON -D WITH_V4L=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D WITH_CUBLAS=ON -D CUDA_NVCC_FLAGS="-D_FORCE_INLINES" -D WITH_GDAL=ON -D WITH_XINE=ON -D BUILD_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.3.1/modules/ ..

make -j $(($(nproc) + 1))

sudo make install
```



## 2. Windows环境

### 2.1 使用预编译版本

OpenCV在Windows环境下有预编译版本可以直接从[官网](https://opencv.org/releases/)下载使用，但是需要注意预编译版本所依赖的`vc`版本一定要与本地开发用的`vc`版本一致。下载预编译版本后的使用方法参考[链接](https://blog.csdn.net/maizousidemao/article/details/81474834)。

### 2.2 自行编译

#### 2.1 安装CMake和Visual Studio

Windows下编译OpenCV需要安装CMake和Visual Studio，二者安装方法不再赘述。

#### 2.2 下载OpenCV源码



#### 2.3 使用CMake生成OpenCV项目

打开CMake软件，按照下图所示设置源码路径和生成结果保存路径：

![fig1](https://raw.githubusercontent.com/Tenant/Tenant.github.io/assets/images/fig1.png)

然后点击`Configure`，在弹出的窗口中选择对应的编译器：

![fig2](https://raw.githubusercontent.com/Tenant/Tenant.github.io/assets/images/fig2.png)

64位版本编译器应选择显式标注了Win64的版本。

然后在弹出的配置参数列表中，搜索`OPENCV_EXTRA_MODULES_PATH`，将其值设为指向`opencv_contrib/modules`文件夹的路径（路径需要包含`modules`）。搜索`WITH_CUDA`，根据是否需要CUDA对OpenCV进行加速决定是否勾选该项目。

然后反复点击`Configure`进行配置，直到配置结果无错误为止（无红底色项目，软件输出"Configuring done"）。配置过程中常见的错误和解决方法如下：

**Error 1**：CMake HASH mismatch error for ffmpeg

该错误目前尽在`OpenCV 3.2.0`中遇到。

**Error 2**：IPPCV: Download failed: 35; "SSL connect error"

此时，在`sources`目录下的`.cache`文件夹中会保存下载失败文件所对应的空文件。在`build`

文件夹下的`CMakeDownloadLog.txt`中找到该文件对应的下载链接进行重新下载，并对`.cache`中原本的空文件进行替换（需保持和空文件相同的文件名）。

然后点击`Generate`，生成OpenCV项目文件，软件输出"Generating done"表示成功。

#### 2.4 使用Visual Studio编译OpenCV

如图所示，使用Visual Studio打开前一步骤生成的项目文件：

![fig3](https://raw.githubusercontent.com/Tenant/Tenant.github.io/assets/images/fig3.png)

然后在Build -> Batch Build中进行如下配置，在点击`Build`进行编译。

<img src="https://raw.githubusercontent.com/Tenant/Tenant.github.io/assets/images/fig4.png" alt="fig4" style="zoom: 80%;" />

编译结果保存在`build/install`文件夹下，即为最终结果。

### 2.3 Visual Studio中OpenCV的配置。

本节内容可参考[链接](https://blog.csdn.net/hhhuang1991/article/details/79750828)。



