
Armature Modifier
*****************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Panel:    :guilabel:`Modifiers`


Description
===========

The :guilabel:`Armature` modifier is used for building skeletal systems for animating the
poses of characters and anything else which needs to be posed.
With the :guilabel:`Vertex Group` and :guilabel:`Multi Modifier` options,
you can use several armatures to animate a single (mesh) object.

By adding an armature system to an object,
that object can be deformed accurately so that geometry doesn't have to be animated by hand.
The :guilabel:`Armature` modifier allows objects to be deformed by bones simply by specifying
the name of the armature object, without having to use the (old) "parent/child" system.

For more details on armatures usage, see :doc:`this chapter </rigging>`.


Options
=======

.. figure:: /images/25-Manual-Modifiers-Armature.jpg

   Armature modifier


:guilabel:`Object`
   The name of the armature object used by this modifier.

   :guilabel:`Preserve Volume`
      Use quaternions for preserving volume of object during deformation. It can be better in many situations.
   :guilabel:`Vertex Group`
      The name of a vertex group of the object, the weights of which will be used to determine the influence of this :guilabel:`Armature` modifier's result when mixing it with the results from other :guilabel:`Armature` ones. Only meaningful when having at least two of these modifiers on the same object, with :guilabel:`Multi Modifier` activated.
   :guilabel:`Multi Modifier`
      Use the same data as a previous (:guilabel:`Armature` ?) modifier as input. This allows you to use several armatures to deform the same object, all based on the "non-deformed" data (i.e. this avoid having the second :guilabel:`Armature` modifier deform the result of the first one...). The results of the :guilabel:`Armature` modifiers are then mixed together, using the weights of the :guilabel:`VGroup` vertex groups as "mixing guides".

:guilabel:`Bind To`
   Method to bind the armature to the mesh.

   :guilabel:`Vertex Groups`
      Enable/Disable vertex groups defining the deformation (i.e. bones of a given name only deform vertices belonging to groups of same name).
   :guilabel:`Bone Envelopes`
      Enable/Disable bone envelopes defining the deformation (i.e. bones deform vertices in their neighborhood).
   :guilabel:`Invert`
      Inverts the influence set by the vertex group defined in previous setting (i.e. reverts the weight values of this group).


