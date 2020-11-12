.. highlight:: sh

*****************
Building on macOS
*****************

Converting the RST-files into pretty HTML pages.

Open a terminal to the folder ``~/blender_docs`` and simply run::

   make

This is the command you will always use when building the docs.
The building process may take several minutes the first time (or after any major changes),
but the next time you build it should only take a few seconds.


Viewing the Local Manual
========================

Once the docs have been built, all the HTML files can be found inside ``~/blender_docs/build/html``.
Try opening ``build/html/index.html`` in your web browser and read the manual::

   open build/html/index.html

Now that you are able to build the manual, the next paragraph is about an optional quick build.


Building a Single Chapter
=========================

If you are working on a specific chapter of the manual, you can build it quickly using::

   make <chapter name>

For example, to build only the documentation for the modifiers, use ``make modifiers``.
You can then view this quick build by opening ``build/html/contents_quicky.html``.

This will build very quickly, but it will mean your next complete build of all the chapters will be slow.


------------------------

Continue with the next step: :doc:`Editing </about/contribute/editing>`.
