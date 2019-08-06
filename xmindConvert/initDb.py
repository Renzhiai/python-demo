#!/usr/bin/env python
# coding=utf-8
import sqlite3
from contextlib import closing
from xmindConvert.cfg import *

def connect_db():
    '''
    连接数据库
    :return:
    '''
    return sqlite3.connect(DATABASE)


def create_db():
    '''
    创建数据库
    :return:
    '''
    with closing(connect_db()) as db:
        with open('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def init():
    '''
    创建上传文件目录和数据库
    :return:
    '''
    # 创建上传文件目录
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
    # 创建数据库
    if not os.path.exists(DATABASE):
        create_db()