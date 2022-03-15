
************************
Perspective/Orthographic
************************

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Perspective/Orthographic`
   :Shortcut:  :kbd:`Numpad5`

This operator changes the projection of the viewport camera.
Each 3D Viewport supports two different types of projection.
These are demonstrated in the Fig. below.

.. list-table::

   * - .. figure:: /images/editors_3dview_navigate_projections_view-orthographic.png
          :width: 320px

          Orthographic projection.

     - .. figure:: /images/editors_3dview_navigate_projections_view-perspective.png
          :width: 320px

          Perspective projection.

Our eye is used to perspective viewing because distant objects appear smaller.
Orthographic projection often seems a bit odd at first,
because objects stay the same size regardless of their distance.
It is like viewing the scene from an infinitely distant point.
Nevertheless, orthographic viewing is very useful,
because it provides a more "technical" insight into the scene,
making it easier to model and judge proportions.


Options
=======

To change toggle between the two projections for the 3D Viewport, select
:menuselection:`View --> Perspective/Orthographic` or use the shortcut
:kbd:`Numpad5`. Changing the projection for a 3D Viewport does not affect
the way the scene will be rendered. Rendering is in perspective by default.
If you need to create an orthographic rendering, select the camera, go to
the Camera tab and set the type *Orthographic* in the *Lens* panel.

.. seealso::

   - :ref:`Auto-Perspective Preference <prefs-navigation-auto_perspective>`
   - :ref:`Render perspective <camera-lens-type>`
   - :term:`Camera Projections <Projection>`
