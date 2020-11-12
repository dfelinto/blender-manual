
****************
Math Vis Console
****************

Sometimes when writing Python scripts you stumble on complicated
matrix transformations, ray intersections, rotation conversions, mesh modifications, etc.
where its useful to view lines, points and matrices in the viewport to better understand the problem.

Creating mesh data for this purpose isn't difficult but is cumbersome.
The purpose of this add-on is to make it as quick and easy as possible.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click 3D View then Math Vis (Console) to enable the script.


Instructions
============

Math Vis works by displaying Python Console defined mathutils typed variables in the 3D Viewport.

The following types are supported:

- Point: ``Vector(...)``
- Line: ``[Vector(...), Vector(...), ...]``
- Transformation: ``Matrix(...)``
- Transformations (without translation): ``Quaternion(...)``/ ``Euler(...)``


Usage
=====

.. figure:: /images/addons_3d-view_math-vis-console_example.jpg
   :align: center
   :width: 680px

Create a Python Console editor.
In the Python Console define a mathutils variable::

   hello_world = Vector((1, 2, 3))

You should now be able to see this point in the 3D View!

.. admonition:: Reference
   :class: refbox

   :Category:  3D View
   :Description: Display console defined mathutils variables in the 3D Viewport.
   :Location: :menuselection:`Properties --> Scene --> Python Console Menu`
   :File: space_view3d_math_vis.py
   :Author: Campbell Barton
   :Maintainer: Campbell Barton
   :License: GPL
   :Support Level: Official
   :Note: This add-on is bundled with Blender.
