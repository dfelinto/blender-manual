
*****************
Library Overrides
*****************

Library Overrides is the new system designed to replace and
supersede :doc:`Proxies </files/linked_libraries/library_proxies>`.
Most types of linked data-blocks can be overridden, and the properties of those overrides
can then be edited. When the library data changes, unmodified properties of the overridden one
will be updated accordingly.

.. note::

   **It is considered as experimental**, and the current proxy system will be kept alongside for a few releases.
   Automatic conversion from proxies to library overrides *is not planned*,
   there will be a manual operator to do that, but results on complex characters are not guaranteed.

Compared to proxies, library overrides support:

- Multiple independent overrides of a same linked data (e.g. a whole character).
- Adding new modifiers and constraints, anywhere in the stack.
- Recursively chaining overrides (i.e. link and override overrides from another library file, etc.).

.. - Overriding many more types of data-blocks, and selectively edit some of their properties
   (e.g. materials, textures...).

.. note::

   There are still many known TODOs/issues that have to be addressed.
   Please check the `release notes <https://wiki.blender.org/wiki/Reference/Release_Notes/2.81/Library_Overrides>`__
   and Phabricator `main task of the project <https://developer.blender.org/T53500>`__, for more details.


Creating an Override
====================

There are two ways to create an override of a linked data-block.


Single Data-Block Override
--------------------------

You can override a single data-block from two places:

- The Outliner (it's in the context menu of IDs), in which case **all** local usages
  of that linked ID will be remapped to the new local override.
- The data-block menu in the UI (:kbd:`Shift-LMB` on the chain icon to the right),
  in which case only that specific usage will be remapped to the new local override.


Make Library Override Operator
------------------------------

This one operates in the 3D Viewport, over linked objects or local empties instantiating a linked collection
(typically, a linked character). It is very similar to the *Make Proxy* operator,
and is found in the same submenu :menuselection:`Object --> Relations --> Make Library Overrides...`.

Unlike the method described above, it will go through the whole hierarchy of collections and objects,
and override all those needed to allow posing/animation of a character.

.. note:: Proper Collections Layout Matters

   For this operator to work properly, it is crucial that **all** the collections needed by
   the character are children of the root (linked and instantiated) one.
   Otherwise, some won't be automatically overridden, and manual work will be needed to fix the override.


.. _bpy.ops.object.convert_proxy_to_override:

Converting Proxies to Library Override
======================================

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Relations --> Convert Proxy to Library Override`

Converts older a :doc:`Proxy </files/linked_libraries/library_proxies>` to a local override.
This operator is used to help convert older blend-files to the new override system.
In the future, this conversion will likely happen automatically.


Editing an Override
===================

Essentially, an override is edited the same way as a regular local data-block.
You can use operators on them, edit their properties from various editors, etc.

There are some limitations however, most notably Edit Mode is not allowed currently for overrides.

In most cases, as soon as you edit a property, you can see that it's overridden by its teal blue
outline/background (like the yellow/green/purple colors of animated/driven ones).

You can also animate overrides, animated properties just replace/supersede overrides then.
Note that you cannot override-edit an existing animation, you'll have to create a new action.

You can manually define or remove an override from the context menu of the relevant property.
