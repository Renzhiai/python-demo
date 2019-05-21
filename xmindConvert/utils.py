#!/usr/bin/env python
# coding = utf-8
import os
import xmind
from xml.etree.ElementTree import Element, SubElement, ElementTree
import tarfile
import sys
import shutil

class Node(object):
    def __init__(self, level=None, title=None, path=None, childs=None, index=None):
        '''
        初始化节点
        :param level:
        :param title:
        :param path:
        :param childs:
        :param index:
        '''
        self.level = level
        self.title = title
        self.path = path
        self.childs = childs
        self.index = index

def getValue(results, n, nodes, levels):
    '''
    递归获取所有节点层级
    :param results:
    :param n:
    :param nodes:
    :param levels:
    :return:
    '''
    n = n + 1
    for item in results:
        topics = item.get('topics')
        childs = ''
        if topics:
            childs = topics
        title = item.get('title')
        node = Node()
        levels.append(n)
        node.level = n
        node.title = title
        node.childs = childs
        nodes.append(node)
        if topics:
            getValue(topics, n, nodes, levels)
    return nodes, levels

def getXmindData(path):
    '''
    获取xmind，转换成json
    :param path:
    :return:
    '''
    print('进入'+sys._getframe().f_code.co_name)
    resultList = []
    workbook = xmind.load(path)
    # 获取所有xmind数据
    result = workbook.getData()
    resultList.append(result[0]['topic'])
    # 递归获取所有层级和节点
    nodes, levels = getValue(resultList, 0, [], [])
    # 获取节点最大层级
    maxLevel = max(levels)
    if maxLevel < 4:
        return -1, -1
    else:
        return nodes, maxLevel

def display(nodes):
    '''
    xmind展示
    :param nodes:
    :return:
    '''
    print('进入' + sys._getframe().f_code.co_name)
    resultList = []
    # 开始执行
    for index in range(len(nodes)):
        node = nodes[index]
        # 替换掉/和\
        if node.title:
            node.title = node.title.replace('\\', '-')
            node.title = node.title.replace('/', '-')
        else:
            print('节点内容为空，请检查后再操作')
            raise Exception('节点内容为空，请检查后再操作')
        # 层级是1的节点
        if node.level == 1:
            node.path = node.title
        else:
            # 递归得到的层级是按一定顺序排列的，非1层级的节点，从当前位置往回遍历
            for indexParent in range(index-1, -1, -1):
                if node.level - nodes[indexParent].level == 1:
                    node.path = os.path.join(nodes[indexParent].path, node.title)
                    titles = node.path.split(os.sep)
                    # 子节点为0的添加到list中
                    if len(node.childs) == 0:
                        resultList.append(titles)
                    break
    return resultList

def convertToDisplay(filePath):
    '''

    :param filePath:
    :return:
    '''
    print('进入' + sys._getframe().f_code.co_name)
    # 文件存在且是xmind格式
    if os.path.exists(filePath):
        if os.path.splitext(filePath)[1] == '.xmind':
            #获取xmind数据
            nodes, maxLevel = getXmindData(filePath)
            if nodes == -1 and maxLevel == -1:
                print('节点过少，不支持转换')
                raise Exception('节点过少，不支持转换')
            reultsList = display(nodes)
            return reultsList, maxLevel
        else:
            print('非xmind文件')
            raise Exception('非xmind文件')
    else:
        print('输入路径有误')
        raise Exception('输入路径有误')

def convertToXml(nodes, maxLevel, path, mode):
    pass

def xmind_to_testlink_xml_file(xmind_file, mode):
    pass

def xmind_to_robot_tar_file(xmind_file, mode):
    pass