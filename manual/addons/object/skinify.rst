
***********
Skinify Rig
***********

This add-on creates a mesh object "Skinify Guy" covering an armature with a mesh.

- It works with Rigify:
- It works with BVH imports:
- It works with manuelbastionilab add-on:


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Object then Scatter Objects to enable the script.


Usage
=====

Select your armature in Pose Mode and skin the selected or all bones with a per-bone mesh or whole cover.
If bones in your rig give unwanted results, often scaling and re-positioning the bones in Edit Mode can help.
If your doing this to create your own "Skinify Guy" you can also delete bones.
It will work with custom shapes but results may vary.
More to come...

.. seealso::

   Please see the
   `old Wiki <https://archive.blender.org/wiki/index.php/Extensions:2.6/Py/Scripts/Modeling/Extra_Tools/>`__
   for the archived original docs.


.. admonition:: Reference
   :class: refbox

   :Category:  Object
   :Description: Creates a mesh object from selected bones.
   :Location: :menuselection:`3D Viewport Pose Mode --> Sidebar --> Create tab`
   :File: object_skinify.py
   :Author: Albert Makac (karab44)
   :License: GPL 2+
   :Note: This add-on is bundled with Blender.
