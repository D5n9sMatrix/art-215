#!-*- coding: utf-8 -*-
"""Python File Remuneration Art 215"""
import collections
import curses


class _art4(curses.A_LOW):
    def __init__(self):
        self.art4_collections = None

    def CoursePanelLow(self, Sold=collections, Badge=collections, FindKey=collections):
        self.art4_collections = Sold.Collection
        self.art4_collections = Badge.Collection
        self.art4_collections = FindKey.Collection
