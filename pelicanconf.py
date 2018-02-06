#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gautam Manohar'
SITENAME = "Gautam Manohar"
SITEURL = 'http://gautammanohar.com'

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

TYPOGRIFY = True
MATH_JAX = {'tex_extensions': ['color.js']}

DEFAULT_PAGINATION = False

DEFAULT_DATE_FORMAT = ('%-d %B %Y')

THEME = "../pelican-themes/gcman"
STATIC_PATHS = ['images', 'figures', 'extra/CNAME', 'extra/404.html']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},'extra/404.html': {'path': '404.html'},}

READERS = {'html': None}

PLUGIN_PATHS=['../pelican-plugins']
PLUGINS = ["render_math","pelican-toc","neighbors"]

TOC = {
    'TOC_HEADERS'       : '^h[1-2]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression

    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated

    'TOC_INCLUDE_TITLE': 'false',     # If 'true' include title in toc
}

RELATIVE_URLS = True