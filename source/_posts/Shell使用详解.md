---
title: Shell使用详解
date: 2021-01-08 16:41:25
categories:
  - 操作系统
  - Shell
tags:
  - 操作系统
  - Shell
description: 本节总结了常用的Shell编程。
---

## 1. Shell变量

本部分详细内容可参考[链接](https://www.runoob.com/linux/linux-shell-variable.html)，下面所示为部分示例：

```bash
#!/bin/bash

myUrl="https://www.google.com" # 定义变量
readonly myUrl # 设置变量为只读
echo ${myUrl} # 访问变量
echo ${#myUrl} # 获取字符串长度
unset myUrl # 删除变量
```

## 2. Shell参数传递

本部分详细内容可参考[链接](https://www.runoob.com/linux/linux-shell-passing-arguments.html)。

我们可以在执行 Shell 脚本时，向脚本传递参数，脚本内获取参数的格式为：`$n`。`n`代表一个数字，1 为执行脚本的第一个参数，2 为执行脚本的第二个参数，以此类推。

## 3. Shell数组

本部分详细内容可参考[链接](https://www.runoob.com/linux/linux-shell-array.html)。

数组中可以存放多个值。Bash Shell 只支持一维数组（不支持多维数组），初始化时不需要定义数组大小。与大部分编程语言类似，数组元素的下标由0开始。Shell 数组用括号来表示，元素用"空格"符号分割开。

## 4. Shell运算符

本节详细内容可参考[链接](https://www.runoob.com/linux/linux-shell-basic-operators.html)。原生bash不支持简单的数学运算，但是可以通过其他命令来实现，例如`awk`和`expr`，`expr`最常用，示例如下：

```bash
#!/bin/bash

val=`expr 2 + 2` # 表达式和运算符之间要有空格
echo "两数之和为 : $val"
```

### 4.1 关系运算符



## 5. Shell流程控制

本节详细内容可参考[链接](https://www.runoob.com/linux/linux-shell-process-control.html)。

## 6. 其它常见命令

**wait命令**

`wait`命令一个很重要用途就是在`Bash shell`的并行编程中，可以在`Bash shell`脚本中启动多个后台进程（使用`&`），然后调用`wait`命令，等待所有后台进程都运行完毕，`Bash shell`脚本再继续向下执行。

```bash
wait [PID-number]
```

**sleep命令**

```bash
sleep [sleep-time]
```

