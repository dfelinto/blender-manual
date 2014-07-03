

..    TODO/Review: {{review|partial=X}} .


Introduction
============

Since we are working with new and improving Python API,
if you have something that needs to be answered, please add it here.
We will find answers from dev's if we do not know them and provide an answer here.


Geometry
========


How can I generate a mesh object using the API?
-----------------------------------------------


Download this code example
[https://svn.blender.org/svnroot/bf-extensions/contrib/py/api-doc/Script_GeneratePyramidMesh.py
 Script_GeneratePyramidMesh.py] and run it from the Text Window.


How do I apply a modifier using the API?
----------------------------------------


::


   bpy.ops.object.convert(target='MESH', keep_original=False)


All the modifiers in the stack will be applied.

In case you just want to apply only the subsurf modifier and leave others alone,
and create a new mesh (Old mesh will retain all its modifiers), the
following code shows one way of doing it.
::


   for modifier in bpy.context.object.modifiers:
   if modifier.type != 'SUBSURF':
   modifier.show_render=True
   bpy.ops.object.convert(target='MESH', '''keep_original=True''')


How do I get the world coordinates of a control vertex of a BezierCurve?
------------------------------------------------------------------------


::


   wmtx = bpy.context.active_object.matrix_world

   localCoord = bpy.context.active_object.data.splines[0].bezier_points[1].co

   worldCoord = wmtx * localCoord


.. figure:: /images/Manual-Part20-scripting-faq-CV-in-world-coords.jpg
   :width: 480px
   :figwidth: 480px


`More info... <https://sites.google.com/site/satishgoda/blender/blog/blender25xscriptinggettingtheworldcoordinates>`__


How do I select/deselect the control points of a Curve
------------------------------------------------------


Method 1
~~~~~~~~


.. figure:: /images/Manual-Part20-scripting-faq-select-curve-control-point-method-1.jpg
   :width: 480px
   :figwidth: 480px


::


   curve = bpy.context.selected_objects[0]

   curve.data.splines[0].bezier_points[0].select_control_point = True
   curve.data.splines[0].bezier_points[2].select_control_point = True


Method 2
~~~~~~~~


.. figure:: /images/Manual-Part20-scripting-faq-select-curve-control-point-method-2.jpg
   :width: 480px
   :figwidth: 480px


::


   bpy.context.active_object.data.splines[0].bezier_points[0].select_control_point = True


`More info... <https://sites.google.com/site/satishgoda/blender/blog/blender25xScriptingSelectCVusingPython>`__


Materials
=========


How to link a mesh/object to a material?
----------------------------------------

TODO


Customization
=============


How do I automate custom hotkeys?
---------------------------------


