
Common Shadowing Lamps Options
==============================

.. figure:: /images/Manual-Lighting-Shadow-Common-Properties.jpg
   :width: 310px
   :figwidth: 310px

   Common shadowing options for lamps


All lamps able to cast shadows (:doc:`Lamp <lighting/lamps/lamp>`, :doc:`Spot <lighting/lamps/spot>`, :doc:`Area <lighting/lamps/area>` and :doc:`Sun <lighting/lamps/sun>`) share some options, described below:

:guilabel:`This Layer Only`
   When this option is enabled, only the objects on the same layer as the light source will cast shadows.
:guilabel:`Only Shadow`
   The light source will not illuminate an object but will generate the shadows that would normally appear.
   This feature is often used to control how and where shadows fall by having a light which illuminates but has no shadow, combined with a second light which doesn't illuminate but has :guilabel:`Only Shadow` enabled, allowing the user to control shadow placement by moving the "Shadow Only" light around.

Shadow color
   This color picker control allows you to choose the color of your cast shadows (black by default).
   The images below were all rendered with a white light and the shadow color was selected independently.

+--------------------------------------------------------------------+----------------------------------------------------------------------+---------------------------------------------------------------------+
+.. figure:: /images/Manual_-_Shadow_and_Spot_-_Red_Buffer_Shadow.jpg|.. figure:: /images/Manual_-_Shadow_and_Spot_-_Green_Buffer_Shadow.jpg|.. figure:: /images/Manual_-_Shadow_and_Spot_-_Blue_Buffer_Shadow.jpg+
+   :width: 190px                                                    |   :width: 190px                                                      |   :width: 190px                                                     +
+   :figwidth: 190px                                                 |   :figwidth: 190px                                                   |   :figwidth: 190px                                                  +
+                                                                    |                                                                      |                                                                     +
+   Red colored shadow example                                       |   Green colored shadow example                                       |   Blue colored shadow example                                       +
+--------------------------------------------------------------------+----------------------------------------------------------------------+---------------------------------------------------------------------+

   Although you can select a pure white color for a shadow color, it appears to make a shadow disappear.


See Also
--------

- :doc:`Shadows <lighting/shadows>`
- :doc:`Common Raytraced Options <lighting/shadows/raytraced_properties>`
- :doc:`Lamp Light Raytraced Shadows <lighting/lamps/lamp>`
- :doc:`Spot Light Raytraced Shadows <lighting/lamps/spot>`
- :doc:`Area Light Raytraced Shadows <lighting/lamps/area>`
- :doc:`Sun Light Raytraced Shadows <lighting/lamps/sun>`
- :doc:`Spot Light Buffered Shadows <lighting/lamps/spot/buffered_shadows>`


