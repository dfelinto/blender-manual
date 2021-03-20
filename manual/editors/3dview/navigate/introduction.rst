
************
Introduction
************

Navigating in the 3D space is done with the use of both mouse movement and keyboard shortcuts.

To be able to work in the three-dimensional space that Blender uses,
you must be able to change your viewpoint as well as the viewing direction of the scene.
While we will describe the *3D Viewport* editor, most of the other editors have similar functions.
For example, it is possible to pan and zoom in the Image editor.

.. tip:: Mouse Buttons and Numpad

   If you have a mouse with less than three buttons or a keyboard without a numpad,
   see the :doc:`Keyboard and Mouse </getting_started/configuration/hardware>`
   page of the manual to learn how to use them with Blender.


.. _navigation-gizmo:

Navigation Gizmo
================

.. figure:: /images/editors_3dview_navigate_introduction_gizmo.png
   :align: right

   Navigation Gizmo.

The navigation gizmo can be found in the top right of the editor.
The four buttons (listed from top to bottom) do the following:

- :ref:`Zooms the 3D Viewport <editors_3dview_navigation_zoom>`
- :ref:`Pans the 3D Viewport <bpy.ops.view3d.view_pan>`
- :doc:`Toggles the Camera View </editors/3dview/navigate/camera_view>`
- :doc:`Toggles the Projection </editors/3dview/navigate/projections>`

The :ref:`Orbit <bpy.ops.view3d.view_orbit>` gizmo at the top can be used to rotate around the 3D Viewport.
Hovering over the gizmo and dragging with :kbd:`LMB` will orbit the view.
Clicking any of the axis labels will :doc:`Align </editors/3dview/navigate/align>` to that view.
Clicking the same axis again switches to the opposite side of that same axis.
