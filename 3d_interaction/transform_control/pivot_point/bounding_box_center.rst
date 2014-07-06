
Bounding Box Center as Pivot
****************************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object mode` and :guilabel:`Edit mode`
   | Menu:     Select from the following icon in the 3D window header

   .. figure:: /images/Icon-library_3D-Window_header-pivot-point.jpg
   | Hotkey:   :kbd:`,`


The bounding box is a rectangular box that is wrapped as tightly as possible around the
selection. It is oriented parallel to the world axes.
In this mode the pivot point lies at the center of the bounding box. You can set the pivot
point to bounding box with the :kbd:`,` hotkey or via the menu in the :guilabel:`Window
Header`. The image below shows how the Object's Bounding Box size is determined by the size
of the Object.

:doc:`Read more about selecting different pivot points » <3d_interaction/transform_control/pivot_point>`


.. figure:: /images/3D_interaction-Transform_Control-Pivot_Point-Bounding_Box_Center-bounding-box-demo.jpg

   Relationship between an Object and its Bounding Box.


In Object mode
==============

In :guilabel:`Object` mode, the bounding box is wrapped around the Object and transformation
takes place relative to the location of the Object center (indicated by the yellow circle).
The image below shows the results of using the Bounding Box as the pivot point in a number of
situations.

For example, images A (before rotation)
and B show rotation when the Object center is in its default position, while images C
(before rotation) and D shows the result when the Object center has been moved.
Image E shows that when multiple Objects are selected,
the pivot point is calculated based on the Bounding Box of all the selected Objects.


.. figure:: /images/3D_interaction-Transform_Control-Pivot_Point-Bounding_Box_Center-object-rotation.jpg

   The grid of four images on the left (ABCD) shows the results of Object rotation when the pivot point is set to Bounding Box. The image to the right (E) shows the location of the Bounding Box pivot point when multiple Objects are selected. The pivot point is shown by a yellow circle.


In Edit mode
============

This time it is the ObData that is enclosed in the bounding box.
The bounding box in :guilabel:`Edit mode` takes no account of the Object(s) centers,
only the center of the selected vertices.


.. figure:: /images/3D_interaction-Transform_Control-Pivot_Point-Bounding_Box_Center-edit-mode-rotation.jpg

   The effects of rotation in different mesh selection modes when the bounding box is set as the pivot point. The pivot point is shown by a yellow circle.


