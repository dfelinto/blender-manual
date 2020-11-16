
*********
Relations
*********

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Panel:     :menuselection:`Bone --> Relations`

.. figure:: /images/animation_armatures_bones_properties_relations_panel.png

   Relations panel.

In this panel you can arrange sets of bones in different layers for easier manipulation.


Bone Layers
===========

Moving Bones between Layers
---------------------------

Obviously, you have to be in *Edit Mode* or *Pose Mode* to move bones between layers.
Note that as with objects, bones can lay in several layers at once,
just use the usual :kbd:`Shift-LMB` clicks...
First of all, you have to select the chosen bone(s)!

- In the Properties, use the "layer buttons" of each selected bone Relations panel (*Bones* tab)
  to control in which layer(s) it lays.
- In the *3D View* editor, use the menu :menuselection:`Armature --> Move Bone To Layer` or
  :menuselection:`Pose --> Move Bone To Layer` or press :kbd:`M` to show the usual pop-up layers menu.
  Note that this way, you assign the same layers to all selected bones.


.. _bone-relations-bone-group:

Bone Group
==========

.. admonition:: Reference
   :class: refbox

   :Mode:      Pose Mode

To assign a selected bone to a given bone group use the *Bone Group* data ID.


Object Children
===============

.. admonition:: Reference
   :class: refbox

   :Mode:      Pose Mode

Relative Parenting
   Changes how transformation of the bone is applied to its child Objects.


.. _bone-relations-parenting:

Parenting
=========

Parent
   A :ref:`ui-data-id` to select the bone to set as a parent.
Connected
   The *Connected* checkbox set the head of the bone to be connected with its parent root.


Transformations
---------------

Bones relationships have effects on transformations behavior.

By default, children bones inherit:

- Their parent position, with their own offset of course.
- Their parent rotation (i.e. they keep a constant rotation relatively to their parent).
- Their parent scale, here again with their own offset.

.. list-table:: Examples of transforming parented/connected bones.

   * - .. figure:: /images/animation_armatures_bones_properties_relations_rest.png
          :width: 200px

          The armature in its rest position.

     - .. figure:: /images/animation_armatures_bones_properties_relations_root-rotation.png
          :width: 200px

          Rotation of a root bone.

     - .. figure:: /images/animation_armatures_bones_properties_relations_root-scale.png
          :width: 200px

          Scaling of a root bone.

Exactly like standard children objects. You can modify this behavior on a per-bone basis,
using the Relations panel in the *Bones* tab:

.. _bone-relations-inherit-settings:

Local Location
   When disabled, the location transform property is evaluated in the parent bone's local space,
   rather than using the bone's own *rest pose* local space orientation.
Inherit Rotation
   When disabled, this will "break" the rotation relationship to the bone's parent.
   This means that the child will keep its rotation in the armature object space when its parent is rotated.
Inherit Scale
   Specifies which effects of parent scaling the bone inherits:

   Full
      The bone inherits all effects of parent scaling and shear.
   Fix Shear
      Full parent effects are applied to the rest state of the child, after which any shear is
      removed in a way that preserves the bone direction, length and volume, and minimally affects
      roll on average. The result is combined with the local transformation of the child.

      If the inherited scale is non-uniform, this does not prevent shear from reappearing due to
      local rotation of the child bone, or of its children.
   Aligned
      Parent scaling is inherited as if the child was oriented the same as the parent, always
      applying parent X scale over child X scale, and so on.
   Average
      Inherits a uniform scaling factor that is the total change in the volume of the parent.
   None
      Ignores all scaling and shear of the parent.
   None (Legacy)
      Ignores all scaling, provided the parent is not sheared. If it is, there are no guarantees.

      This choice replicates the behavior of the old Inherit Scale checkbox, and may be removed in a future release.

These inheriting behaviors propagate along the bones' hierarchy.
So when you scale down a bone, all its descendants are by default scaled down accordingly.
However, if you disable one bone's *Inherit Scale* or *Inherit Rotation*
property in this "family", this will break the scaling propagation,
i.e. this bone *and all its descendants* will no longer be affected when you scale one of its ancestors.

.. tip::

   The various *Inherit Scale* options are provided as tools in avoiding shear that is caused
   by non-uniform scaling combined with parenting and rotation. There is no obvious best way
   to achieve that, so different options are useful for different situations.

   None
      Useful for gaining full control over the scaling of the child in order
      to e.g. manually overwrite it with constraints.

   Average
      Useful to block squash and stretch propagation between sub-rigs, while
      allowing uniform changes in the size and volume to pass through.

   Aligned
      Can be used within bone chains, e.g. tentacles, in order to propagate
      lengthwise scaling as lengthwise, and sideways as sideways, no matter
      how the tentacle bends. Similar to using *None* with
      :doc:`Copy Scale </animation/constraints/transform/copy_scale>` from parent.

   Fix Shear
      May be useful at the base of an appendage in order to reallocate squash and stretch
      between axes based on the difference in rest pose orientations of the parent and child.
      It behaves closest to *Full* while suppressing shear.

.. list-table:: Examples of transforming parented/connected bones with Inherit Rotation disabled.

   * - .. figure:: /images/animation_armatures_bones_properties_relations_inherit-rot-disabled.png

          The yellow outlined Inherit Rotation disabled bone in the armature.

     - .. figure:: /images/animation_armatures_bones_properties_relations_inherit-rot-disabled-descendant.png

          Rotation of a bone with an Inherit Rotation disabled bone among its descendants.

     - .. figure:: /images/animation_armatures_bones_properties_relations_inherit-rot-disabled-scale.png

          Scaling of a bone with an Inherit Rotation disabled bone among its descendants.

Connected bones have another specificity: they cannot be moved. Indeed,
as their root must be at their parent's tip, if you do not move the parent,
you cannot move the child's root, but only its tip, which leads to a child rotation.
This is exactly what happens, when you press :kbd:`G` with a connected bone selected,
Blender automatically switches to rotation operation.

Bones relationships also have important consequences on how selections of multiple bones
behave when transformed. There are many different situations which may not be included on this list,
however, this should give a good idea of the problem:

- Non-related selected bones are transformed independently, as usual.
- When several bones of the same "family" are selected,
  *only* the "most parent" ones are really transformed --
  the descendants are just handled through the parent relationship process, as if they were not selected
  (see Fig. :ref:`fig-rig-pose-edit-scale` the third tip bone,
  outlined in yellow, was only scaled down through the parent relationship,
  exactly as the unselected ones, even though it is selected and active.
  Otherwise, it should have been twice smaller!)

  .. _fig-rig-pose-edit-scale:

  .. figure:: /images/animation_armatures_bones_properties_relations_scale-related.png
     :align: center
     :width: 320px

     Scaling bones, some of them related.

- When connected and unconnected bones are selected,
  and you start a move operation, only the unconnected bones are affected.
- When a child connected hinge bone is in the selection,
  and the "most parent" selected one is connected, when you press :kbd:`G`,
  nothing happens, because Blender remains in move operation, which of course has no effect on a connected bone.

So, when posing a chain of bones, you should always edit its elements from the root bone to the tip bone.
This process is known as :term:`Forward Kinematics` (FK).
We will see in a :ref:`later page <bone-constraints-inverse-kinematics>`
that Blender features another pose method, called :term:`Inverse Kinematics` (IK),
which allows you to pose a whole chain just by moving its tip.

.. note::

   This feature is somewhat extended/completed by
   the :doc:`pose library </animation/armatures/properties/pose_library>` tool.
