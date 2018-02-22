#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import markdown
import figureAltCaption

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

DEFAULT_PAGINATION = False

DEFAULT_DATE_FORMAT = ('%-d %B %Y')

DEFAULT_CATEGORY = 'misc'

THEME = "../pelican-themes/gcman"
STATIC_PATHS = ['images', 'figures', 'extra/CNAME', 'extra/404.html', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},'extra/404.html': {'path': '404.html'},'extra/favicon.ico': {'path': 'favicon.ico'}}

READERS = {'html': None}

PLUGIN_PATHS = ['../pelican-plugins']
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

MARKDOWN = {
    'extensions' : ['markdown.extensions.codehilite',
    'markdown.extensions.extra',
    ],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'guess_lang': 'True','use_pygments': 'True'},
    }
}

RELATIVE_URLS = True