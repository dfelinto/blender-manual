
Controlling the fluid volume
============================

To control the volume of the fluid simulation, you can set objects in the scene to add or absorb fluid within the :doc:`Fluid Domain <physics/fluid/domain>`.


Inflow
------

.. figure:: /images/Blender_fluids_inflow.jpg
   :width: 300px
   :figwidth: 300px

   Fluid inflow settings


This object will put fluid into the simulation, like a water tap.


FIXME(Template Unsupported: Doc:2.6/Manual/Physics/Fluid/volume_init;
{{Doc:2.6/Manual/Physics/Fluid/volume_init}}
)

:guilabel:`Inflow velocity`
   Speed of the fluid that is created inside of the object.

:guilabel:`Local Coords` / :guilabel:`Enable`
   Use local coordinates for the inflow. This is useful if the inflow object is moving or rotating, as the inflow stream will follow/copy that motion. If disabled, the inflow location and direction do not change.


FIXME(Template Unsupported: Doc:2.6/Manual/Physics/Fluid/animated_mesh_export;
{{Doc:2.6/Manual/Physics/Fluid/animated_mesh_export}}
)


Outflow
-------

.. figure:: /images/Blender_fluids_outflow.jpg
   :width: 300px
   :figwidth: 300px

   Fluid outflow settings


Any fluid that enters the region of this object will be deleted
(think of a drain or a black hole).
This can be useful in combination with an inflow to prevent the whole domain from filling up.
When enabled, this is like a tornado (waterspout) or "wet vac" vacuum cleaner,
and the part where the fluid disappears will follow the object as it moves around.


FIXME(Template Unsupported: Doc:2.6/Manual/Physics/Fluid/volume_init;
{{Doc:2.6/Manual/Physics/Fluid/volume_init}}
)


FIXME(Template Unsupported: Doc:2.6/Manual/Physics/Fluid/animated_mesh_export;
{{Doc:2.6/Manual/Physics/Fluid/animated_mesh_export}}
)
