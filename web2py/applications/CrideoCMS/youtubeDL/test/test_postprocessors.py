#!/usr/bin/env python

from __future__ import unicode_literals

import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from applications.CrideoCMS.modules.youtube_dl import MetadataFromTitlePP


class TestMetadataFromTitle(unittest.TestCase):
    def test_format_to_regex(self):
        pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
        self.assertEqual(pp._titleregex, '(?P<title>.+)\ \-\ (?P<artist>.+)')
