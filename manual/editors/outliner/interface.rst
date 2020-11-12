
*********
Interface
*********

Object Mode
===========

The far left of the Outliner contains a region to toggle the current :doc:`Object Mode </editors/3dview/modes>`.
When an object is in a mode other than Object Mode, the mode icon will be displayed in this region.
Any other objects that are valid to be added or swapped into the current mode display a dot.
Clicking the dot icon will swap that object with the current active object.
For modes that support :ref:`3dview-multi-object-mode`,
:kbd:`Ctrl-LMB` on the dot icon will add that object to the current mode.
Clicking the mode icon next to the active object removes it or all other objects
from the current mode depending if multiple object are in the same mode.


.. _editors-outliner-interface-restriction_columns:

Restriction Columns
===================

The following toggles, in the right side of the *Outliner* editor,
are available for collections, objects, bones, modifiers and constraints.

By default only the temporary viewport visibility is enabled.
The other options can be enabled in the *Restriction Toggles* option in the Outliner `filter`_.

- Holding :kbd:`Shift` sets or unsets the value to all its child collections or objects.
- Holding :kbd:`Ctrl` isolates the object or collection, so they are the only ones with its value set.

.. _bpy.types.LayerCollection.exclude:

Enable Collection (checkbox, collection only)
   Exclude the collection from the view layer. This option is shown in front of
   the collection icon, it is not part of the restrictions column.

Visibility (eye icon)
   Toggles the visibility of the object or collection in the 3D Viewport.
   This is a file-local setting, and does not get imported when this data-block
   is linked into another blend-file. Objects hidden this way are still part of
   the :doc:`View Layer </scene_layout/view_layers/index>` and evaluated,
   so they still affect playback performance.

.. note::

   The following options are hidden by default and need to be enabled in
   the Outliner Filter before they can be used.

.. _bpy.types.Collection.hide_select:

Selectability (mouse cursor icon)
   This is useful for if you have placed something in the scene
   and do not want to accidentally select it when working on something else.

.. _bpy.types.LayerCollection.hide_viewport:

Global Viewport Visibility (screen icon)
   This will still render the object/collection, but it will be ignored by all the viewports.
   Often used for collections with high-poly objects that need to be instanced in other files.
   Objects hidden this way are no longer part of the :doc:`View Layer </scene_layout/view_layers/index>`,
   are not evaluated, and such do not negatively affect playback performance.

Rendering (camera icon)
   This will still keep the object visible in the scene, but it will be ignored by the renderer.
   Usually used by support objects that help modeling and animation yet do not belong in the final images.

.. _bpy.types.LayerCollection.holdout:

Holdout (collection only)
   Mask out objects in collection from view layer.

.. _bpy.types.LayerCollection.indirect_only:

Indirect Only (collection only)
   Objects in these collections only contribute to indirect light -- *Cycles only*.


Header
======

Display Mode
------------

The editors header has a select menu that let you filter what the Outliner should show.
It helps to narrow the list of objects so that you can find things quickly and easily.

Scenes
   Shows *everything* the *Outliner* can display (in all scenes, all view layers, etc.).
View Layer
   Shows all the collections and objects in the current view layer.
Video Sequencer
   Lists data, images and videos, that are used by the :doc:`Video Sequencer </video_editing/index>`.
Blender File
   Lists all data in the current blend-file.
Data API
   Lists every :doc:`data-block </files/data_blocks>` along with any properties that they might have.
Orphan Data
   Lists :doc:`data-blocks </files/data_blocks>`
   which are unused and/or will be lost when the file is reloaded.
   It includes data-blocks which have only a fake user. You can add/remove Fake User
   by clicking on cross/tick icon in the right side of the Outliner editor.


Searching
---------

You can search the view for data-blocks,
by using Search field in the header of the *Outliner*,
The `Filter`_ menu lets you toggle the following options:

- Case Sensitive Matches Only
- Complete Matches Only

.. _editors-outliner-interface-filter:

Filter
------

Restriction Toggles
   Set which `Restriction Columns`_ should be visible.
Sort Alphabetically
   Sort the entries alphabetically.

Sync Selection
   Sync Outliner selection to and from the :doc:`3D Viewport </editors/3dview/index>` and
   :doc:`Video Sequencer </video_editing/index>` editors. Disable to manage collections,
   object relations, and scene data without changing the selection state.
   Selection syncing is only available in Scenes, View Layer, and Video Sequencer display modes.

Collections
   List the objects and collections under
   the :doc:`collection hierarchy </scene_layout/collections/index>` of the scene.
   Objects may appear in more than one collection.
Objects
   List of all the objects, respecting the other filter options.
   Disabled only if you need an overview of the collections without the objects.
Object State
   All
      The default option, no restrictions.
   Visible
      List only the objects visible in the viewports.
      The global and temporary visibility settings are taken into consideration.
   Invisible
      List only the objects not visible in the viewports.
   Selected
      Lists the object(s) that are currently selected in the 3D Viewport.
      See :doc:`selecting in the 3D Viewport </scene_layout/object/selecting>` for more information.
   Active
      Lists only the active (often last selected) object.
Object Contents
   List materials, modifiers, mesh data, ...
Object Children
   List the object children. If the *Collections* option is enabled,
   you will see the object children even if the children are not in the collection.
   However the Outliner shows them as a dashed line.
Data-Block
   Allows you to filter out certain data-blocks currently present in the scene.


.. _bpy.ops.outliner.orphans_purge:

Miscellaneous
-------------

Some options in the header will only show if compatible with the active `Display Mode`_.

New Collection (View Layer)
   Add a new collection inside selected collection.
Filter ID Type (Orphan Data, Blender File)
   Restrict the type of the data-blocks shown in the Outliner.
Keying Sets (Data API)
   Add/Remove selected data to the active :doc:`Keying Set </animation/keyframes/keying_sets>`.
Drivers
   Add/Remove :doc:`Drivers </animation/drivers/index>` to the selected item.
Purge (Orphan Data)
   Remove all unused data-blocks from the file (cannot be undone).
