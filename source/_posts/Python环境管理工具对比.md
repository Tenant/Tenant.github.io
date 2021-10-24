---
title: Python环境管理工具对比
date: 2021-05-25 17:11:14
categories:
  - 编程
  - Python
tags:
  - 编程
  - Python
description: 本文对常用的Python环境管理工具及其使用方法进行了整理。
---

部分开源Python程序有较为复杂的环境依赖，为了解决在同一系统安装不同开源程序的需求，Python环境管理工具应用而生。

## Anaconda

相比而言，Anaconda的优点在于可以在环境配置过程中自定义Python版本并完成自动化安装。

### 安装和配置源

1. 官网下载安装脚本：

   [Installing on Linux — Anaconda documentation](https://docs.anaconda.com/anaconda/install/linux/)

2. 执行如下命令安装脚本

   ```bash
   mkdir -p ~/net_ws/3rd/conda
   bash Anaconda3-xxxx.xx-Linux-x86_64.sh
   ```

   在随后的启动的安装流程中，将anaconda安装路径设置为`~/net_ws/3rd/conda`，并拒绝之后脚本自动修改bash的选项。

3. 然后在anaconda目录下新建`setup.sh`脚本，输入如下信息：

   ```bash
   eval "$(/home/calc/net_ws/3rd/conda/bin/conda shell.bash hook)"
   conda config --set auto_activate_base true
   ```

4. 之后需要使用anaconda时，在bash中source该脚本即可。可以在terminal中输入如下命令检测是否安装成功：

   ```bash
   conda list
   ```

5. 更换Conda源

   创建`~/.condarc`文件，并填写如下内容：

   ```bash
   channels:
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
   ssl_verify: true
   ```

### 创建、删除、激活和退出环境

列出当前创建的所有环境：

```bash
conda info -e
```

创建环境

```bash
conda create --name py36 python=3.6 
```

删除环境

```bash
conda remove --name py36 --all
```

重命名环境

```bash
conda create --name new_name --clone old_name
conda remove --name old_name --all
```

激活环境

```bash
conda activate py36
```

退出环境

```bash
conda deactivate
```



### 常用Conda环境安装

#### spconv

```bash
conda create --name spconv-1.2 python=3.6 pytorch=1.4 cudatoolkit=10.1 --channel pytorch --channel=conda-forge
conda activate spconv-1.2
conda install cudnn
conda install boost
git clone https://gitee.com/calcite/spconv.git --recursive
cd spconv/third_party/pybind11/
git clone https://gitee.com/calcite/clang-cindex-python3.git clang --recursive
git reset --hard 6a00cbc
python setup.py bdist_wheel
pip install spconv-1.2.1-cp36-cp36m-linux_x86_64.whl
```

#### Pytorch

```bash
conda install pytorch torchvision torchaudio cudatoolkit=11.2 -c pytorch
```

## VirtualEnv

VirtualEnv是一个轻量化的Python环境管理工具，但是安装只能基于系统已有的Python版本，不能进行自动化安装。

### 常见VirtualEnv环境安装



## Docker

Docker是系统级的虚拟环境，可以实现最大程度的环境独立，但相应的磁盘消耗也最大，对于一些依赖比较复杂的程序，使用Docker构建开发环境是最为便利的。

当前大量开源程序作者都会给出Docker安装文件，使用Docker是最为简便的环境配置方法。但是使用Docker环境进行开发不便于GUI IDE的使用，特别对于调试而言。

Docker的使用方法见如下链接：

[Tag: Docker | 亓淇小站 (calria.plus)](https://blog.calria.plus/tags/Docker/)













