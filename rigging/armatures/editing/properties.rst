

..    TODO/Review: {{review|copy=X}} .


Editing Bone Properties
=======================

In this page, you will learn how to edit and control most of the properties for Blender bones - For editing bones in an armature, you should read the :doc:`previous page <rigging/armatures/editing/bones>` first! We will see how to
FIXME(TODO: Internal Link;
[[#Chain Editing|manage the bones' relationships]]
),
FIXME(TODO: Internal Link;
[[#Naming Bones|rename them]]
), etc.


Transforming Bones
------------------


We won't detail here the various transformations of bones, nor things like axis locking, pivot points, and so on, as they are common to most object editing, and already described :doc:`here <3d_interaction/transform_control>` (note however that some options, like snapping, do not seem to work, even though they are available…). The same goes for mirroring, as it's nearly the same as with :doc:`mesh editing <modeling/meshes/tools/transform_deform#mirror>`\ . Just keep in mind that bones' roots and tips behave more or less like meshes' vertices, and bones themselves act like edges in a mesh.

As you know, bones can have two types of relationships: They can be parented,
and in addition connected. Parented bones behave in :guilabel:`Edit` mode exactly as if they
had no relations - you can grab, rotate, scale, etc.
a parent bone without affecting its descendants. However,
connected bones must always have parent's tips connected to child's roots,
so by transforming a bone, you will affect all its connected parent/children/siblings.


.. figure:: /images/ManRiggingTransformPropertiesPanelEditMode.jpg
   :width: 200px
   :figwidth: 200px

   The Transform Properties panel for armatures in Edit mode.


Finally, you can edit in the :guilabel:`Transform Properties` panel (\ :kbd:`N`\ ) the positions and radius of both ends of the active selected bone, as well as its :doc:`roll rotation <rigging/armatures/editing/properties#bone_roll>`\ .


Radius and Scaling in Envelope Visualization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit mode`\ , :guilabel:`Envelope` visualization
   | Menu:     :menuselection:`Armature --> Transform --> Scale`
   | Hotkey:   :kbd:`S`


When bones are displayed using :guilabel:`Octahedron`\ , :guilabel:`Stick` or :guilabel:`B-Bone` visualizations, scaling will behave as expected, similar to scaling mesh objects. When bones are displayed using :guilabel:`Envelope` visualization, scaling will have a different effect: it will scale the radius of the selected bones's ends. (see: :doc:`skinning part <rigging/skinning>`\ ). As you control only one value (the radius), there is no axis locking here. And as usual, with connected bones, you scale at the same time the radius of the parent's tip and of the children's roots.


+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
+**Scaling of a bone in** :guilabel:`Octahedron` **and** :guilabel:`Envelope` **visualizations.**|.. figure:: /images/ManRiggingBoneSelectExEditModeWholeBone.jpg                                     |.. figure:: /images/ManRiggingBoneScalingExEditModeOctahedron.jpg+
+                                                                                                |   :width: 300px                                                                                    |   :width: 300px                                                 +
+                                                                                                |   :figwidth: 300px                                                                                 |   :figwidth: 300px                                              +
+                                                                                                |                                                                                                    |                                                                 +
+                                                                                                |   A single selected bone…                                                                          |   …Scaled in Octahedron visualization.                          +
+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
+.. figure:: /images/ManRiggingBoneScalingExEditModeEnvelope1.jpg                                |.. figure:: /images/ManRiggingBoneScalingExEditModeEnvelope2.jpg                                                                                                      +
+   :width: 300px                                                                                |   :width: 300px                                                                                                                                                      +
+   :figwidth: 300px                                                                             |   :figwidth: 300px                                                                                                                                                   +
+                                                                                                |                                                                                                                                                                      +
+   A single selected bone…                                                                      |   …Scaled in Envelope visualization - its length remains the same, but its ends' radius are bigger.                                                                  +
+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+


Note that when you resize a bone (either by directly scaling it,
or by moving one of its ends), Blender automatically adjusts the end-radii of its envelope
proportionally to the size of the modification. Therefore,
it is advisable to place all the bones first, and only then edit these properties.


ScaleB and Envelope
~~~~~~~~~~~~~~~~~~~


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit mode`
   | Hotkey:   :kbd:`ctrl-alt-S`


:kbd:`ctrl-alt-S` activates a transform tool that is specific to armatures. It has different behavior depending on the active visualization, as explained below:

In :guilabel:`Envelope` visualization, it allows you to edit the influence of the selected bones (their :guilabel:`Dist` property, see the :doc:`skinning part <rigging/skinning>`\ ) - as with the "standard" scaling with this visualization (see the previous section), this is a one-value property, so there is no axis locking and such.


+----------------------------+----------------------------------------------------------------+------------------------------------------------------------------+
+**Envelope scaling example**|.. figure:: /images/ManRiggingBoneScalingExEditModeEnvelope1.jpg|.. figure:: /images/ManRiggingBoneAltScalingExEditModeEnvelope.jpg+
+                            |   :width: 300px                                                |   :width: 300px                                                  +
+                            |   :figwidth: 300px                                             |   :figwidth: 300px                                               +
+                            |                                                                |                                                                  +
+                            |   A single bone selected in Envelope visualization.            |   Its envelope scaled with [ctrl][alt][S].                       +
+----------------------------+----------------------------------------------------------------+------------------------------------------------------------------+


In the other visualizations, it allows you to edit the "bone size".
This seems to only have a visible effect in :guilabel:`B-Bone` visualization, but is available
also with :guilabel:`Octahedron` and :guilabel:`Stick`\ …  This tool in this situation has
another specific behavior: While with other transform tools,
the "local axes" means the object's axes, here they are the bone's own axes
(when you lock to a local axis, by pressing the relevant key twice,
the constraint is applied along the selected bone's local axis,
not the armature object's axis).

WARNING! If you have more than one bone selected, using this tool crashes Blender!


+-------------------------------+-----------------------------------------------------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------------------+
+**"Bone size" scaling example**|.. figure:: /images/ManRiggingBoneAltScalingExEditModeBBone1.jpg |.. figure:: /images/ManRiggingBoneAltScalingExEditModeBBone2.jpg|.. figure:: /images/ManRiggingBoneAltScalingExObjectModeBBone.jpg                            +
+                               |   :width: 200px                                                 |   :width: 200px                                                |   :width: 200px                                                                             +
+                               |   :figwidth: 200px                                              |   :figwidth: 200px                                             |   :figwidth: 200px                                                                          +
+                               |                                                                 |                                                                |                                                                                             +
+                               |   A single "default size" bone selected in B-Bone visualization.|   Its size scaled with [ctrl][alt][S].                         |   The same armature in Object mode and B-Bone visualization, with Bone.004's size scaled up.+
+-------------------------------+-----------------------------------------------------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------------------+


Bone Direction
--------------


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Specials --> Switch Direction`
   | Hotkey:   :kbd:`W-3`


This tool is not available from the :guilabel:`Armature` menu,
but only from the :guilabel:`Specials` pop-up menu(\ :kbd:`W`\ ).
It allows you to switch the direction of the selected bones (i.e.
their root will become their tip, and vice versa).

*Switching the direction of a bone will generally break the chain(s) it belongs to*\ . However, if you switch a whole (part of a) chain, the switched bones will still be parented/connected, but in "reversed order". See the *Switching example*\ .


+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+.. figure:: /images/ManRiggingBoneSwitchExEditMode1.jpg                                             |.. figure:: /images/ManRiggingBoneSwitchExEditMode2.jpg                                                                                                                                                                               +
+   :width: 300px                                                                                    |   :width: 300px                                                                                                                                                                                                                      +
+   :figwidth: 300px                                                                                 |   :figwidth: 300px                                                                                                                                                                                                                   +
+                                                                                                    |                                                                                                                                                                                                                                      +
+   An armature with one selected bone, and one selected chain of three bones, just before switching.|   The selected bones have been switched. Bone.005 is no more connected nor parented to anything. The chain of switched bones still exists, but reversed (Now Bone.002 is its root, and Bone is its tip). Bone.003 is now a free bone.+
+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+Switching example.                                                                                                                                                                                                                                                                                                                         +
+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Bone Roll
---------


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Armature --> Bone Roll --> …`
   | Hotkey:   :kbd:`ctrl-R`\ , :kbd:`ctrl-N`


In :guilabel:`Edit` mode, you have options dedicated to the control of the bone roll rotation
(i.e. the rotation around the Y axis of the bone). Each time you add a new bone,
its default roll is so that its Z axis is as perpendicular to the current 3D view as possible.
And each time you transform a bone, Blender tries to determine its best roll…

But this might lead to an unclear armature,
with bones rolled in all angles… nasty! To address this problem, you have three options:

- :menuselection:`Armature --> Bone Roll --> Set Roll` (\ :kbd:`ctrl-R`\ ) will start a roll-specific rotation, which behaves like any other transform operations (i.e. move the mouse and :kbd:`lmb` click to validate, or type a numeric value and hit enter - or :kbd:`rmb` click or hit :kbd:`Esc` to cancel everything).
- :menuselection:`Armature --> Bone Roll --> Clear Roll (Z-Axis Up)` (or :kbd:`ctrl-N-1`\ :menuselection:`popup --> Recalculate Bone Roll Angles --> Clear Roll (Z-Axis Up)`\ ) will reset the selected bone roll so that their Z axis is as much as possible aligned with the global Z axis.
- :menuselection:`Armature --> Bone Roll --> Roll to Cursor` (or :kbd:`ctrl-N-2`\ :menuselection:`popup --> Recalculate Bone Roll Angles --> Align Z-Axis to 3D-Cursor`\ ) will set the selected bone roll so that their Z axis is as much as possible pointed to the 3D cursor.


Properties
----------


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Armature Bones` (\ :guilabel:`Editing` context, :kbd:`F9`\ )
   | Menu:     :menuselection:`Armature --> Bone Settings --> …`
   | Hotkey:   :kbd:`shift-W`\ , :kbd:`ctrl-shift-W`\ , :kbd:`alt-W`


.. figure:: /images/ManRiggingEditingCxtArmatureBonesPanelEditMode.jpg
   :width: 200px
   :figwidth: 200px

   The Armature Bones panel in Edit mode.


Most bones' properties (excepted the transform ones) are regrouped in each bone's sub-panel,
in the :guilabel:`Armature Bones` panel (\ :guilabel:`Editing` context, :kbd:`F9`\ ).
Let's detail them.

Note that some of them are also available in the 3D views,
through the three pop-up menus :guilabel:`Toggle Setting`
(\ :kbd:`shift-W` or :menuselection:`Armature --> Bone Settings --> Toggle a Setting`\ ),
:guilabel:`Enable Setting`
(\ :kbd:`ctrl-shift-W` or :menuselection:`Armature --> Bone Settings --> Enable a Setting`\ ),
and :guilabel:`Disable Setting`
(\ :kbd:`alt-W` or :menuselection:`Armature --> Bone Settings --> Disable a Setting`\ )
- all three have the same entries, their respective effect should be obvious…

:guilabel:`BO`
   The bone name field, see
FIXME(TODO: Internal Link;
[[#Naming Bones|below]]
).

:guilabel:`child of`
   These two settings control the bone relationship, as detailed
FIXME(TODO: Internal Link;
[[#Chain Editing|below]]
).

:guilabel:`Segm`
   This setting controls the number of segments that a bone has; see
FIXME(TODO: Internal Link;
[[#Bone Rigidity Settings|below]]
).

:guilabel:`Dist`\ , :guilabel:`Weight`\ , :guilabel:`Deform` (also :menuselection:`[shift][W] --> Deform` & co), :guilabel:`Mult` (also :menuselection:`[shift][W] --> Mult VG` & co)
   These settings control how the bone influences its geometry - along with the bones' ends radius. This will be detailed in the :doc:`skinning part <rigging/skinning>`\ .

:guilabel:`Hinge` (also :menuselection:`[shift][W] --> Hinge` & co), :guilabel:`S` (also :menuselection:`[shift][W] --> No Scale` & co)
   These settings affect the behavior of children bones while transforming their parent in :guilabel:`Pose` mode, so this will be detailed in the :doc:`posing part <rigging/posing>`\ !

:guilabel:`Hide`
   This will hide the bone (same as hitting :kbd:`H` in the 3D views, see :doc:`this page <rigging/armatures/visualization#hiding_bones>`\ ).

:guilabel:`Lock` (also :menuselection:`[shift][W] --> Locked` & co)
   This will prevent all editing of the bone in :guilabel:`Edit` mode, see the :doc:`previous page <rigging/armatures/editing/bones>`\ .

Layers button
   These small buttons allow you to control to which bone layer this bone belongs; see :doc:`this page <rigging/armatures/visualization#bone_layers>`\ .


Bone Rigidity Settings
----------------------


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` and :guilabel:`Pose` modes
   | Panel:    :guilabel:`Armature Bones` (\ :guilabel:`Editing` context, :kbd:`F9`\ )


.. figure:: /images/ManRiggingEditingCxtArmatureBonesPanelPoseMode.jpg
   :width: 200px
   :figwidth: 200px

   The Armature Bones panel in Pose mode.


Even though you have the :guilabel:`Segm` setting available in :guilabel:`Edit` mode
(bones sub-panel, in the :guilabel:`Armature Bones` panel),
you should switch to the :guilabel:`Pose` mode (\ :kbd:`ctrl-tab`\ ) to edit these "smooth"
bones' properties - one explanation to this strange need is that in :guilabel:`Edit` mode,
even in :guilabel:`B-Bone` visualization, bones are drawn as sticks,
so you can't visualize the effects of these settings.


.. figure:: /images/ManRiggingBBoneSegmentExPoseMode.jpg
   :width: 200px
   :figwidth: 200px

   An armature in Pose mode, B-Bone visualization: Bone.003 has one segment, Bone.004 has four, and Bone.005 has sixteen.


We saw in :doc:`this page <rigging/armatures/bones>` that bones are made of small rigid segments mapped to a "virtual" Bézier curve. The :guilabel:`Segm` numeric field allows you to set the number of segments inside a given bone - by default, it is **1**\ , which gives a standard rigid bone! The higher this setting (max **32**\ ), the smoother the bone, but the heavier the pose calculations…

Each bone's ends are mapped to its "virtual" Bézier curve's :doc:`"auto" <modeling/curves#editing_bezier_curves>` handle. Therefore, you can't control their direction, but you can change their "length" using the :guilabel:`In` and :guilabel:`Out` numeric fields, to control the "root handle" and "tip handle" of the bone, respectively. These values are proportional to the default length, which of course automatically varies depending on bone length, angle with previous/next bones in the chain, and so on.


+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-----------------------------------------------+
+**Bone** :guilabel:`In`\ **/**\ :guilabel:`Out` **settings example, with a materialized Bézier curve.**|.. figure:: /images/ManRiggingBBoneInOutEx1.jpg                 |.. figure:: /images/ManRiggingBBoneInOutEx2.jpg+
+                                                                                                       |   :width: 300px                                                |   :width: 300px                               +
+                                                                                                       |   :figwidth: 300px                                             |   :figwidth: 300px                            +
+                                                                                                       |                                                                |                                               +
+                                                                                                       |   Look at Bone.004: it has the default In and Out values (1.0).|   Bone.004 with In at 2.0, and Out at 0.0.    +
+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+-----------------------------------------------+


Chain Editing
-------------


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Armature Bones` (\ :guilabel:`Editing` context, :kbd:`F9`\ )
   | Menu:     :menuselection:`Armature --> Parent --> …`
   | Hotkey:   :kbd:`ctrl-P`\ , :kbd:`alt-P`


You can edit the relationships between bones (and hence create/modify the chains of bones)
both from the 3D views and the :guilabel:`Buttons` window. Whatever method you prefer,
it's always a matter of deciding, for each bone, if it has to be parented to another one,
and if so, if it should be connected to it.

To parent and/or connect bones, you can:

- In a 3D view, select the bone and *then* its future parent, and hit :kbd:`ctrl-P` (or :menuselection:`Armature --> Parent --> Make Parent…`\ ). In the small :guilabel:`Make Parent` menu that pops up, choose :guilabel:`Connected` if you want the child to be connected to its parent, else click on :guilabel:`Keep Offset`\ . If you have selected more than two bones, they will all be parented to the last selected one. If you only select one already-parented bone, or all selected bones are already parented to the last selected one, your only choice is to connect them, if not already done. If you select only one non-parented bone, you'll get the :guilabel:`Need selected bone(s)` error message…

   *With this method, the newly-children bones won't be scaled nor rotated - they will just be translated if you chose to connect them to their parent's tip.*

- In the :guilabel:`Buttons` window, :guilabel:`Armature Bones` panel, for each selected bone, you can select its parent in the :guilabel:`Parent` drop-down list to the upper right corner of its sub-panel. If you want them to be connected, just enable the little :guilabel:`Con` button to the right of the list.

   *With this method, the tip of the child bone will never be translated - so if* :guilabel:`Con` *is enabled, the child bone will be completely transformed by the operation.*


+------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
+**Parenting example.**                                                        |.. figure:: /images/ManRiggingBoneRelationshipExEditMode1.jpg                                         |.. figure:: /images/ManRiggingBoneRelationshipExEditMode4.jpg                                                                                          +
+                                                                              |   :width: 300px                                                                                      |   :width: 300px                                                                                                                                       +
+                                                                              |   :figwidth: 300px                                                                                   |   :figwidth: 300px                                                                                                                                    +
+                                                                              |                                                                                                      |                                                                                                                                                       +
+                                                                              |   The starting armature, with Bone.005 parented and connected to Bone.004.                           |   Bone.005 re-parented to Bone.002, but not connected to it (same result, using either [ctrl][P][2] in 3D view, or the Armature Bones panel settings).+
+------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
+.. figure:: /images/ManRiggingBoneRelationshipExEditMode2.jpg                 |.. figure:: /images/ManRiggingBoneRelationshipExEditMode3.jpg                                                                                                                                                                                                 +
+   :width: 300px                                                              |   :width: 300px                                                                                                                                                                                                                                              +
+   :figwidth: 300px                                                           |   :figwidth: 300px                                                                                                                                                                                                                                           +
+                                                                              |                                                                                                                                                                                                                                                              +
+   Bone.005 parented and connected to Bone.002, using [ctrl][P][1] in 3D view.|   Bone.005 parented and connected to Bone.002, using the Parent drop-down list of Bone.005 sub-panel.                                                                                                                                                        +
+------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+


To disconnect and/or free bones, you can:

- In a 3D view, select the desired bones, and hit :kbd:`alt-P` (or :menuselection:`Armature --> Parent --> Clear Parent…`\ ). In the small :guilabel:`Clear Parent` menu that pops up, choose :guilabel:`Clear Parent` to completely free all selected bones, or :guilabel:`Disconnect Bone` if you just want to break their connections.
- In the :guilabel:`Buttons` window, :guilabel:`Armature Bones` panel, for each selected bone, you can select no parent in the :guilabel:`Parent` drop-down list of its sub-panel, to free it completely. If you just want to disconnect it from its parent, disable the :guilabel:`Con` button.

Note that relationships with non-selected children are never modified.


Naming Bones
------------


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Armature Bones` (\ :guilabel:`Editing` context, :kbd:`F9`\ ), :guilabel:`Transform Properties` (3D views, :kbd:`N`\ )


You can rename your bones, either using the :guilabel:`Bone` field of the :guilabel:`Transform
Properties` panel in the 3D views, for the active bone (\ :kbd:`N`\ ), or using the
:guilabel:`BO` field in each bone sub-panel of the :guilabel:`Armature Bones` panel
(\ :guilabel:`Editing` context, :kbd:`F9`\ ).

Blender also provides you some tools that take advantage of bones named in a left/right
symmetry fashion, and others that automatically name the bones of an armature.
Let's look at this in detail.


Naming Conventions
~~~~~~~~~~~~~~~~~~


.. figure:: /images/Ie_bonesname.jpg
   :width: 440px
   :figwidth: 440px

   An example of left/right bone naming in a simple rig.


Naming conventions in Blender are not only useful for you in finding the right bone,
but also to tell Blender when any two of them are counterparts.

In case your armature can be mirrored in half (i.e. it's bilaterally symmetrical),
it's worthwhile to stick to a left/right naming convention.
This will enable you to use some tools that will probably save you time and effort
(like the :guilabel:`X-Axis Mirror` editing tool we saw above…).


- First you should give your bones meaningful base-names, like ``leg``\ , ``arm``\ , ``finger``\ , ``back``\ , ``foot``\ , etc.
- If you have a bone that has a copy on the other side (a pair), like an arm, give it one of the following separators:
  - Left/right separators can be either the second position (\ ``L``\ **_**\ ``calfbone``\ ) or last-but-one (\ ``calfbone``\ **.**\ ``R``\ )
  - If there is a lower or upper case ``L``\ , ``R``\ , ``left`` or ``right``\ , Blender handles the counterpart correctly. See below for a list of valid separators. Pick one and stick to it as close as possible when rigging; it will pay off. For example:

+---------------------+---------------+-------+----------------+
+**Valid Separators.**|Separator      |example                 +
+---------------------+---------------+-------+----------------+
+ *(nothing)*         |hand\ **Left** |→      |hand\ **Right** +
+---------------------+---------------+-------+----------------+
+**_** *(underscore)* |Hand\ **_L**   |→      |Hand\ **_R**    +
+---------------------+---------------+-------+----------------+
+**.** *(point)*      |hand\ **.l**   |→      |hand\ **.r**    +
+---------------------+---------------+-------+----------------+
+**-** *(dash)*       |Foot\ **-l**   |→      |Foot\ **-r**    +
+---------------------+---------------+-------+----------------+
+****  *(space)*      |pelvis **LEFT**|→      |pelvis **RIGHT**+
+---------------------+---------------+-------+----------------+

      Note that all examples above are also valid with the left/right part placed before the name. You can only use the short ``L``\ /\ ``R`` code if you use a separator (i.e. ``handL``\ /\ ``handR`` won't work!).

- Before Blender handles an armature for mirroring or flipping, it first removes the number extension, if it's there (like ``.001``\ )
- You can copy a bone named ``bla.L`` and flip it over using :menuselection:`[W] --> Flip Left-Right Names`\ . Blender will name the copy ``bla.L.001`` and flipping the name will give you ``bla.R``\ .


Bone name flipping
~~~~~~~~~~~~~~~~~~


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Armature --> Flip Left & Right Names`
   | Hotkey:   :kbd:`W-4`


You can flip left/right markers (see above) in selected bone names,
using either :menuselection:`Armature --> Flip Left & Right Names`\ ,
or :menuselection:`Specials --> Flip Left-Right Names` (\ :kbd:`W-4`\ ).
This can be useful if you have constructed half of a symmetrical rig
(marked for a left or right side) and duplicated and mirrored it,
and want to update the names for the new side.
Blender will swap text in bone names according to the above naming conventions,
and remove number extensions if possible.


Auto bone naming
~~~~~~~~~~~~~~~~


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Armature --> AutoName Left-Right`\ , :menuselection:`Armature --> AutoName Front-Back`\ , :menuselection:`Armature --> AutoName Top-Bottom`
   | Hotkey:   :kbd:`W-5`\ , :kbd:`W-6`\ , :kbd:`W-7`


The three :guilabel:`AutoName` entries of the :guilabel:`Armature` and :guilabel:`Specials`
(\ :kbd:`W`\ ) menus allows you to automatically add a suffix to all selected bones, *based
on the position of their root relative to the armature center and its local coordinates*\ :

- :guilabel:`AutoName Left-Right` will add the ``.L`` suffix to all bones *with a positive X-coordinate root*\ , and the ``.R`` suffix to all bones *with a negative X-coordinate root*\ . If the root is exactly at **0.0** on the X-axis, the X-coordinate of the tip is used. If both ends are at **0.0** on the X-axis, the bone will just get a period suffix, with no L/R (as Blender cannot decide whether it is a left or right bone…).
- :guilabel:`AutoName Front-Back` will add the ``.Bk`` suffix to all bones *with a positive Y-coordinate root*\ , and the ``.Fr`` suffix to all bones *with a negative Y-coordinate root*\ . The same as with :guilabel:`AutoName Left-Right` goes for **0.0** Y-coordinate bones…
- :guilabel:`AutoName Top-Bottom` will add the ``.Top`` suffix to all bones *with a positive Z-coordinate root*\ , and the ``.Bot`` suffix to all bones *with a negative Z-coordinate root*\ . The same as with :guilabel:`AutoName Left-Right` goes for **0.0** Z-coordinate bones…


