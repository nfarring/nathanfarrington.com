#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

###########################
# PELICAN: BASIC SETTINGS #
###########################

# A list of directories to exclude when looking for articles in addition to
# PAGE_PATHS.
ARTICLE_EXCLUDES = ['articles/images']

# A list of directories and files to look at for articles, relative to PATH.
ARTICLE_PATHS = ['articles']

# If True, saves content in caches. See Reading only modified content for
# details about caching.
CACHE_CONTENT = False

# Directory in which to store cache files.
CACHE_PATH = 'cache'

# Controls how files are checked for modifications.
CHECK_MODIFIED_METHOD = 'mtime'

# If set to 'reader', save only the raw content and metadata returned by
# readers. If set to 'generator', save processed content objects.
CONTENT_CACHING_LAYER = 'reader'

# The default category to fall back on.
DEFAULT_CATEGORY = 'uncategorized'

# Delete the output directory, and all of its contents, before generating new
# files. This can be useful in preventing older, unnecessary files from
# persisting in your output. However, this is a destructive setting and should
# be handled with extreme care.
DELETE_OUTPUT_DIRECTORY = False

# Whether to display categories on the menu of the template. Templates may or
# not honor this setting.
DISPLAY_CATEGORIES_ON_MENU = True

# Whether to display pages on the menu of the template. Templates may or may not
# honor this setting.
DISPLAY_PAGES_ON_MENU = True

# Extra configuration settings for the docutils publisher (applicable only to
# reStructuredText). See Docutils Configuration settings for more details.
DOCUTILS_SETTINGS = {}

# A list of metadata fields containing reST/Markdown content to be parsed and
# translated to HTML.
FORMATTED_FIELDS = ['summary']

# If True, use gzip to (de)compress the cache files.
GZIP_CACHE = True

# A dictionary of custom Jinja2 environment variables you want to use. This also
# includes a list of extensions you may want to include. See Jinja Environment
# documentation.
JINJA_ENVIRONMENT = {'trim_blocks': True, 'lstrip_blocks': True}

# A dictionary of custom Jinja2 filters you want to use. The dictionary should
# map the filtername to the filter function.
JINJA_FILTERS = {}

# A list of glob patterns. Files and directories matching any of these patterns
# will be ignored by the processor. For example, the default ['.#*'] will ignore
# emacs lock files, and ['__pycache__'] would ignore Python 3’s bytecode caches.
IGNORE_FILES = ['.#*']

# Regular expression that is used to parse internal links. Default syntax when
# linking to internal files, tags, etc., is to enclose the identifier, say
# filename, in {} or ||. Identifier between { and } goes into the what capturing
# group. For details see Linking to internal content.
INTRASITE_LINK_REGEX = '[{|](?P<what>.*?)[|}]'

# If True, load unmodified content from caches.
LOAD_CONTENT_CACHE = False

# A list of filenames that should be retained and not deleted from the output
# directory. One use case would be the preservation of version control data.
OUTPUT_RETENTION = ['.git']

# Where to output the generated files.
OUTPUT_PATH = 'output/'

# Set to True if you want to copy the articles and pages in their original
# format (e.g. Markdown or reStructuredText) to the specified OUTPUT_PATH.
OUTPUT_SOURCES = False

# Controls the extension that will be used by the SourcesGenerator. Defaults to
# .text. If not a valid string the default value will be used.
OUTPUT_SOURCES_EXTENSION = '.text'

# Path to content directory to be processed by Pelican. If undefined, and
# content path is not specified via an argument to the pelican command, Pelican
# will use the current working directory.
PATH = 'content'

# A list of directories to exclude when looking for pages in addition to
# ARTICLE_PATHS.
PAGE_EXCLUDES = []

# A list of directories and files to look at for pages, relative to PATH.
PAGE_PATHS = ['pages']

# The list of plugins to load.
PLUGINS = ['extract_toc', 'sitemap', 'tipue_search']

# A list of directories where to look for plugins.
PLUGIN_PATHS = ['/Users/nfarring/src/pelican-plugins']

# A list of default Pygments settings for your reStructuredText code blocks. See
# Syntax highlighting for a list of supported options.
PYGMENTS_RST_OPTIONS = {
#   'anchorlinenos': True,  # wrap line numbers in anchor tags
#   'classprefix': '',      # string to prepend to token class names
#   'hl_lines': [],         # list of lines to be highlighted
#   'lineanchors': True,    # wrap each line in an anchor
    'linenos': 'table',     # If present or set to “table” output line numbers
                            # in a table, if set to “inline” output them inline.
                            # “none” means do not output the line numbers.
#   'linenospecial': True,  # every nth line gets ‘special’ css class
#   'linenostart': 1,       # line number for the first line
#   'linenostep': 1,        # print every nth line number
#   'lineseparator': '\n',  # string to print between lines of code,
                            # ‘n’ by default.
#   'linespans': '',        # wrap each line in a span
#   'nobackground': True,   # do not output background color
#   'nowrap': True,         # do not wrap the tokens at all
#   'tagsfile':             # ctags file to use for name definitions
#   'tagurlformat':         # format for the ctag links
}

# A dictionary of file extensions / Reader classes for Pelican to process or
# ignore.
READERS = {}

# Your site name
SITENAME = "Nathan Farrington"

# Base URL of your website. Not defined by default, so it is best to specify
# your SITEURL; if you do not, feeds will not be generated with properly-formed
# URLs. You should include http:// and your domain, with no trailing slash at
# the end. Example: SITEURL = 'http://mydomain.com'
SITEURL = 'http://nathanfarrington.com'

# Specifies where you want the slug to be automatically generated from. Can be
# set to title to use the ‘Title:’ metadata tag or basename to use the article’s
# file name when creating the slug.
SLUGIFY_SOURCE = 'title'

# A list of directories to exclude when looking for static files.
STATIC_EXCLUDES = []

# A list of directories (relative to PATH) in which to look for static files.
# Such files will be copied to the output directory without modification.
# Articles, pages, and other content source files will normally be skipped, so
# it is safe for a directory to appear both here and in PAGE_PATHS or
# ARTICLE_PATHS. Pelican’s default settings include the “images” directory here.
STATIC_PATHS = [
    'articles/images',
    'bib',
    'extra',
    'images',
    'papers',
    'patents',
    'pdfs',
    'posters',
    'presentations',
]

# When creating a short summary of an article, this will be the default length
# (measured in words) of the text created. This only applies if your content
# does not otherwise specify a summary. Setting to None will cause the summary
# to be a copy of the original content.
SUMMARY_MAX_LENGTH = 50

# If set to True, several typographical improvements will be incorporated into
# the generated HTML via the Typogrify library.
TYPOGRIFY = True

# A list of tags for Typogrify to ignore. By default Typogrify will ignore pre
# and code tags. This requires that Typogrify version 2.0.4 or later is
# installed.
TYPOGRIFY_IGNORE_TAGS = []

# When you don’t specify a category in your post metadata, set this setting to
# True, and organize your articles in subfolders, the subfolder will become the
# category of your post. If set to False, DEFAULT_CATEGORY will be used as a
# fallback.
USE_FOLDER_AS_CATEGORY = False

# If disabled, content with dates in the future will get a default status of
# draft. See Reading only modified content for caveats.
WITH_FUTURE_DATES = True

# If this list is not empty, only output files with their paths in this list are
# written. Paths should be either absolute or relative to the current Pelican
# working directory. For possible use cases see Writing only selected content.
WRITE_SELECTED = []

#########################
# PELICAN: URL SETTINGS #
#########################

# The location to save the article archives page.
ARCHIVES_SAVE_AS = 'archives.html'

# The place where we will save an article.
ARTICLE_SAVE_AS = 'articles/{slug}.html'

# The URL to refer to an article which doesn’t use the default language.
ARTICLE_LANG_URL = 'articles/{slug}-{lang}.html'

# The URL to refer to an article.
ARTICLE_URL = 'articles/{slug}.html'

# The place where we will save an article which doesn’t use the default
# language.
ARTICLE_LANG_SAVE_AS = 'articles/{slug}-{lang}.html'

# The location to save an author.
AUTHOR_SAVE_AS = ''

# Substitutions for authors. SLUG_SUBSTITUTIONS is not taken into account here!
AUTHOR_SUBSTITUTIONS = ()

# The URL to use for an author.
AUTHOR_URL = 'author/{slug}.html'

# The location to save the author list.
AUTHORS_SAVE_AS = ''

# The location to save a category.
CATEGORY_SAVE_AS = ''

# Added to SLUG_SUBSTITUTIONS for categories.
CATEGORY_SUBSTITUTIONS = ()

# The URL to use for a category.
CATEGORY_URL = 'category/{slug}.html'

# The location to save the category list.
CATEGORIES_SAVE_AS = 'categories.html'

# The location to save per-day archives of your posts.
DAY_ARCHIVE_SAVE_AS = ''

# The place where we will save an article draft.
DRAFT_SAVE_AS = 'drafts/{slug}.html'

# The URL to refer to an article draft.
DRAFT_URL = 'drafts/{slug}.html'

# The place where we will save an article draft which doesn’t use the default
# language.
DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}.html'

# The URL to refer to an article draft which doesn’t use the default language.
DRAFT_LANG_URL = 'drafts/{slug}-{lang}.html'

# The location to save the list of all articles.
INDEX_SAVE_AS = 'index.html'

# The location to save per-month archives of your posts.
MONTH_ARCHIVE_SAVE_AS = ''

# The location we will save the page. This value has to be the same as PAGE_URL
# or you need to use a rewrite in your server config.
PAGE_SAVE_AS = '{slug}.html'

# The URL we will use to link to a page.
PAGE_URL = '{slug}.html'

# The URL we will use to link to a page which doesn’t use the default language.
PAGE_LANG_URL = '{slug}-{lang}.html'

# The location we will save the page which doesn’t use the default language.
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

# Defines whether Pelican should use document-relative URLs or not. Only set
# this to True when developing/testing and only if you fully understand the
# effect it can have on links/feeds.
RELATIVE_URLS = True

# Substitutions to make prior to stripping out non-alphanumerics when generating
# slugs. Specified as a list of 3-tuples of (from, to, skip) which are applied
# in order. skip is a boolean indicating whether or not to skip replacement of
# non-alphanumeric characters. Useful for backward compatibility with existing
# URLs.
SLUG_SUBSTITUTIONS = ()

# The location to save the tag page.
TAG_SAVE_AS = ''

# Added to SLUG_SUBSTITUTIONS for tags.
TAG_SUBSTITUTIONS = ()

# The URL to use for a tag.
TAG_URL = 'tag/{slug}.html'

# The location to save the tag list.
TAGS_SAVE_AS = 'tags.html'

# The location to save per-year archives of your posts.
YEAR_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/index.html'

##########################
# PELICAN: TIME AND DATE #
##########################

# The timezone used in the date information, to generate Atom and RSS feeds.
#
# If no timezone is defined, UTC is assumed. This means that the generated Atom
# and RSS feeds will contain incorrect date information if your locale is not
# UTC.
TIMEZONE = 'America/Los_Angeles'

# The default date you want to use. If 'fs', Pelican will use the file system
# timestamp information (mtime) if it can’t get date information from the
# metadata. If given any other string, it will be parsed by the same method as
# article metadata. If set to a tuple object, the default datetime object will
# instead be generated by passing the tuple to the datetime.datetime
# constructor.
DEFAULT_DATE = None

# The default date format you want to use.
#DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# If you manage multiple languages, you can set the date formatting here.
DATE_FORMATS = {}

# Change the locale
LOCALE = ('en_US.UTF-8', 'C', 'POSIX')

###########################
# PELICAN: TEMPLATE PAGES #
###########################

# List of templates that are used directly to render content. Typically direct
# templates are used to generate index pages for collections of content (e.g.,
# tags and category index pages). If the tag and category collections are not
# needed, set DIRECT_TEMPLATES = ['index', 'archives']
DIRECT_TEMPLATES = [
    'archives',
    'categories',
    'index',
    'search',
    'tags',
    '404',
]

# A list of paths you want Jinja2 to search for templates. Can be used to
# separate templates from the theme. Example: projects, resume, profile ...
# These templates need to use DIRECT_TEMPLATES setting.
EXTRA_TEMPLATES_PATHS = []

# Provides the direct templates that should be paginated.
PAGINATED_DIRECT_TEMPLATES = ['index']

# A mapping containing template pages that will be rendered with the blog
# entries. See Template pages. If you want to generate custom pages besides
# your blog entries, you can point any Jinja2 template file with a path pointing
# to the file and the destination path for the generated file.
TEMPLATE_PAGES = {
}

#####################
# PELICAN: METADATA #
#####################

# Default author (usually your name).
AUTHOR = 'Nathan Farrington'

# The default metadata you want to use for all articles and pages.
DEFAULT_METADATA = {
    'status': 'draft',
}

# Extra metadata dictionaries keyed by relative path. Relative paths require
# correct OS-specific directory separators (i.e. / in UNIX and \ in Windows)
# unlike some other Pelican file settings.
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

# The regexp that will be used to extract any metadata from the filename. All
# named groups that are matched will be set in the metadata object.
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

# Like FILENAME_METADATA, but parsed from a page’s full path relative to the
# content source directory.
PATH_METADATA = ''

##########################
# PELICAN: FEED SETTINGS #
##########################

AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
FEED_ATOM = None
FEED_DOMAIN = None
FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

#######################
# PELICAN: PAGINATION #
#######################

# The minimum number of articles allowed on the last page. Use this when you
# don’t want the last page to only contain a handful of articles.
DEFAULT_ORPHANS = 0

# The maximum number of articles to include on a page, not including orphans.
# False to disable pagination.
DEFAULT_PAGINATION = 10

# A set of patterns that are used to determine advanced pagination output.
# PAGINATION_PATTERNS

#########################
# PELICAN: TRANSLATIONS #
#########################

# The default language to use.
DEFAULT_LANG = 'en'

#############################
# PELICAN: ORDERING CONTENT #
#############################

# Order archives by newest first by date. (False: orders by date with older
# articles first.)
NEWEST_FIRST_ARCHIVES = True

# Reverse the category order. (True: lists by reverse alphabetical order;
# default lists alphabetically.)
REVERSE_CATEGORY_ORDER = False

# Defines how the articles (articles_page.object_list in the template) are
# sorted. Valid options are: metadata as a string (use reversed- prefix the
# reverse the sort order), special option 'basename' which will use the basename
# of the file (without path) or a custom function to extract the sorting key
# from articles. The default value, 'reversed-date', will sort articles by date
# in reverse order (i.e. newest article comes first).
ARTICLE_ORDER_BY = 'reversed-date'

# Defines how the pages (PAGES variable in the template) are sorted. Options are
# same as ARTICLE_ORDER_BY. The default value, 'basename' will sort pages by
# their basename.
PAGE_ORDER_BY = 'basename'

###################
# PELICAN: THEMES #
###################

# Specify the CSS file you want to load.
CSS_FILE = 'main.css'

# Theme to use to produce the output. Can be a relative or absolute path to a
# theme folder, or the name of a default theme or a theme installed via
# pelican-themes (see below).
THEME = 'theme'

# Destination directory in the output path where Pelican will place the files
# collected from THEME_STATIC_PATHS. Default is theme.
THEME_STATIC_DIR = 'theme'

# Static theme paths you want to copy. Default value is static, but if your
# theme has other static paths, you can put them here. If files or directories
# with the same names are included in the paths defined in this settings, they
# will be progressively overwritten.
THEME_STATIC_PATHS = ['static']

####################
# PELICAN: LOGGING #
####################

# A list of tuples containing the logging level (up to warning) and the message
# to be ignored.
LOG_FILTER = []

###########################
# PELICAN PLUGIN: SITEMAP #
###########################

SITEMAP = {
    'format': 'xml',
}

##################
# THEME SETTINGS #
##################

BIOGRAPHY = """
<p>Nathan Farrington is currently the Director of Software and System
Architecture at Rockley Photonics. Previously, Nathan was the founder and CEO of
Packetcounter, a computer network software and services company. Before that he
was a data center network engineer at Facebook developing the Open Compute
Project top-of-rack switch (Wedge and FBOSS). Before grad school, Nathan worked
for the US Navy in mobile robotics and situational awareness applications for
the Department of Homeland Security.</p>

<p>Nathan graduated from the University of California, San Diego, with a PhD in
Computer Science and Computer Engineering. He was advised by Amin Vahdat, now at
Google, as well as George Porter, George Papen, and Yeshaiahu “Shaya" Fainman.
Nathan’s dissertation topic was on novel optical communications for data center
networks. Nathan has served on the TPC of OFC 2014–2016 and ACM SOSR 2016, and
as a reviewer for numerous journals including IEEE/ACM Transactions on
Networking, IEEE/OSA Journal of Lightwave Technology, IEEE Micro, and ACM
SIGCOMM Computer Communications Review. He is a member of the IEEE, the OSA, and
the ACM.</p>
"""

# Thumbnail image to show when homepage is shared on social media. It also
# serves as the default image for posts whose featured_image is not set.
FEATURED_IMAGE = ''

# Dictionary with two keys: title, details.
LANDING_PAGE_ABOUT = {
    'title': '',
    'details': BIOGRAPHY,
}

# Array of dictionaries, each having three keys: name, url, description.
PROJECTS = [{
    'name': 'RedisRPC',
    'url': 'https://github.com/nfarring/redisrpc',
    'description': 'Lightweight RPC using Redis',
}]

# Used in meta tags for SEO.
SITE_DESCRIPTION = """The professional homepage of Nathan Farrington."""

# License appears in the footer of every page.
SITE_LICENSE = """
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="/images/cc-by-80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
"""

# Displayed along with SITENAME in the footer of every page.
SITESUBTITLE = ''

# Display favicon and speed dial icon.
USE_SHORTCUT_ICONS = True
