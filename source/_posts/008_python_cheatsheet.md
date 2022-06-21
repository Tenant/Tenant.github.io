---
title: Python常用命令
categories:
  - 编程
  - Python
tags:
  - 编程
  - Python
description: 本文记录了Python常用命令
---

## 1. 常用命令

### 1.1 字符串

```python
s.rfind('l') # if s = "hello", then this expression returns 3
"123".isdigit()
```

### 1.2 文件系统

```python
import os, sys
os.makedirs(r"E:/a/b/", exist_ok=True)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
abosulte_path = os.path.join(dir_path, filename)
if not os.path.exists(folder_path):
    os.
filenames = os.listdir(dir_path)
os.path.mkdirs(dir_path, exist_ok=True)
os.path.isdir(one_path)
os.path.isfile(one_path)
os.path.basename(one_path)
os.path.dirname(one_path)
os.remove(one_path)

files = glob.glob("./*/*_pose/*.pose")
```

### 1.3 格式化输出

```pytho
print("this is a string", flush=True)
```

### 1.4 类型判定

```python
dataset = dataset if isinstance(dataset, (list, tuple)) else [dataset]
```

### 1.5 循环遍历

```python
for i, (k, v) in enumerate(zip(names, values))
for k, v in zip(names, values)
```

### 1.6 numeric

```python
sys.float_info.min # 2.2250738585072014e-308
sys.float_info.max # 1.7976931348623157e+308
float('inf')
float('nan')
```

### 1.7 文件读写

```python
with open(filename, "w") as fout:
    print(" ".join(map(str， data)), file=fout)
    fout.flush()
```

### 1.8 Error/Exception

```python
raise ValueError("The {} does not exist".format(filename))
```

### 1.9 系统命令调用

```python
# demo 1
if not os.path.exists(data_dir):
    www = 'https://modelnet.cs.princeton.edu/ModelNet40.zip'
    zipfile = os.path.basename(www)
    os.system('wget %s; unzip %s' % (www, zipfile))
    os.system('mv %s %s' % (zipfile[:-4], base_dir))
    os.system('rm %s' % (zipfile))
# demo 2
import subprocess
args = "./3DSmoothNet -f " + point_cloud_files[i] + " -k " + keypoints_files[i] + " -o ./data/demo/sdv/"
subprocess.call(args, shell=True)
```

### 1.10 Setup

```bash
python3 setup.py install
```

## 2. 样例代码片段
