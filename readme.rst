TODO
====

Cleanup:

- Replace all instances of ``nicetip`` with the ``.. tip::`` directive.
- Replace some unnecessary tables with bullets - eg: ``render/output/video.rst:220``
- ``FIXME(Link Type Unsupported: ...`` we have a lot of these, could automate fixes.
- There are links into http://wiki.blender.org, these need to be corrected
- Fix titles, allowing only one ``h1`` per file (clearer menu structure)


Conventions:

- Choose a way to reference UI elements, ``:guilabel:`` is used all over, but may want to just use bold/italic.
- lots of lines over 120 length (low priority)
- check out the following syntax for titles


.. code-block:: rst

   h1 header
   *********

   h2 header
   =========

   h3 header
   ---------

   h4 header
   ~~~~~~~~~


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
(introducting) to the contents of the section.