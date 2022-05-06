# # coding:utf-8
# """
# @file: .py
# @author: dannyXSC
# @ide: PyCharm
# @createTime: 2022年05月04日 20点40分
# @Function: 测试
# """
# import time
#
# from ETL.Modal.Author import Author
# from ETL.Repository.AuthorRepo import AuthorRepo
# from utils import *
# from py2neo import *
# from Repository.AffiliationRepo import AffiliationRepo
# from Modal.Affiliation import Affiliation
# from ETL.Reader.AuthorReader import *
#
# from py2neo import *
#
# from ETL.Reader.AuthorReader import read_author
# from ETL.Repository.AffiliationRepo import AffiliationRepo
# from ETL.Repository.AuthorRepo import AuthorRepo
# from ETL.Repository.InterestRepo import InterestRepo
# from ETL.utils import *
#
# url, account, password = "http://localhost:9742/browser/", "neo4j", "password"
# graph = Graph(url, auth=(account, password))
#
# existed_author_set = set()
# existed_affiliation_set = set()
# existed_interest_set = set()
#
#
# @timer("获得已存在的名称信息")
# def get_exist_name():
#     global existed_author_set, existed_affiliation_set, existed_interest_set
#     # 获取所有已经创建的节点
#     # 获得所有作者的名称
#     existed_author_set = AuthorRepo.get_all_author_name(graph)
#     # 获得所有机构的名称
#     existed_affiliation_set = AffiliationRepo.get_all_affiliation_name(graph)
#     # 获得所有兴趣的名称
#     existed_interest_set = InterestRepo.get_all_interest_name(graph)
#     print(f"已存在的作者数量：{len(existed_author_set)}\n"
#           f"已存在的机构数量：{len(existed_affiliation_set)}\n"
#           f"已存在的兴趣数量：{len(existed_interest_set)}")
#
#
# create_nodes = []
# create_node_cnt = 0
# author_list = []
#
#
# @timer("读取本地作者信息")
# def read_author_info():
#     global create_node_cnt, create_nodes, author_list
#
#     create_node_cnt = 0
#
#     cnt = 0
#
#     for author in read_author():
#         author_list.append(author)
#         if author.name not in existed_author_set:
#             existed_author_set.add(author.name)
#             create_nodes.append(AuthorRepo.to_neo4j_node(author))
#             create_node_cnt += 1
#
#         for affiliation in author.get_affiliations_list():
#             if affiliation.name not in existed_affiliation_set:
#                 existed_affiliation_set.add(affiliation.name)
#                 create_nodes.append(AffiliationRepo.to_neo4j_node(affiliation))
#                 create_node_cnt += 1
#
#         for interest in author.get_interests_list():
#             if interest.name not in existed_interest_set:
#                 existed_interest_set.add(interest.name)
#                 create_nodes.append(InterestRepo.to_neo4j_node(interest))
#                 create_node_cnt += 1
#
#         cnt += 1
#         if cnt % 1000 == 0:
#             print(f"已完成{cnt}")
#
#
# batch_size = 100
#
#
# @timer("批量创建节点")
# def create_node():
#     if create_node_cnt > 0:
#         for i in range(create_node_cnt // batch_size + 1):
#             subgraph = Subgraph(create_nodes[i * batch_size: (i + 1) * batch_size])
#             graph.create(subgraph)
#             print(f"create {(i + 1) * batch_size} nodes | total {create_node_cnt} nodes")
#
#
# create_rel_cnt = 0
# create_relations = []
#
#
# @timer("读取本地作者信息")
# def read_author_info2():
#     global create_rel_cnt, create_relations
#
#     create_rel_cnt = 0
#     cnt = 0
#
#     for author in read_author():
#         author_node = AuthorRepo.get_author_by_name(graph,author.name)
#         if author_node is None:
#             break
#         affiliation_nodes = AuthorRepo.get_affiliation_list(graph, author)
#         interest_nodes = AuthorRepo.get_interest_list(graph, author)
#         for affiliation_node in affiliation_nodes:
#             create_relations.append(Relationship(author_node, "Work At", affiliation_node))
#             create_relations.append(Relationship(affiliation_node, "HAVE", author_node))
#             create_rel_cnt += 1
#
#         for interest_node in interest_nodes:
#             create_relations.append(Relationship(author_node, "Interest in", interest_node))
#             create_relations.append(Relationship(interest_node, "HAVE", author_node))
#             create_rel_cnt += 1
#
#         cnt += 1
#         print(f"已完成{cnt}")
#
#
#
#
# batch_size = 100
#
#
# @timer("批量创建关系")
# def create_relationship():
#     if create_rel_cnt > 0:
#         for i in range(create_rel_cnt // 50 + 1):
#             subgraph = Subgraph(relationships=create_relations[i * batch_size: (i + 1) * batch_size])
#             graph.create(subgraph)
#             print(f"create {(i + 1) * batch_size} relations")
#
#
# get_exist_name()
# read_author_info()
# create_node()
#
# # read_author_info2()
# # create_relationship()
