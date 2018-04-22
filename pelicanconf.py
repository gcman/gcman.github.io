#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import markdown

AUTHOR = 'Gautam Manohar'
SITENAME = 'Gautam Manohar'
SITEURL = 'https://gautammanohar.com'

CSS_FILE = 'article.css'

GOOGLE_ANALYTICS = 'UA-115904815-1'

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

TYPOGRIFY = False

DEFAULT_PAGINATION = False

DEFAULT_DATE_FORMAT = ('%-d %B %Y')

DEFAULT_CATEGORY = 'misc'

<<<<<<< HEAD
THEME = "gcman"
=======
THEME = "content/theme"
>>>>>>> 99d16111cabf9a769cccd0c466ddf7ad8b5702d2
STATIC_PATHS = ['extra/CNAME', 'extra/404.html', 'extra/favicon.ico', 'extra/README.txt','extra/thanks.html','extra/google9cbd00c2e42ee352.html','extra/index.html']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
'extra/404.html': {'path': '404.html'},
'extra/favicon.ico': {'path': 'favicon.ico'},
'extra/README.txt': {'path': 'README.md'},
'extra/thanks.html': {'path': 'thanks/index.html'},
'extra/google9cbd00c2e42ee352.html': {'path': 'google9cbd00c2e42ee352.html'},
'extra/index.html': {'path': 'index.html'}}

READERS = {'html': None}

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ["pelican-toc","neighbors","pandoc_reader"]

PANDOC_ARGS = [
  '--mathjax',
]

PANDOC_EXTENSIONS = [
  "+yaml_metadata_block",
  "+smart",
  '-citations',
  "+markdown_in_html_blocks",
  "+backtick_code_blocks"
]

TOC = {
    'TOC_HEADERS'       : '^h[1-2]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression

    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated
    'TOC_INCLUDE_TITLE': 'false',    # If 'true' include title in toc
}

RELATIVE_URLS = True

ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"
INDEX_SAVE_AS = "blog/index.html"