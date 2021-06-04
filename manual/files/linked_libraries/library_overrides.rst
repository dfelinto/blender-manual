
*****************
Library Overrides
*****************

Library Overrides is a system designed to replace and supersede
:doc:`Proxies </files/linked_libraries/library_proxies>`. Most types of
linked data-blocks can be overridden, and the properties of those overrides
can then be edited. When the library data changes, unmodified properties of
the overridden one will be updated accordingly.

.. note::

   The current proxy system will be kept alongside for a few releases.
   Automatic conversion from proxies to library overrides *is not planned*,
   there will be a manual operator to do that, but results on complex characters are not guaranteed.

Library overrides supports:

- Multiple independent overrides of a same linked data
  (e.g. having the same character multiple times in the same scene).
- Adding new modifiers and constraints, anywhere in the stack.
- Recursively chaining overrides (i.e. link and override overrides from another library file, etc.).

.. - Overriding many more types of data-blocks, and selectively edit some of their properties
   (e.g. materials, textures...).

.. note::

   There are known issues that have to be addressed. See Phabricator `main task of the project
   <https://developer.blender.org/T73318>`__, for more details.


Creating an Override
====================

.. admonition:: Reference
   :class: refbox

   :Editor:    3D Viewport and Outliner
   :Mode:      Object Mode
   :Menu:      :menuselection:`3D Viewport --> Header --> Object --> Relations --> Make Override Library`
               :menuselection:`Outliner --> Context Menu --> ID Data --> Make Library Override Hierarchy`
               :menuselection:`Outliner --> Context Menu --> ID Data --> Make Library Override`

There are two ways to create an override of a linked data-block.


Single Data-Block Override
--------------------------

You can override a single data-block from two places:

- The Outliner (it's in the context menu of IDs), in which case **all** local usages
  of that linked ID will be remapped to the new local override.
- The data-block menu in the UI (:kbd:`Shift-LMB` on the chain icon to the right),
  in which case only that specific usage will be remapped to the new local override.


.. _bpy.ops.object.make_override_library:

Make Library Override Operator/Make Library Override Hierarchy
--------------------------------------------------------------

This operator goes over linked objects or local empties instantiating a linked collection
(typically, a linked character).

The operator will go through the whole hierarchy
of collections and objects, and override all those needed to allow posing/animation of a character.

.. note:: Proper Collections Layout Matters

   For this operator to work properly, it is crucial that **all** the collections needed by
   the character are children of the root (linked and instantiated) one.
   Otherwise, some won't be automatically overridden, and manual work will be needed to fix the override.


.. _bpy.ops.object.convert_proxy_to_override:

Converting Proxies to Library Override
======================================

.. admonition:: Reference
   :class: refbox

   :Editor:    3D Viewport and Outliner
   :Mode:      Object Mode
   :Menu:      :menuselection:`3D Viewport --> Header --> Object --> Relations --> Convert Proxy to Library Override`
               :menuselection:`Outliner -->  ID Data --> Convert Proxy to Library Override`

Converts a :doc:`Proxy </files/linked_libraries/library_proxies>` to a local override.
This operator is used to help convert older blend-files to the new override system.


Syncing Overrides
=================

The relationships between linked data-blocks can be changed resulting in outdated overrides.
When this happens overrides need to be resynced to match the new structure.
Overrides are automatically resynced when opening blend-files, however,
overrides can be resynced manually using `Resync Library Override Hierarchy`_.

.. tip::

   Auto resyncing can be disabled in the :doc:`Experimental Preferences </editors/preferences/experimental>`.


Editing an Override
===================

Essentially, an override is edited the same way as a regular local data-block.
You can use operators on them, edit their properties from various editors, etc.
There are some limitations however, most notably Edit Mode is not allowed for overrides.
In most cases, as soon as you edit a property, you can see that it's overridden by its teal blue
outline/background.

You can also animate overrides, animated properties just replace/supersede overrides then.
Note that you cannot override-edit an existing animation, you'll have to create a new action.
You can manually define or remove an override from the context menu of the relevant property.


.. _bpy.ops.ui.override_type_set_button:

Define Overrides
----------------

.. admonition:: Reference
   :class: refbox

   :Editor:    Any
   :Mode:      Object Mode
   :Property:  :menuselection:`Context Menu --> Define Overrides`
               :menuselection:`Context Menu --> Define Override`

Mark a property to be overridden in the local blend-file. For array properties
all elements will be overridden.


Define Single Override
----------------------

.. admonition:: Reference
   :class: refbox

   :Editor:    Any
   :Mode:      Object Mode
   :Property:  :menuselection:`Context Menu --> Define Single Override`

Mark a property to be overridden in the local blend-file. For array properties only
the selected element will be overridden.


.. _bpy.ops.ui.remove_override_button:

Remove Overrides
----------------

.. admonition:: Reference
   :class: refbox

   :Editor:    Any
   :Mode:      Object Mode
   :Property:  :menuselection:`Context Menu --> Remove Overrides`
               :menuselection:`Context Menu --> Remove Override`

Remove the property from the overrides. The value of the linked in data-block will be used.
For array properties all elements will be removed from the override.


Remove Single Override
----------------------

.. admonition:: Reference
   :class: refbox

   :Editor:    Any
   :Mode:      Object Mode
   :Property:  :menuselection:`Context Menu --> Remove Single Override`

Remove the property from the overrides. The value of the linked in data-block will be used.
For array properties only the selected elements will be removed from the override.


Reset Library Override
======================

.. admonition:: Reference
   :class: refbox

   :Editor:    Outliner
   :Mode:      Object Mode
   :Outliner:  :menuselection:`Context Menu --> ID Data --> Reset Library Override`
               :menuselection:`Context Menu --> ID Data --> Reset Library Override Hierarchy`

Reset the override to its original values. *Reset Library Override Hierarchy* will also reset
the overrides of its child data-blocks.


Resync Library Override Hierarchy
=================================

.. admonition:: Reference
   :class: refbox

   :Editor:    Outliner
   :Mode:      Object Mode
   :Outliner:  :menuselection:`Context Menu --> ID Data --> Resync Library Override Hierarchy`

The structure of the linked data (the relationships between linked data-blocks) can be changed.
Overrides need to be resynced to match the new structure. This operator will resync the override
to the new structure in the library.

.. warning::

   While resyncing a library override it is possible that edited overrides
   get deleted if they are changed in the original library.
   If this is the case, a warning message will be displayed stating how many overrides were deleted,
   if the deletion is undesirable the resync can be undone before saving the blend-file.


Resync Library Override Hierarchy Enforce
=========================================

.. admonition:: Reference
   :class: refbox

   :Editor:    Outliner
   :Mode:      Object Mode
   :Outliner:  :menuselection:`Context Menu --> ID Data --> Resync Library Override Hierarchy Enforce`

In some cases, especially with older blend-files that were saved with 'broken' (non-hierarchy-matching) overrides,
a regular resync itself cannot rebuild properly the override as expected (e.g. some objects might go missing).
To solve this issue, this operator rebuilds the local override from its linked reference,
as well as its hierarchy of dependencies, enforcing that hierarchy to match the linked data
(i.e. ignoring existing overrides on data-blocks properties).
This is similar to a regular resync but is a more forceful resync,
at the cost of a potential loss of some overrides on ID pointers properties.


Delete Library Override Hierarchy
=================================

.. admonition:: Reference
   :class: refbox

   :Editor:    Outliner
   :Mode:      Object Mode
   :Outliner:  :menuselection:`Context Menu --> ID Data --> Delete Library Override Hierarchy`

Remove the library override from the selected data-block and all its children and replace them with
the original linked data-block. This will revert the *Make Library Override*.
