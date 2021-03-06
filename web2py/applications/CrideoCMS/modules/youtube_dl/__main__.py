#!/usr/bin/env python
from __future__ import unicode_literals

import sys

if __package__ is None and not hasattr(sys, 'frozen'):
    # direct call of __main__.py
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

import youtube_dl

if __name__ == '__main__':
    youtube_dl.main()
