.. _tool-add-cube:

********
Add Cube
********

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode Edit Mode
   :Tool:      :menuselection:`Toolbar --> Add Cube`

Interactively add a :ref:`cube mesh object <bpy.ops.mesh.primitive_cube_add>`.


Usage
=====

The tool works by first defining the base of the object by
holding :kbd:`LMB` and dragging to define size of the base.
Next release the :kbd:`LMB` and drag to define the height of the object.
Finally, press :kbd:`LMB` again to confirm the shape of the object.

You can also use the hotkeys below to constrain the object.

.. list-table::
   :widths: 10 90

   * - :kbd:`Ctrl`
     - Toggles snapping on or off.
   * - :kbd:`Alt`
     - Toggles the *Origin* setting that is not the default.
   * - :kbd:`Shift`
     - Toggles the *Aspect* setting that is not the default.


Tool Settings
=============

Depth
   The initial depth used when placing the cursor.

   :Surface: Start placing on the surface, using the 3D cursor as a fallback.
   :Cursor Plane: Start placement using a point projected onto the orientation axis at the 3D cursor position.
   :Cursor View: Start placement using a point projected onto the view plane at the 3D cursor position.

Orientation
   The alignment of the cursor when placing objects; defines the orientation of the base.

   :Surface: Align the object using the surface orientation,
             using the :doc:`/editors/3dview/controls/orientation` as a fallback.
   :Default: Align the object using the default :doc:`/editors/3dview/controls/orientation`.

Snap to
   The target to use while :doc:`/editors/3dview/controls/snapping`.

   :Geometry: Snap to all types of geometry (vertices, edges, and faces).
   :Default: Snap to the snap target defined in the global :doc:`/editors/3dview/controls/snapping` controls.

Plane Axis
   The axis used for placing the base region.

   :X: Use the X axis to place the base region.
   :Y: Use the Y axis to place the base region.
   :Z: Use the Z axis to place the base region.

Auto Axis
   Select the closest axis when placing objects (surface overrides).

.. rubric:: Base

Origin
   The initial position of the base.

   :Edge: Places the object edge first and define the size of the base
          as the distance from the first edge to the adjacent edge.
   :Center: Places the object center first and define the size of the base
            as the distance from the base center to the perimeter.

Aspect
   The initial setting for the aspect of the object's base.

   :Free: Draws the length and width of the base using an unconstrained aspect.
   :Fixed: Draws the length and width of the base using a 1:1 aspect.

.. rubric:: Height

Origin
   The initial position of the height.

   :Edge: Places the object edge first and define the size of the height
          as the distance from the first edge to the adjacent edge.
   :Center: Places the object center first and define the size of the height
            as the distance from the base center to the perimeter.

Aspect
   The initial setting for the aspect of the object's height.

   :Free: Draws the length and width of the height using an unconstrained aspect.
   :Fixed: Draws the length and width of the height using a 1:1 aspect.
