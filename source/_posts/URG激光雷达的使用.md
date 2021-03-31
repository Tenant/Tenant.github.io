---
title: URG激光雷达的使用
date: 2021-01-18 20:24:03
categories:
- 传感器
- LiDAR
tags:
- 传感器
- LiDAR
description: 本文详解了URG激光雷达的使用
---

## 1. 简介

Hokuyo的2D单线激光雷达URG系列因其低廉的成本在机器人领域得到了较多的应用。

## 2. 在线数据读取

ROS支持UGR激光雷达数据的在线读取，仓库链接见[ros-drivers/urg_node: ROS wrapper for the Hokuyo urg_c library. ](https://github.com/ros-drivers/urg_node)，使用方法见[hokuyo_node/Tutorials/UsingTheHokuyoNode - ROS Wiki](http://wiki.ros.org/hokuyo_node/Tutorials/UsingTheHokuyoNode).

配置安装上述仓库后，可以通过如下命令在`launch`文件中启动`urg node`：

```xml
<arg name="urgip" default="192.168.0.10" />
<arg name="urgport" default="/dev/ttyACM0" />
<arg name="urgbaud" default="115200" />
<arg name="urgframeid" default="laser" />

<node name="urg_node" pkg="urg_node" type="urg_node" output="screen">
    <param name="ip_address" value="$(arg urgip)"/>
    <param name="serial_port" value="$(arg urgport)"/>
    <param name="serial_baud" value="$(arg urgbaud)"/>
    <param name="frame_id" value="$(arg urgframeid)"/>
    <param name="calibrate_time" value="true"/>
    <param name="publish_intensity" value="false"/>
    <param name="publish_multiecho" value="false"/>
    <param name="angle_min" value="-1.5707963"/>
    <param name="angle_max" value="1.5707963"/>
```

如需录制数据，可以在`launch`文件中添加如下命令：

```xml
<node name="urgrecord" pkg="rosbag" type="record" args="/scan /GPSIMUdata -o /root/data/urg"/>
```

数据将以`rosbag`的形式保存在指定路径下，消息类型为`sensor_msgs/LaserScan`。

## 3. 数据解析

`sensor_msgs/LaserScan`类型的数据可以直接被`ROS`解析识别，无需转换，可以直接使用。

但在一些情况下，需要将URG数据转换为其他格式，此处以自定义`lms`格式为例。格式定义如下：

<img src="https://raw.githubusercontent.com/Tenant/Tenant.github.io/assets/images/image-20210118204026200.png" alt="image-20210118204026200" style="zoom:80%;" />

文件最开始的12个字节依次为`angle range`，`angle resolution`和`unit`，均为4字节的`float`型变量，小端模式。其中`angle range`表示单线激光测距的角度范围，`angle resolution`表示单线激光测距的水平角分辨率，`unit`表示距离记录结果的单位，记录中的值除以`unit`为真实的距离测量值，单位为`m`。文件之后的内容为按照时间顺序排列的测量记录，测量记录数不定。每条记录包含两部分：第一部分是4字节`long`型变量，表示时间戳；第二部分为`ang_range / angle resolution + 1`个`uint16`变量，表示每一条激光线的测距记录值。

解析程序示例如下：

```python
def read_urg_lms(fn):
    with open(fn, "rb") as f:
        ang_range = struct.unpack('<f', f.read(4))[0] # ang range: float, 4 byte, = 180
        ang_resol = struct.unpack('<f', f.read(4))[0] # ang resolution: float, 4 byte, = 0.125
        unit = struct.unpack('<f', f.read(4))[0] # unit: float, 4 byte, = 100
        bim_numbers = int(ang_range // ang_resol + 1)
        while True:
            p_data = f.read(4)
            if len(p_data) < 4:
                break
            timestamp = struct.unpack('<l', p_data)[0]
            p_data = f.read(bim_numbers * 2)
            
def write_urg_lms(fn):
    unit = 100.0
    with open(fn) as f:
        f.write(struct.pack('f', 180.0))
        f.write(struct.pack('f', 0.125))
        f.write(struct.pack('f', unit))
        for _time, _range in zip(timestamps, ranges):
            f.write(struct.pack('i', _time))
            for dist in _range:
                if not math.isnan(dist):
                	f.write(struct.pack('h', int(dist * unit))
                else:
                    f.write(struct.pack('h', 0))
```

`rosbag`转`lms`示例如下：

```python
'''
This script saves each topic in a bagfile as a csv.

Accepts a filename as an optional argument. Operates on all bagfiles in current directory if no argument provided

Written by Nick Speal in May 2013 at McGill University's Aerospace Mechatronics Laboratory
www.speal.ca

Supervised by Professor Inna Sharf, Professor Meyer Nahon 

'''

import rosbag, sys, csv
import time
import string
import os #for file management make directory
import shutil #for file management, copy file

#verify correct input arguments: 1 or 2
if (len(sys.argv) > 2):
	print "invalid number of arguments:   " + str(len(sys.argv))
	print "should be 2: 'bag2csv.py' and 'bagName'"
	print "or just 1  : 'bag2csv.py'"
	sys.exit(1)
elif (len(sys.argv) == 2):
	listOfBagFiles = [sys.argv[1]]
	numberOfFiles = "1"
	print "reading only 1 bagfile: " + str(listOfBagFiles[0])
elif (len(sys.argv) == 1):
	listOfBagFiles = [f for f in os.listdir(".") if f[-4:] == ".bag"]	#get list of only bag files in current dir.
	numberOfFiles = str(len(listOfBagFiles))
	print "reading all " + numberOfFiles + " bagfiles in current directory: \n"
	for f in listOfBagFiles:
		print f
	print "\n press ctrl+c in the next 2 seconds to cancel \n"
	time.sleep(2)
else:
	print "bad argument(s): " + str(sys.argv)	#shouldnt really come up
	sys.exit(1)

count = 0
for bagFile in listOfBagFiles:
	count += 1
	print "reading file " + str(count) + " of  " + numberOfFiles + ": " + bagFile
	#access bag
	bag = rosbag.Bag(bagFile)
	bagContents = bag.read_messages()
	bagName = bag.filename


	#create a new directory
	folder = string.rstrip(bagName, ".bag")
	try:	#else already exists
		os.makedirs(folder)
	except:
		pass
	shutil.copyfile(bagName, folder + '/' + bagName)


	#get list of topics from the bag
	listOfTopics = []
	for topic, msg, t in bagContents:
		if topic not in listOfTopics:
			listOfTopics.append(topic)


	for topicName in listOfTopics:
		#Create a new CSV file for each topic
		filename = folder + '/' + string.replace(topicName, '/', '_slash_') + '.csv'
		with open(filename, 'w+') as csvfile:
			filewriter = csv.writer(csvfile, delimiter = ',')
			firstIteration = True	#allows header row
			for subtopic, msg, t in bag.read_messages(topicName):	# for each instant in time that has data for topicName
				#parse data from this instant, which is of the form of multiple lines of "Name: value\n"
				#	- put it in the form of a list of 2-element lists
				msgString = str(msg)
				msgList = string.split(msgString, '\n')
				instantaneousListOfData = []
				for nameValuePair in msgList:
					splitPair = string.split(nameValuePair, ':')
					for i in range(len(splitPair)):	#should be 0 to 1
						splitPair[i] = string.strip(splitPair[i])
					instantaneousListOfData.append(splitPair)
				#write the first row from the first element of each pair
				if firstIteration:	# header
					headers = ["rosbagTimestamp"]	#first column header
					for pair in instantaneousListOfData:
						headers.append(pair[0])
					filewriter.writerow(headers)
					firstIteration = False
				# write the value from each pair to the file
				values = [str(t)]	#first column will have rosbag timestamp
				for pair in instantaneousListOfData:
					if len(pair) > 1:
						values.append(pair[1])
				filewriter.writerow(values)
	bag.close()
print "Done reading all " + numberOfFiles + " bag files."
```

