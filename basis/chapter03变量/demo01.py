#! C:\Program Files\Python37\python.exe
# _*_ Coding:UTF-8 -*-
"""
模块介绍：实现加减乘除运算
~~~~~~~~~~~~~~~~~~~~~~~~~~
两数相加：add(num01,num02)
两数相键：sub(num01,num02)
两数相乘：mul(num01,num02)
两数相商：div(num01,num02)

"""
def add(num01,num02):
    # 返回两数之和
    return num01 + num02

def sub(num01,num02):
    # 返回两数之差
    return num01 - num02

def mul(num01,num02):
    # 返回两数之积
    return num01 * num02

def div(num01,num02):
    #返回两数之商
    return num01 / num02

# 程序的入口：main函数
if __name__=='__main__':
    print("两数之和:",add(100, 200))
    print("两数之差:",sub(100, 200))
    print("两数之积:",mul(100, 200))
    print("两数之商:",div(100, 200))