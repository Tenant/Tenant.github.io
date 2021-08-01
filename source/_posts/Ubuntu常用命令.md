---
title: Ubuntu常用命令
date: 2021-04-09 21:29:21
categories:
  - 操作系统
tags:
  - 操作系统
  - Ubuntu
description: 本文记录了Ubuntu平台下用的命令。
---

## 系统内核和文件系统

### 系统安装与配置

**更新系统软件源**

由于国内访问Ubuntu默认软件源速度较慢，在安装系统后需要更新软件源为国内镜像地址。下面的设置以阿里云为例。通过如下命令打开系统软件源文件。

```bash
vim /etc/apt/sources.list
```

使用如下内容替换`sources.list`里面的内容：

```bash
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
 
# src
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
```

需要注意，不同版本Ubuntu内核名称不同。其中，16.04对应的内核名称为`bionic`，18.04对应的内核名称为`melodic`，20.04对应的内核名称为`focal`。

替换完成后，执行如下命令更新软件源数据库。

```bash
sudo apt update
```

**更新Python源**

由于国内访问Python默认源速度较慢，在安装好Python后需要更新Python源为国内镜像地址。下面以清华源为例。通过如下命令打开Python源文件。

```bash
vim ~/.pip/pip.conf
```

如果该文件不存在，则使用下述命令创建文件。

```bash
mkdir -p ~/.pip
vim ~/.pip/pip.conf
```

使用如下内容替换`pip.conf`中的内容。

```bash
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn
```

替换完成后，之后的Python包安装就会使用国内源了。

**检查系统内核版本**

使用如下命令查看系统内核版本。

```bash
lsb_release -a
```

### 开发环境配置

#### Python

Python版本确定

```bash
python -V
```

#### CMake

查询CMAKE版本：

```python
cmake --version
```

Ubuntu系统自带的CMake通常为低版本。由于CMake在3.12版本后进行了较大的更新，因此一些开源程序不支持使用低版本CMake进行编译。为此需要自行安装高版本CMake。CMake安装方法见[CMake用法详解 | 亓淇小站 (calria.plus)](https://blog.calria.plus/2021/01/05/CMake%E7%94%A8%E6%B3%95%E8%AF%A6%E8%A7%A3/)。

#### CUDA

CUDA版本确定

```bash
nvcc --version
```

```
export LD_LIBRARY_PATH=/home/sukie/program/cuda-10.1/lib64:$LD_LIBRARY_PATH
```



### 联网协同

**生成`SSH`公钥和密钥**

On your client computer generate public key:
```bash
ssh-keygen
```

Copy the client public key to the server:
```bash
scp ~/.ssh/id_rsa.pub user@222.22.2.2.:~
```

Check whether `authorized_keys` exists in the directory `~/.ssh/` on the server. If not, create it:
```bash
touch authorized_keys
chmod 600 authorized_keys
```

Append the client public key to the server's authorized_keys:
```bash
cat ~/id_rsa.pub >> ~/.ssh/authorized_keys
```

### 1.3 Change Shell Version

```bash
# List the all installed shells
cat /etc/shells

# Check which Terminal you are using
ls -l /proc/$$/exe
echo $SHELL

# Change default shell for the current user
chsh -s /path/to/shell
```

However, if you are using ssh to connect to a remote server, the abovementioned prompt may be invalid. Using the following prompt instead.

```bash
exec /bin/dash
exec /bin/zsh
```

**Mount and unmount disk remotely**

```bash
fdisk -l # list all available disks
mount -t ntfs /dev/sdb2 /media/sukie/Data # mount
df -lh # check disk usage
umount /dev/sdb2 # unmount
```

**Check disk usage & spare space**

```bash
df -h # list all partions' usage condition
du -hs /path/to/directory # list the disk usage of each FILE recursively
```

**Calculate amounts of FILES**
```bash
# Reference: https://blog.csdn.net/xh_hit/article/details/80651565
ls -l|grep "^-"| wc -l
ls -lR|grep "^-"| wc -l
ls -l|grep "^d"| wc -l
```

Recursively coping files with specified extension**

```bash
cp --parents -R folder_src/**/*.mp4 ./folder_dst
```

**nohup**

```bash
nohup ./scripts/train.sh > log.txt 2>&1 &
```

**Batch rename files**

```bash
ls *jpg | awk -F\. '{print "mv "$0" C"NR".jpg"}' | sh
```



**Empty Trash in Command Line**

```bash
rm -rf ~/.local/share/Trash/*
```

**Calculate md5**

```bash
certutil -hashfile filename MD5 # windows
md5sum filename # ubuntu
```

**Summarize disk usage of each FILE recursively**

```bash
du -hs /path/to/directory # ubuntu
```

`grep` display multiple lines infomation

 ```bash
 grep -C 5 foo file 显示file文件里匹配foo字串那行以及上下5行
grep -B 5 foo file 显示foo及前5行
grep -A 5 foo file 显示foo及后5行
 ```
修改用户文件夹路径

```
vim ~/.config/user-dirs.dirs
```

### 2. SSH

**Install SSH server**

```bash
sudo apt-get install openssh-server
```

**Start SSH server**

```bash
sudo /etc/init.d/ssh start
```

**Set password for user**

```bash
sudo passwd user-name
```

**Enable SSH password authentication**

```bash
sudo vim /etc/ssh/sshd_config
# set PasswordAuthentication as yes
```

**Restart SSH service**

```bash
sudo service sshd restart
```


**Install SSH client**

```bash
sudo apt-get install openssh-client
```

### 3. VNC

**Install VNC server**

```bash
sudo apt-get install x11vnc
```
**Set VNC password**

```bash
x11vnc -storepasswd
```

**Start VNC service**

```bash
x11vnc -usepw
```

### 4. TensorboardX

```bash
tensorboard --host 0.0.0.0 --logdir runs --port 6006 # tensorflow and tensorboardX are required
```
Then open the link `http://162.105.92.77:6006` in your local browser.

The following command may be useful
```bash
lsof -i: 6006 # list process that occupying port 6006
kill PID # use the actual value instead of PID
```

tensorboard: ` Permission denied: '/tmp/.tensorboard-info/pid-2274.info' `

```bash
# 申明环境变量
export TMPDIR=/tmp/$USER; 
# 创建目录
mkdir -p $TMPDIR;
# 打开tensorboard
tensorboard --logdir $LOGDIR
```

### 5. CUDA

**Check cuda version**

```bash
/usr/local/cuda/bin/nvcc --version
```

**Activate and deactivate enviroment**

```bash
source activate tensorflow
source deactive tensorflow
```

**Install commonly used packages**

```bash
conda install ipython
conda install jupyter
conda install opencv
```

### 6. Virtualenv

**Install virtualenv and create new venv**

```bash
sudo apt install pip // install pip

pip3 install virtualenv // install virtualenv via pip3

python -m virtualenv venv # 用这个命令替换下面的
virtualenv -p /usr/bin/python3 --no-site-packages venv // create new virtual enviroments named venv

source venv/bin/activate // activate virtual enviroment
```

**List all installed packaegs**

```bash
pip3 list
```

**Build into Virtualenv**

```bash
export $VIRTUAL_ENV=[your_path_to_env]
cmake -D MAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=$VIRTUAL_ENV/local/ -D PYTHON_EXECUTABLE=$VIRTUAL_ENV/bin/python -D PYTHON_PACKAGES_PATH=$VIRTUAL_ENV/lib/python2.7/site-packages -D INSTALL_PYTHON_EXAMPLES=ON ..
make -j
make install
```

**Deactivate virtalenv**

```bash
deactivate venv
```

### 7. Media

**Converting batches images into video**

```bash
ffmpeg -framerate 25 -i C%06d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4
```

### 8. Jupyter Notebook

**Install**

```bash
# Create a virtual environment to install ipython and jupyter notebbook
pip3 install ipython[all] # Install packages in the virutal environment
```

**Set remote access**

Generate the template configuration file.

```bash
jupyter notebook --generate-config
```

Open your python environment in the terminal, and then input the following commands.

```python
from IPython.lib import passwd
passwd()
```

Copy the output`sha1` value, and edit the configuration file `~/.jupyter/jupyter_notebook_config.py` as the following.

```bash
c.NotebookApp.ip='*'
c.NotebookApp.password = u'sha:ce...'
c.NotebookApp.open_browser = False
c.NotebookApp.port =8888 #可自行指定一个端口, 访问时使用该端口
```

Run the jupyter notebook in thte background

```bash
nohup jupyter notebook > /dev/null 2>&1 &
```

Now you can access the jupyter notebook in your server at the url `http://162.122.11.23:8888`.

### Nvidia

```bash
nvidia-smi
```