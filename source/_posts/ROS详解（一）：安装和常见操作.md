---
title: ROS详解（一）：安装和常见操作
date: 2021-01-14 13:44:57
categories: ROS
tags: ROS
description: 本文对ROS的安装和常见操作进行了总结归纳。
---

[Tutorial](http://wiki.ros.org/ROS/Tutorials0)

## 1. BUILD

```bash
catkin_make_isolated --only-pkg-with-deps [your_packages] --use-ninja
catkin_make --only-pkg-with-deps [your_package] -DCMAKE_BUILD_TYPE=Release
```

**Refresh WorkingSpace**

```bash
source devel/setup.sh
```



**rosparam**

```bash
rosparam get /use_sim_time
rosparam set /use_sim_time true
```



**rosbag play**

```bash
rosbag play [your_bag] -l --clock --pause -r 0.8
rosbag info [your_bag]
```



**Convert pcap to rosbag**

```bash
rosrun ve lodyne_driver velodyne_node _model:=VLP16 [32E] _pcap:=/your/file.pcap _read_once:=true
rosrun rosbag record -O your_output.bag -a [/velodyne_packets]
```



**Initialize Workspace**

```bash
mkdir catkin_ws
cd catkin_ws
wstool init src
wstool update -t src
```



**How to Create a package**

```bash
cd catkin_ws/src
catkin_create_pkg [package-name]
```



**Start ROS server**

```bash
roscore
```



**rostopic**

```bash
rostopic echo /velodyne_points | grep frame_id
rostopic echo /tf | grep frame_id
rostopic list
rosrun rviz rviz
rosbag record [topic1] [topic2] -O bagfile.bag
```



**rviz**

```rviz
rviz
rosrun rviz rviz
```





```html
<remap from="original_defined_topic" to="acturally_used_topic" / >
```



```bash
roslaunch loam_velodyne loam_velodyne.launch
```



```bash
roslaunch velodyne_pointcloud 64e_points-2.launch
```

