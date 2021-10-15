
***************
Simplify Curves
***************

The Simplify Curves tool works on a single selected curve object.
It generates a new curve based on the original one.
The higher the *Distance Error* threshold is set the more control points are removed.

The Simplify F-Curves tool works the same way, but on selected F-curves.

*Merge by Distance* tool glues nearby points on a single Bézier curve.
In fact it is an analog of the usual *Merge by Distance* on a mesh, but for curves.
Unlike the mesh one, it does not connect the points from different parts of the curves,
even if they are on the ends of the two curves.
To glue such points, you must first connect them with *Make Segment*.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Add Curve then Simplify Curves to enable the script.


Interface
=========

The *Merge By Distance* and *Curve Simplify* buttons are located in
the :menuselection:`3D Viewport --> Curve Context Menu` in curve Edit Mode.

The *Simplify F-Curves* tool can be accessed by enabling :ref:`Developer Extras <prefs-interface-dev-extras>`
and using the :ref:`bpy.ops.wm.search_menu` to search for "Simplify F-Curves" in the Dope Sheet or Graph Editor.


.. reference::

   :Category:  Add Curve
   :Description: Simplify curves in the 3D Viewport, and Dope Sheet, merge by distance in 3D Viewport.
   :Location: :menuselection:`3D Viewport --> Add --> Curve --> Curve Simplify`,
              :menuselection:`Dope Sheet and Graph editors --> Channel --> Simplify F-Curves`
   :File: curve_simplify.py
   :Author: testscreenings, Michael Soluyanov
   :Maintainer: To Do
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
