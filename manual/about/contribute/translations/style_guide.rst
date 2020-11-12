
***********
Style Guide
***********

This page covers conventions concerning the translations.

.. note::

   - We expect our readers to use the English version of Blender, not a translated one.
   - The translations are licensed under the same :doc:`/copyright` as the original.


Should I Translate\.\.\. ?
==========================

Maybe
-----

Hyperlinks
   Can be translated, but only as an addition, not as a replacement.
   See also `Adding Text`_.

Technical Terms
   Only translate these, when the localized expression is common!
   See also `Technical Terms`_.

Text you are not sure you understood
   Simply mark the text as fuzzy and/or add a comment.
   The next translator might understand it.


Never
-----

Images
   You probably will not find the original scene if it is a screenshot of a file
   and it is too much load on the server (and too much work for you).

Menu and button names
   We expect our readers to use the English UI.

Text you do not understand
   Do not translate it! It will do more harm than good!


Technical Terms
===============

In general, the technical terms used in computer graphics are quite new or even downright
neologisms invented for the needs,
so they do not always have a translation in your language. Moreover,
a large part of Blender users use its English interface.

As a result, unless a term has an evident translation,
you should preferably use the English one, *putting it in italic*.
You can then find a translation for it, which you will use from times to times (e.g. to avoid repetitions...).
This is also valid in the other way: even when a term has a straightforward translation,
do not hesitate to use its English version from times to times, to get the reader used with it...

If a term is definitively not translatable, simply use the English one,
but make sure its glossary entry is translated.

In the glossary, the English term is written first (to maintain alphabetic order)
with the translated entry following in parenthesis, when appropriate.


Adding Text
===========

Generally, **you should always translate exactly what is in the text**,
and avoid providing updates or extra information.

But sometimes that is necessary, for example when talking about the manual itself:
To a foreign reader it is not clear, that they can contribute English text only,
whereas this is obvious to an English reader.

In these (rare) cases you can and should provide extra information.


Keeping Pages Up To Date
========================

When the manual is updated, those translations which are outdated will be marked as fuzzy.
To keep track with that, you can use a tool we created for that task,
see :ref:`How to install it <translations-fuzzy-strings>`.
