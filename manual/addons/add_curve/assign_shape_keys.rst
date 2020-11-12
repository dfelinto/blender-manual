
*****************
Assign Shape Keys
*****************

This add-on lets you assign one or more Bézier curve(s) as shape keys to other curve.
Useful for morphing curves and curve based text objects.

.. youtube:: Ly64vezt0Go


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Add Curve then Assign Shape Keys to enable the script.


Interface
=========

Located in the :menuselection:`3D Viewport --> Sidebar --> Edit tab`.

.. figure:: /images/addons_add-curve_assign-shape-keys_ui.jpg
   :align: right
   :width: 220px


Usage
=====

#. Select the target and shape key Bézier curve objects.
#. Make sure the target is the active object; you can do this by
   :kbd:`Shift-RMB`-clicking the target curve after the other selections are made.
#. Go to the *Curve Shape Keys* tab and click *Assign Shape Keys* button.
#. Now a copy of the active object curve will be created, which will have the other selected curves as its target.

If the *Remove Shape Key Objects* option is checked, the selected curve objects will be deleted
and only the target is kept.

There are some options to align the closed (cyclic spline) target and the shape-key curves.
Also it's possible to match individual parts from a multipart (multiple splines) of target
and shape key curves (e.g. a text object converted into a curve) based on various criteria.

For smoother transition, you can subdivide the segments of one of the curves in the selection group.


Manual Alignment of Starting Vertices
-------------------------------------

In Edit Mode the *Assign Shape Keys* panel shows a single button -- *Mark Starting Vertices*.
When clicked, all the starting vertices of the closed splines (disconnected parts) of
the selected curves are indicated by a marking point. Now if you select any vertex,
the marker moves to this selected vertex, indicating the new starting vertex.
You need to confirm the new positions by pressing :kbd:`Return`.
Pressing :kbd:`Esc`, reverts the positions to the earlier order.


.. admonition:: Reference
   :class: refbox

   :Category:  Add Curve
   :Description: Assigns one or more Bézier curves as a shape key for another Bézier curve.
   :Location: :menuselection:`Sidebar --> Edit tab`
   :File: curve_assign_shapekey.py
   :Author: Shrinivas Kulkarni
   :Maintainer: Shrinivas Kulkarni
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
