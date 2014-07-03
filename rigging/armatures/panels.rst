


Armature Panels Overview
========================


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object mode`\ , :guilabel:`Edit mode` and :guilabel:`Pose mode`
   | Panel:    All in :guilabel:`Properties` window, :guilabel:`Object data` property


Let's first have a general overview of the various panels gathering the armature settings,
in :guilabel:`Properties` window, :guilabel:`Object data` context:


.. figure:: /images/Man2.5RiggingEditingObjectDataPropertyWindow.jpg
   :width: 267px
   :figwidth: 267px

   The Object data property in the Properties window.


{{Literal|Skeleton}} panel (all modes)
--------------------------------------


.. figure:: /images/Man2.5RiggingEditingObjectDataPropertyCxtSkeletonPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Skeleton panel.


   In this panel you can arrange sets of bones into different layers for easier manipulation.


{{Literal|Display}} panel (all modes)
-------------------------------------


.. figure:: /images/Man2.5RiggingEditingObjectDataPropertyCxtDisplayPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Display panel.


   This controls the way the bones appear in 3D view; you have 4 different options you can select.

   There are several other options available which we will cover later on.


{{Literal|Bone groups}} panel (pose mode)
-----------------------------------------


.. figure:: /images/Man2.5RiggingEditingObjectDataPropertyCxtBonesGroupsPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Bone Groups panel.


   Lets you assign sets of bones into groups for easy manipulation and management.


{{Literal|Pose Library}} panel ({{Literal|Pose}} mode)
------------------------------------------------------


.. figure:: /images/Man2.5RiggingEditingObjectDataPropertyCxtPoseLibraryPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Pose Library panel.


   Allows you to save different settings (location, rotation, scale) for selected bones for later use.


{{Literal|Ghost}} panel (all modes)
-----------------------------------


.. figure:: /images/Man2.5RiggingEditingObjectDataPropertyCxtGhostPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Ghost panel.


   Allows you to see a set of different consecutive poses, very useful when animating.


{{Literal|iTaSC parameters}} panel (all modes)
----------------------------------------------


.. figure:: /images/Man2.5RiggingEditingObjectDataPropertyCxtiTaSCparametersPanel.jpg
   :width: 250px
   :figwidth: 250px

   The iTaSC parameters panel.


   Defines the type of IK solver used in your animation.


{{Literal|Motion Paths}} panel ({{Literal|Pose}} mode)
------------------------------------------------------


.. figure:: /images/Man2.5RiggingEditingObjectDataPropertyCxtMotionPathsPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Motion Paths panel.


   In this panel you can enable visualization of the motion path your skeleton leaves when animated.


{{Literal|Custom Properties}} panel (all modes)
-----------------------------------------------


.. figure:: /images/Man2.5RiggingEditingObjectDataPropertyCxtCustomPropertiesPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Custom Properties panel.


   Panel for defining custom properties; this is used when scripting.


Bone Panels Overview
====================


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object mode`\ , :guilabel:`Edit mode` and :guilabel:`Pose mode`
   | Panel:    All in :guilabel:`Properties` window, :guilabel:`Bone` property


Let's first have a general grasp of the various panels gathering the bone settings,
in :guilabel:`Properties` window, :guilabel:`Bone` context:


.. figure:: /images/Man2.5RiggingBonePrincipalsBonePropertyWindow.jpg
   :width: 250px
   :figwidth: 250px

   The Bone context.


{{Literal|Relations}} panel (edit mode)
---------------------------------------


.. figure:: /images/Man2.5RiggingEditingBoneCxtRelationsPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Relations panel.


   In this panel you can arrange sets of bones in different layers for easier manipulation.


{{Literal|Display}} panel (object mode)
---------------------------------------


.. figure:: /images/Man2.5RiggingEditingBoneCxtDisplayPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Display panel.


   Display panel lets you customize the look of your bones taking the shape of a another existing object.


{{Literal|Deform}} panel (all modes)
------------------------------------


.. figure:: /images/Man2.5RiggingEditingBoneCxtDeformPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Deform panel.


   In this panel you can set basic properties of the bones.

   Turning the Deform option on and off, includes the active bone in the Automatic Weight Calculation when the Mesh is Parented to the Armature using the Armature Deform with the "With Automatic Weights" option.

   Also it's worth noting that by turning off a bone's deform option, makes it not influence the mesh at all, overriding any weights that it might have been assigned before; It mutes its influence.


{{Literal|Custom Properties}} panel (all modes)
-----------------------------------------------


.. figure:: /images/Man2.5RiggingEditingObjectDataPropertyCxtCustomPropertiesPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Custom Properties panel.


   Panel for defining custom properties, this is used when scripting.


{{Literal|Transform}} panel (edit and pose mode)
------------------------------------------------


.. figure:: /images/Man2.5RiggingEditingBoneCxtTransformPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Transform panel(edit mode).


   When in edit mode you can use this panel to control position and roll of individual bones.

   When in pose mode you can only set location for the main bone, and you can now set rotation and scale.


.. figure:: /images/Man2.5RiggingEditingBoneCxtTransformPPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Transform panel(pose mode).


{{Literal|Transform Locks}} panel (pose mode)
---------------------------------------------


.. figure:: /images/Man2.5RiggingEditingBoneCxtTranformLocksPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Transform Locks panel.


   This panel appears only in pose mode and allows you to restrict position, rotation and scale by axis on each bone in the armature.


{{Literal|Inverse Kinematics}} panel (pose mode)
------------------------------------------------


.. figure:: /images/Man2.5RiggingEditingBoneCxtInverseKinematicsPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Inverse Kinematics panel.


   This panel controls the way a bone or set of bones behave when linked in an inverse kinematic chain.


