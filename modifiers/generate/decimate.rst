


Decimate Modifier
=================


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Panel:    :guilabel:`Modifiers`


Description
-----------

The :guilabel:`Decimate` modifier allows you to reduce the vertex/face count of a mesh with
minimal shape changes. This is not applicable to meshes which have been created by modeling
carefully and economically,
where all vertices and faces are necessary to correctly define the shape,
but if the mesh is the result of complex modeling, with proportional editing,
successive refinements, possibly some conversions from SubSurfed to non-SubSurfed meshes,
you might very well end up with meshes where lots of vertices are not really necessary.

The :guilabel:`Decimate` modifier is a quick and easy way of reducing the polygon count of a
mesh non-destructively. This modifier demonstrates the advantages of a mesh modifier system
because it shows how an operation which is normally permanent and destroys original mesh data,
can be done interactively and safely using a modifier.

Unlike the majority of existing modifiers, the :guilabel:`Decimate` modifier does not allow
you to visualize your changes in :guilabel:`Edit mode`\ .

:guilabel:`Decimate` only handles triangles, so each quadrilateral face is implicitly split into two triangles for decimation.


Options
-------


.. figure:: /images/25-Manual-Modifiers-Decimate.jpg

   decimate modifier


:guilabel:`Ratio`
   The ratio of faces to keep after decimation, from **0.0** (0%, all faces have been completely removed) to **1.0** (100%, mesh is completely intact, except quads have been triangulated).
    As the percentage drops from **1.0** to **0.0**\ , the mesh becomes more and more decimated until it no longer visually looks like the original mesh.

:guilabel:`Face Count` (display only)
   This field shows the number of remaining faces as a result of applying the :guilabel:`Decimate` modifier.


Examples
--------


Simple plane
~~~~~~~~~~~~

A simple example is a plane, and a 4x4 undeformed :guilabel:`Grid` object.
Both render exactly the same, but the plane has one face and four vertices,
while the grid has nine faces and sixteen vertices, hence lots of unneeded vertices and faces.
The :guilabel:`Decimate` modifier allows you to eliminate these unneeded faces.


Decimated cylinder
~~~~~~~~~~~~~~~~~~

We take a simple example of decimating a cylinder with the default of **32** segments.
This will generate a cylinder with **96** faces.
When the :guilabel:`Decimate` modifier is applied,
the face count goes up! This is because the modifier converts all quadrangles (\ *quads*\ )
into triangles (\ *tris*\ ) which always increases the face count.
Each quad decomposes into two triangles.

The main purpose of the :guilabel:`Decimate` modifier is to reduce mesh resources through a
reduction of vertices and faces,
but at the same time maintain the original shape of the object.

In the following picture, the percentage dropped in each successive image,
from **100%** to **5%** (a ratio of **0.05**\ ).
Notice that the face count has gone from **128** to **88** at a ratio of **0.6**
(\ **60%**\ ) and yet the cylinder continues to look very much like a cylinder,
and we discarded **40** unneeded faces.


.. figure:: /images/25-Manual-Modifiers-Decimate-ExampleCylinder.jpg
   :width: 600px
   :figwidth: 600px

   1.0 (100%). Faces: 128; 0.8 (80%). Faces: 102; 0.6 (60%). Faces: 88
   0.2 (20%). Faces: 24; 0.1 (10%). Faces: 12; 0.05 (5%). Faces: 6


As you can see, when the ratio reaches **0.1**\ , the cylinder looks more like a cube.
And when it reaches **0.05**\ , it doesn't even look like a cube!

Once you have reached the face count and appearance you were looking for,
you can :guilabel:`Apply` the modifier.
If you want to convert many of the tris back to quads to reduce mesh resources further,
you can switch to :guilabel:`Edit mode`\ , select all vertices (\ :kbd:`A`\ ),
and hit :kbd:`alt-J`\ .


