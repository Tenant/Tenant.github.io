---
title: Ubuntu C++ Performance Profile
date: 2021-01-05 12:24:12
categories:
  - 编程
  - C++
  - 性能优化
tags: 
  - 编程
  - C++
  - 性能优化
description: 本文对Ubuntu平台下C++程序的性能优化工具进行了整理。

---
# Ubuntu C++ 程序性能优化

## 时间优化

### 系统计时工具

#### gpof

用gprof对程序进行分析主要分以下三个步骤：

1. 用编译器对程序进行编译，加上`-pg`参数；

2. 运行编译后的程序；
3. 用gprof命令查看程序的运行时信息。

**安装**

gprof在发行的Linux系统中通常都有内置。

**使用**

在编译程序时使用`-gp`命令，对于以CMakelist组织的程序而言，可以为`cmake`添加如下参数：

```bash
cmake -DCMAKE_CXX_FLAGS=-pg -DCMAKE_EXE_LINKER_FLAGS=-pg -DCMAKE_SHARED_LINKER_FLAGS=-pg <SOURCE_DIR>
```

对于`gcc`而言，可以使用如下形式：

```bash
gcc example.c -pg -o example 
```

完成编译后，正常执行程序。在程序运行结束后，工作目录下会生成名为`gmou.out`的文件，该文件记录了程序的运行信息。

解码该信息需要安装`gprof2dot`，安装命令如下：

```bash
pip install gprof2dot
```

然后可以一下命令中的任一命令查看结果：

```bash
gprof ./example gmon.out|less -S  可以直接查看文字
gprof  ./example gmon.out |gprof2dot |dot -Tpng -o example.png  可视化展示 
```

更多内容可以参考[链接](https://www.cnblogs.com/youxin/p/7988479.html)。

#### valgrid + callgrid

### 程序内计时

`C++ 11`提供了新的程序内计时特性，精度可以到微秒，示例如下：

```c++
#include <chrono>   

auto start = std::chrono::system_clock::now();
// do something...
auto end   = std::chrono::system_clock::now();
auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
std::cout <<  "Time consuming: " << double(duration.count()) * std::chrono::microseconds::period::num / std::chrono::microseconds::period::den << "s" << std::endl;
```

