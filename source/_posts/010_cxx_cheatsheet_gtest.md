---
title: C++ Cheatsheet GTest
date: 2021-01-05 12:24:12
categories:
  - 编程
  - C++
  - GTest
tags: 
  - 编程
  - C++
  - GTest
description: 本文对C++中GTest的用法进行了总结。
---
# C++ Cheatsheet: GTest

## Install

## CMake Config

## Macro Usage

在同一份TestCase中不能同时出现TEST和TEST_F两者进行混用；其次TEST_F比TEST强的地方是会通过继承::testing::Test生成一个新类,而且这是必须的。在新类中可以通过void SetUp();和void TearDown();进行创建和清除相关的资源数据。

### TEST

```
TEST(test_case_name, test_name)
```

- test_case_name第一个参数是测试用例名,通常是取测试函数名或者测试类名
- test_name 第二个参数是测试名这个随便取，但最好取有意义的名称
- 当测试完成后显示的测试结果将以"测试用例名.测试名"的形式给出

