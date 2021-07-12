
***********************
Inset Straight Skeleton
***********************

This add-on makes 'inset polygons', which you get when you advance the edges of
the polygon inwards at a constant rate. Sometimes when you do that, an advancing edge shrinks to nothing,
or edges hit an advancing concave corner. The algorithm tries to do the right thing when this happens:
one or more new polygons may form at that point, and insetting can continue inside those new polygons.

You can either inset a single polygon or you can treat groups of polygons connected together as a single region,
forming a complicated polygon (that may include holes) to be insetted as a unit.

In addition to insetting, it is often useful to raise or lower the inset polygon (perpendicular to the inset plane),
so a parameter to do that is included also.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Mesh then Inset Straight Skeleton to enable the script.


Description
===========

Enter mesh Edit Mode on a mesh object, and select one or more faces.

Scale
   Percent
      Means that amounts are a percentage of the amount for a full inset.
   Absolute
      Means that the amounts are in units.
Amount
   The distance to move the edges inward.
Height
   The distance to move the inset polygons upward.
Region
   If checked, treat all selected faces as a region to be inset, otherwise inset each face individually.
Quadrangulate
   Todo.


Technical Details
=================

The method used is described on
the `Straight Skeleton <https://en.wikipedia.org/wiki/Straight_skeleton>`__ Wikipedia page.
Consider this starting polygonal region:

As the edges move inward at a constant speed, two kinds of events can happen.
One is that an advancing corner can hit an advancing edge, as seen on the right part of this picture:

When this happens, the inset polygon splits into two.

The other is that an advancing edge can shrink to a point.
When the whole process continues until the end, you get something like this:

One cool thing about this algorithm is that if you move upwards or downwards
(perpendicular to the inset plane) at a constant speed, you form 'roofs' with a fixed pitch.

.. seealso::

   Please see the
   `old Wiki <https://archive.blender.org/wiki/index.php/Extensions:2.6/Py/Scripts/Modeling/Inset-Polygon/>`__
   for the archived original docs.


.. reference::

   :Category:  Mesh
   :Description: Make an inset inside selection using straight skeleton algorithm.
   :Location: 3D Viewport operator
   :File: mesh_inset folder
   :Author: Howard Trickey
   :License: GPL
   :Note: This add-on is bundled with Blender.
