#!/usr/bin/env python
# coding=utf-8
import os

# 当前目录路径
here = os.path.abspath(os.path.dirname(__file__))
# 数据库路径
DATABASE = os.path.join(here, 'data.db3')
# 上传文件路径
UPLOAD_FOLDER = os.path.join(here, 'uploads')
