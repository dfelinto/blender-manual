
Copy Transforms Constraint
**************************

Description
===========

The :guilabel:`Copy Transforms` constraint forces its owner to have the same transforms as its
target.


Options
=======

.. figure:: /images/25-Manual-Constraints-Transform-CopyTransforms.jpg
   :width: 304px
   :figwidth: 304px

   Copy Transforms panel


Target
   This constraint uses one target, and is not functional (red state) when it has none.

   Bone
      If :guilabel:`Target` is an :guilabel:`Armature`, a new field is displayed offering the optional choice to set an individual bone as :guilabel:`Target`.

      Head/Tail
         If a :guilabel:`Bone` is set as :guilabel:`Target`, a new field is displayed offering the optional choice of where along this bone the target point lies.
   Vertex Group
      If :guilabel:`Target` is a :guilabel:`Mesh`, a new field is displayed offering the optional choice to set a :guilabel:`Vertex Group` as target.
Space
   This constraint allows you to choose in which space to evaluate its owner's and target's transform properties.


