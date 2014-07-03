


Bones
=====


.. figure:: /images/ManRiggingBonePrinciples3DViewEditModeOctahedron.jpg
   :width: 100px
   :figwidth: 100px

   The elements of a bone.


Bones are the base elements of armatures.

They have three elements:

- the "start point" named **root** or **head**\ ,
- the "body" itself,
- and the "end point" named **tip** or **tail**\ .

Select the :doc:`default armature <rigging/armatures/object_mode#your_first_armature>` and press :kbd:`tab` to enter :guilabel:`Edit mode`\ . As you can see, in this mode you can select the root and the tip, and move them as you do with mesh vertices (don't lose too much time here though, specific pages about selecting and editing will come later).

Both root and tip (the "ends") define the bone by their respective position.

They also have a radius property, only useful for the envelope deformation method (see below).


Bones Visualization
-------------------


Bones can be visualized in various ways: :guilabel:`Octahedron`\ , :guilabel:`Stick`\ ,
:guilabel:`B-Bone`\ , :guilabel:`Envelope` and :guilabel:`Wire`\ . Custom shapes can be used, too!


.. figure:: /images/Man2.5RiggingBonePrincipalsBoneDisplayOctahedral.jpg
   :width: 300px
   :figwidth: 300px

   Octahedral bone display.


.. figure:: /images/Man2.5RiggingBonePrincipalsBoneDisplayStick.jpg
   :width: 300px
   :figwidth: 300px

   Stick bone display.


.. figure:: /images/Man2.5RiggingBonePrincipalsBoneDisplayBBone.jpg
   :width: 300px
   :figwidth: 300px

   B-Bone bone display.


.. figure:: /images/Man2.5RiggingBonePrincipalsBoneDisplayEnvelope.jpg
   :width: 300px
   :figwidth: 300px

   Envelope bone display.


Since armatures are made of bones, you'll find more about this when we'll talk about :doc:`Armatures Visualization <rigging/armatures/visualization>`\ .

Activating :guilabel:`Axes` checkmark on the :guilabel:`Armature`\ /\ :guilabel:`Display` panel,
will show local axes for each bone's tip. The Y axis is always aligned along the bone,
oriented from root to tip. So, this is the "roll" axis of the bones.


.. figure:: /images/Man2.5RiggingBonePrincipalsBonePropertyWindow.jpg
   :width: 250px
   :figwidth: 250px

   The Bone context.


Bones properties
----------------


When bones are selected (hence in :guilabel:`Edit mode` and :guilabel:`Pose mode`\ ), their
properties are shown in the :guilabel:`Bone` button context of the :guilabel:`Properties`
window.

This shows different panels used to control features of each selected bone;
the panels change depending on which mode you're working in.


Bones Rigidity
--------------


Even though bones are rigid (i.e. behave as rigid sticks),
they are made out of :guilabel:`segments`\ . :guilabel:`Segments` are small,
rigid linked elements that can rotate between each other. By default,
each new bone has only one segment and as such it cannot "bend" along its length.
It is a rigid bone.

You can see these segments in :guilabel:`Object mode` and in :guilabel:`Pose mode`\ ,
and only if bones are visualized as :guilabel:`B-bones`\ ;
while in :guilabel:`Edit mode` bones are always drawn as rigid sticks.
Note that in the special case of a single bone,
you can't see these segments in :guilabel:`Object mode`\ , because they're aligned.


.. figure:: /images/ManRiggingBBoneEx3DViewEditMode.jpg
   :width: 300px
   :figwidth: 300px

   An armature of B-Bones, in Edit mode


.. figure:: /images/ManRiggingBBoneEx3DViewPrinciples.jpg
   :width: 300px
   :figwidth: 300px

   The Bézier curve superposed to the chain, with its handles placed at bones' ends.


.. figure:: /images/ManRiggingBBoneEx3DViewObjectMode.jpg
   :width: 300px
   :figwidth: 300px

   The same armature in Object mode


When you connect bones to form a :doc:`chain <rigging/armatures/structure#chains_of_bones>`\ , Blender calculates a Bezier curve passing through all the bones' ends, and bones' segments in the chain will bend and roll to follow this invisible curve.

*You have no direct access to this curve*\ ; you can only control it to some extent using bone properties, as explained in the :doc:`editing pages <rigging/armatures/editing/properties#bone_rigidity_settings>`\ .

In :guilabel:`An armature of B-Bones in Edit mode` we connected 3 bones,
each one made of 5 segments. These are :guilabel:`B-bones` but as you see,
in :guilabel:`Edit mode` they are shown as rigid elements.
Look at :guilabel:`The same armature in Object mode`\ : now, in :guilabel:`Object mode`\ ,
we can see how the bones' segments smoothly "blend" into each other, even for roll.

Of course,
a geometry influenced by the chain is smoothly deformed according to the Bezier curve!
In fact,
smooth bones are an easy way to replace long chains of many small rigid bones posed using IK...

However, if the chain has an influence on objects rather than geometry, the segments' orientation is not taken in account (details are explained in the :doc:`skinning part <rigging/skinning>`\ ).

When not visualized as :guilabel:`B-Bone`\ s, bones are always shown as rigid sticks, *even though the bone segments are still present and effective* (see :doc:`skinning to ObData <rigging/skinning/obdata>`\ ).

This means that even in e.g. :guilabel:`Octahedron` visualization,
if some bones in a chain have several segments,
they will nonetheless smoothly deform their geometry...


Bones influence
---------------


Basically, a bone controls a geometry when vertices "follow" the bone. This is like how the
muscles and skin of your finger follow your finger-bone when you move a finger.

To do this, you have to define **how much** a bone influences a certain vertex.

The simplest way is to have each bone affecting those parts of the geometry that are within a
given range from it. This is called the *envelope technique*\ ,
because each bone can control only the geometry "enveloped" by its own influence area.


.. figure:: /images/ManRiggingEnvelopePrinciples3DViewEditMode.jpg
   :width: 250px
   :figwidth: 250px

   A bone in Envelope visualization, in Edit mode.


If a bone is visualized as :guilabel:`Envelope`\ ,
in :guilabel:`Edit mode` and in :guilabel:`Pose mode` you can see the area of influence,
which depends on:

- the :guilabel:`distance` property
- the root's radius and the tip's radius.


.. figure:: /images/ManRiggingEnvelopeEx3DViewPoseMode.jpg
   :width: 300px
   :figwidth: 300px

   Our armature in Envelope visualization, in Pose mode.


All these influence parameters are further detailed in the :doc:`skinning pages <rigging/skinning>`\ .


