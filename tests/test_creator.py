#!/usr/bin/env python
#=====================
from __future__ import print_function

import unittest

import os
import shutil
import sys

sys.path.append('..')      # Needed to import code

from gistit.creator import Creator


@unittest.skipIf('SKIP_SLOW_TESTS' in os.environ, 'Requested fast tests')
class test_online_functional(unittest.TestCase):
    def setUp(self):
        self.creator = Creator()
        self.dummy_content = "Somebody ran GistIt tests: http://is.gd/GistIt"
        pass

    def tearDown(self):
        pass

    def test_create_returns_something_not_null(self):
        jsoon = self.creator.create("")
        self.assertTrue(jsoon != None)

    def test_create_returns_html_url_in_json(self):
        jsoon = self.creator.create(self.dummy_content)
        self.assertTrue('html_url' in jsoon.keys())
        self.assertFalse('errors' in jsoon.keys())

    def test_create_public_gist_by_default(self):
        jsoon = self.creator.create(self.dummy_content)
        self.assertTrue(jsoon['public'])

    def test_create_returns_error_in_json_for_empty_content(self):
        jsoon = self.creator.create("")
        self.assertTrue('errors' in jsoon.keys())

unittest.main()
