
*************
Cell Fracture
*************

Todo.

.. seealso::

   Please see
   the `old Wiki <https://archive.blender.org/wiki/index.php/Extensions:2.6/Py/Scripts/Object/CellFracture/>`__
   for the archived original docs.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Object then Cell Fracture to enable the script.


Usage
=====

#. In Object Mode select the object you want to break apart.
#. Use the :ref:`Operator Search <bpy.ops.wm.search_operator>`: "Cell fracture selected mesh"
   (search "cell" will find the list item). This will pop up the add-ons menu's.
#. Then choose your settings (you can try small values first, large values may be slow).
   If you use the defaults and when the next layer checkbox is active,
   the fractured object will appear on the next layer to the active objects layer.


.. reference::

   :Category:  Object
   :Description: Tool for the fracturing of objects.
   :Location: :menuselection:`3D Viewport --> Object menu --> Quick Effects`
   :File: object_fracture_cell folder
   :Author: ideasman42, phymec, Sergey Sharybin
   :License: GPL
   :Note: This add-on is bundled with Blender.
