#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys

from . import path_to_enlightenment
from .sensei import Sensei
from .writeln_decorator import WritelnDecorator

class Mountain:
    def __init__(self):
        self.stream = WritelnDecorator(sys.stdout)
        self.lesson = Sensei(self.stream)

    def walk_the_path(self, name="koans"):
        "Run the koans tests with a custom runner output."
        self.tests = unittest.TestLoader().loadTestsFromName("koans." + name)

        self.tests(self.lesson)
        self.lesson.learn()
        return self.lesson
