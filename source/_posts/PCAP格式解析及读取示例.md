---
title: PCAP格式解析及读取示例
date: 2021-01-15 23:59:22
tag:
  - PCAP
  - Velodyne
description: 本文总结了PCAP的格式，并展示了简单的读取demo。
---

## 1. 通用PCAP格式

PCAP是一种通用的数据流格式，很多开源的项目都需要用到这种格式的文件。PCAP文件可以分为三个部分：

- Global Header：24 Byte，定义如下：
  - Magic：4 Byte，标记PCAP文件的开始，用来识别文件开头和文件大小端。其中`\xa1\xb2\xc3\d4`表示大端模式，`\xd4\xc3\b2\xa1`表示小端模式
  - Major：2 Byte，uint16，当前文件主要版本号
  - Minor：2 Byte，uint6，当前文件次要版本号
  - ThisZone：4 Byte，int32，当地标准时间
  - SigFigs：4 Byte，uint32，时间戳的精度
  - SnapLen：4 Byte，uint32，最大存储长度
- Packet Header：16 Byte，每一个抓取的Packet都有一个Packet Header，Packet Header记录了Packet Data的长度和时间戳等信息，定义如下：
  - Seconds：4 Byte， uint32， Unix时间戳以秒为单位的整数部分
  - uSeconds：4 Byte， uint32， Unix时间戳以秒为单位的小数部分，单位是`1e-6`秒
  - CapLen：4 Byte， uint32， 抓取得到的的数据帧的长度，即Packet Data的长度，由此可以计算下一个数据帧的位置
  - Len：4 Byte， uint32，网络中实际数据帧的长度，一般不大于CapLen，多数情况下和CapLen相等
- Packet Data：紧跟在自己的Packet Header后面，长度为CapLen Byte，为记录的消息的本体。

PCAP的标准格式示例如下：

![img](https://raw.githubusercontent.com/Tenant/Tenant.github.io/assets/images/L3Byb3h5L2h0dHAvaGkuY3Nkbi5uZXQvYXR0YWNobWVudC8yMDEwMDMvMjgvNDYzMzYzOV8xMjY5NzUyMDI4ZzlDQi5wbmc%3D.jpg)

## 2. LiDAR PCAP示例

LiDAR传感器通常通过UDP网络报的形式发送数据，因此通常将LiDAR数据报文录制为PCAP文件进行后处理。

### 2.1 报文录制

录制LiDAR报文数据和录制其他网络包一样，使用如下命令即可：

```bash
#!/bin/bash

ID=`id -un`
TS=`date "+%Y-%m-%d-%H-%M-%S"`.pcap
mkdir -p ~/data
cd ~/data
/usr/sbin/tcpdump -i $1 -Z $ID -s 0 -w $TS
```

### 2.2 数据格式

录制的完整PCAP文件的格式如下图所示：

![2021-01-15_235541](https://raw.githubusercontent.com/Tenant/Tenant.github.io/assets/images/2021-01-15_235541-1610769627577.png)

其中前24 Byte表示PCAP文件的文件头，后续部分为按顺序排列的一个个报文，每个报文包含了16 Byte字节的Packet Header和相应长度的Packet Data。

在Wireshark中打开PCAP文件效果如下图所示：

![2021-01-15_235504](https://raw.githubusercontent.com/Tenant/Tenant.github.io/assets/images/2021-01-15_235504-1610769572062.png)

解析数据时，按照上述格式读取即可。

### 2.3 解析程序示例

```python
import os

def read_uint16(data, idx):
  return data[idx+1]*256 + data[idx+0]

def read_uint32(data, idx):
  return data[idx+3]*256*256*256 + data[idx+2]*256*256 + data[idx+1]*256 + data[idx+0]

def read_uint64(data, idx):
  return read_uint32(data, idx+4)*256*256*256*256 + read_uint32(data, idx)

def read_sint32(data, idx):
  val = data[idx+3]*256*256*256 + data[idx+2]*256*256 + data[idx+1]*256 + data[idx+0] 
  return val-2**32 if val > 2**31-1 else val

def convert_unix_to_local(ss, us):
    t_max = 60 * 60 * 24
    t = (ss % t_max + 60 * 60 * 8) * 1000 + us // 1000
    return t

def read_pcap_header(f):
    p_data = f.read(24)
    if len(p_data) < 24:
        return False
    if p_data[0:4] == b'\xd4\xc3\xb2\xa1':
        version_major = read_uint16(p_data, 4)
        version_minor = read_uint16(p_data, 6)
        thiszone = read_sint32(p_data, 8)
        timestamp = read_uint32(p_data, 12)
        print("version: {}.{}".format(version_major, version_minor))
        print("timezone: {}".format(thiszone))
        print("timestamp: {}".format(timestamp))
        return p_data
    else:
        print("This is not a pcap file") 
        return None

def split_pcap_file(fn):
    with open(fn, 'rb') as f:
        pcap_header = read_pcap_header(f)
        if not pcap_header:
            return
        while True:
            p_data = f.read(16)
            if len(p_data) < 16:
                break
            else:
                s_seconds = read_uint32(p_data,0)
                u_seconds = read_uint32(p_data,4)
                m_seconds = convert_unix_to_local(s_seconds, u_seconds)
                data_len = read_uint16(p_data, 12)
                if data_len > 0:
                    if head <= m_seconds <= tail:
                        out_info.append(p_data)
                    p_data = f.read(data_len)
                    if head <= m_seconds <= tail:
                        out_info.append(p_data)

if __name__ == "__main__":
    split_csv_file(sys.argv[1])
```

注：开发二进制解析程序时，可以结合WinHex和Wireshark等软件以及产品文档了解清楚数据的格式定义，然后进行对应的读取即可。



