# coding:utf-8
"""
@file: .py
@author: dannyXSC
@ide: PyCharm
@createTime: 2022年05月04日 20点49分
@Function: 工具函数
"""
import yaml
from ETL.EnvironmentVariable import *


def get_neo4j_info():
    with open(resource_path, "r") as stream:
        try:
            obj = yaml.safe_load(stream)["neo4j"]
            return obj["url"], obj["account"], obj["password"]
        except yaml.YAMLError as exc:
            print(exc)
            return "" "" ""


def get_author_path():
    with open(resource_path, "r") as stream:
        try:
            obj = yaml.safe_load(stream)["AMiner"]
            return obj["author_path"]
        except yaml.YAMLError as exc:
            print(exc)
            return ""


def get_coauthor_path():
    with open(resource_path, "r") as stream:
        try:
            obj = yaml.safe_load(stream)["AMiner"]
            return obj["coauthor_path"]
        except yaml.YAMLError as exc:
            print(exc)
            return ""


def get_paper_path():
    with open(resource_path, "r") as stream:
        try:
            obj = yaml.safe_load(stream)["AMiner"]
            return obj["paper_path"]
        except yaml.YAMLError as exc:
            print(exc)
            return ""
