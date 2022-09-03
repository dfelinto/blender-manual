
*********
Interface
*********

Header
======

.. _bpy.types.SpaceOutliner.display_mode:

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

.. _bpy.types.SpaceOutliner.lib_override_view_mode:

Library Overrides
   Display library override data in the current blend-file. Separated further into two view modes:

   Properties:
      Display data-blocks with overridden properties. The overridden properties are listed together with widgets to
      modify the value of the properties.
   Hierarchies:
      Visualize the hierarchical dependencies between data-blocks with library overrides. For example, to create a
      library override of a mesh used by an object inside of a linked collection, Blender automatically creates
      (disabled) library overrides for the object and the collection, resulting in a collection > object > mesh
      library override hierarchy.

      .. _bpy.ops.ed.lib_id_override_editable_toggle:

      This library override view mode has a column on the right side
      of the editor to toggle if the library is editable or not.

Orphan Data
   Lists :doc:`data-blocks </files/data_blocks>`
   which are unused and/or will be lost when the file is reloaded.
   It includes data-blocks which have only a fake user. You can add/remove Fake User
   by clicking on cross/tick icon in the right side of the Outliner editor.


.. _bpy.types.SpaceOutliner.filter_text:

Display Filter
--------------

You can search the view for data-blocks,
by using Search field in the header of the *Outliner*,


.. _editors-outliner-interface-filter:

Filter
------

.. _bpy.types.SpaceOutliner.show_restrict_column:

Restriction Toggles
   Set which `Restriction Columns`_ should be visible.

.. _bpy.types.SpaceOutliner.use_sort_alpha:

Sort Alphabetically
   Sort the entries alphabetically.

.. _bpy.types.SpaceOutliner.use_sync_select:

Sync Selection
   Sync Outliner selection to and from the :doc:`3D Viewport </editors/3dview/index>` and
   :doc:`Video Sequencer </video_editing/index>` editors. Disable to manage collections,
   object relations, and scene data without changing the selection state.
   Selection syncing is only available in Scenes, View Layer, and Video Sequencer display modes.

.. _bpy.types.SpaceOutliner.show_mode_column:

Show Mode Column
   Show the object mode toggling column in View Layer and Scenes display modes.


.. rubric:: Search

.. _bpy.types.SpaceOutliner.use_filter_complete:

Exact Match
   The results of :ref:`bpy.types.SpaceOutliner.filter_text` must match the full text and not just a part of it.

.. _bpy.types.SpaceOutliner.use_filter_case_sensitive:

Case Sensitive
   The results of :ref:`bpy.types.SpaceOutliner.filter_text` are case sensitive.


.. rubric:: Filter

Some options will only show if compatible with the active `Display Mode`_.

.. _bpy.types.SpaceOutliner.use_filter_view_layers:

All View Layers
   Toggle between only the active or all the :doc:`view layers </scene_layout/view_layers/index>` of the scene.
   Combined with disabling the *Objects* filter it gives a compact overview of all the collections in relation
   to the view layers.

.. _bpy.types.SpaceOutliner.use_filter_collection:

Collections
   List the objects and collections under
   the :doc:`collection hierarchy </scene_layout/collections/index>` of the scene.
   Objects may appear in more than one collection.

.. _bpy.types.SpaceOutliner.use_filter_object:

Objects
   List of all the objects, respecting the other filter options.
   Disabled only if you need an overview of the collections without the objects.

.. _bpy.types.SpaceOutliner.filter_invert:
.. _bpy.types.SpaceOutliner.filter_state:

Object State
   List the objects based on their state or restrictions.
   The results can be inverted using the *Invert* button.

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
   Selectable
      List all objects whose :ref:`Selectability <bpy.types.Collection.hide_select>` option is enabled.

.. _bpy.types.SpaceOutliner.use_filter_object_content:

Object Contents
   List materials, modifiers, mesh data, ...

.. _bpy.types.SpaceOutliner.use_filter_children:

Object Children
   List the object children. If the *Collections* option is enabled,
   you will see the object children even if the children are not in the collection.
   Yet the Outliner shows them as a dashed line.

.. _bpy.types.SpaceOutliner.use_filter_object_mesh:
.. _bpy.types.SpaceOutliner.use_filter_object_light:
.. _bpy.types.SpaceOutliner.use_filter_object_camera:
.. _bpy.types.SpaceOutliner.use_filter_object_empty:
.. _bpy.types.SpaceOutliner.use_filter_object_others:

Data-Block
   Allows you to filter out certain data-blocks currently present in the scene.

.. _bpy.types.SpaceOutliner.use_filter_lib_override_system:

System Overrides
   Shows the data-block properties that are defined/controlled automatically (e.g. to make users of an overridden
   data-block point to the override data, not the original linked data). Only available in the *Library Overrides*
   `Display Mode`_.


.. _bpy.ops.outliner.orphans_purge:

Miscellaneous
-------------

Some options in the header will only show if compatible with the active `Display Mode`_.

New Collection (View Layer)
   Add a new collection inside selected collection.
Filter by Type (Orphan Data, Blender File)
   Restrict the type of the data-blocks shown in the Outliner.
Keying Sets (Data API)
   Add/Remove selected data to the active :doc:`Keying Set </animation/keyframes/keying_sets>`.
Drivers
   Add/Remove :doc:`Drivers </animation/drivers/index>` to the selected item.
Purge (Orphan Data)
   Recursively remove all unused data-blocks from the file (cannot be undone).


Main Region
===========

Object Mode
-----------

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
-------------------

The following toggles, in the right side of the *Outliner* editor,
are available for collections, objects, bones, modifiers and constraints.

By default only the temporary viewport visibility is enabled.
The other options can be enabled in the *Restriction Toggles* option in the Outliner `filter`_.

- Holding :kbd:`Shift` sets or unsets the value to all its child collections or objects.
- Holding :kbd:`Ctrl` isolates the object or collection, so they are the only ones with its value set.

.. _bpy.types.LayerCollection.exclude:

Enable Collection (checkbox, collection only)
   Exclude the collection from the view layer.

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
   Toggles the ability to select the objects from the 3D Viewport.
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
