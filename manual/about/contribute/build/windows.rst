.. highlight:: sh

*******************
Building on Windows
*******************

Converting the RST-files into pretty HTML pages is simple.

There are two ways to run the build process.

.. rubric:: File browser

Open :file:`make.bat` in the ``C:\blender_docs`` folder.

.. rubric:: Command prompt

#. Or open the command prompt and change to the repository with ``cd C:\blender_docs``.
#. Build using the following command

::

      make

This is the command you should always use when building the docs,
however, other commands are avaible by typing ``make help``.
This command will convert the RST-files into HTML pages
and automaticlly open your default web browser to view the result.
The command will continue to run and watch for changes made to the RST-files
and refresh the HTML pages as necessary.

.. tip::

   The converted pages can also be viewed manual by browsing the build directory: ``~/blender_docs/build/html``.
   For example to open the home page, open :file:`build/html/index.html` to read the manual.


The building process may take several minutes the first time (or after any major changes),
but for subsequent changes it should only take a few seconds.


------------------------

Continue with the next step: :doc:`Editing </about/contribute/editing>`.
