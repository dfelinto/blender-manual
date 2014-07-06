
3D Cursor as Pivot
******************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object mode` and :guilabel:`Edit mode`
   | Hotkey:   :kbd:`.`


The 3D cursor is the most intuitive of the pivot points.
With the 3D cursor selected as the active pivot point
(from either the :guilabel:`Window Header` or via the :kbd:`.` hotkey),
simply position the 3D cursor and then do the required transformation. All rotation and
scaling transformations will now be done relative to the location of the 3D cursor.
The image below shows the difference when rotating an Object from its starting position
(first panel) 90 degrees around the median point (second panel)
and 90 degrees around the 3D cursor (third panel).

:doc:`Read more about selecting different pivot points » <3d_interaction/transform_control/pivot_point>`


.. figure:: /images/3D_interaction_Transform-Control_Pivot-Point_3D-cursor_median-cursor-example.jpg
   :width: 640px
   :figwidth: 640px

   Rotation around the 3D cursor compared to the median point.


Positioning the 3D cursor
=========================

There are a few methods to position the 3D cursor.


Direct placement with the mouse
-------------------------------

.. figure:: /images/3D_interaction_Transform-Control_Pivot-Point_3D-cursor_two-view-positioning.jpg
   :width: 300px
   :figwidth: 300px

   Positioning the 3D cursor with two orthogonal views.


- Using :kbd:`lmb` in the 3D area will place the 3D cursor directly under your mouse pointer. For accuracy you should use two perpendicular orthogonal 3D views, i.e. any combination of top (:kbd:`pad7`), front (:kbd:`pad1`) and side (:kbd:`pad3`). That way you can control the positioning along two axes in one view and determine depth in the second view.


Using the Snap Menu
-------------------

.. figure:: /images/3D_interaction_Transform-Control_Pivot-Point_3D-cursor_snap-menu.jpg

   The Snap menu.


The :guilabel:`Snap` menu (:kbd:`Shift-S` or :menuselection:`Object/Mesh --> Snap`)
will allow you to snap the cursor in the following ways:


- :guilabel:`Cursor to Selected`: snaps the cursor to the currently selected vertex, edge or face. In :guilabel:`Object` mode this option will snap the cursor to the center of the currently selected Object.
- :guilabel:`Cursor to Center`: snaps the cursor to the origin point of the grid (location 0,0).
- :guilabel:`Cursor to Grid`: snaps the cursor to the nearest **visible** part of the grid.
- :guilabel:`Cursor to Active`: snaps the cursor to the *active* (last selected) object, edge, face or vertex.

The :guilabel:`Cursor to Selected` option is also affected by the number of elements in the
selection and the current pivot point.  For example,
with several elements selected and the :guilabel:`Bounding Box Center` pivot point active,
the :guilabel:`Cursor to Selected` option will snap the 3D cursor to the:


- **Center of the bounding box** surrounding the objects' centers in :guilabel:`Object` mode or the **center of the bounding box** surrounding the selected vertices when in :guilabel:`Edit` mode.

When the :guilabel:`Median Point` pivot point is selected,
:guilabel:`Cursor to Selected` will snap the 3D cursor to:

- The median of the object centers in :guilabel:`Object` mode and the median of the selected vertices in :guilabel:`Edit` mode.


Numeric input
-------------

.. figure:: /images/3D_interaction_Transform-Control_Pivot-Point_3D-cursor_view-properties.jpg
   :width: 285px
   :figwidth: 285px

   The 3D Cursor panel of the Properties shelf.


The 3D cursor can also be positioned by entering Numeric location values into the :guilabel:`3D
cursor` panel of the :guilabel:`Properties` shelf (:kbd:`N`).


