..    TODO/Review: {{review}} .

Fluid Obstacle
**************

This object will be used as an obstacle in the simulation. As with a fluid object,
obstacle objects currently should not intersect. As for fluid objects,
the actual mesh geometry is used for obstacles. For objects with a volume,
make sure that the normals of the obstacle are calculated correctly, and radiating properly
(use the :guilabel:`Flip Normal` button, in :guilabel:`Edit mode`,
:guilabel:`Mesh Tools` panel, :guilabel:`Editing` context [\ :kbd:`f9` ]),
particularly when using a spinned container. Applying the Modifier :guilabel:`SubSurf` before
baking the simulation could also be a good idea if the mesh is not animated.


FIXME(Template Unsupported: Doc:2.6/Manual/Physics/Fluid/volume_init;
{{Doc:2.6/Manual/Physics/Fluid/volume_init}}
)

:guilabel:`Boundary type`
   Determines the stickiness of the obstacle surface, called "Surface Adhesion". Surface Adhesion depends in real-world on the fluid and the graininess or friction/adhesion/absorption qualities of the surface.

   - :guilabel:`Noslip` causes the fluid to stick to the obstacle (zero velocity).
   - :guilabel:`Free` (-slip) allows movement along the obstacle (only zero normal velocity).
   - :guilabel:`Part` (-slip) mixes both types, with 0 being mostly noslip, and 1 being identical to freeslip.

   Note that if the mesh is moving, it will be treated as noslip automatically.


.. figure:: /images/Manual-Part-X-bndtcomp.jpg
   :width: 610px
   :figwidth: 610px

   Example of the different boundary types for a drop falling onto the slanted wall. From left to right: no-slip, part-slip 0.3, part-slip 0.7 and free-slip.


FIXME(Template Unsupported: Doc:2.6/Manual/Physics/Fluid/animated_mesh_export;
{{Doc:2.6/Manual/Physics/Fluid/animated_mesh_export}}
)

:guilabel:`PartSlip Amount`
   Amount of mixing between no- and free-slip, described above.


.. note:: Moving obstacles support

   Blender supports now moving obstacles.

   In the past, a  moving obstacle was automatically treated as no slip (sticky),
   so if you wanted to splash off of a moving object,
   you had to put a transparent plane in the spot where the fluid will hit the moving object,
   exactly aligned and shaped as the object, to fake the splash. This is not needed anymore.


:guilabel:`Impact Factor`
   Amount of fluid volume correction for gain/loss from impacting with moving objects. If this object is not moving, this setting has no effect. However, it if is and the fluid collides with it, a negative value takes volume away from the Domain, and a positive number adds to it. Ranges from -2.0 to 10.0.

