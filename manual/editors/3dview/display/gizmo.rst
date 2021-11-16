.. |gizmo-icon| image:: /images/editors_3dview_display_gizmo_header.png
.. _bpy.types.SpaceView3D.show_gizmo:

***************
Viewport Gizmos
***************

.. reference::

   :Mode:      Object and Edit Modes
   :Header:    |gizmo-icon| :menuselection:`Viewport Gizmos --> Object Gizmos`

The way how gizmos are displayed in the 3D Viewport can be changed in the Viewport Gizmos pop-over.
There is a toggle to hide all gizmos for the 3D Viewport.


Viewport Gizmos
===============

Navigate
   Enable/disable the navigation gizmo.
Active Tool
   Enable/disable the gizmo of the active tool.
Active Object
   Enable/disable the gizmo for the active object.


Object Gizmos
=============

The Object Gizmos allows mouse controlled translation, rotation and scaling in the 3D Viewport.
There is a separate gizmos for each operation.
Each gizmo can be used separately or in combination with the others.
You can use the gizmos by dragging one of the three colored axes with :kbd:`LMB`.
The transformation will be locked to the clicked axis.

Holding down :kbd:`Shift` *after* you :kbd:`LMB`
the gizmo handle will constrain the action to smaller increments.
Holding down :kbd:`Shift` *before* you :kbd:`LMB` click on one of the handles will cause the gizmo action
to be performed relative to the other two axes. See :ref:`view3d-transform-plane-lock`.

Orientation
   The orientation to use for the gizmo. The orientations can be
   configured in the viewport orientation :doc:`Orientations menu </editors/3dview/controls/orientation>`.
Move
   Show the gizmo to control the location.
   Dragging the small white circle allows free transformation.
Rotate
   Show the gizmo to control the rotation.
   When you hover your mouse over the gizmo a highlighted circle will appear,
   clicking this will activate :ref:`trackball rotation <view3d-transform-trackball>`.
Scale
   Show the gizmo to control the scaling.

.. list-table::

   * - .. figure:: /images/editors_3dview_display_gizmo_options-translate.png
          :width: 320px

          Move.

     - .. figure:: /images/editors_3dview_display_gizmo_options-rotate.png
          :width: 320px

          Rotate.

     - .. figure:: /images/editors_3dview_display_gizmo_options-scale.png
          :width: 320px

          Scale.

     - .. figure:: /images/editors_3dview_display_gizmo_options-all.png
          :width: 320px

          Combination.

.. seealso::

   The :ref:`Gizmo Preferences <prefs-viewport-gizmo-size>`.


Empty
=====

Gizmo settings for empties.

Image
   Show the gizmo to adjust the image size and position of empties.
Force Field
   Show the gizmo to adjust the force field.


Light
=====

Gizmo settings for lights.

Size
   Show the gizmo to adjust the size of lights.
Look At
   Show the gizmo to adjust the direction of the light.


Camera
======

Gizmo settings for cameras.

Lens
   Show the gizmo to adjust the lens and orthographic size.
Focus Distance
   Show to gizmo to adjust the focus distance.
