
**************
Holes in Faces
**************

This section will look at some alternative ways of dealing with holes in surface.
In Blender, holes are generally dealt with by using boolean modifiers,
or boolean operations in Edit mode.
These result in many quad, or tri faces on what is essentially a flat surface.
CAD Designers would traditionally want a flat complex face to be an Ngon,
since Sub-Division modifiers would not be used for this type of modelling.

Alternative methods include using 2D curve surface, where any internal faces are treated as holes.
The disadvantage of this system is that to include these in a vertex mesh they must first be converted to meshes,
resulting in many tris on the flat face, again causing problems because these cannot be bevelled.


PDT Approach to Holes:
======================

In PDT, we have adopted a new approach of cutting the front face into as few Ngons
as possible to accommodate holes. This is still not ideal and two other options are being advocated:

* Allow holes in faces as they are in 2D curve surfaces and CAD software packages.
* Introduce "Hybrid" objects that can accommodate 2D curve surfaces and vertex meshes.

Allowing holes would mean that certain functions, like sculpting would not be possible,
so this type of face would be excluded from such functions.

.. figure:: /images/addons_pdt_holes_1.png
   :width: 400px

You can see the front face is in fact two faces split across the hole.

The process was to remove the existing front face, draw the hole as a cylinder,
then use PDT Join 2 Vertices to make the joining edges between the outer edge and the hole,
then making two faces, by selecting edges and using the Blender Face (Hotkey F) command.

Below is an example of a 2D curve surface, with the settings shown to make it a filled surface:

.. figure:: /images/addons_pdt_holes_2.png
   :width: 400px

These curve surface can then be placed in front of a mesh object to make a face,
but this will require Align tools in awkward rotational angles, something we have not released yet.
The proviso on this is that you can never ``Apply`` the rotations used, but that is no hardship.

Below is what this looks like if converted to a mesh,
producing totally unsuitable topology for precision modelling, or even bevelling:

.. figure:: /images/addons_pdt_holes_3.png
   :width: 400px

This object has 146 faces, versus only 3 curves for the donor 2D curve surface.

Here is another example of a holed surface using PDT techniques:

.. figure:: /images/addons_pdt_holes_4.png
   :width: 400px

Count the Faces! - 49 holes, 3 faces on the front and 3 on the back.
