
Mirror Modifier
***************

.. admonition:: Reference
   :class: refbox

   | Mode:     Any mode
   | Panel:    :guilabel:`Modifiers`


Description
===========

.. figure:: /images/25-Manual-Modifiers-Mirror-example-Cube.jpg
   :width: 350px
   :figwidth: 350px

   The corner of a cube mirrored across three axes to form ... well ... a cube.


The :guilabel:`Mirror` modifier automatically mirrors a mesh along its **local** X,
Y and/or Z axes, which pass through the object's center
(the mirror plane is then defined by the two other axes).
It can also use another object as mirror center,
then use that object's local axes instead of its own.
It can weld vertices together on the mirror plane within a specified *tolerance* distance.
Vertices from the original object can be prevented from moving across or through the mirror
plane. And last but not least, it can also mirror vertex groups and UV coordinates.


Options
=======

.. figure:: /images/25-Manual-Modifiers-Mirror.jpg

   Mirror modifier


:guilabel:`Axis`
   The axis (:guilabel:`X`, :guilabel:`Y`, or :guilabel:`Z`) along which to mirror (i.e. the axis perpendicular to the mirror plane of symmetry). To understand how the axis applies to the mirror direction, if you were to mirror on the X axis, the X plus values of the original mesh would become X minus values on the mirrored instance.
   You can select more than one of these axes - you'll then get more mirror instances, so that all planes of symmetry selected are "fully processed" (i.e. with one axis you get a single mirror, with two axes four mirrors, and with all three axes eight mirrors).

:guilabel:`Options`:
   :guilabel:`Merge`
      Merges vertices at the mirror plane.  See :guilabel:`Merge Limit` below.

   :guilabel:`Clipping`
      Prevents vertices from crossing through the mirror plane(s). Note that this is only valid in :guilabel:`Edit mode` (i.e when using object transformations, translations, scaling, et cetera, in :guilabel:`Object mode`, vertices will happily cross these borders.)
      If :guilabel:`Clipping` is selected but vertices are outside of the :guilabel:`Merge Limit` the vertices will not merge. As soon as the vertices are within :guilabel:`Merge Limit` they are clipped together and cannot be moved beyond the mirror plane. If several vertices are selected and are at different distances from the mirror plane, they will one by one be clipped at the mirror plane.
      Once you have confirmed clipped vertices with :kbd:`lmb` you must, if you want to break the clipping, un-select :guilabel:`Clipping` to be able to move vertices away from the mirror.

   :guilabel:`Vertex Groups`
      When this button is enabled, the :guilabel:`Mirror` modifier will try to mirror existing vertex groups. A very nice feature, but that has quite specific prerequisites.

   - First, the vertex groups you want to mirror must be named following the usual left/right pattern (i.e. suffixed by something like "\ ``.R`` ", "\ ``.right`` ", "\ ``.L`` ", et cetera).
   - Next, you must have the "mirrored" groups already existing (i.e. same names suffixed by the "other side") *and completely empty* (no vertex assigned to it), else it won't work.

     Usually, the mirrored copies of the vertices of a group remain in this group. Once this option is activated,
     all groups following the rules described above will only be valid on the original object - the mirrored copy
     will put these same vertices into the "mirror" group. Very handy with armatures, for example:
     you just model half of your object, carefully rig it with half of your armature,
     and just let the :guilabel:`Mirror` modifier build the other half.
     Just be sure to put your :guilabel:`Armature` modifier(s) after the :guilabel:`Mirror` one.

     A final word about multi-axes mirror: in these cases, the "direct", "first level" copies get the mirrored groups, the copies of copies ("second level") get the original groups, et cetera.

:guilabel:`Textures`
   The :guilabel:`U` and :guilabel:`V` options allows you to mirror, respectively, the U and V texture coordinates. The values are "mirrored" around the ``0.5`` value, i.e. if you have a vertex with UV coordinates of (``0.3``, ``0.85``), its mirror copy will have UV coordinates of (``0.7``, ``0.15``) with both buttons enabled.

:guilabel:`Merge Limit`
   The maximal distance between vertices and mirror plane for the welding between original and mirrored vertices to take place. The vertices then will snap together, allowing linking the original mesh to its mirrored copy.

:guilabel:`Mirror Object`
   The name of another object (usually an empty), to be used as the reference for the mirror process: its center and axes will drive the plane(s) of symmetry. You can of course animate its position/rotation (Ipo curves or others), to animate the mirror effect.


Hints
=====

Many modeling tasks involve creating objects that are symmetrical. However, there used to be
no quick way to model both halves of an object without using one of the workarounds that have
been discovered by clever Blender artists over the years.  A common technique is to model one
half of an object and use :kbd:`alt-D` to create a linked duplicate which can then be
mirrored on one axis to produce a perfect mirror-image copy,
which updates in real time as you edit.

The :guilabel:`Mirror` modifier offers another, simpler way to do this. Once your modeling is
completed you can either click :guilabel:`Apply` to make a real version of your mesh or leave
it as is for future editing.


Using Mirror modifier with {{Literal|Subdivision Surface}} modifier
-------------------------------------------------------------------

When using the :guilabel:`Mirror` modifier along with the :guilabel:`Subsurf` modifier,
the order in which the modifiers are placed is important.


.. figure:: /images/25-Manual-Modifiers-Mirror-Subsurf2.jpg
   :width: 300px
   :figwidth: 300px

   Subsurf modifier before Mirror modifier


This shows the :guilabel:`Subsurf` modifier placed before the :guilabel:`Mirror` one; as you
can see the effect of this is that the mesh splits down the center line of the mirror effect.


.. figure:: /images/25-Manual-Modifiers-Mirror-Subsurf1.jpg
   :width: 300px
   :figwidth: 300px

   Mirror modifier before Subsurf modifier


This shows the :guilabel:`Mirror` modifier placed before the :guilabel:`Subsurf` modifier.
In this order you will get the the center line of the mesh snapped to the center line,
which in most cases would be the desired effect.


Aligning for Mirror
-------------------

To apply a :guilabel:`Mirror` modifier, it is common to have to move the object's center onto
the edge or face that is to be the axis for mirroring.
This can be tricky when attempted visually. A good technique to achieve an exact position is
to determine the edge against which you wish to mirror. Select two vertices on that edge.
Then use :kbd:`shift-S` followed by :guilabel:`Cursor to Selection` (:kbd:`c`).
This will center the 3D cursor exactly on the edge midway between the two vertices. Finally,
press :kbd:`Ctrl-Alt-Shift-c` for the :guilabel:`Set Origin` popup,
then select :guilabel:`Origin to 3D Cursor` (:kbd:`t`).
This will move the object's center to where the 3D cursor is located,
and the mirroring will be exact.

An alternative is to use an Empty as a :guilabel:`Mirror Object` that you move to the correct
position.


