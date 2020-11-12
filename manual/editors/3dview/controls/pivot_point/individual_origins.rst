.. |pivot-icon| image:: /images/editors_3dview_controls_pivot-point_menu.png

******************
Individual Origins
******************

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode and Edit Mode
   :Header:    |pivot-icon| :menuselection:`Pivot Point --> Individual Origins`
   :Hotkey:    :kbd:`Period`


In Object Mode
==============

The origin of an object is shown in the 3D Viewport by a small orange circle.
It tells Blender the relative position of that object in 3D space.

The origin does not have to be located in the center of the geometry (e.g. mesh).
This means that an object can have its origin located on one end of the mesh or
even completely outside the mesh.

.. figure:: /images/editors_3dview_controls_pivot-point_individual-origins_rotation-around-center.png
   :align: center

   Rotation around individual origins.

For example, the orange rectangle in the image above has its origin located on the far left of the mesh,
while the blue rectangle has its origin located in the center of the mesh.

When the Pivot Point is set to *Individual Origins*,
the origin of each object remains in place while the object rotates or scales around it.

.. figure:: /images/editors_3dview_controls_pivot-point_individual-origins_objects-rotate.png
   :align: center

   Rotation around Individual Origins (middle) compared to the Median Point (right).

.. figure:: /images/editors_3dview_controls_pivot-point_individual-origins_objects-scale.png
   :align: center

   Scaling around Individual Origins (middle) compared to the Median Point (right).


In Edit Mode
============

.. figure:: /images/editors_3dview_controls_pivot-point_individual-origins_rotation-faces.png
   :align: center

   Rotation of individual faces around Individual Origins (middle) and the Median Point (right).

.. figure:: /images/editors_3dview_controls_pivot-point_individual-origins_scale-individual-faces.png
   :align: center

   Scaling with non-touching faces around Individual Origins (middle) and the Median Point (right).

When you rotate or scale the touching faces/edges,
they are treated as a single element, and keep the shape of the group.
Each group is transformed independently around its median point.
