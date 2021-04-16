---
title: CUDA安装与配置
date: 2021-04-16 18:08:46
categories:
  - CUDA
tags:
  - CUDA
description: 本文介绍了Git常用的命令。
---

## 安装与卸载
### 卸载

```bash
# Uninstall CUDA

sudo apt-get remove cuda
sudo apt-get autoclean
sudo apt-get remove cuda*

cd /usr/local/
sudo rm -r cuda*

# Uninstall cuDNN

cd ~/bin
sudo rm -r cuda*
```

