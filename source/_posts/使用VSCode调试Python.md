---
title: 使用VSCode调试Python
date: 2021-05-04 17:17:28
tags:
---

首先通过单击`Run`启动调试程序，然后选择创建配置文件`launch.json`，配置文件内容示例如下：

示例如下：

```js
    "version": "0.2.0",
    "configurations": [
        {
            "name": "debug train.py",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": ["--dataset", "COCO", "--dataset_root", "D:/Desktop/tiny-datasets/coco2014/small_coco", "--image_set", "train_2017_small", "--batch_size", "2", "--cuda", "False"]
        }
    ]
}
```

