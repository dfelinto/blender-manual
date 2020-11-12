.. |pivot-icon| image:: /images/editors_3dview_controls_pivot-point_menu.png

**************
Active Element
**************

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode and Edit Mode
   :Header:    |pivot-icon| :menuselection:`Pivot Point --> Active Element`
   :Hotkey:    :kbd:`Alt-Period`

The *active element* can be an object, vertex, edge or a face.
The active element is the last one to be selected and
will be shown in a lighter orange color when in *Object Mode* and white when in *Edit Mode*.
With *Active Element* as *Pivot* set to active, all transformations will occur relative to the active element.

.. figure:: /images/editors_3dview_controls_pivot-point_active-element_object-mode-display.png
   :align: center

   Display of active elements in Object Mode where the active element (cube) is a lighter orange.

.. figure:: /images/editors_3dview_controls_pivot-point_active-element_edit-mode-display.png
   :align: center

   Active elements for vertices, edges and faces in Edit Mode are displayed in white.


In Object Mode
==============

When in *Object Mode*,
rotation and scaling happen around the origin of the active object.
This is shown by the figure to the below where the active object (the cube)
remains in the same location (note its position relative to the background grid)
while the other objects rotate and scale in relation to the active element.

.. figure:: /images/editors_3dview_controls_pivot-point_active-element_object-mode-rotation.png
   :align: center

   Rotation and scaling with the cube as the active element.


In Edit Mode
============

Using the active element as a pivot point in *Edit Mode* may seem complex but all
the possible transformations follow a few rules:

- The pivot point is always at the median of the active element.
- The transformations occur by transformation of the *vertices* of the selected element(s).
  If an unselected element shares one or more vertices with a selected element
  then the unselected one will get some degree of transformation also.

Let us examine the following examples: in each case we will see that the two rules apply.


Single Selection
----------------

When one single element is selected it becomes automatically active. In the image below,
you can see that when it is transformed its vertices move, with the consequence that
any adjacent element which shares one or more vertices with the active element is also transformed.

.. figure:: /images/editors_3dview_controls_pivot-point_active-element_edit-mode-single.png
   :align: center

   Edit Mode and only one element selected.

Let us review each case:

- *Faces* have their pivot point where the median of their vertices is.
- *Edges* have their pivot point on their middle since this is always where the median of an edge is.
- A single *vertex* has no dimensions at all so it cannot show any transformation
  (except translation, which is not affected by the pivot point).


Multiple Selection
------------------

When multiple elements are selected they all transform.
The pivot points stay in the same place as what we have described above.
In the image below, the selected elements have been rotated.

.. figure:: /images/editors_3dview_controls_pivot-point_active-element_edit-mode-multiple.png
   :align: center

   Edit Mode and multiple selections.

- For *faces* the transformation occurs around the median of the vertices of the selected face.
- *Edges* also keep the same behavior with their pivot point at their median.
- There is a case for *vertices* this time: the active vertex is where the pivot point resides.
  All other vertices are transformed relative to it.
