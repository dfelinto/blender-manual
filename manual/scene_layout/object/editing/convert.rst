.. _object-convert-to:
.. _bpy.ops.object.convert:

*******
Convert
*******

Curve
=====

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Convert --> Curve`

Converts the selected mesh, or text object to a curve object.
For mesh objects, only edges belonging to no faces will be taken into account.
The resulting curve will be a poly curve type, but can be converted to have
smooth segments as described in :ref:`curve-convert-type`.


Mesh
====

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Convert --> Mesh`

Converts the selected curve, metaball, surface, or text object to a mesh object.
The actual defined resolution of these objects will be taken into account for the conversion.
Note that it also keeps the faces and volumes created by closed and extruded curves.


Grease Pencil
=============

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Convert --> Grease Pencil`

Converts the selected curve or mesh object to a Grease Pencil object
with strokes matching the curve/mesh; basic materials are also add.
When multiple curves/meshes are selected, they are all converted into
the same Grease Pencil object.


Options
-------

Keep Original
   Duplicates the original object before converting it.
Thickness
   Strokes thickness.
Threshold Angle
   Threshold value that determines the strokes end.
Stroke Offset
   Sets offset to separate strokes from filled strokes.
Only Seam Edges
   Convert only edges marked as seam.
Export Faces
   Convert faces as filled strokes.


Trace Image to Grease Pencil
============================

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Convert --> Trace Image to Grease Pencil`

See :doc:`/grease_pencil/modes/object/trace_image`.
