

..    TODO/Review: {{review|copy=X}} .


Armature Templating
===================

The idea of templating is to use an already existing armature as base ("template")
to create a new armature. It differs from a simple copy in that you can directly define the
new armature different in some aspects than its reference rig.

In Blender, the only templating tool is the bone sketching one (Etch-a-ton, described in :doc:`the previous page <rigging/armatures/editing/sketching>`\ ), with its :guilabel:`Template` conversion method - so you should have read its page before this one!


Using Bone Sketching
--------------------


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Bone Sketching` (\ :guilabel:`3D View` window)
   | Menu:     :menuselection:`Armature --> Bone Sketching`
   | Hotkey:   :kbd:`P`


The :guilabel:`Template` conversion method of :guilabel:`Bone Sketching` tool maps a copy of
existing bones to each selected stroke. The new bones will inherit some of their properties
(influence, number of segments, etc.) from the corresponding bones in the template,
but they will acquire their lengths, rolls and rotation from the sketch;
so these properties would be different as compared to the template.

This is easier to understand with some examples.

In the following image, ``armature.002`` is set as the template,
and the stroke maps with ``chain_a`` of this template.
None of the bones are selected in the template.
Note that there is no second stroke to map with chain ``chain_b`` of the template.
The result is shown at right:
Blender creates a copy of ``chain_a`` and matches the bones with the stroke.

Blender also creates a copy of ``chain_b``\ , but this chain is not altered in any way;
because this command can map only one selected chain with a stroke.


+-----------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+In the following example, no template is selected. (In other words, all the action is within the armature itself.)                                   |+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------++
+                                                                                                                                                     |+.. figure:: /images/ManRiggingTemplatingStrokeConversionSameArmatureTemplateEx1.jpg                                                                                                                 |.. figure:: /images/ManRiggingTemplatingStrokeConversionSameArmatureTemplateEx2.jpg++
+Two bones are selected in ``chain_b``\ ,                                                                                                             |+                                                                                                                                                                                                    |                                                                                   ++
+and the property panel is set to map the joints with the stroke. So these two selected bones                                                         |+   Before conversion.                                                                                                                                                                               |   After conversion.                                                               ++
+are copied and the newly created copy of the chain is matched with the stroke.                                                                       |+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------++
+(Note that the newly created bones are named in continuation of the original chain.)                                                                 |+If you had selected both the chains (\ ``Chain_a`` and ``Chain_b``\ ), you would have still got the same result as in the example above, because the command maps to stroke only one selected chain.                                                                                    ++
+                                                                                                                                                     |+                                                                                                                                                                                                                                                                                        ++
+                                                                                                                                                     |+In the following example also, only one chain is selected,                                                                                                                                                                                                                              ++
+                                                                                                                                                     |+but there are three strokes to map to. In this case, the same chain is copied three times                                                                                                                                                                                               ++
+                                                                                                                                                     |+(once for each stroke) and then mapped to individual strokes.                                                                                                                                                                                                                           ++
+                                                                                                                                                     |+Note how a two-bone chain is fitted to a three-segment stroke.                                                                                                                                                                                                                          ++
+                                                                                                                                                     |+                                                                                                                                                                                                                                                                                        ++
+                                                                                                                                                     |+The newly created bones are numbered sequentially, after the original bones' names.                                                                                                                                                                                                     ++
+                                                                                                                                                     |+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------++
+-----------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
++-------------------------------------------------------------------------+-------------------------------------------------------------------------+                                                                                                                                                                                                                                                                                           +
++.. figure:: /images/ManRiggingTemplatingMultiPolyStrokesConversionEx1.jpg|.. figure:: /images/ManRiggingTemplatingMultiPolyStrokesConversionEx2.jpg+                                                                                                                                                                                                                                                                                           +
++                                                                         |                                                                         +                                                                                                                                                                                                                                                                                           +
++   Before conversion.                                                    |   After conversion.                                                     +                                                                                                                                                                                                                                                                                           +
++-------------------------------------------------------------------------+-------------------------------------------------------------------------+                                                                                                                                                                                                                                                                                           +
++                                                                                                                                                   +                                                                                                                                                                                                                                                                                           +
++-------------------------------------------------------------------------+-------------------------------------------------------------------------+                                                                                                                                                                                                                                                                                           +
+-----------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


OK now let us see some important ground rules:


- This conversion method can use as reference bones either *the selected bones in the currently edited armature*\ , or *all bones from another armature*\ . In general, it is a better idea to create new "templated" bones inside the "reference" armature, so you can precisely select which bones to use as template - if you want the new bones in a different armature, you can then use the :guilabel:`Separate` (\ :kbd:`ctrl-alt-P`\ ) and optionally :guilabel:`Join` (\ :kbd:`ctrl-J` in :guilabel:`Object` mode) commands…
- This tool only considers *one chain of bones*\ , so it's better to select only one chain of bones inside the current armature (or use a single-chain armature object as template). Else, the chain of the template containing the first created bones will be mapped to the selected strokes, and *the other chains will just be "copied" as is*\ , without any modification.
- This tool maps the same chain of bones on all selected strokes, so you can't use multiple strokes to map a multi-chains template - you will rather get a whole set of new bones for each selected stroke!
- If you have strokes only made of straight segments, *they must have at least as much segments as there are bones in the template chain* (else, the newly created chain is not mapped at all to the stroke, and remains an exact duplicate of its template). If there are more segments than necessary, the conversion algorithm will chose the best "joints" for the bones to fit to the reference chain, using the same influence settings as for free segments (\ :guilabel:`A`\ , :guilabel:`L` and :guilabel:`D` settings, see below).
- If you try to :guilabel:`Convert` without template bones (i.e. either an empty armature selected as template, or no bones selected in the current edited armature), you will get the error message "\ ``No Template and no deforming bones selected``\ ", and nothing will occur.


+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
+.. figure:: /images/ManRiggingTemplatingBoneSketchingPanelCurrentArmatureTemplate.jpg    |.. figure:: /images/ManRiggingTemplatingBoneSketchingPanelOtherArmatureTemplate.jpg+
+                                                                                         |                                                                                   +
+   With current edited armature as template.                                             |   With another armature as template.                                              +
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
+The :guilabel:`Bone Sketching` panel with :guilabel:`Template` conversion method enabled.                                                                                    +
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+

Now, let us see the settings of this conversion method:

:guilabel:`No`\ , :guilabel:`View`\ , :guilabel:`Joint` buttons
   These three toggle buttons (mutually exclusive) control how the roll angle of newly created bones is affected:

   - :guilabel:`No`\ : Do not alter the bones roll (i.e. the new bones' rolls fit their reference ones).
   - :guilabel:`View`\ : Roll each bone so that one of its X, Y or Z local axis is aligned (as much as possible) with the current view's Z axis.
   - :guilabel:`Joint`\ : New bones roll fit their original rotation (as :guilabel:`No` option), but with regards to the bend of the joint with its parent.


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+
+.. figure:: /images/ManRiggingTemplatingBoneRollExNo.jpg                                                                                                                                           |.. figure:: /images/ManRiggingTemplatingBoneRollExView.jpg|.. figure:: /images/ManRiggingTemplatingBoneRollExJoint.jpg+
+   :width: 200px                                                                                                                                                                                   |   :width: 200px                                          |   :width: 200px                                           +
+   :figwidth: 200px                                                                                                                                                                                |   :figwidth: 200px                                       |   :figwidth: 200px                                        +
+                                                                                                                                                                                                   |                                                          |                                                           +
+   With No roll option.                                                                                                                                                                            |   With View roll option.                                 |   With Joint roll option.                                 +
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+
+Templating: bone roll example. The ``Bone.003``\ -to-\ ``Bone.005`` chain is the mapped-to-stroke version of ``Bone``\ -to-\ ``Bone.002`` selected one, and ``Bone.001`` has a modified roll angle.                                                                                                                       +
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+


:guilabel:`Template` drop-down list
   Here you select the armature to use as template. If you choose :guilabel:`None`\ , the selected bones from the currently edited armature will be used as reference, else all bones of the other armature will be used.

:guilabel:`A`\ , :guilabel:`L`\ , :guilabel:`D` are numeric fields.

Think of them as A(ngle of bones), L(ength of bones) and D(efinition of stroke).

   These settings control how the template is mapped to the selected strokes.
   Each one can have a value between **0.0** and **10.0**\ , the default being **1.0**\ .

   - :guilabel:`A` controls the influence of the angle of the joints (i.e. angle between bones) - the higher this value, the more the conversion process will try to preserve these joints angle in the new chain.
   - :guilabel:`L` controls the influence of the bones' length - the higher this value, the more the conversion process will try to preserve these lengths in the new bones.
   - :guilabel:`D` controls the influence of the stroke's shape - the higher this value, the more the conversion process will try to follow the stroke with the new chain.


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+
+.. figure:: /images/ManRiggingTemplatingInfluenceWeightsEx111.jpg                                                                                                             |.. figure:: /images/ManRiggingTemplatingInfluenceWeightsEx100.jpg|.. figure:: /images/ManRiggingTemplatingInfluenceWeightsEx010.jpg|.. figure:: /images/ManRiggingTemplatingInfluenceWeightsEx001.jpg+
+   :width: 150px                                                                                                                                                              |   :width: 150px                                                 |   :width: 150px                                                 |   :width: 150px                                                 +
+   :figwidth: 150px                                                                                                                                                           |   :figwidth: 150px                                              |   :figwidth: 150px                                              |   :figwidth: 150px                                              +
+                                                                                                                                                                              |                                                                 |                                                                 |                                                                 +
+   A: 1.0; L: 1.0; D: 1.0.                                                                                                                                                    |   A: 1.0; L: 0.0; D: 0.0.                                       |   A: 0.0; L: 1.0; D: 0.0.                                       |   A: 0.0; L: 0.0; D: 1.0.                                       +
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+
+Examples of :guilabel:`Template` conversions for various influence weights values, with one stroke quite similar to the template chain's shape, and one stroke very different.                                                                                                                                                                                                      +
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+


:guilabel:`S` and :guilabel:`N` text fields, "auto" button
   These control how the new bones are named. By default, they just take the same names as the originals from the template - except for the final number, increased as needed. However, if the template bones have "\ ``&s``\ " somewhere in their name, this "placeholder" will be replaced in the "templated" bones' names by the content of the :guilabel:`S` text field ("S" for "side"). Similarly, a "\ ``&n``\ " placeholder will be replaced by the :guilabel:`N` field content ("N" for "number"). If you enable the small "auto" button, the :guilabel:`N` field content is auto-generated, producing a number starting from nothing, and increased each time you press the :guilabel:`Convert` button, and the "\ ``&s``\ " placeholder is replaced by the side of the bone (relative to the local X axis: "\ ``r``\ " for negative X values, "\ ``l``\ " for positive ones).

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
++--------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------++
++.. figure:: /images/ManRiggingTemplatingNamePlaceholdersEx1.jpg                 |.. figure:: /images/ManRiggingTemplatingNamePlaceholdersEx2.jpg                                                                ++
++   :width: 325px                                                                |   :width: 205px                                                                                                               ++
++   :figwidth: 325px                                                             |   :figwidth: 205px                                                                                                            ++
++                                                                                |                                                                                                                               ++
++   Before conversion (note the &n and &s placeholders in template bones' names).|   After conversion: the placeholders have been replaced by the content of the S and N text fields of the Bone Sketching panel.++
++--------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------++
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+Naming and placeholders, using a simple leg template.                                                                                                                                                             +
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
++------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+                  +
++.. figure:: /images/ManRiggingTemplatingAutoNamingEx1.jpg                                                                           |.. figure:: /images/ManRiggingTemplatingAutoNamingEx2.jpg+                  +
++   :width: 285px                                                                                                                    |   :width: 315px                                         +                  +
++   :figwidth: 285px                                                                                                                 |   :figwidth: 315px                                      +                  +
++                                                                                                                                    |                                                         +                  +
++   Before conversion (note that, in the Bone Sketching panel, the S and N fields are empty, and the small "auto" button is enabled).|                                                         +                  +
++------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+                  +
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+Auto naming and placeholders, using a simple leg template.                                                                                                                                                        +
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Static text line
   The line just above the :guilabel:`Peel Objects` button gives you two informations:

   - The "\ *n* ``joints``\ " part gives you the number of joints (i.e. bones' ends, with connected ends considered as one joint), either from the selected bones of the edited armature, or in the whole other template armature.
   - The second part is only present when another armature has been selected as template - it gives you *the root bone's name of the chain that will be mapped to the strokes*\ . Or, while you are drawing a stroke with straight segments, the name of the bone corresponding to the current segment (and "\ ``Done``\ " when you have enough segments for all bones in the template chain).


