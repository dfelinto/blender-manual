
Copy Transforms Constraint
==========================

Description
-----------

The :guilabel:`Copy Transforms` constraint forces its owner to have the same transforms as its
target.


Options
-------

.. figure:: /images/25-Manual-Constraints-Transform-CopyTransforms.jpg
   :width: 304px
   :figwidth: 304px

   Copy Transforms panel


:guilabel:`Target`
   This constraint uses one target, and is not functional (red state) when it has none.

   :guilabel:`Bone`
      If :guilabel:`Target` is an :guilabel:`Armature`, a new field is displayed offering the optional choice to set an individual bone as :guilabel:`Target`.

      :guilabel:`Head/Tail`
         If a :guilabel:`Bone` is set as :guilabel:`Target`, a new field is displayed offering the optional choice of where along this bone the target point lies.
   :guilabel:`Vertex Group`
      If :guilabel:`Target` is a :guilabel:`Mesh`, a new field is displayed offering the optional choice to set a :guilabel:`Vertex Group` as target.
:guilabel:`Space`
   This constraint allows you to choose in which space to evaluate its owner's and target's transform properties.


