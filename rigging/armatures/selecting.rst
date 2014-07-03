


Selecting armature's bones
==========================


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit mode`
   | Panel:    :menuselection:`Bone` panel


You can select and edit bones of armatures in :guilabel:`Edit mode` and in :guilabel:`Pose mode`\ . Here, we will see how to select bones in :guilabel:`Edit mode`\ . Selecting bones in :guilabel:`Pose mode` is similar to selecting in :guilabel:`Edit mode` with a few specific differences that will be detailed in the :doc:`posing part <rigging/posing/editing>`\ .

Similar to :doc:`vertices/edges selection <modeling/meshes/selecting>` in meshes, there are two ways to select whole bones in :guilabel:`Edit mode`\ :

- directly, by selecting the bone's body
- selecting both of its end points (root and tip)

This is an important point to understand,
because selecting bones' ends only might lead to non-obvious behavior,
with respect to which bone you actually select, see the .

Note that unlike the mesh draw type the armature draw type has no effect on selection
behavior. In other words,
you can select a bone's end or body the same way regardless of the bone visualization chosen.


Selecting bones' ends
---------------------


To select bones' ends you have the standard selection methods.

+----------------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+-----+
+action                                  |shortcut                                                                                         |menu                                           |mouse+
+----------------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+-----+
+Select a bone's end                     |:kbd:`rmb`\ -click on it                                                                                                                               +
+----------------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+-----+
+Add or Remove from the current selection|:kbd:`shift-rmb`                                                                                                                                       +
+----------------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+-----+
+(De)select the ends of all bones        |:kbd:`A`                                                                                         |:menuselection:`Select --> Select/Deselect All`      +
+----------------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+-----+
+Invert the current selection            |:kbd:`ctrl-I`                                                                                    |:menuselection:`Select --> Inverse`                  +
+----------------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+-----+
+Box selection tool ON                   |:kbd:`B`                                                                                         |:menuselection:`Select --> Border Select`            +
+----------------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+-----+
+Box selection                           |click and drag :kbd:`lmb` the box around the ends you want to add to the current selection                                                             +
+                                        |click and drag :kbd:`lmb` to remove from the current selection                                                                                         +
+                                        |release :kbd:`lmb` to validate                                                                                                                         +
+                                        |hit :kbd:`Esc` or click :kbd:`rmb` to cancel                                                                                                           +
+----------------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+-----+
+Box selection tool OFF                  |:kbd:`B` or :kbd:`esc`                                                                           |:kbd:`rmb`                                           +
+----------------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+-----+
+Lasso selection                         |click and drag :kbd:`ctrl-lmb` the lasso around the ends you want to add to the current selection                                                      +
+                                        |click and drag :kbd:`ctrl-shift-lmb` to remove from the current selection                                                                              +
+                                        |release :kbd:`lmb` to validate                                                                                                                         +
+                                        |hit :kbd:`Esc` or click :kbd:`rmb` to cancel                                                                                                           +
+----------------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+-----+


Inverse selection
~~~~~~~~~~~~~~~~~


As stated above, you have to remember that these selection tools are for bones' ends only,
not the bones' bodies.

For example, the :guilabel:`Inverse` selection option (\ :kbd:`ctrl-I`\ )
inverts the selection of bones' ends, not of bones (see *Inverse selection*\ ).

Remember that a bone is selected only if both its ends are selected. So,
when the selection status of bones' ends is inverted, a new set of bones is selected.


+-------------------+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
+*Inverse selection*|.. figure:: /images/ManRiggingBoneSelectExEditModeTwoBones.jpg|.. figure:: /images/ManRiggingBoneSelectExEditModeThreeBoneEnds.jpg                                                          +
+                   |   :width: 300px                                              |   :width: 300px                                                                                                             +
+                   |   :figwidth: 300px                                           |   :figwidth: 300px                                                                                                          +
+                   |                                                              |                                                                                                                             +
+                   |   Two bones selected.                                        |   The result of the inverse selection ([ctrl][I]): the bones' ends selection has been inverted, and not the bones selection…+
+-------------------+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+


Selecting connected bones' ends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Another example is: when you select the root of a bone connected to its parent,
you also implicitly select the tip of its parent (and vice versa).

Remember: when selecting bones' ends,
the tip of the parent bone is the "same thing" as the root of its children bones.


Selecting Bones
---------------


By :kbd:`rmb`\ -clicking on a bone's body, you will select it
(and hence you will implicitly select its root and tip).

To each selected bone corresponds a sub-panel in the :guilabel:`Armature Bones` panel
(\ :guilabel:`Editing` context, :kbd:`F9`\ ).
These sub-panels contain settings for some of the bones' properties (regarding e.g.
relationships between bones, bones' influence on deformed geometry, etc.),
as we will see later.

Using :kbd:`shift-rmb`\ , you can add to/remove from the selection.

You also have some **advanced selection** options, based on their relations.

You can select at once all the bones in the chain which the active (last selected)
bone belongs to by using the *linked selection* tool, :kbd:`L`\ .


+------------------------+---------------------------------------------------------------+----------------------------------------------------------------+
+*Linked bones selection*|.. figure:: /images/ManRiggingBoneSelectExEditModeWholeBone.jpg|.. figure:: /images/ManRiggingBoneSelectExEditModeWholeChain.jpg+
+                        |   :width: 300px                                               |   :width: 300px                                                +
+                        |   :figwidth: 300px                                            |   :figwidth: 300px                                             +
+                        |                                                               |                                                                +
+                        |   A single selected bone.                                     |   Its whole chain selected with [L].                           +
+------------------------+---------------------------------------------------------------+----------------------------------------------------------------+


You can deselect the active bone and select its immediate parent or one of its children using
respectively :menuselection:`Select --> Select Parent` (\ :kbd:`[`\ ) or :menuselection:`Select --> Select Child`
(\ :kbd:`]`\ ). If you prefer to keep the active bone in the selection,
use :menuselection:`Select --> Extend Select Parent` (\ :kbd:`ctrl-[`\ )
or :menuselection:`Select --> Extend Select Child` (\ :kbd:`ctrl-]`\ ).


Deselecting connected bones
~~~~~~~~~~~~~~~~~~~~~~~~~~~


There is a subtlety regarding connected bones.

When you have several connected bones selected, if you deselect one bone,
*you will in fact deselect its tip,
but not its root if it is also the tip of another selected bone.*

To understand this, look at *Bone deselection in a selected chain*\ .


+--------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+
+*Bone deselection in a selected chain*|.. figure:: /images/ManRiggingBoneSelectExEditModeWholeChain.jpg|.. figure:: /images/ManRiggingBoneSelectExEditModeTwoBones.jpg+
+                                      |   :width: 300px                                                |   :width: 300px                                              +
+                                      |   :figwidth: 300px                                             |   :figwidth: 300px                                           +
+                                      |                                                                |                                                              +
+                                      |   A selected chain.                                            |   After [shift][rmb]-clicking Bone.003                       +
+--------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+


After :kbd:`shift-rmb`\ -clicking ``Bone.003``\ :

- ``Bone.003``\ 's tip (which is same as ``Bone.004``\ 's root) is deselected
-  ``Bone`` is ``Bone.003``\ 's parent. Therefore ``Bone.003``\ 's root is same as the tip of ``Bone``\ . Since ``Bone`` is still selected, its tip is selected. Thus the root of  ``Bone.003`` remains selected.


