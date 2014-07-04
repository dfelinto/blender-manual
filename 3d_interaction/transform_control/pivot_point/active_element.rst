
Active Element as Pivot
=======================

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object mode` and :guilabel:`Edit mode`
   | Menu:     Select from the following icon in the 3D window header

   .. figure:: /images/Icon-library_3D-Window_header-pivot-point.jpg
   | Hotkey:   :kbd:`alt-.`


The *active* element can be an Object, vertex, edge or a face. The active element is the
last one to be selected and will be shown in a lighter orange color when in :guilabel:`Object
mode` and white when in :guilabel:`Edit mode`.
With :guilabel:`Active element as Pivot` set to active,
all transformations will occur relative to the active element.

:doc:`Read more about selecting different pivot points » <3d_interaction/transform_control/pivot_point>`


.. figure:: /images/3D_interaction-Transform_control-Pivot_point-Active_element-selected-active-element.jpg
   :width: 640px
   :figwidth: 640px

   Display of active elements in Object mode is shown on the left of the image where the active element (cube) is a lighter orange. Active elements for vertices, edges and faces in Edit mode are displayed in white and are shown on the right.


In Object mode
--------------

When in :guilabel:`Object mode`,
rotation and scaling happen around the active Object's center.
This is shown by the figure to the below where the active Object (the cube)
remains in the same location (note its position relative to the 3D cursor)
while the other Objects rotate and scale in relation to the active element.


.. figure:: /images/3D_interaction-Transform_control-Pivot_point-Active_element-active-object-rotation.jpg
   :width: 640px
   :figwidth: 640px

   Rotation and scaling with the cube as the active element.


In Edit mode
------------

Using the active element as a pivot point in :guilabel:`Edit mode` may seem complex but all
the possible transformations follow a few rules:


- The pivot point is always at the median of the active element(s).
- The transformations occur by transformation of the **vertices** of the selected element(s). If an unselected element shares one or more vertices with a selected element then the unselected one will get some degree of transformation also.

Let's examine the following examples: in each case we will see that the two rules apply.


Single selection
~~~~~~~~~~~~~~~~

When one single element is selected it becomes automatically active. In the image below,
you can see that when it is transformed its vertices move, with the consequence that any
adjacent element which shares one or more vertices with the active element is also
transformed.


.. figure:: /images/3D_interaction-Transform_control-Pivot_point-Active_single-element-selection.jpg
   :width: 640px
   :figwidth: 640px

   Edit mode and only one element selected.


Let's review each case:

- *Faces* have their pivot point where their selection dot appears, which is where the median of their vertices is.
- *Edges* have their pivot point on their middle since this is always where the median of an edge is.
- :doc:`Fgons <modeling/meshes/mesh_structures#fgons>` behave the same as faces.
- A single *Vertex* has no dimensions at all so it can't show any transformation (except translation, which is not affected by the pivot point).


Multiple selection
~~~~~~~~~~~~~~~~~~

When multiple elements are selected they all transform.
The pivot points stay in the same place as what we've seen above,
with only one exception for Fgons. In the image below,
the selected elements have been rotated.


.. figure:: /images/3D_interaction-Transform_control-Pivot_point-Active_multiple-element-selection.jpg
   :width: 640px
   :figwidth: 640px

   Edit mode and multiple selections.


- For *Faces* the transformation occurs around the selection dot of the active face.
- *Edges* also keep the same behavior with their pivot point at their median.
- *Fgons* behave exactly like faces.
- There is a case for *Vertices* this time: the active Vertex is where the pivot point resides. All other vertices are transformed relative to it.


