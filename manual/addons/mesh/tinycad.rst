
******************
tinyCAD Mesh Tools
******************

The add-on is a combination of several scripts which should be useful to anyone
who has used other :abbr:`CAD (Computer-Aided Design)` software for drafting with some level of precision.
The context menu has the tinyCAD functions prepended to it.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Mesh then tinyCAD Mesh tools to enable the script.


Description
===========

VTX
---

Automatically extends, projects or intersects the two selected edges if they are co-planar.
For auto VTX you must be in (Edit Mode and edge mode) and have two edges selected.
When invoked the add-on will detect if you are trying to intersect, project or extend two edges.
It will internally pick from V, T or X. It will also notify you if the edge are not co-planar / do not intersect.

- V: Extending two edges towards their calculated intersection point.
- T: Extending the path of one edge towards another edge.
- X: Two edges intersect, their intersection gets a weld vertex. You now have four edges and five vertices.


V2X
---

Places a new separate vertex at projected intersection of two selected edges.


XALL
----

This mass intersects a collection of edges. Pick a collection of edges and invoke XALL.
It will deselect any edge that doesn't intersect other edges first.
Then it goes through all combinations of the remaining edges to see if there are intersections.
Each intersection is dealt with and the result is added to the collection of edges to check.
This process continues until no more intersections are found.


BIX
---

Given two selected edges, this script creates the bisector of these edges.
The edges are first checked for co-planarity.


CCEN
----

Construct a circle and its center.
Pick three vertices that once made up a circle, then :menuselection:`W --> CCEN`,
the script adds a Grease Pencil representation of the circle.
To add a mesh of that constructed circle you can press :kbd:`F6` straight afterwards and
adjust the circle's vertex count. Then press *Make Circle Mesh* to add a new circle.
This is a little bit experimental, but works fine.


.. admonition:: Reference
   :class: refbox

   :Category:  Mesh
   :Description: Mesh modeling toolkit. Several tools to aid modeling.
   :Location: :menuselection:`3D Viewport Edit Mode --> context menu`
   :File: tiny_cad folder
   :Author: zeffii (Dealga McArdle)
   :License: GPL
   :Note: This add-on is bundled with Blender.
