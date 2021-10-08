.. highlight:: sh

**********
Contribute
**********

On this page French (``fr``) is used for examples. However, it can be replaced with other
`languages codes <https://www.gnu.org/software/gettext/manual/html_node/Usual-Language-Codes.html>`__.
So, be sure to change the ``/fr`` suffixes in this guide to the language you are translating!

To see which languages are currently available, you can browse the repository:
https://developer.blender.org/diffusion/BMT/browse/trunk/blender_docs/locale

.. note::

   First of all, it is assumed that you have the manual already building.
   If you have not done this already go back too
   the :ref:`Getting Started <about-getting-started>` section.


Installing
==========

Language Files
--------------

From the directory containing your checkout of the manual run::

   svn checkout https://svn.blender.org/svnroot/bf-manual-translations/trunk/blender_docs/locale/fr locale/fr

This will create a ``locale/fr`` subdirectory.

You should have a directory layout like this::

   blender_docs
      |- locale/
      |  |- fr/
      |  |  |- LC_MESSAGES/
      |- manual/

.. note::

   When running subversion from the command line (such as updating or committing),
   you will need to change directory to ``locale/fr`` first.

   Otherwise you will get a warning: ``'locale' is not under version control``


A PO Editor
-----------

To make edit the PO files you will need to install a PO editor.
We recommended that you use `Poedit <https://poedit.net/>`__
however, any PO editor will do.

.. note::

   For Linux users, you will have to check with
   your distribution's software center for a version of Poedit.
   This editor is only a recommendation. There are others, such as Kate and Kwrite, that
   could offer syntax highlighting and basic tools for text editing, e.g. letter case transposes.
   Other platforms can use some text editors supporting the syntax highlighting for PO files,
   or allowing you to create a custom one (such as Notepad++ on Windows).


Building with Translations
==========================

Now you can build the manual with the translation applied:

On Linux and macOS run::

   make -e BF_LANG=fr

On Windows run::

   set BF_LANG=fr
   make html

Now you will have a build of the manual with translations applied.


Editing Translation Files
=========================

Now you can edit the PO translation files, in the ``LC_MESSAGES`` folder you have two files:

- ``blender_manual.po`` -- This is the main translation file that you will be editing.
- ``sphinx.po`` -- This translation file is much smaller and contains translations for the website theme.

To edit these files open them up in your translation editor, i.e. Poedit.
Once in your editor you will see a list of texts, each of these items represent some part of the user manual.
You may need to adjust your editor to sort the list in a way that makes sense for example "by source".

You can now select an untranslated string and your editor will have an input box to add the translation.
The modified ``.po`` files can now submitted as a patch or committed back to SVN.

.. tip::

   Make sure that you `Building with Translations`_ to catch any syntax errors you may make while translating.
   These errors will be displayed as warnings while building the manual.


Commit Translation Files
========================

See :ref:`Submit Patches <contribute-patch_submit>`.


Maintenance
===========

.. _translations-fuzzy-strings:

Keeping Track of Fuzzy Strings
------------------------------

When the manual is updated, those translations which are outdated will be marked as fuzzy.
To keep track with that, you can use a tool we created for that task.

You can do this by running::

   make report_po_progress

This will only give a quick summary however, you can get more information by running::

   python tools_report/report_translation_progress.py locale/fr/

You should get a list of all the files with information about the number of empty and fuzzy strings.
For more options see::

   python tools_report/report_translation_progress.py --help


Updating PO Files
-----------------

As the original manual changes, the templates will need updating.
Note, doing this is not required,
as administrator usually update the files for all languages at once.
This allows all languages to be on the same version of the manual.
However, if you need to update the files yourself, it can be done as follows::

   make update_po

The updated templates can then be committed to svn.

.. seealso::

   A guide how to add a new language can be found in the :doc:`/about/contribute/translations/add_language`.
