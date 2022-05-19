# Configuration file for the Blender Manual documentation.
# created by the Sphinx 4.1.2 quickstart utility.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

from sphinx import version_info as sphinx_version

sys.path.insert(0, os.path.abspath(os.path.join('..', 'exts')))

# Sphinx errors out on single threaded builds see T86621
sys.setrecursionlimit(2000)


# -- Local Vars --------------------------------------------------------------

# Not used directly by Sphinx, but used by this file and the buildbot.

blender_version = '3.3'


# -- Project information -----------------------------------------------------

project = 'Blender %s Manual' % blender_version
copyright = ': This page is licensed under a CC-BY-SA 4.0 Int. License'
author = 'Blender Documentation Team'

# The major project version, used as the replacement for |version|.
version = blender_version
# The full version, including alpha/beta/rc tags
# release = " ".join((blender_version, "alpha"))
release = blender_version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'reference',
    'peertube',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    '404'
]

# Is there a better way to check for PDF building?
if "latex" in sys.argv:
    # To convert gif's when making a PDF.
    extensions.append('sphinx.ext.imgconverter')
    image_converter = "magick"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../resources/templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = ['_build']

# A string of reStructuredText that will be included at the end of every
# source file that is read. This is a possible place to add substitutions
# that should be available in every file.
rst_epilog = """
.. |BLENDER_VERSION| replace:: %s
.. |TODO| replace:: The documentation here is incomplete, you can help by :doc:`contributing </about/index>`.
""" % blender_version

# Quit warnings about missing download file
# suppress_warnings = ['download.not_readable']

# If set to a major.minor version string like '1.1', Sphinx will compare it
# with its version and refuse to build if it is too old.
needs_sphinx = '3.3'

# The default language to highlight source code in.
highlight_language = 'python3'

# If true, figures, tables and code-blocks are automatically numbered if they have a caption.
numfig = False

# if set to 0, figures, tables and code-blocks are continuously numbered starting at 1.
numfig_secnum_depth = 0

# The style name to use for Pygments highlighting of source code.
pygments_style = 'default'


# -- Options for Internationalization ----------------------------------------

# The code for the language the docs are written in.
# Any text automatically generated by Sphinx will be in that language.
language = 'en'

# Directories in which to search for additional message catalogs,
# relative to the source directory.
locale_dirs = ['../locale/']
gettext_compact = "blender_manual"

# If true, “fuzzy” messages in the message catalogs are used for translation.
gettext_allow_fuzzy_translations = False


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "default"
try:
    import sphinx_rtd_theme
    html_theme = "sphinx_rtd_theme"
    del sphinx_rtd_theme
except ModuleNotFoundError:
    pass

# A dictionary of options that influence the look and feel of
# the selected theme. These are theme-specific.
html_theme_options = {}

# A list of paths that contain custom themes, either as subdirectories
# or as zip files. Relative paths are taken as relative to
# the configuration directory.
html_theme_path = []

if html_theme == "sphinx_rtd_theme":
    html_theme_options = {
        "analytics_id": "UA-1418081-1",
        # included in the title
        "display_version": False,
        "collapse_navigation": True,
        "navigation_depth": -1,
    }

    extensions.append('sphinx_rtd_theme')

# The “title” for HTML documentation generated with Sphinx’s own templates.
# This is appended to the <title> tag of individual pages, and
# used in the navigation bar as the “topmost” element.
html_title = "Blender Manual"

# The base URL which points to the root of the HTML documentation.
# It is used to indicate the location of document using
# The Canonical Link Relation.
html_baseurl = "https://docs.blender.org/manual/en/latest/"

# If given, this must be the name of an image file
# (path relative to the configuration directory) that is the logo of the docs,
# or URL that points an image file for the logo.
#
# Socket logo from: https://www.blender.org/about/logo
html_logo = "../resources/theme/blender-logo.svg"

# If given, this must be the name of an image file
# (path relative to the configuration directory) that is the favicon of
# the docs, or URL that points an image file for the favicon.
html_favicon = "../resources/theme/favicon.ico"

if html_theme == "sphinx_rtd_theme":
    html_css_files = ["css/theme_overrides.css",
                      "css/version_switch.css"]
    html_js_files = ["js/version_switch.js"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["../resources/theme"]

# If this is not None, a ‘Last updated on:’ timestamp is inserted at
# every page bottom, using the given strftime() format.
# The empty string is equivalent to '%b %d, %Y'
# (or a locale-dependent equivalent).
html_last_updated_fmt = '%m/%d/%Y'

# Additional templates that should be rendered to HTML pages,
# must be a dictionary that maps document names to template names.
html_additional_pages = {
    '404': '404.html',
}

# If true, the reST sources are included in the HTML build as _sources/name.
html_copy_source = False

# If true (and html_copy_source is true as well), links to the reST sources
# will be added to the sidebar.
html_show_sourcelink = False

# If nonempty, an OpenSearch description file will be output,
# and all pages will contain a <link> tag referring to it.
# Ed. Note: URL has to be adapted, when versioning is set up.
html_use_opensearch = 'https://docs.blender.org/manual/' + language + '/latest'

# If true, “(C) Copyright …” is shown in the HTML footer.
html_show_copyright = True

# If true, “Created using Sphinx” is shown in the HTML footer.
html_show_sphinx = False

# If true, the text around the keyword is shown as summary of each search result.
html_show_search_summary = True


# -- Options for HTML help output --------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Blender Reference Manual'


# -- Options for Epub output -------------------------------------------------

# The basename for the epub file. It defaults to the project name.
# epub_basename = ''

# The HTML theme for the epub output. Since the default themes are
# not optimized for small screen space, using the same theme for HTML
# and epub output is usually not wise.
epub_theme = 'epub'

# Bibliographic Dublin Core info.
# These default to their non epub counterparts.
# epub_title = ''
epub_description = 'Blender Reference Manual'
# epub_author = ''
epub_publisher = 'Blender Foundation'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
#epub_language = ''

epub_copyright = 'This manual is licensed under a CC-BY-SA 4.0 Int. License.'

# An identifier for the document. This is put in the Dublin Core metadata.
# For published documents this is the ISBN number, but you can also
# use an alternative scheme, e.g. the project homepage.
# epub_identifier = ''

# The publication scheme for the epub_identifier.
# This is put in the Dublin Core metadata.
# For published books the scheme is 'ISBN'.
# If you use the project homepage, 'URL' seems reasonable.
# epub_scheme = ''

# A unique identifier for the document.
# This is put in the Dublin Core metadata.
# epub_uid = ''

# The cover page information. This is a tuple containing the filenames of
# the cover image and the html template.
epub_cover = ('_static/cover.png', 'epub-cover.html')

epub_css_files = ["css/epub_overrides.css"]

# Meta data for the guide element of content.opf.
# This is a sequence of tuples containing the type,
# the uri and the title of the optional guide information.
# epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# Additional files that should be inserted after the text generated by Sphinx.
# It is a list of tuples containing the file name and the title.
# epub_post_files = []

# A list of files that are generated/copied in the build directory
# but should not be included in the epub file.
epub_exclude_files = ['search.html', '404.html']

# The depth of the table of contents in the file toc.ncx.
epub_tocdepth = 2

# This flag determines if a toc entry is inserted again at
# the beginning of its nested toc listing.
# epub_tocdup = True

# This setting control the scope of the epub table of contents.
# epub_tocscope = 'default'

# This flag determines if sphinx should try to fix image formats
# that are not supported by some epub readers.
# epub_fix_images = False

# This option specifies the maximum width of images.
# epub_max_image_width = 0

# Control whether to display URL addresses.
epub_show_urls = 'no'

# If true, add an index to the epub document.
# epub_use_index = True


# -- Options for LaTeX output ------------------------------------------------
# see https://github.com/sphinx-doc/sphinx/issues/3289

latex_engine = 'xelatex'

# This value determines how to group the document tree into LaTeX source files.
# It must be a list of tuples
# (startdocname, targetname, title, author, theme, toctree_only).
latex_documents = [
    ('index', 'blender_manual.tex', 'Blender User Manual',
     'Blender Community', 'manual'),
]

# If given, this must be the name of an image file
# (relative to the configuration directory) that is the logo of the docs.
# It is placed at the top of the title page.

# Disable for now, causes:
# LaTeX Error: Cannot determine size of graphic in blender-logo.svg (no
# Boundin gBox).

'''
latex_logo = "../resources/theme/blender-logo.svg"
'''

# This value determines the topmost sectioning unit. It should be chosen from
# 'part', 'chapter' or 'section'.
#latex_toplevel_sectioning = 'None'

# A list of document names to append as an appendix to all manuals.
#latex_appendices = []

# If true, generate domain-specific indices in addition to the general index.
#latex_domain_indices = True

# If true, add page references after internal references.
# This is very useful for printed copies of the manual.
#latex_show_pagerefs = False

# Control whether to display URL addresses.
latex_show_urls = "no"

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.

    'sphinxsetup': 'hmargin=0.75in, vmargin=1in',

    'classoptions': ',openany,oneside',
    #  'babel': '\\usepackage[english]{babel}',
    # note that xelatex will use polyglossia by default,
    # but if 'babel' key is redefined like above, it will use babel package.

    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',

    'preamble': u'''
\\renewenvironment{wrapfigure}[2]{\\begin{figure}[H]}{\\end{figure}}
\\usepackage{newunicodechar}

\\usepackage{pifont}
\\newunicodechar{✔}{\\ding{52}}
\\newunicodechar{✗}{\\ding{55}}
\\newunicodechar{✛}{\\ding{59}}

\\usepackage{fontawesome}
\\newunicodechar{⏮}{\\faFastBackward}
\\newunicodechar{⏪}{\\faBackward}
\\newunicodechar{▶}{\\faPlay}
\\newunicodechar{⏩}{\\faForward}
\\newunicodechar{⏭}{\\faFastForward}
\\newunicodechar{⏸}{\\faPause}
\\newunicodechar{◀}{\\reflectbox{▶}}
''',

}


# -- Options for manual page output ------------------------------------------

# This value determines how to group the document tree into manual pages.
# It must be a list of tuples
# (startdocname, name, description, authors, section).
man_pages = [
    ('index', 'manual_docs', 'Blender Manual Documentation Documentation',
     [''], 1)
]

# If true, add URL addresses after links.
man_show_urls = False


# -- Options for Texinfo output ----------------------------------------------

# This value determines how to group the document tree into
# Texinfo source files. # It must be a list of tuples
# (startdocname, targetname, title, author, dir_entry,
# description, category, toctree_only)
texinfo_documents = [
    ('index', 'Blender Reference Manual', 'Blender Manual Documentation',
     'Blender Documentation Team', 'Blender Reference Manual'),
]

# A list of document names to append as an appendix to all manuals.
#texinfo_appendices = []

# If true, generate domain-specific indices in addition to the general index.
#texinfo_domain_indices = True

# Control how to display URL addresses.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the “Top” node’s menu
# containing entries for each sub-node in the document.
#texinfo_no_detailmenu = False


# -- Extension configuration -------------------------------------------------

intersphinx_mapping = {
    'blender_api': (
        'https://docs.blender.org/api/' +
        blender_version +
        '/',
        None)}
peertube_instance = "https://video.blender.org/"

# If true, `todo` and `todoList` produce output, else they produce nothing.
# if not release.endswith("release"):
todo_include_todos = True
# todo_link_only = True


# ----------------------------------------------------------------------------
# Monkey Patch, without this 'zh-hant' fails
#
# See: https://lists.blender.org/pipermail/bf-docboard/2017-October/005259.html


def monkey_patch_babl_locale_dash():
    try:
        from sphinx.util.i18n import CatalogInfo
    except ImportError:
        return
    CatalogInfo._write_mo_real = CatalogInfo.write_mo
    if sphinx_version >= (4, 3, 0):
        CatalogInfo.write_mo = lambda self, locale, use_fuzzy: CatalogInfo._write_mo_real(
            self, locale.replace('-', '_'))
    else:
        CatalogInfo.write_mo = lambda self, locale: CatalogInfo._write_mo_real(
            self, locale.replace('-', '_'))


monkey_patch_babl_locale_dash()
