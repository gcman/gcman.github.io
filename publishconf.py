#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://gautammanohar.com/blog'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

GOOGLE_ANALYTICS = "UA-115904815-1"

# Following items are often useful when publishing
#DISQUS_SITENAME = ""
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'