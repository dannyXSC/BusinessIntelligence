# coding:utf-8
"""
@file: .py
@author: dannyXSC
@ide: PyCharm
@createTime: 2022年05月04日 20点40分
@Function: 测试
"""
from ETL.Modal.Author import Author
from ETL.Repository.AuthorRepo import AuthorRepo
from utils import *
from py2neo import *
from Repository.AffiliationRepo import AffiliationRepo
from Modal.Affiliation import Affiliation
from ETL.Reader.AuthorReader import *

url, account, password = get_neo4j_info()
graph = Graph(url, auth=(account, password))

cnt = 0
for author in read_author():
    AuthorRepo.create_author_check(graph, author)
    cnt += 1
    if cnt % 10 == 0:
        print("已完成{}条".format(cnt))
