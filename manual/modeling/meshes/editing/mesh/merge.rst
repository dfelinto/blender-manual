.. _bpy.ops.mesh.merge:
.. _vertex-merging:

*****
Merge
*****

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Merge`,
               :menuselection:`Context Menu --> Merge`
   :Shortcut:  :kbd:`M`

This tool allows you to merge all selected vertices to a unique one, dissolving all others.
You can choose the location of the remaining vertex in the menu this tool pops up before executing:

At Center
   It will place the remaining vertex at the center of the selection.
   Available in all select modes.
At Cursor
   It will place the remaining vertex at the 3D Cursor.
   Available in all select modes.
Collapse
   Every island of selected vertices (connected by selected edges) will merge on its own median center,
   leaving one vertex per island.
At First
   It will place the remaining vertex at the location of the first one selected.
   Only available in *Vertex* select mode.
At Last
   It will place the remaining vertex at the location of the last one selected (the active one).
   Only available in *Vertex* select mode.

Merging vertices of course also deletes some edges and faces. But Blender will do everything
it can to preserve edges and faces only partly involved in the reunion.

.. note::

   *At First* and *At Last* depend on that the selection order is saved:
   the order is lost, for instance, after changing selection mode.

UVs
   If *UVs* is ticked in the :ref:`bpy.ops.screen.redo_last` panel,
   the UV mapping coordinates, if existing, will be corrected to avoid image distortion.


By Distance
===========

Todo.
