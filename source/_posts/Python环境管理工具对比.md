---
title: Python环境管理工具对比
date: 2021-05-25 17:11:14
tags:
---

## Anaconda

相比而言，Anaconda的优点在于可以在环境配置过程中自定义Python版本并完成自动化安装。

### 安装

```bash
wget 
chmod +X A
./A
```

安装过程中选择默认选项即可。

### 创建环境

```bash
conda create --name spconv-1.0 python=3.6 pytorch=1.1 cudatoolkit=9.2 cudatoolkit-dev=9.2 cmake --channel pytorch --channel=conda-forge
```

### 常用安装脚本

#### spconv

```bash
conda create --name spconv-1.0 python=3.6 pytorch=1.1 cudatoolkit=9.2 cudatoolkit-dev=9.2 cmake --channel pytorch --channel=conda-forge
conda activate spconv-1.0
conda install cudnn
conda install boost
git clone https://github.com/traveller59/spconv spconv_8da6f96 --recursive
cd spconv_8da6f96
git checkout 8da6f967fb9a054d8870c3515b1b44eca2103634
python setup.py bdist_wheel
```

$$
\frac{1}{P_{T}^2} = \frac{1}{\frac{1}{A}}
$$



## VirtualEnv

VirtualEnv是一个轻量化的Python环境管理工具，但是安装只能基于系统已有的Python版本，不能进行自动化安装。















