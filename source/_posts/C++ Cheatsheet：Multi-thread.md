---
title: C++ Cheatsheet: Multi-thread
date: 2021-01-05 12:24:12
categories:
  - 编程
  - C++
  - 多线程
tags: 
  - 编程
  - C++
  - 多线程
description: 本文对CMake安装、常见用法进行了总结归纳。

---
# C++ Cheatsheet: Multi-thread

## STL

### Lock_guard

 std::lock_guard在构造时只被锁定一次，并且在销毁时解锁。

> 在std::lock_guard对象构造时，传入的mutex对象(即它所管理的mutex对象)会被当前线程锁住。在lock_guard对象被析构时，它所管理的mutex对象会自动解锁，不需要程序员手动调用lock和unlock对mutex进行上锁和解锁操作。lock_guard对象并不负责管理mutex对象的生命周期，lock_guard对象只是简化了mutex对象的上锁和解锁操作，方便线程对互斥量上锁，即在某个lock_guard对象的生命周期内，它所管理的锁对象会一直保持上锁状态；而lock_guard的生命周期结束之后，它所管理的锁对象会被解锁。程序员可以非常方便地使用lock_guard，而不用担心异常安全问题。

```c++
// demo.h
#include <mutex>
class Demo {
private:
  std::mutex init_mutex_;
};

// demo.cpp
void Demo::Process() {
  std::lock_guard<std::mutex> lock(instance_mutex_);
  // do something
}
```



