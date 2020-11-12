
********************
Edit Operator Source
********************

This add-on allows searching for operator names (``bl_idname``) and opens source files containing them.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Development then Edit Operator Source to enable the script.


Description
===========

In the :menuselection:`Text Editor --> Sidebar` on the left find the Edit Operator panel and
press the *Edit Operator* button. A searchable menu will show up. Scroll down until the operator is found.
Enter the keywords in the search field to narrow down the available options.
The source file containing the operator will open pointing to it's line.

To access the previously opened text files, select them from the header data-block menu.

.. note::

   Similar to the *Operator Cheat Sheet*, the script will produce a small memory leak (~0.03mb)
   when enabled by accessing the Operator attributes from Python.
   It is a conscious trade-off made by Blender developers, as the needed setting/call
   in the source C code for this purpose, would increase the size of every Python instance by 4 bytes.
   In case of complex scenes, the increased memory footprint would be nontrivial compared to
   the few usage cases where it is currently needed.


.. admonition:: Reference
   :class: refbox

   :Category:  Development
   :Description: Opens source file of chosen operator or call locations, if source not available.
   :Location: :menuselection:`Text Editor --> Sidebar --> Edit Operator`
   :File: development_edit_operator.py
   :Author: scorpion81
   :Maintainer: scorpion81
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
