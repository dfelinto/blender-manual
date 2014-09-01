#########
  Readme
#########

Building the Manual
*******************

The manual is built using Sphinx, see: http://sphinx-doc.org


Makefile
========

We provide a Makefile tested on Linux and OSX, so you can simply typen run ``make`` to build documents.
To avoid having to build the entire manual, we have support for making single chapters:
eg: ``make render`` or ``make modeling``, see ``make help`` for a full list of options.

This will generate documents in ``./html``


Sphinx-Build
============

You may want to run sphinx-build directly,
(currently only supported method on MS-Windows):

.. code-block::

  sphinx-build -b html ./manual ./html


Conventions
***********

- 3 space indentation.
- lots of lines over 120 length (low priority)
- check out the following syntax for titles
- TODO: Choose a way to reference UI elements, ``:guilabel:`` is used all over, but may want to just use bold/italic.


Migration
*********

We're currently migrating the docs from MediaWiki, so there are some leftover TODO's.

Cleanup:

- Replace all instances of ``nicetip`` with the ``.. tip::`` directive.
- Replace some unnecessary tables with bullets - eg: ``render/output/video.rst:220``
- ``FIXME(Link Type Unsupported: ...`` and ``Internal Link;`` we have a lot of these, could automate fixes.
- ``FIXME(Tag Unsupported:youtube``, integrate youtube extension (over 50 youtube links), see:
  http://sphinx-doc.org/extensions.html
  https://bitbucket.org/birkenfeld/sphinx-contrib
- There are links into http://wiki.blender.org, these need to be corrected
- Fix titles, allowing only one ``h1`` per file (clearer menu structure)
- Some links to the ``changelog_`` should be setup to dynamic update to current Blender Version.


Directory layout
================

Sections should be generally structured as follows:

- *directory_name*

  - ``index.rst`` (contains links to internal files)
  - ``introduction.rst``
  - ``section_1.rst``
  - ``section_2.rst``

For example:

- rendering/

  - ``index.rst``
  - ``cycles/``

    - ``index.rst``
    - ``introduction.rst``
    - ``materials/``

      - ``index.rts``
      - ``introduction.rst``
      - ``volumes.rst``

The idea is to enclose all the content of a section inside of a folder. Ideally every section
should have an index.rst (containing the TOC for that section) and an introduction.rst 
(introducing) to the contents of the section.


Table of Contents
=================

By default a table of contents should show two levels of depth.

.. code-block:: rst

   .. toctree::
   :maxdepth: 2

   introduction.rst
   perspective.rst
   depth_of_field.rst


Style guidelines
================

Headings

.. code-block:: rst

   h1 header
   *********

   h2 header
   =========

   h3 header
   ---------

   h4 header
   ~~~~~~~~~

