
************
Object Modes
************

.. _fig-view3d-mode-select:

.. figure:: /images/editors_3dview_modes_menu.png
   :align: right

   The Mode select menu.

*Modes* are an object-oriented feature, which means that the available modes vary
depending on the selected active object's type -- most of them only enable
the default *Object Mode* (like cameras, lights, etc.).

Each mode is designed to edit an aspect of the selected object.
See Tab. :ref:`tab-view3d-modes` below for details.

You set the current mode in the *Mode* selector of 3D Viewport header
(see Fig. :ref:`fig-view3d-mode-select`).

.. container:: lead

   .. clear

Modes can affect many things in Blender:

- They can modify the panels and/or controls available in some Properties tabs.
- They can modify the behavior of the whole editor, like e.g. the UV Editor and 3D Viewport.
- They can modify the available header tools (menus and/or menu entries, as well as other controls...).
  For example, in the 3D Viewport, the *Object* menu in Object Mode changes to a *Mesh* menu in Edit Mode
  (with an active mesh object!), and a *Paint* menu in Vertex Paint Mode...
- They can modify the available shortcuts.


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
     - The default mode, available for all object types,
       as it is dedicated to *Object* data-block editing (e.g. position, rotation, size).
   * - .. figure:: /images/editors_3dview_modes_icons-edit-mode.png
     - :doc:`Edit Mode </modeling/index>`
     - A mode available for all renderable object types,
       as it is dedicated to their "shape" *Object Data* data-block editing
       (e.g. vertices/edges/faces for meshes, control points for curves/surfaces,
       strokes/points for Grease Pencil, etc.).
   * - .. figure:: /images/editors_3dview_modes_icons-sculpt-mode.png
     - :doc:`Sculpt Mode </sculpt_paint/sculpting/index>`
     - A mesh-only mode, that enables Blender's mesh 3D-sculpting tool.
   * - .. figure:: /images/editors_3dview_modes_icons-vertex-paint.png
     - :doc:`Vertex Paint Mode </sculpt_paint/vertex_paint/index>`
     - A mesh-only mode, that allows you to set your mesh's vertices colors (i.e. to "paint" them).
   * - .. figure:: /images/editors_3dview_modes_icons-weight-paint.png
     - :doc:`Weight Paint Mode </sculpt_paint/weight_paint/index>`
     - A mesh-only mode, dedicated to vertex group weighting.
   * - .. figure:: /images/editors_3dview_modes_icons-texture-paint.png
     - :doc:`Texture Paint Mode </sculpt_paint/texture_paint/index>`
     - A mesh-only mode, that allows you to paint your mesh's texture directly on the model, in the 3D Viewport.
   * - .. figure:: /images/editors_3dview_modes_icons-particle-edit.png
     - :doc:`Particle Edit Mode </physics/particles/mode>`
     - A mesh-only mode, dedicated to particle systems, useful with editable systems (hair).
   * - .. figure:: /images/editors_3dview_modes_icons-pose-mode.png
     - :doc:`Pose Mode </animation/armatures/posing/index>`
     - An armature only mode, dedicated to armature posing.
   * - .. figure:: /images/editors_3dview_modes_icons-grease-pencil.png
     - :doc:`Draw Mode </grease_pencil/modes/draw/index>`
     - A Grease Pencil only mode, dedicated to create Grease Pencil strokes.

.. note::

   The cursor becomes a brush in :doc:`Paint and Sculpt Modes </sculpt_paint/index>`.

We will not go into any more detail on mode usages here,
because they are dealt with in their own sections.

.. hint::

   If you are reading this manual and some button or menu option is referenced
   that does not appear on your screen, it may be that you are not in the proper
   mode for that option to be valid.


.. _3dview-multi-object-mode:

Multi-Object Editing
====================

Edit and Pose Modes support editing of multiple objects at once.

This is convenient if you want to perform the same edits on multiple objects
or want to animate multiple characters at once.

- To use edit multiple objects at once, simply select multiple objects and enter the mode.
- The Outliner can also be used to add/remove objects while you are in a mode,
  by setting or clearing the mode from the context menu, or :kbd:`Ctrl-LMB` clicking on the objects data icon.
- Only the active object will be used to display properties such as shape keys, UV layers, etc.
- Selecting any element from an object will set this as the active object.
- There are limits to the kinds of operations that can run on multiple objects.

  *You can't for example create an edge that has vertices from different objects.*
