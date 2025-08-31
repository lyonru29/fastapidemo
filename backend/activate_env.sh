#!/bin/bash
# 激活 uv 虚拟环境
# 作者: lyonru29
# 日期: 2025-01-27

echo "正在激活 uv 虚拟环境..."
source .venv/bin/activate
echo "虚拟环境已激活！"
echo "现在可以使用 python 命令了"
echo ""
echo "Python 路径: $(which python)"
echo "Python 版本: $(python --version)"
