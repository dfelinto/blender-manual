
Fluid Object
============


.. figure:: /images/Blender_fluids_fluid.jpg
   :width: 300px
   :figwidth: 300px

   Fluid object settings


All regions of this object that are inside the domain bounding box will be used as actual
fluid in the simulation. If you place more than one fluid object inside the domain,
they should currently not intersect. Also make sure the surface normals are pointing outwards.
In contrast to domain objects, the actual mesh geometry is used for fluid objects.


FIXME(Template Unsupported: Doc:2.6/Manual/Physics/Fluid/volume_init;
{{Doc:2.6/Manual/Physics/Fluid/volume_init}}
)


FIXME(Template Unsupported: Doc:2.6/Manual/Physics/Fluid/animated_mesh_export;
{{Doc:2.6/Manual/Physics/Fluid/animated_mesh_export}}
)

Initial velocity
   Speed of the fluid at the beginning of the simulation, in meters per second.


.. admonition:: The direction of Surface Normals makes a big difference!
   :class: nicetip

   Blender uses the orientation of the Surface Normals to determine what is "inside of" the Fluid object and what is "outside". You want all of the normals to face *outside* (in :guilabel:`Edit mode`\ , use :kbd:`ctrl-N` or press :kbd:`Space` and choose :guilabel:`Edit` → :guilabel:`Normals` → :guilabel:`Calculate Outside`\ ). If the normals face the wrong way, you'll be rewarded with a "gigantic flood of water" because Blender will think that the volume of the object is outside of its mesh! This applies regardless of the :guilabel:`Volume init` type setting.


