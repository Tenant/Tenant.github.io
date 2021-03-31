---
title: Latex详解（一）：本地安装和环境配置
date: 2021-01-14 11:42:17
tags:
description: LaTex用法详解
---

## 1. 安装

LaTex有多个发行版本，本文使用TexLive2019，TexLive各个版本的下载见[链接](http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/)。

下载完成后，加载镜像，运行`install-tl-advanced.bat`进行安装。安装过程耗时会比较久，需耐心等待。安装完成后，可以调用`Terminal`，分别输入以下命令来检验安装是否成功。

```bash
tex -v
latex -v
xelatex -v
pdflatex -v
```

TexLive2019安装完成后，需要安装编辑器，这里选择`VS code`作为编辑器，相应的配置方法见[链接](https://github.com/EthanDeng/vscode-latex)。

## 2. LaTex模板

一个简单的LaTex模板示例如下：

```latex
% !TEX program = pdflatex
\documentclass{article}

\usepackage{hyperref}
\usepackage[round]{natbib}
\usepackage{newtxtext,newtxmath}
\author{Dongsheng Deng}
\title{Configuration of Visual Studio Code for \LaTeX{} Users}
\date{\today}

\begin{document}
\maketitle

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat.Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, \cite{GraffZivin2018} sunt in culpa qui officia deserunt mollit anim id est laborum.

\begin{equation}
  a^2+b^2=c^2
\end{equation}

\bibliography{info}
\bibliographystyle{plainnat}

\end{document}
```

`info.bib`格式示例：

```latex
@Article{GraffZivin2018,
  author  = {Graff Zivin, Joshua and Hsiang, Solomon M and Neidell, Matthew},
  title   = {Temperature and Human Capital in the Short and Long Run},
  journal = {Journal of the Association of Environmental and Resource Economists},
  year    = {2018},
  volume  = {5},
  number  = {1},
  pages   = {77-105},
  issn    = {2333-5955},
  type    = {Journal Article},
}

@Book{Lutz2017,
  title     = {World Population \& Human Capital in the Twenty-First Century: An Overview},
  publisher = {Oxford University Press},
  year      = {2017},
  author    = {Lutz, Wolfgang and Butz, William P and Samir, KC ed},
  isbn      = {0192542834},
  type      = {Book},
}

@Article{Zeng2017,
  author  = {Zeng, X. and Liu, L. and Leung, S. and Du, J. and Wang, X. and Li, T.},
  title   = {A decision support model for investment on P2P lending platform},
  journal = {PLoS One},
  year    = {2017},
  volume  = {12},
  number  = {9},
  pages   = {e0184242},
  issn    = {1932-6203 (Electronic)
1932-6203 (Linking)},
  doi     = {10.1371/journal.pone.0184242},
  type    = {Journal Article},
  url     = {https://www.ncbi.nlm.nih.gov/pubmed/28877234},
}
```

