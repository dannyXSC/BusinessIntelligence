# coding:utf-8
"""
@file: .py
@author: dannyXSC
@ide: PyCharm
@createTime: 2022年05月04日 22点09分
@Function: 请描述这个py文件的作用
"""
from py2neo import Graph, NodeMatcher, Node

from ETL.Modal.Interest import Interest


class InterestRepo:
    def __init__(self):
        pass

    @staticmethod
    def create_interest_check(graph: Graph, interest: Interest):
        node_matcher = NodeMatcher(graph)
        node = node_matcher.match("Interest", name=interest.name).first()
        if node is None:
            node = InterestRepo.create_interest(graph, interest)
        return node

    @staticmethod
    def create_interest(graph: Graph, interest: Interest):
        node = Node("Interest", name=interest.name)
        graph.create(node)
        graph.push(node)
        return node
