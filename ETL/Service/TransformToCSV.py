# coding:utf-8
"""
@file: .py
@author: dannyXSC
@ide: PyCharm
@createTime: 2022年05月16日 15点03分
@Function: 将author、paper和couthor打包
"""
from ETL.Service.TransformAuthorToCSV import main as m1
from ETL.Service.TransformPaperToCSV import main as m2
from ETL.Service.TransformCoauthorToCSV import main as m3


def main():
    m1()
    m2()
    m3()
