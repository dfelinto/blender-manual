.. _bpy.ops.mesh.poke:

**********
Poke Faces
**********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Faces --> Poke Faces`

Splits each selected faces into a triangle fan,
creating a new center vertex and triangles between the original face edges
and new center vertex. The *Offset* can be used to make spikes or depressions.

Poke Offset
   Offset the new center vertex along the face normal.
Offset Relative
   Multiply the Offset by the average length from the center to the face vertices.
Poke Center
   Computes the center of a face.

   :Weighted Mean: Using the mean average weighted by edge length.
   :Mean: Using the mean average.
   :Bounds: Uses center of bounding box.
