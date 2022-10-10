
************
Object Modes
************

.. _fig-view3d-mode-select:

.. figure:: /images/editors_3dview_modes_menu.png
   :align: right

   The Mode select menu.

Modes allow editing different aspects of objects. While Object Mode allows
you to position/rotate/scale them, Edit Mode allows changing their geometry,
Pose Mode allows posing them, and so on.

You can change the current mode using the *Mode* selector in the 3D Viewport header.
Which modes are available depends on the object's type. The complete list
is shown below.

Apart from using the selector, you can also press :kbd:`Ctrl-Tab` to bring up
a pie menu around the cursor for faster access. (If the selected object is an
:doc:`Armature </animation/armatures/introduction>`, this shortcut will instead
switch between Object Mode and Pose Mode.)

Pressing :kbd:`Tab` will toggle Edit Mode for objects that support it.

.. container:: lead

   .. clear

Modes can affect many things in Blender:

- Each mode changes the header and Toolbar to show its own unique set of menus and tools.
  This also means it affects the available keyboard shortcuts.
- Modes can completely change the look of the viewport. For example, Weight Paint mode
  will shade the object to show its vertex weights, which are not normally visible.
- Modes can affect other editors. For example, the :doc:`UV Editor </editors/uv/introduction>`
  can only be used if the 3D Viewport is in Edit Mode. In the
  :doc:`Properties </editors/properties_editor>` editor, too, certain buttons and panels
  can only be used in certain modes.


Object Mode List
================

.. _tab-view3d-modes:

.. list-table:: Blender's Modes
   :header-rows: 1
   :class: valign
   :widths: 10 24 50

   * - Icon
     - Name
     - Details
   * - .. figure:: /images/editors_3dview_modes_icons-object-mode.png
     - :doc:`Object Mode </scene_layout/object/index>`
     - The default mode, available for all object types.
       Allows editing position, rotation and scale, duplicating objects, and so on.
   * - .. figure:: /images/editors_3dview_modes_icons-edit-mode.png
     - :doc:`Edit Mode </modeling/index>`
     - A mode for editing an object's shape
       (vertices/edges/faces for meshes, control points for curves/surfaces,
       points/strokes for Grease Pencil, etc.).
   * - .. figure:: /images/editors_3dview_modes_icons-sculpt-mode.png
     - :doc:`Sculpt Mode </sculpt_paint/sculpting/index>`
     - Provides an alternative toolset for editing an object's shape (only for meshes).
   * - .. figure:: /images/editors_3dview_modes_icons-vertex-paint.png
     - :doc:`Vertex Paint Mode </sculpt_paint/vertex_paint/index>`
     - A mesh-only mode that allows you to set your mesh's vertex colors (i.e. to "paint" them).
   * - .. figure:: /images/editors_3dview_modes_icons-weight-paint.png
     - :doc:`Weight Paint Mode </sculpt_paint/weight_paint/index>`
     - A mesh-only mode, dedicated to vertex group weighting.
   * - .. figure:: /images/editors_3dview_modes_icons-texture-paint.png
     - :doc:`Texture Paint Mode </sculpt_paint/texture_paint/index>`
     - A mesh-only mode that allows you to paint a texture directly on the model, in the 3D Viewport.
   * - .. figure:: /images/editors_3dview_modes_icons-particle-edit.png
     - :doc:`Particle Edit Mode </physics/particles/mode>`
     - A mesh-only mode dedicated to particle systems, useful for editable systems (hair).
   * - .. figure:: /images/editors_3dview_modes_icons-pose-mode.png
     - :doc:`Pose Mode </animation/armatures/posing/index>`
     - An armature-only mode, dedicated to posing.
   * - .. figure:: /images/editors_3dview_modes_icons-grease-pencil.png
     - :doc:`Draw Mode </grease_pencil/modes/draw/index>`
     - A Grease Pencil-only mode, dedicated to creating Grease Pencil strokes.

.. note::

   The cursor becomes a :doc:`brush </sculpt_paint/brush/introduction>`
   in :doc:`Paint and Sculpt Modes </sculpt_paint/index>`.

We will not go into any more detail on mode usages here,
because they are dealt with in their own sections.

.. hint::

   If you are reading this manual and some button or menu option is referenced
   that does not appear on your screen, it may be that you are not in the proper
   mode for that option to be valid.


.. _bpy.ops.object.transfer_mode:

Switching Objects
=================

.. reference::

   :Mode:      All Modes
   :Shortcut:  :kbd:`Alt-Q`

If you enter a mode such as Weight Paint for an object and then select another
object, Blender will typically switch back to Object Mode.
This means that, if you want to weight paint the other object too,
you have to enter the mode a second time.

There is a way of avoiding this, however. Once you enter a mode, the 
:doc:`Outliner </editors/outliner/introduction>` will show a dot next
to other objects that also support it. By clicking such a dot, you can
switch over to another object without leaving the mode.

Alternatively, you can hover over the other object in the 3D Viewport
and press :kbd:`Alt-Q`.

.. seealso::
   :ref:`Lock Object Modes <bpy.types.ToolSettings.lock_object_mode>` for
   preventing *accidental* mode changes.


.. _3dview-multi-object-mode:

Multi-Object Editing
====================

Edit Mode and Pose Mode let you work with multiple objects even more
easily than described above, as they can have multiple objects in the mode
at the same time.

There are two ways of accomplishing this:

- If you're not yet in the mode, you can simply select all the objects
  and enter it.
- If you're already in the mode, you can bring other objects into it
  by clicking :kbd:`Ctrl-LMB` on the dot in the Outliner.
  Removing objects from the mode works in the same way.

Some points of note:

- The Properties editor will only ever show the details (shape keys,
  UV maps...) of the active object, not of all the selected ones.
- Selecting any element from an object will make it the active one.
- There are limits to the edits you can make.
  For example, you can't create an edge that connects vertices from
  different objects.
