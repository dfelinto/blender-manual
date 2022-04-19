
*****************
Library Overrides
*****************

Library Overrides is a system designed to replace and supersede
Proxies. Most types of linked data-blocks can be overridden, and the properties
of those overrides can then be edited. When the library data changes,
unmodified properties of the overridden one will be updated accordingly.

.. note::

   The old proxy system has been deprecated in Blender 3.0, and fully removed in Blender 3.2.
   Automatic conversion from proxies to library overrides happens when loading a blend-file,
   but results on complex characters are not guaranteed and may need manual fixes.

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


Override Hierarchies
====================

Hierarchy is a very important concept to understand when working with library overrides.
In Blender, a real-life asset (a character, a prop, a set, etc.) is almost never made of a
single data-block, but is rather a group of data-blocks with dependency relationships to each-other.
E.g. a character sill typically have an armature object, several geometry objects,
rig-controllers objects, the object data for all of those objects, materials, textures, etc. 

Those relationships can be represented as a tree, with a root data-block 'linking-in' all its
dependencies, recursively. With library overrides, typically, the root of the hierarchy is also
the data-block that is directly linked when importing the asset (usually a collection).

This concept of hierarchy can also be seen as some sort of super meta-data-block. It is critical
when there are several overrides of the same linked data, since it allows to clearly identify a given
data-block to one override, leaving no ambiguity to processes that affect the whole hierarchy
(e.g. resyncing overrides with their linked data). It also allows to share relationships between
data-blocks of different hierarchies, like a parenting relationships between two different overrides
of a same character. 


Non-Editable Overrides
=======================

For technical reasons (how relationships between data-blocks are stored), Blender needs to create
overrides of a lot of data-blocks, even when only one or two of them actually needs to be edited
by the user. To reduce the amount of information and risk of potential unwanted editing, most of
those data-blocks are now marked as non-editable by default. This can be changed once the
override has been created.


Creating an Override
====================

.. reference::

   :Editor:    3D Viewport and Outliner
   :Mode:      Object Mode
   :Menu:      :menuselection:`3D Viewport --> Header --> Object --> Relations --> Make Override Library`
               :menuselection:`Outliner --> Context Menu --> ID Data --> Make Library Override Hierarchy`
               :menuselection:`Outliner --> Context Menu --> ID Data --> Make Library Override Single`

There are two ways to create an override of a linked data-block.


.. _bpy.ops.object.make_override_library:

Make Library Override Operator/Make Library Override Hierarchy
--------------------------------------------------------------

This is the main, recommended way to create overrides.
This operator goes over linked objects or local empties instantiating a linked collection
(typically, a linked character).

The operator will go through the whole hierarchy
of collections and objects, and override all those needed to allow posing/animation of a character.

.. note:: Proper Collections Layout Matters

   For this operator to work properly, it is crucial that **all** the collections needed by
   the character are children of the root (linked and instantiated) one, such that there is a clear hierarchy.
   Otherwise, some won't be automatically overridden, and manual work will be needed to fix the override.


Single Data-Block Override
--------------------------

You can override a single data-block from two places:

- The Outliner (it's in the context menu of IDs), in which case **all** local usages
  of that linked ID will be remapped to the new local override.
- The data-block menu in the UI (:kbd:`Shift-LMB` on the chain icon to the right),
  in which case only that specific usage will be remapped to the new local override.

.. note:: Single Overrides Should Be Used With Caution

   While it is always possible to do manual partial override of a hierarchy, this is relatively
   time consuming and error-prone, and can easily live the override hierarchy in an inconsistent
   state (regarding relationships between its data-blocks). This can back-fire later, when a resync
   with the linked data becomes needed e.g.


Resyncing Overrides
===================

The relationships between linked data-blocks can change, resulting in outdated overrides.
When this happens, overrides need to be resynced to match the new structure.
Overrides are automatically resynced if needed on blend-files opening. However,
they can also be resynced manually using `Resync Library Override Hierarchy`_.

.. tip::

   Blender is also able to resync library overrides from external libraries, that are then linked into a
   working file. However, this is a costly process that needs to be fully redone every time the working
   file is loaded, since Blender cannot edit/modify the external library directly.

   So users linking overrides (or creating recursive overrides) should ensure that their library files are
   regularly updated, to avoid this overhead on file load (typically, opening and saving those library files
   should be enough to update them).

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
If an override is not editable, you have to make it editable first.


Make Library Override Editable
------------------------------

.. reference::

   :Editor:    Outliner
   :Mode:      Object Mode
   :Outliner:  :menuselection:`Context Menu --> ID Data --> Make Library Override Editable`

Make the selected library override data-block editable byt the user.


.. _bpy.ops.ui.override_type_set_button:

Define Overrides
----------------

.. reference::

   :Editor:    Any
   :Mode:      Object Mode
   :Property:  :menuselection:`Context Menu --> Define Overrides`
               :menuselection:`Context Menu --> Define Override`

Mark a property to be overridden in the local blend-file. For array properties
all elements will be overridden.


Define Single Override
----------------------

.. reference::

   :Editor:    Any
   :Mode:      Object Mode
   :Property:  :menuselection:`Context Menu --> Define Single Override`

Mark a property to be overridden in the local blend-file. For array properties only
the selected element will be overridden.


.. _bpy.ops.ui.remove_override_button:

Remove Overrides
----------------

.. reference::

   :Editor:    Any
   :Mode:      Object Mode
   :Property:  :menuselection:`Context Menu --> Remove Overrides`
               :menuselection:`Context Menu --> Remove Override`

Remove the property from the overrides. The value of the linked in data-block will be used.
For array properties all elements will be removed from the override.


Remove Single Override
----------------------

.. reference::

   :Editor:    Any
   :Mode:      Object Mode
   :Property:  :menuselection:`Context Menu --> Remove Single Override`

Remove the property from the overrides. The value of the linked in data-block will be used.
For array properties only the selected elements will be removed from the override.


Reset Library Override
======================

.. reference::

   :Editor:    Outliner
   :Mode:      Object Mode
   :Outliner:  :menuselection:`Context Menu --> ID Data --> Reset Library Override Single`
               :menuselection:`Context Menu --> ID Data --> Reset Library Override Hierarchy`

Reset the override to its original values. *Reset Library Override Hierarchy* will also reset
the overrides of its child data-blocks. Unlike the Clear operations below, this never removes
the override data-blocks themselves.


Resync Library Override Hierarchy
=================================

.. reference::

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

.. reference::

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


Clear Library Override Single
=============================

.. reference::

   :Editor:    Outliner
   :Mode:      Object Mode
   :Outliner:  :menuselection:`Context Menu --> ID Data --> Clear Library Override Single`

Reset the override to its original values, and if possible without breaking the existing hierarchy,
replace it by its linked data. Otherwise, keep the override but mark it as non-editable.


Clear Library Override Hierarchy
================================

.. reference::

   :Editor:    Outliner
   :Mode:      Object Mode
   :Outliner:  :menuselection:`Context Menu --> ID Data --> Clear Library Override Hierarchy`

Remove the library override from the selected data-block and all its children and replace them with
the original linked data-block. This will revert the *Make Library Override*.
