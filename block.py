import os
from string import Template
import shutil
import datetime
import time

######################################################
root = '../trunk/src/module'
# 头部注释
TfileHead = './temp/Afileheader.ets'
Tctrl = './temp/Ctrl.ets'
Tmodel = './temp/Model.ets'
Tview = './temp/View.ets'
Tvm = './temp/ViewModel.ets'

# 日期
date = time.strftime('%Y-%m-%D %H:%M:%S', time.localtime())
author = '永青'
##############################################################


contentMapping = {'CTRL': '', 'VIEWMODEL': '', 'MODEL': '', 'VIEW': ''}
headMapping = {'DATE': date, 'AUTHOR': author}


def generate(rootpath):

    if not os.path.exists(rootpath):
        os.makedirs(rootpath)
    else:
        promt = '%s %s %s' % ('路径', rootpath, '已存在,是否继续? yes / no ?  ')
        cmd = input(promt)
        if cmd != 'yes':
            return

    global contentMapping

    print('batch code', rootpath)
    # ctrl
    batch(rootpath, contentMapping['CTRL'], Tctrl)
    # viewModel
    batch(rootpath, contentMapping['VIEWMODEL'], Tvm)
    # model
    batch(rootpath, contentMapping['MODEL'], Tmodel)
    # view
    batch(rootpath, contentMapping['VIEW'], Tview)

    print('batch code complete')


def batch(path, className, tempPath):
    global contentMapping
    fCode = open('%s/%s.ts' % (path, className), mode='w+', encoding='utf-8')

    # 写入头部注释
    header = open(TfileHead, encoding='utf-8').read()
    headstr = Template(header).substitute(headMapping)
    fCode.writelines(headstr)
    fCode.writelines("\r\n")

    # 写入内容
    temp = open(tempPath, encoding='utf-8').read()
    codeTemplate = Template(temp)
    code = codeTemplate.substitute(contentMapping)
    fCode.writelines(code)
    print(fCode.name, '创建成功')
    fCode.close()


def main():
    global contentMapping
    name = input("please enter the module name: ")
    if(len(name) == 0):
        return

    print('开始生成模块代码', name)
    name = name.lower()
    rootpath = root + '/' + name
    # 首字母大写
    Lname = name.capitalize()

    contentMapping['CTRL'] = Lname + 'Ctrl'
    contentMapping['MODEL'] = Lname + 'Model'
    contentMapping['VIEWMODEL'] = Lname + 'ViewModel'
    contentMapping['VIEW'] = Lname + 'View'
    generate(rootpath)


main()
