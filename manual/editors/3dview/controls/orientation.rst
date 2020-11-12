.. _bpy.types.TransformOrientation:
.. _bpy.types.SpaceView3D.transform_orientation:
.. TODO/Review: {{review|Need to change and explain the behavior of the transform orientation.
   It is toggled between the chosen orientation and
   the global orientation when transformations are made by shortcuts}}.

**********************
Transform Orientations
**********************

.. admonition:: Reference
   :class: refbox

   :Mode:      Object and Edit Modes
   :Panel:     :menuselection:`Header --> Transform Orientations`
   :Hotkey:    :kbd:`Comma`

*Transform Orientations* affect the behavior of
:doc:`Transformations </scene_layout/object/editing/transform/index>`.
You will see an effect on the :doc:`Object Gizmo </editors/3dview/display/gizmo>`
(the widget in the center of the selection), as well as on transformation constraints,
:doc:`Axis Locking </scene_layout/object/editing/transform/control/axis_locking>`.

For example, when you press :kbd:`X`, during the execution of the operation,
it will constrain the transformation to the *Global* X axis.
But if you press :kbd:`X` a second time it will constrain to your *Transform Orientation*\ 's X axis.

.. figure:: /images/editors_3dview_controls_orientation_menu.png

   Transform Orientations selector.

The Orientations options can be set through the *Transform Orientation* selector in a 3D Viewport header.

In addition to the five preset options,
you can define your own custom orientation (see `Custom Orientations`_ below).


Orientations
============

Global
   Align the transformation axes to world space.

   The :ref:`Navigation Gizmo <navigation-gizmo>` in the top right corner of the viewport,
   and the *Grid Floor*, shows the axes of world coordinate system.

Local
   Align the transformation axes to the selected objects' space.

   When an object is rotated, the direction of the *Local* gizmo
   matches to the object's rotation relative to the global axes.
   While the *Global* gizmo always correspond to world coordinates.

Normal
   Align the transformation axes so that the Z axis of the gizmo will match the average
   :doc:`Normal </modeling/meshes/editing/mesh/normals>` of the selected element.
   If multiple elements are selected, it will orient towards the average of those normals.

   In *Object Mode*, this is equivalent to *Local* orientation.

Gimbal
   Align each axis to the Euler rotation axis as used for input.
   Uses a :term:`Gimbal` behavior that can be changed
   depending on the current :ref:`Rotation Mode <rotation-modes>`.

View
   Align the transformation axes to the window of the 3D Viewport:

   - Y: Up/Down
   - X: Left/Right
   - Z: Towards/Away from the screen

Cursor
   Align the transformation axes to the 3D cursor.


Examples
--------

.. list-table:: Cube with the rotation gizmo active in multiple transform orientations.

   * - .. figure:: /images/editors_3dview_controls_orientation_manipulator-global-1.png

          Default cube with Global transform orientation selected.

     - .. figure:: /images/editors_3dview_controls_orientation_manipulator-global-2.png

          Rotated cube with Global orientation, gizmo has not changed.

     - .. figure:: /images/editors_3dview_controls_orientation_manipulator-local.png

          Local orientation, gizmo matches to the object's rotation.

   * - .. figure:: /images/editors_3dview_controls_orientation_manipulator-normal.png

          Normal orientation, in Edit Mode.

     - .. figure:: /images/editors_3dview_controls_orientation_manipulator-gimbal.png

          Gimbal transform orientation.

     - .. figure:: /images/editors_3dview_controls_orientation_manipulator-view.png

          View transform orientation.


Custom Orientations
-------------------

.. admonition:: Reference
   :class: refbox

   :Mode:      Object and Edit Modes
   :Panel:     :menuselection:`Header --> Transform Orientations`

You can define custom transform orientations, using object or mesh elements.
Custom transform orientations defined from objects use the *Local* orientation of the object
whereas those defined from selected mesh elements (vertices, edges, faces)
use the *Normal* orientation of the selection.

.. figure:: /images/editors_3dview_controls_orientation_custom.png

   Transform Orientations panel.

The *Transform Orientations* panel, found in the header of the 3D Viewport,
can be used to manage transform orientations: selecting the active orientation,
adding ("+" icon), deleting ("X" icon) and rename custom orientations.

The default name for these orientations is derived from what you have selected.
If it's an edge, it will be titled, "Edge", if it's an object,
it will take that object's name, etc.


Create Orientation
^^^^^^^^^^^^^^^^^^

To create a custom orientation, select the object or mesh element(s) and
click the "+" button on the *Transform Orientations* panel.

.. figure:: /images/editors_3dview_controls_orientation_custom-name.png

   Create Orientation :ref:`ui-undo-redo-adjust-last-operation` panel.

Just after creating the orientation,
the *Create Orientation* :ref:`ui-undo-redo-adjust-last-operation` panel gives a few options:

Name
   Text field for naming the new orientation.
Use View
   The new orientation will be aligned to the view space.
Use After Creation
   If checked it leaves the newly created orientation active.
Overwrite Previous
   If the new orientation is given an existing name, a suffix will be added to it to avoid overwriting the old one,
   unless *Overwrite Previous* is checked, in which case it will be overwritten.
