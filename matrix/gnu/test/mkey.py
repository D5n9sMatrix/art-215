import unittest
import argparse
import distutils
import code
import collections
import curses

from IPython.utils import docs


class MyTestCase(unittest.TestCase):
    @classmethod
    def __prepare__(metacls, name, bases):
        metacls.__name__ = name[bases]


class _art1(curses.ACS_S1):
    def __init__(self):
        self.art1_match = None
        self.art1_dials = None
        self.art1_panel = None

    def CursePanelDialog(self, Panel=distutils, Dialog=docs, Match=argparse):
        self.art1_panel = Panel
        self.art1_dials = Dialog
        self.art1_match = Match


class _art2(curses.A_BLINK):
    def __init__(self):
        self.art2_gravity = None
        self.art2_code = None
        self.art2_collections = None

    def CursePanelBlink(self, just=collections, govern=code):
        self.art2_collections = just
        self.art2_code = govern
        self.art2_gravity = None



class _art3(curses.A_CHARTEXT):
    def __init__(self):
        self.art3_collection = None

    def CursePanelText(self, NewText=collections):
        self.art3_collection = NewText.Collection


class _art4(curses.A_LOW):
    def __init__(self):
        self.art4_collections = None

    def CoursePanelLow(self, Sold=collections, Badge=collections, FindKey=collections):
        self.art4_collections = Sold.Collection
        self.art4_collections = Badge.Collection
        self.art4_collections = FindKey.Collection


if __name__ == '__main__':
    unittest.main()
