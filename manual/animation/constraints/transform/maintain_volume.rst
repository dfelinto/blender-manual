.. index:: Object Constraints; Maintain Volume Constraint
.. _bpy.types.MaintainVolumeConstraint:

**************************
Maintain Volume Constraint
**************************

The *Maintain Volume* constraint limits the volume of a mesh or
a bone to a given ratio of its original volume.

.. seealso::

   `Harkyman on the development of the Maintain Volume constraint
   <http://www.harkyman.com/2010/03/16/maintaining-bone-volume-a-new-constraint/>`__.


Options
=======

.. figure:: /images/animation_constraints_transform_maintain-volume_panel.png

   Maintain Volume Constraint.

Mode
   Specifies how the constraint handles scaling of the non-free axes.

   Strict
      This mode overrides non-free axis scaling to strictly maintain the specified volume.
      Only the ratio between the scale of the non-free axes is passed through.
   Uniform
      This mode maintains the volume as specified only when the pre-constraint scaling is uniform.
      Deviations from uniform scaling on non-free axes are passed through.
   Single Axis
      This mode maintains the volume only when the object is scaled just on its free axis.
      Any additional non-free axis scaling is passed through.

Free Axis
   The free-scaling axis of the object.

Volume
   The bone's rest volume.

Owner
   This constraint allows you to choose in which space to evaluate its owner's transform properties.
   See :ref:`common constraint properties <rigging-constraints-interface-common-space>` for more information.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Example
=======

.. vimeo:: 171275315
