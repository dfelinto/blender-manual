
..    TODO/Review: {{review
   |im= examples
   }} .


Spline IK Constraint
====================

The :guilabel:`Spline IK` constraint aligns a chain of bones along a curve. By leveraging the
ease and flexibility of achieving aesthetically pleasing shapes offered by curves and the
predictability and well-integrated control offered by bones,
:guilabel:`Spline IK` is an invaluable tool in the riggers' toolbox.
It is particularly well suited for rigging flexible body parts such as tails, tentacles,
and spines, as well as inorganic items such as ropes.

To set up :guilabel:`Spline IK`\ ,
it is necessary to have a chain of connected bones and a curve to constrain these bones to.

- With the last bone in the chain selected, add a :guilabel:`Spline IK` constraint from the :guilabel:`Bone Constraints` tab in the :guilabel:`Properties Editor`\ .
- Set the 'Chain Length' setting to the number of bones in the chain (starting from and including the selected bone) that should be influenced by the curve.
- Finally, set :guilabel:`Target` to the curve that should control the curve.


Options
-------

.. figure:: /images/25-Manual-Constraints-Tracking-SplineIK.jpg
   :width: 305px
   :figwidth: 305px

   Spline IK panel


:guilabel:`Target`
   The target curve
:guilabel:`Spline Fitting`\ :
   :guilabel:`Chain Length`
      How many bones are included in the chain
   :guilabel:`Even Division`
      Ignore the relative length of the bones when fitting to the curve
   :guilabel:`Chain Offset`
      Offset the entire chain relative to the root joint

:guilabel:`Chain Scaling`\ :
   :guilabel:`Y stretch`
      Stretch the Y axis of the bones to fit the curve
   :guilabel:`XZ Scale Mode`\ :
      :guilabel:`None`
         Don't scale the X and X axes (default)
      :guilabel:`Bone Original`
         Use the original scaling of the bones
      :guilabel:`Volume Preservation`
         Scale of the X and Z axes is the inverse of the Y scale
   :guilabel:`Use Curve Radius`
      Average radius of the endpoints is used to tweak the X and Z scaling of the bones, on top of the X and Z scale mode


See also
========

This subject is seen in depth in the :doc:`Rigging/Posing section <rigging/posing/inverse_kinematics/spline_ik>`\ .


- `Blender.org 2.56 Release Log for Spline IK <http://www.blender.org/development/release-logs/blender-256-beta/spline-ik/>`__


