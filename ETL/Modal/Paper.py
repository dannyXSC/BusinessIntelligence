# coding:utf-8
"""
@file: .py
@author: dannyXSC
@ide: PyCharm
@createTime: 2022年05月04日 21点16分
@Function: 请描述这个py文件的作用
"""


class Paper:
    def __init__(self, index=-1, title="", year=-1, authors=None, venue="", cites=None, abstract=""):
        if authors is None:
            authors = []
        if cites is None:
            cites = []

        self.index = index
        self.title = title
        self.year = year
        self.authors = authors
        self.venue = venue
        self.cites = cites
        self.abstract = abstract
