
Copy Rotation Constraint
========================

The :guilabel:`Copy Rotation` constraint forces its owner to match the rotation of its target.


Options
-------


.. figure:: /images/25-Manual-Constraints-Transform-CopyRot.jpg
   :width: 307px
   :figwidth: 307px

   Copy Rotation panel


:guilabel:`Target`
   This constraint uses one target, and is not functional (red state) when it has none.
   :guilabel:`Bone`
      If :guilabel:`Target` is an :guilabel:`Armature`\ , a new field is displayed offering the optional choice to set an individual bone as :guilabel:`Target`\ .
      :guilabel:`Head/Tail`
         If a :guilabel:`Bone` is set as :guilabel:`Target`\ , a new field is displayed offering the optional choice of where along this bone the target point lies.
   :guilabel:`Vertex Group`
      If :guilabel:`Target` is a :guilabel:`Mesh`\ , a new field is displayed offering the optional choice to set a :guilabel:`Vertex Group` as target.

:guilabel:`X`\ , :guilabel:`Y`\ , :guilabel:`Z`
   These buttons control which axes are constrained - by default, all three are on.
   :guilabel:`Invert`
      The :guilabel:`Invert` buttons invert their respective rotation values.

:guilabel:`Offset`
   When enabled, this control allows the owner to be rotated (using its current transform properties), relative to its target's orientation.

:guilabel:`Space`
   This constraint allows you to choose in which space to evaluate its owner's and target's transform properties.


