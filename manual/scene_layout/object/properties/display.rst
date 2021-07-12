
****************
Viewport Display
****************

.. reference::

   :Mode:      Object Mode
   :Panel:     :menuselection:`Properties --> Object Properties --> Viewport Display`

The *Viewport Display* panel is used to enable extra display options for the 3D Viewport.

.. figure:: /images/scene-layout_object_properties_display_panel.png

   Viewport Display panel.

.. _bpy.types.Object.show:

Show
   Name
      Displays the name of the object in the 3D Viewport.
   Axis
      Displays an object similar to an empty that shows the object's axis.
   Wireframe
      Displays an object's wireframe on top of the solid display.
   All Edges
      Displays all edges for mesh objects.
   Texture Space
      Displays the objects :term:`Texture Space`.
   Shadow
      Allows the object to cast shadows in the viewport.
   In Front
      Makes the object display in front of others. (Unsupported for instanced objects.)

.. _bpy.types.Object.display_type:

Display As
   The shading mode to display in the 3D Viewport; this can be useful if you have
   a high-poly object that is slowing down the viewport.

.. _bpy.types.Object.color:

Color
   Allows to specify the object's color when using the Workbench renderer.

.. _bpy.types.Object.show_bounds:
.. _bpy.types.Object.display_bounds_type:

Bounds
   Displays a bounding shape around an object.
   This can be helpful if you have high-poly objects that slow down the viewport.
   The shape of the object's bounds can be calculated with different primitive shapes
   that might be closer to what the original object looks like.
