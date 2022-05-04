# coding:utf-8
"""
@file: .py
@author: dannyXSC
@ide: PyCharm
@createTime: 2022年05月04日 21点47分
@Function: 请描述这个py文件的作用
"""
from ETL.Modal.Affiliation import Affiliation
from py2neo import Graph, NodeMatcher, Node


class AffiliationRepo:
    def __init__(self):
        pass

    @staticmethod
    def create_affiliation_check(graph: Graph, affiliation: Affiliation):
        node_matcher = NodeMatcher(graph)
        node = node_matcher.match("Affiliation", name=affiliation.name).first()
        if node is None:
            node = AffiliationRepo.create_affiliation(graph, affiliation)
        return node

    @staticmethod
    def create_affiliation(graph: Graph, affiliation: Affiliation):
        node = Node("Affiliation", name=affiliation.name)
        graph.create(node)
        graph.push(node)
        return node
