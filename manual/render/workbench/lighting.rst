
********
Lighting
********

The Workbench engine does not use the lights of the scene.
The lighting conditions that will be used can be set in the Lighting panel.

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Properties --> Render --> Lighting`

Flat
   Do not calculate any lighting. The base color of the scene will be rendered.

Studio
   Use studio lights to light the objects.
   The studio lights can be :ref:`configured in the preferences <prefs-lights-studio>`.
   Studio lights can follow the camera or be fixed. When fixed the angle of the lights can be adjusted.

   World Space Lighting
      Uses world space lighting so lights do not follow the view camera.
   Rotation
      The rotation of the studio lights on the Z axis.

.. _render-workbench-matcap:

MatCap
   Use a material capture to light the objects in the scene.

   Custom MatCaps can be :ref:`loaded in the preferences <prefs-lights-matcaps>`.

   MatCaps can be flipped horizontally by clicking the Flip MatCap button.
