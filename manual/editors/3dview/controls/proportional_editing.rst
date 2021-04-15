.. _bpy.types.ToolSettings.use_proportional_edit_objects:
.. _bpy.types.ToolSettings.use_proportional_edit:
.. |prop-edit-icon| image::
   /images/editors_3dview_object_editing_transform_control_proportional-edit_header.png

********************
Proportional Editing
********************

.. admonition:: Reference
   :class: refbox

   :Mode:      Object and Edit Mode
   :Header:    Via the |prop-edit-icon| icon in the header.
   :Shortcut:  :kbd:`O`

.. figure:: /images/editors_3dview_controls_proportional-editing_tool.png
   :align: right
   :width: 250px

   Proportional Editing popover.

Proportional Edit is a way of transforming selected elements (such as vertices)
while having that transformation affect other nearby elements. For example,
having the movement of a single vertex cause the movement of unselected vertices within a given range.
Unselected vertices that are closer to the selected vertex will move more than those farther from it
(i.e. they will move proportionally relative to the location of the selected element).
Since Proportional Editing affects the nearby geometry,
it is very useful when you need to smoothly deform the surface of a dense mesh.

.. note::

   Blender also has :ref:`painting-sculpting-index`
   that contains brushes and tools for proportionally editing a mesh without seeing the individual vertices.


Controls
========

Disable :kbd:`O`, :kbd:`Alt-O`
   Proportional Editing is off, only selected vertices will be affected.
Enable :kbd:`O`, :kbd:`Alt-O`
   Vertices other than the selected vertex are affected, within a defined radius.


Influence
---------

You can increase or decrease the radius of the tool's influence during a transform operation
with :kbd:`WheelUp`, :kbd:`WheelDown` or :kbd:`PageUp`, :kbd:`PageDown` respectively.
As you change the radius, the points surrounding your selection will adjust their positions accordingly.

.. figure:: /images/editors_3dview_controls_proportional-editing_influence.png
   :align: center

   Influence circle.


.. _bpy.types.ToolSettings.proportional_edit_falloff:
.. _3dview-transform-control-proportional-edit-falloff:

Falloff
-------

While editing, you can change the curve profile used by either
using the header icon *Falloff* menu, or by pressing :kbd:`Shift-O` to toggle between the various options.

.. list-table::

   * - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-constant.png

          Constant, No Falloff.

     - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-random.png

          Random Falloff.

     - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-linear.png

          Linear Falloff.

   * - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-sharp.png

          Sharp Falloff.

     - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-root.png

          Root Falloff.

     - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-sphere.png

          Sphere Falloff.

   * - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-smooth.png

          Smooth Falloff.

     - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-inverse-square.png

          Inverse Square Falloff.

     -


Object Mode
===========

Proportional Editing is typically used in *Edit Mode*, however, it can also be used in *Object Mode*.
In *Object Mode* the tool works on entire objects rather than individual mesh components.

In the image below, the right cylinder is scaled along the Z axis.
When the *Proportional Editing* is enabled, the adjacent cylinders are also within the tool's radius of influence.

.. figure:: /images/editors_3dview_controls_proportional-editing_object-mode.png
   :width: 50%
   :align: center

   Proportional Editing in Object Mode.


Edit Mode
=========

When working with dense geometry, it can become difficult to make subtle adjustments to
the vertices without causing visible lumps and creases in the model's surface.
When you face situations like this the Proportional Editing tool
can be used to smoothly deform the surface of the model.
This is done by the tool's automatic modification of unselected vertices within a given range.

.. figure:: /images/editors_3dview_controls_proportional-editing_mode.png
   :align: center

   Proportional Editing in Edit Mode.


Options
-------

.. _bpy.types.ToolSettings.use_proportional_connected:

Connected Only :kbd:`Alt-O`
   Rather than using a radius only, the proportional falloff spreads via connected geometry.
   This means that you can proportionally edit the vertices in a finger of a hand
   without affecting the other fingers. While the other vertices are physically close (in 3D space),
   they are far away following the topological edge connections of the mesh.
   The icon will have a blue center when *Connected* is active.
   This mode is only available in *Edit Mode*.

.. _bpy.types.ToolSettings.use_proportional_projected:

Projected from View
   Depth along the view is ignored when applying the radius.

   .. figure:: /images/editors_3dview_controls_proportional-editing_2d-compare.png

      The difference between regular and Projected (2D) proportional option (right).


Example
=======

The image below shows the final render of the low-poly landscape
obtained by moving up the vertices of the triangulated grid
with enabled *Proportional Editing*.

.. figure:: /images/editors_3dview_controls_proportional-editing_landscape.jpg

   A landscape obtained via Proportional Editing.
