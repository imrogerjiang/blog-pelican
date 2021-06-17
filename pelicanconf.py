#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import date


AUTHOR = 'Roger'
AUTHORS = {
    'Roger':{}
}

SITENAME = 'rogerjiang'
SITEURL = ''

USE_SHORTCUT_ICONS = True

PATH = 'content'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives']
# , 'search', '404'

THEME = 'clean-blog'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('envelope', 'mailto:imrogerjiang@gmail.com'),
    ('linkedin', 'https://www.linkedin.com/in/roger-jiang/'),
    ('github', 'https://github.com/imrogerjiang/'),
    ('twitter', 'https://twitter.com/imrogerjiang'),
    )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Settings added from archerimagine
ARTICLE_PATHS = ['articles',]
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

STATIC_PATHS = ['theme/images', 'images']

PLUGINS = ['sitemap', 'tipue_search', 'extract_toc', 'neighbors']
PLUGIN_PATHS = ['../pelican-plugins']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc' :{'permalink' : ' ➚'},

    },
    'output_format': 'html5',
}

FAVICON = 'theme/images/favicon.ico'

MENUITEMS = (
    ('portfolio', 'portfolio'),
    ('tags', 'tags'),
    ('archive', 'archives'),
)

TEMPLATE_PAGES = {
    'portfolio.html': 'portfolio.html'
}

CURRENTYEAR = date.today().year