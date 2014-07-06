
Armature Structure
******************

.. figure:: /images/Manual-Part-I-Quick51.jpg
   :width: 250px
   :figwidth: 250px

   The very basic armature of the :doc:`Gingerbread Man tutorial <your_first_animation/2.animating_the_gingerbread_man>`.


Armatures mimic real skeletons. They are made out of bones, which are (by default) rigid elements. But you have more possibilities than with real skeletons: In addition to the "natural" rotation of bones, you can also translate and even scale them! And your bones do not have to be connected to each other; they can be completely free if you want. However, the most natural and useful setups imply that some bones are related to others, forming so-called "chains of bones", which create some sort of "limbs" in your armature, as detailed
FIXME(TODO: Internal Link;
[[#Chains of Bones|below]]
).


Chains of Bones
===============

.. figure:: /images/ManRiggingChainEx3DViewEditMode.jpg
   :width: 250px
   :figwidth: 250px

   An armature with two chains of bones.


The bones inside an armature can be completely independent from each other (i.e.
the modification of one bone does not affect the others).
But this is not often a useful set up: To create a leg,
all bones "after" the thigh bone should move "with" it in a well-coordinated manner.
This is exactly what happens in armatures - by parenting a bone to the next one in the limb,
you create a "chains of bones". These chains can be ramified. For example,
five fingers attached to a single "hand" bone.

Bones are chained by linking the tip of the parent to the root of the child.
Root and tip can be *connected*, i.e. they are always exactly at the same point;
or they can be *free*, like in a standard parent-child object relationship.

A given bone can be the parent of several children,
and hence be part of several chains at the same time.

The bone at the beginning of a chain is called its *root bone*,
and the last bone of a chain is the *tip bone*
(don't confuse them with similar names of bones' ends!).

Chains of bones are a particularly important topic in :doc:`posing <rigging/posing>` (especially with the standard *forward kinematics* versus "automatic" *inverse kinematics* posing techniques). You create/edit them in :guilabel:`Edit` mode, but except in case of connected bones, their relationships have no effect on bone transformations in this mode (i.e. transforming a parent bone won't affect its children).


Editing Bones Relationships
---------------------------

This is detailed in the :doc:`editing pages <rigging/armatures/editing/properties#chain_editing>`, but let us have a quick look at this important feature.


.. figure:: /images/Man2.5RiggingEditingBoneCxtRelationsPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Armature Bones panel with two bones selected, and their Child of settings highlighted.


The easiest way to manage bones relationships is to use the :guilabel:`Relations` panel
:guilabel:`Bone` context:

- First, :doc:`select <rigging/armatures/selecting>` the bones you want to edit (selection order does not matter here).
- To *parent* a bone to another one, select the name of this parent in its drop-down :guilabel:`Parent` list.
- To *unparent* a bone, just select the void entry in the same :guilabel:`Parent` list.
- To *connect* a bone to its parent, enable its small :guilabel:`Con` button.
- To *unconnect* a bone, disable its :guilabel:`Con` button.


