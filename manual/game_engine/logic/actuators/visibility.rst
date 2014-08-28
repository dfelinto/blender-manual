
Visibility Actuator
*******************

The Visibility actuator allows the user to change the visibility of objects during runtime.


.. figure:: /images/2.5_Game_Engine_Actuator_Visibility.jpg
   :width: 271px
   :figwidth: 271px

   Visibility actuator


See :doc:`Actuator Common Options </game_engine/logic/actuators/common_options>` for common options.

Special Options:

**Visible**
   Toggle checkbox to toggle visibility
**Occlusion**
   Toggle checkbox to toggle occlusion. Must be initialised from the Physics tab.
**Children**
   Toggle checkbox to toggle recursive setting - will set visibility / occlusion state to all child objects, children of children (recursively)


Usage Notes
===========

Using the visiblity actuator will save on Rasterizer usage, however not Physics,
and so is limited in terms of Level of Detail (LOD). For LOD look at replace mesh,
but be aware that the logic required can negate the effect of the LOD.


