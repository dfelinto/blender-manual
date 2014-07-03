
Copy Location Constraint
========================

Description
-----------

The :guilabel:`Copy Location` constraint forces its owner to have the same location as its
target.


 .. warning::

   FIXME - warning body below

 Note that if you use such a constraint on a *connected* bone, it will have no effect, as it is the parent's tip which controls the position of your owner bone's root.


Options
-------

.. figure:: /images/25-Manual-Constraints-Transform-CopyLoc.jpg
   :width: 307px
   :figwidth: 307px

   Copy Location panel


:guilabel:`Target`
   This constraint uses one target, and is not functional (red state) when it has none.
   :guilabel:`Bone`
      If :guilabel:`Target` is an :guilabel:`Armature`\ , a new field is displayed offering the optional choice to set an individual bone as :guilabel:`Target`\ .
      :guilabel:`Head/Tail`
         If a :guilabel:`Bone` is set as :guilabel:`Target`\ , a new field is displayed offering the optional choice of where along this bone the target point lies.
   :guilabel:`Vertex Group`
      If :guilabel:`Target` is a :guilabel:`Mesh`\ , a new field is displayed offering the optional choice to set a :guilabel:`Vertex Group` as target.

:guilabel:`X`\ , :guilabel:`Y`\ , :guilabel:`Z`
   These buttons control which axes (i.e. coordinates) are constrained - by default, all three ones are.
   :guilabel:`Invert`
      The :guilabel:`Invert` buttons invert their respective preceding coordinates.

:guilabel:`Offset`
   When enabled, this control allows the owner to be translated (using its current transform properties), relative to its target's position.

:guilabel:`Space`
   This constraint allows you to choose in which space to evaluate its owner's and target's transform properties.


