.. |pivot-icon| image:: /images/editors_3dview_controls_pivot-point_menu.png

*******************
Bounding Box Center
*******************

.. reference::

   :Mode:      Object Mode and Edit Mode
   :Header:    |pivot-icon| :menuselection:`Pivot Point --> Bounding Box Center`
   :Shortcut:  :kbd:`Period`

The bounding box is a rectangular box that is wrapped as tightly as possible around the selection.
It is oriented parallel to the world axes. In this mode the pivot point lies at the center of the bounding box.
You can set the pivot point to *Bounding Box* with :kbd:`Comma` or via the menu in the editor's header.
The image below shows how the object's bounding box size is determined by the size of the object.

.. figure:: /images/editors_3dview_controls_pivot-point_bounding-box-center_demo.png
   :align: center

   Relationship between an object and its bounding box.


In Object Mode
==============

In *Object Mode*, transformation takes place relative to the location of the objects origin
(indicated by the yellow circle), and the size of objects is not taken into account.
The image below shows the results of using the *Bounding Box* as the pivot point in some situations.

.. figure:: /images/editors_3dview_controls_pivot-point_individual-origins_rotation-around-center.png
   :align: center

   Single object rotation.

In this example, the orange rectangle has its origin located on the far left of the mesh,
while the blue rectangle has its origin located in the center of the mesh.

When a single object is selected, the rotation takes place around its origin.

.. figure:: /images/editors_3dview_controls_pivot-point_bounding-box-center_object-mode.png
   :align: center

   Shows the location of the bounding box (right) pivot point compared to the median point (left).

The image above (left) shows that when multiple objects are selected,
the pivot point is calculated based on the location of all the selected objects.
More precisely, the centers of objects are taken into account.


In Edit Mode
============

This time it is the geometry that is enclosed in the bounding box.
The bounding box in *Edit Mode* takes no account of the object(s) origins,
only the center of the selected vertices.

.. figure:: /images/editors_3dview_controls_pivot-point_bounding-box-center_edit-mode-rotation.png
   :align: center

   The effects of rotation in different mesh selection modes when the bounding box is set as the pivot point.
   The pivot point is shown by a yellow circle.

.. figure:: /images/editors_3dview_controls_pivot-point_bounding-box-center_median-point.png
   :align: center

   The bounding box center compared to the median point.
