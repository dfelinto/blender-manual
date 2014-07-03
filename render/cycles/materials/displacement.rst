


Displacement
============


*Implementation not finished yet, marked as
FIXME(TODO: Internal Link;
[[../../Experimental_Features|experimental feature]]
).*

The shape of the surface and the volume inside its mesh may be altered by the displacement
shaders. This way, textures can then be used to make the mesh surface more detailed.


Type

----


.. figure:: /images/Selection_017.jpg


Depending on the settings, the displacement may be virtual,
only modifying the surface normals to give the impression of displacement,
known as bump mapping, or a combination of real and virtual displacement.
The displacement type options are:

- **True Displacement**\ : Mesh vertices will be displaced before rendering, modifying the actual mesh. This gives the best quality results, if the mesh is finely subdivided. As a result this method is also the most memory intensive.
- **Bump Mapping**\ : When executing the surface shader, a modified surface normal is used instead of the true normal. This is a quick alternative to true displacement, but only an approximation. Surface silhouettes will not be accurate and there will be no self-shadowing of the displacement.
- **Displacement + Bump**\ : Both methods can be combined, to do displacement on a coarser mesh, and use bump mapping for the final details.


Subdivision
-----------


.. figure:: /images/cycles_manual_materials_displacementbump.jpg

   Bump Mapped Displacement


*Implementation not finished yet, marked as
FIXME(TODO: Internal Link;
[[../../Experimental_Features|experimental feature]]
).*

When using *True Displacement* or *Displacement + Bump* and enabling *Use Subdivision*
you can reduce the **Dicing Rate** to subdivide the mesh.
This only affects the render and does not show in the viewport
(but does show in *Rendered Shading Mode*\ ).
Displacement can also be done manually by use of the Displacement Modifier.


.. figure:: /images/Manual-Cycles-Displacement-Dicing.jpg
   :width: 567px
   :figwidth: 567px

   Subdivision Off - On, Dicing Rate 1.0 - 0.3 - 0.05 (Monkeys look identical in viewport, no modifiers)

