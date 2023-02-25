#!-*- coding: utf-8 -*-
"""Python File Remuneration art 215"""
import argparse
import curses
import distutils

from IPython.utils import docs


class _art1(curses.ACS_S1):
    def __init__(self):
        self.art1_match = None
        self.art1_dials = None
        self.art1_panel = None

    def CursePanelDialog(self, Panel=distutils, Dialog=docs, Match=argparse):
        self.art1_panel = Panel
        self.art1_dials = Dialog
        self.art1_match = Match
        