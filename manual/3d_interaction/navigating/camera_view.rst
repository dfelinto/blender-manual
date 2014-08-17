
Camera View
***********

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Menu:     :menuselection:`View --> Camera --> Active Camera`
   | Hotkey:   :kbd:`pad0`


Cameras View can be used to virtually compose shots and preview how the scene will look when
rendered.
Pressing :kbd:`pad0` will show the scene as viewed from the currently active camera. In
this view you can also set the :guilabel:`Render Border` which defines the portion of the
camera view to be rendered.


.. figure:: /images/3D-interaction_Navigating_Camera-View-perspective-camera-render.jpg
   :width: 640px
   :figwidth: 640px

   Camera view provides a preview for the final rendered image.


Render Border
=============

.. figure:: /images/3D-interaction_Navigating_Camera-View-render-border-toggle.jpg

   Render Border toggle


While in camera view,
you can define a :guilabel:`Render Border` by pressing :kbd:`Ctrl-B`.
This will allow you to draw out a dotted orange rectangle within the camera view.
Your renders will now be limited to the part of scene visible within the render border.
This can be very useful for reducing render times. The border can be disabled by disabling the
:guilabel:`Border` option in the :guilabel:`Dimensions` panel of the :guilabel:`Render`
context or by using :kbd:`Ctrl-B` to set a :guilabel:`Render Border` larger than the
camera view.


.. admonition:: Anti-Aliasing and blur options with borders
   :class: note

   Note that when Render Borders are activated, Full Sampling Anti-Aliasing will be disabled while Sampled Motion Blur will become available.

   :doc:`Read more about Anti-Aliasing » <render/options/antialiasing>`
   :doc:`Read more about Motion Blur » <render/post_process/motion_blur>`


.. figure:: /images/3D-interaction_Navigating_Camera-View-render-border.jpg
   :width: 640px
   :figwidth: 640px

   Render border and associated render.


:doc:`Read more about Render Output options » <render/output>`

:doc:`Read more about Cameras » <render/camera>`

