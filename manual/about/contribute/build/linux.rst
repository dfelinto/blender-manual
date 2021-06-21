.. highlight:: sh

*****************
Building on Linux
*****************

Converting the RST-files into pretty HTML pages is simple.

Open a terminal to the folder ``~/blender_docs`` and simply run::

   make

This is the command you should always use when building the docs,
however, other commands are avaible by typing ``make help``.
This command will convert the RST-files into HTML pages
and automaticlly open your default web browser to view the result.
The command will continue to run and watch for changes made to the RST-files
and refresh the HTML pages as necessary.

.. tip::

   The converted pages can also be viewed manually by browsing the build directory: ``~/blender_docs/build/html``.
   For example to open the home page, open :file:`build/html/index.html` to read the manual.


The building process may take several minutes the first time (or after any major changes),
but for subsequent changes it should only take a few seconds.

Now that you are able to build the manual, the next paragraph is about an optional quick build.


Building a Single Chapter
=========================

If you are working on a specific chapter of the manual, you can build it quickly using::

   make <chapter name>

For example, to build only the documentation for the modifiers, use ``make modeling``.
You can then view this quick build by opening :file:`build/html/contents_quicky.html`.

This will build very quickly, but it will mean your next complete build of all the chapters will be slow.


------------------------

Continue with the next step: :doc:`Editing </about/contribute/editing>`.
