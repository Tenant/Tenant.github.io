---
title: 需要使用Pointer to Pointer的场合
date: 2022-12-16 23:20:00
categories:
  - 编程
  - C++
tags:
  - 编程
  - C++
description: why we need pointer to pointer
---
# 需要使用Pointer to Pointer的场合

如下所示，当我们将一个变量作为函数参数传递时，有时需要将函数内部对变量的修改加以返回：

```c++
void bar(int* foo) {
    *foo = 1;
}
```

类似的，当我们需要使用pointer to pointer时，也是需要将函数内部对作为参数传递的指针的修改加以返回。

这里需要区别的是，返回的是会指针的修改，而不是对指针指向对象的修改。其实对指针指向对象的修改就是上面的示例。为了明确，C++中对指针的修改如下：

- 将指针指向新的地址，如`*p = nullptr`
这种行为通常伴随着对内存空间的申请或释放，一个完整的示例如下：

```c++
void save_free(Foo* p) {
    free(*p);
    *p = nullptr;
}

int main(int argc, char** argv) {
    Foo* p = (Foo*)malloc(sizeof(Foo));
    save_free(&p);
    
    return 0;
}
```
