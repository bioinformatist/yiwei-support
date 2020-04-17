# yiwei-support

> “一苇酱支援计划。”

## 项目目录

点击进入具体目录可看到程序运行所需环境部署指南和使用说明。

| 目录 | 功能简述 |
| ---- | ----|
| RBL_query | 确认某邮件服务器的IP地址是否被列入黑名单 |
| SBL_query | 查询当前运营商所有的IP是否有（某些）被列入黑名单 |

## 备注

本工具集在Linux下完成编写与调试，**代码是跨平台的**，但需要使用者有足够的操作系统使用经验（对，用不起来就是**你连操作系统都不会用**，你太**蔡**了，回炉重造去8）。

或者大家可以成立一个“**关爱一苇小可爱基金会**”，赞助一下，我可以为repo部署一个docker image呀。

本工具集使用Python 3.x完成编写与调试，请使用与之相符的Anaconda版本。

针对常见问题，总结如下：

1. 在Windows下应该使用`conda activate ENV_NAME`去激活虚拟环境
    > 其实Linux下也应该尽量使用`conda activate`而不是`source activate`，但需要在`.bashrc`等中进行额外配置
2. 在windows下应该使用`python3 xxx.py`而不是`./xxx.py`
    > Linux下可以使用`./xxx.py`的形式自动调用解释器是因为我写了shebang：`#!/usr/bin/env python3`
3. 如果Windows下找不到Python解释器，证明你没有把解释器等写入`PATH`变量，这是个好习惯，但请使用*Anaconda (Powershell) prompt*运行。