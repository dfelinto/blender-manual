
******************
Point Density Node
******************

.. figure:: /images/render_shader-nodes_textures_point-density_node.png
   :align: right

   Point Density Node.

The *Point Density* node is used to add volumetric points for each particle or vertex of another object.


Inputs
======

Vector
   Texture coordinate to sample texture at;
   defaults to global position (*Position* output of *Geometry* node) if the socket is left unconnected.


Properties
==========

Point Data
   Where to get points from.

   Particle System
      Use each particle position from the specified particle system.
   Object Vertices
      Use each vertex position from the specified object.
Object
   Which object's vertices or particle system will be used.
Particle System
   Particle positions from this system will be used.
Space
   The coordinate system for mapping points.

   World Space
      Map each point exactly where the source particle/vertex is.
   Object Space
      Fit the points from the source particles/vertices
      inside the bounding box of the object with the point density texture.

Radius
   Size of the points.

Interpolation
   Texel filtering type.

   Closest
      No interpolation, use nearest texel. Produces blocky looking points.
   Linear
      Interpolate linearly between texels, producing soft, round points.
   Cubic
      Use cubic falloff, producing very soft points. Useful when points are very densely packed.
Resolution
   The dimensions of the texture holding the point data.
Color Source
   Which attribute of the particle system or mesh is used to color the output.

   Particle Color Sources
      Particle Age
         Lifetime mapped as (0.0 - 1.0) intensity.
      Particle Speed
         Particle speed (absolute magnitude of velocity) mapped as (0.0 - 1.0) intensity.
      Particle Velocity
         XYZ velocity mapped to RGB colors.
   Vertex Color Sources
      Vertex Color
         Use a vertex color layer for coloring the point density texture.

         .. note::

            Vertex colors are defined per face corner.
            A single vertex can have as many different colors as faces it is part of.
            The actual color of the point density texture is averaged from all vertex corners.

      Vertex Weight
         Use weights from a vertex group as intensity values.
      Vertex Normals
         Use object-space vertex normals as RGB values.


Outputs
=======

Color
   Texture color output.
Density
   Density of volume.


Examples
========

.. figure:: /images/render_shader-nodes_textures_point-density_example.jpg
   :width: 200px

   Domain object with Point Density texture using vertices from ball as points.
