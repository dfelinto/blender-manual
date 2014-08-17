
..    TODO/Review: {{review
   |text=
   This needs a complete rewrite,
   because we should not be using BA thread and video to exaplain something in the manual.
   It's ok as a extra but not at the main way to describe a feature.
   }} .


Pivot Constraint
****************

Description
===========

The :guilabel:`Pivot` constraint allows the owner to rotate around a target object.

It was originally intended for foot rigs.


Options
=======

.. figure:: /images/25-Manual-Constraints-Relationship-Pivot.jpg
   :width: 302px
   :figwidth: 302px

   Pivot panel


:guilabel:`Target`
   The object to be used as a pivot point

   :guilabel:`Bone`
      When :guilabel:`Target` is an armature, a new field for a bone is displayed.
   :guilabel:`Head/Tail`
      When using a bone target, you can choose where along this bone the target point lies.
   :guilabel:`Vertex Group`
      When :guilabel:`Target` is a mesh, a new field is display where a vertex group can be selected.

:guilabel:`Pivot Offset`
   Offset of pivot from target
:guilabel:`Pivot When`:
:guilabel:`Always`, :guilabel:`Z Rot`, :guilabel:`Y Rot`, ...


Example
=======

FIXME(Tag Unsupported:youtube;
<youtube>sncFstaycIo</youtube>
)


See also
********

- `Blender Artists Forum: Head-Tail pivot Constrain proposal (with Video and .blend) <http://blenderartists.org/forum/showthread.php?t=186169&page=1>`__, the thread where the constraint was first proposed


