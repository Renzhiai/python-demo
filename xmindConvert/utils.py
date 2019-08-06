#!/usr/bin/env python
# coding=utf-8
import os
import xmind
from xml.etree.ElementTree import Element, SubElement, ElementTree
import tarfile
import sys
import shutil
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s - %(levelname)s : %(message)s')


class Node(object):
    def __init__(self, level=None, title=None, path=None, childs=None, index=None):
        '''
        初始化节点
        :param level:当前节点所在的层级
        :param title:当前节点的内容
        :param path:当前节点路径
        :param childs:当前节点的子节点
        :param index:子节点的索引
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
    logging.info('进入{}'.format(sys._getframe().f_code.co_name))
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
    :param path: xmind路径
    :return: nodes,节点对象，maxLevel，最大层级
    '''
    logging.info('进入{}'.format(sys._getframe().f_code.co_name))
    resultList = []
    workbook = xmind.load(path)
    # 获取所有xmind数据
    result = workbook.getData()
    resultList.append(result[0]['topic'])
    # 递归获取所有层级和节点
    nodes, levels = getValue(resultList, 0, [], [])
    # 获取节点最大层级
    maxLevel = max(levels)
    logging.info('最大层级为：{}'.format(str(maxLevel)))
    # 判断节点最大层级
    if maxLevel < 4:
        return -1, -1
    else:
        return nodes, maxLevel

def display(nodes):
    '''
    xmind展示
    :param nodes:节点
    :return:
    '''
    logging.info('进入{}'.format(sys._getframe().f_code.co_name))
    resultList = []
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

def convertToXml(nodes, maxLevel, path, mode):
    '''
    转换为xml，xmind不低于4个层级
    :param nodes: 节点
    :param maxLevel: 最大层级
    :param path: 文件路径
    :param mode: 模式为1，不补充，模式为2，自动填充
    :return:
    '''
    logging.info('进入{}'.format(sys._getframe().f_code.co_name))
    root = Element('testsuite')
    for n in range(len(nodes)):
        node = nodes[n]
        # testlink上传限制
        if len(node.title) > 80:
            node.title = node.title[:80]
        # 处理xml的特殊字符，一般只需要处理 < >
        filterStr = ['"', ':', '<', '>', '?', '*', '|', '\\', '/', '“', '”']
        for fs in filterStr:
            node.title = node.title.replace(fs, '-')
        # 层级是1的节点
        if node.level == 1:
            node.path = SubElement(root, 'testsuite')
            node.path.set('name', node.title)
        else:
            # 递归得到的层级是按一定顺序排列的，非1层级的节点，从当前位置往回遍历
            for indexParent in range(n - 1, -1, -1):
                if node.level - nodes[indexParent].level == 1:
                    # 给每个节点加上index
                    for i in range(len(nodes[indexParent].childs)):
                        # 由于node.title已经替换了特殊字符，所以childs里面的title也需要替换特殊字符
                        filterStr = ['"', ':', '<', '>', '*', '|', '\\', '/', '“', '”']
                        nodeParentTitie = nodes[indexParent].childs[i].get('title')
                        for fs in filterStr:
                            nodeParentTitie = nodeParentTitie.replace(fs, '-')
                        if nodeParentTitie == node.title:
                            node.index = i + 1
                        # 倒数第一项为预期结果
                        if node.level == maxLevel:
                            # 预期结果在测试步骤里面添加，不在此处理
                            pass
                        # 倒数第二项为测试步骤
                        elif node.level == maxLevel - 1:
                            node.path = SubElement(nodes[indexParent].path, 'step')
                            step_number = SubElement(node.path, 'step_number')
                            step_number.text = '<![CDATA[{}]]>'.format(str(node.index))
                            actions = SubElement(node.path, 'actions')
                            actions.text = '<![CDATA[{}]]>'.format(node.title)
                            expectedresults = SubElement(node.path, 'expectedresults')
                            # 如果有子节点（有预期结果），就填写预期结果，没有预期结果就为空
                            if len(node.childs) != 0:
                                expectedresults.text = '<![CDATA[{}]]>'.format(node.childs[0]['title'])
                            elif len (node.childs) == 0 and mode == '2':
                                expectedresults.text = '<![CDATA[{}]]>'.format(node.title)
                            else:
                                pass
                            execution_type = SubElement (node.path, 'execution_type')
                            execution_type.text = '<![CDATA[2]]>'
                        # 倒数第三项为測试用例名
                        elif node.level == maxLevel - 2:
                            node.path = SubElement(nodes[indexParent].path, 'testcase')
                            node.path.set('name', node.title)
                            version = SubElement(node.path, 'version')
                            version.text = '<![CDATA[1]]>'
                            summary = SubElement(node.path, 'summary')
                            summary.text = '<![CDATA[]]>'
                            preconditions = SubElement(node.path, 'preconditions')
                            preconditions.text = '<![CDATA[无]]>'
                            execution_type = SubElement(node.path, 'execution_type')
                            execution_type.text = '<![CDATA[1]]>'
                            importance = SubElement(node.path, 'importance')
                            importance.text = '<![CDATA[2]]>'
                            estimated_exec_duration = SubElement(node.path, 'estimated_exec_duration')
                            estimated_exec_duration.text = '3'
                            status = SubElement(node.path, 'status')
                            status.text = '1'
                            # 如果下面有子节点（有测试步骤），就创建<steps>标签
                            if len(node.childs) != 0:
                                node.path = SubElement(node.path, 'steps')
                            # 没有测试步骤了，就直接把用例名称设置为测试步骤，预期结果
                            elif len(node.childs) == 0 and mode == '2':
                                node.path = SubElement(node.path, 'steps')
                                node.path = SubElement(node.path, 'step')
                                step_number = SubElement(node.path, 'step_number')
                                step_number.text = '<![CDATA[{}]]>'.format(str(node.index))
                                actions = SubElement(node.path, 'actions')
                                actions.text = '<![CDATA[{}]]>'.format(node.title)
                                expectedresults = SubElement(node.path, 'expectedresults')
                                expectedresults.text = '<![CDATA[{}]]>'.format(node.title)
                                execution_type = SubElement(node.path, 'execution_type')
                                execution_type.text = '<![CDATA[2]]>'
                            else:
                                pass
                        else:
                            node.path = SubElement(nodes[indexParent].path, 'testsuite')
                            node.path.set('name', node.title)
                        break
    tree = ElementTree(root)
    xmlPath = '{}.xml'.format(os.path.splitext(path)[0])
    tree.write(xmlPath, encoding='utf8', xml_declaration=True)
    return nodes, xmlPath

def replaceXml(xmlPath):
    '''
    去掉xml里面的&lt; &gt; 转换成 <>
    :param xmlPath:
    :return:
    '''
    logging.info('进入{}'.format(sys._getframe().f_code.co_name))
    dealXmlPath = '{}_deal.xml'.format(os.path.splitext(xmlPath)[0])
    # 清掉之前的文件
    if os.path.exists(dealXmlPath):
        os.remove(dealXmlPath)
    f2 = open(dealXmlPath, mode='a', encoding='utf8')
    with open(xmlPath, mode='r', encoding='utf') as f:
        for line in f.readlines():
            line = line.replace('&lt;', '<')
            line = line.replace('&gt;', '>')
            f2.write(line)
        f2.close()
    return dealXmlPath

def createRobotFile(fPath, content, t=0):
    '''

    :param fPath:
    :param content:
    :param t:
    :return:
    '''
    logging.info('进入{}'.format(sys._getframe().f_code.co_name))
    filterStr = ['"', ':', '<', '>', '*', '|', '?']
    filePath = fPath
    for fs in filterStr:
        filePath = filePath.replace(fs, '-')
    with open(filePath, mode='a', encoding='utf8') as f:
        # t=1是写测试用例的步骤，要换行，前面有4个空格
        if t == 1:
            f.write('\n\t')
        # t=2是写预期结果，不用换行，前面有4个空格
        elif t == 2:
            f.write('\t')
        else:
        # t=0是写测试用例名称，换两行
            f.write('\n\n')
        f.write(content)

def convertToRobot(nodes, maxLevel, path, mode):
    '''
    转换成robot文件，xmind不低于5个层级
    :param nodes:
    :param maxLevel:
    :param path:
    :param mode:
    :return:
    '''
    logging.info('进入{}'.format(sys._getframe().f_code.co_name))
    index1 = path.rfind(os.sep)
    fileRootPath = path[:index1]
    logging.info('文件根路径：{}'.format(fileRootPath))
    os.chdir(fileRootPath)
    for index in range(len(nodes)):
        node = nodes[index]
        # 控制长度为80
        if len(node.title) > 80:
            node.title = node.title[:80]
        # 处理windows特殊字符
        filterStr = ['"', ':', '?', '<', '>', '*', '|', '\\', '/', '“', '”']
        for fs in filterStr:
            node.title = node.title.replace(fs, '-')
        # 层级是1的节点，直接创建目录
        if node.level == 1:
            node.path = node.title
            fileRootPath = os.path.join(fileRootPath, node.path)
            logging.info('第一个节点路径：{}'.format(fileRootPath))
            #删除整个目录
            if os.path.exists(fileRootPath):
                shutil.rmtree(fileRootPath)
            os.mkdir(node.path)
            logging.info('创建目录：{}'.format(node.path))
        else:
            # 递归得到的层级是按一定顺序排列的，非1层级的节点，从当前位置往回遍历
            for indexParent in range(index - 1, -1, -1):
                if node.level - nodes[indexParent].level == 1:
                    node.path = os.path.join(nodes[indexParent].path, node.title)
                    # 倒数第一项为预期结果
                    if node.level == maxLevel:
                        index1 = node.path.rfind(os.sep)
                        index2 = node.path.rfind(os.sep, 0, index1)
                        index3 = node.path.rfind(os.sep, 0, index2)
                        pathFinal =  '{}.robot'.format(node.path[:index3])
                        logging.info('写入预期结果：{}'.format(pathFinal))
                        createRobotFile(pathFinal, node.title, 2)
                    # 倒数第二项为测试步骤
                    elif node.level == maxLevel - 1:
                        index1 = node.path.rfind(os.sep)
                        index2 = node.path.rfind(os.sep, 0, index1)
                        pathFinal = '{}.robot'.format(node.path[:index2])
                        logging.info('写入测试步骤：{}'.format(pathFinal))
                        createRobotFile(pathFinal, node.title, 1)
                        # 如果没有子节点（没有预期结果）就补全
                        if len(node.childs) == 0 and mode == '2':
                            createRobotFile(pathFinal, node.title, 2)
                    # 倒数第三项为测试用例名称
                    elif node.level == maxLevel - 2:
                        index = node.path.rfind(os.sep)
                        pathFinal = '{}.robot'.format(node.path[:index])
                        logging.info('写入测试用例：{}'.format(pathFinal))
                        createRobotFile(pathFinal, node.title)
                        # 如果没有子节点（没有测试步骤）就补全步骤和预期结果
                        if len(node.childs) == 0 and mode == '2':
                            createRobotFile(pathFinal, node.title, 1)
                            createRobotFile(pathFinal, node.title, 2)
                    # 倒数第四项为测试模块（robot文件）
                    elif node.level == maxLevel - 3:
                        robotPath = '{}.robot'.format(node.path)
                        # 删除已存在的文件
                        if os.path.exists(robotPath):
                            os.remove(robotPath)
                        # 创建文件
                            logging.info('创建robot文件：{}'.format(robotPath))
                        with open(robotPath, mode='w+', encoding='utf8') as f:
                            f.write('*** Test Cases ***')
                    else:
                        if not os.path.exists(node.path):
                            logging.info('创建目录：{}'.format(node.path))
                            os.mkdir(node.path)
                    break
    logging.info('fileRobotPath:'+fileRootPath)
    return fileRootPath

def convertToDisplay(filePath):
    '''
    展示
    :param filePath:
    :return:
    '''
    print('进入{}'.format(sys._getframe().f_code.co_name))
    # 文件存在且是xmind格式
    if os.path.exists(filePath):
        if os.path.splitext(filePath)[1] == '.xmind':
            #获取xmind数据
            nodes, maxLevel = getXmindData(filePath)
            if nodes == -1 and maxLevel == -1:
                logging.info('节点过少，不支持转换')
                raise Exception('节点过少，不支持转换')
            reultsList = display(nodes)
            return reultsList, maxLevel
        else:
            logging.info('非xmind文件')
            raise Exception('非xmind文件')
    else:
        logging.info('输入路径有误')
        raise Exception('输入路径有误')

def dirToTar(path):
    '''
    打包robot文件
    :param path:
    :return:
    '''
    logging.info('进入{}'.format(sys._getframe().f_code.co_name))
    output_filename = '{}.tar'.format(path)
    with tarfile.open(output_filename, 'w:') as tar:
        tar.add(path, arcname=os.path.basename(path))
    return output_filename

def xmind_to_testlink_xml_file(xmind_file, mode):
    '''

    :param xmind_file:
    :param mode:
    :return:
    '''
    logging.info('进入' + sys._getframe().f_code.co_name)
    nodes, maxLevel = getXmindData(xmind_file)
    nodes, xmlPath = convertToXml(nodes, maxLevel, xmind_file, mode)
    dealXmlPath = replaceXml(xmlPath)
    return dealXmlPath

def xmind_to_robot_tar_file(xmind_file, mode):
    '''

    :param xmind_file:
    :param mode:
    :return:
    '''
    logging.info('进入{}'.format(sys._getframe().f_code.co_name))
    nodes, maxLevel = getXmindData(xmind_file)
    fileRootPath = convertToRobot(nodes, maxLevel, xmind_file, mode)
    output_filename = dirToTar(fileRootPath)
    return output_filename