
**************
Geodesic Domes
**************

Original introduction from Andy Houston (Blender 2.4 series)

- Geodesic spheres based on icosahedrons, octahedrons and tetrahedrons.
- Triangular, hexagonal and hex/tri combo face options.
- A function that turns the current shape into its geometric dual (sort of).
- Grid, Cylinder, Parabola, Torus and Ball primitives.
- Hubs and Struts. Fill out those edges and vertices with your custom, decorative meshes.
- Superformula deforming. Create rounded triangles, wobbly shapes, etc.

Introduction by Brendon Murphy (Blender 2.6/7 series)

- This script can be used to create geodesic objects, not limited to domes or spheres.
- Each mesh type created has it's own set of editable parameters.
- By editing the parameters, you can create many simple or complex mesh shapes.
- Create an equal-sided pyramid, a soccer ball, a wine glass and more.
- Limited only by your imagination (and some cool math limitations).
- Create complex mesh deformations with the superformula parameters.
- In the next section we will cover the menu types and how to use the parameters to "design" your mesh.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Add Mesh then Geodesic Domes to enable the script.


Instructions
============

Main
   The *Main* menu is where you will do most of your work.
   The geodesic default triangle will be shown in the 3D View and the Object Creation parameters can be accessed here.
   Please note: I find it's easier to use the Object Creation parameters first before moving on to
   Faces, Struts and Hubs, these will be explained in the sections below.

For now, let's look at the Object Types and their parameters:

Objects
   There are six Object types you can create by default.
   Using the parameters you can build upon these objects to create more object types.
   Object Types have unique parameter sets and share the Superformula parameters (described below).


Geodesic Object Class Types
===========================

Geodesic
   Please note, the *Frequency* parameters have a high impact on object creation.
   To create a Geodesic Dome you must increase the *Frequency* or the default Triangle.

Subdivide Basic/Triacon
   Class 1 is the "equilateral triangle".
   Class 2 is the "cube".

Hedron
   Choose between Tetrahedron, Octahedron, Icosahedron.

Point
   Point (vertex), edge or face pointing upwards.

Shape
   Choose between tri, hex or star face types.

Round
   Choose between spherical or flat. (May not work for all object types.)


Geodesic Object Parameters
--------------------------

Frequency
   Subdivide base triangles.

Radius
   Overall radius.

Eccentricity
   Scaling on the X/Y axis.

Squish
   Scaling on the Z axis.

Square (X/Y)
   Superellipse action in X/Y.

Square (Z)
   Superellipse action in Z.

Rotate (X/Y)
   Rotate superellipse action in X/Y.

Rotate (Z)
   Rotate superellipse action in Z.

Dual
   Faces become vertices, vertices become faces, edges flip.


Geodesic Object Types
=====================

There are six Object types you can create.
Each type has it's own set of parameters.
As you can see most menu items are self explanatory.
The tooltips will give you further information on individual parameters.

Gap
   Shrink faces in direction.
   Add or remove rows of faces based on height (Z) or (X/Y).

Phase
   Rotate around a pivot.
   Useful for rotating deformation or use with *Gap*.


Import Your Mesh
================

You can import your own mesh into Geodesic Domes for use within the script.
This is limited to the Faces, Struts and Hubs menus.


Faces
=====

This Section adds extrusions and edits face structures on a mesh.


Struts
======

This section allows you to extrude an object along the edges of a mesh.


Hubs
====

This section allows you to place an object at the vertex on a mesh.


Superformula Menu
=================

The superformula settings add a variety of settings such as pinching, twisting, inflate and
more complex edit types.


.. admonition:: Reference
   :class: refbox

   :Category:  Add Mesh
   :Description: Create Geodesic object types.
   :Location: :menuselection:`3D Viewport --> Add --> Mesh`
   :File: add_mesh_geodesic_domes folder
   :Author: Andy Housten
   :Maintainer: To Do
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
