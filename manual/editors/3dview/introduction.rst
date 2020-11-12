
************
Introduction
************

The 3D Viewport is used to interact with the 3D scene for a variety of purposes,
such as modeling, animating, texture painting, etc.


Header Region
=============

.. figure:: /images/editors_3dview_introduction_3d-view-header-object-mode.png

   Object Mode header.

The header contains various menus and controls based on
the current :doc:`mode </editors/3dview/modes>`.

Tools and modes in the 3D Viewport header are split in three groups of buttons:


Mode & Menus
------------

Mode
   The 3D Viewport has :doc:`several modes </editors/3dview/modes>`
   used for editing different kinds of data.

View
   This menu offers tools to :doc:`navigate </editors/3dview/navigate/index>` in 3D space.

Other menus depend on the current mode, Object Mode menus listed below:

Select
   Contains tools for :ref:`selecting <object-select-menu>` objects.
Add
   Gives a list of different :ref:`objects types <objects-types>` that can be added to a scene.
Object
   This menu appears when in Object Mode.
   it contains tools to edit :doc:`objects </scene_layout/object/editing/transform/introduction>`.
   In Edit Mode, it will change to the appropriate menu with :doc:`editing tools </modeling/index>`.


Transform Controls
------------------

Transform Orientations
   Use to select and modify the active :doc:`Transform Orientations </editors/3dview/controls/orientation>`.
Pivot Point
   Used to change the reference point (or :term:`Pivot Point`) used by many mesh manipulation tools.

   Read more about :doc:`Pivot Points </editors/3dview/controls/pivot_point/index>`.
Snapping
   Controls the :doc:`snapping tools </editors/3dview/controls/snapping>`
   that help with transforming and modeling objects.
Proportional Edit
   :doc:`Proportional Edit </editors/3dview/controls/proportional_editing>`.


Display & Shading
-----------------

Object Type Visibility
   Change the :doc:`Object Type Visibility </editors/3dview/display/visibility>`
   and selectability of objects in the 3D Viewport.
Viewport Gizmos
   Change the way how :doc:`gizmos </editors/3dview/display/gizmo>` are
   displayed in the 3D Viewport.
Viewport Overlays
   Change the way how :doc:`overlays </editors/3dview/display/overlays>` are
   displayed in the 3D Viewport.
X-Ray
   Show the whole scene transparent. This is a shortcut to
   the :ref:`X-ray <3dview-shading-xray>` option inside the shading control.
Viewport Shading
   Change the :doc:`shading </editors/3dview/display/shading>` of the 3D Viewport.


Toolbar Region
==============

The Toolbar is a context-sensitive region containing tools depending on the current mode
(for example, modeling tools in *Edit Mode*, brush tools in *Sculpt Mode*...).

See :doc:`Tools </editors/3dview/toolbar/index>` for more information.


Sidebar Region
==============

The Sidebar region contains properties of the active object and selected objects (such as their locations),
as well as properties of the editor itself.

See :doc:`Sidebar Panels </editors/3dview/sidebar>` for more information.
