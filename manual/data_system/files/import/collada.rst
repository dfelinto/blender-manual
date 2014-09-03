
COLLADA Import and Export
*************************

.. figure:: /images/Manual_Data_System_Files_Import_COLLADA_exporter.jpg

The Collada module has been implemented as a flexible tool for exporting and importing .
dae files. We have taken care to provide a set of parameters which should make it possible to
export/import Collada files from/to a variety of tools.
But please be aware that we are not yet finished with the Collada module.
So it may well be possible that your particular usage scenario is not yet supported.


The Collada Exporter
====================

Operator Presets
================

We have added 2 Operator Presets (see top of option panel) for Second Life users:

- **Second Life Static**

 is good for exporting static meshes.

- **Second Life Rigged**

 is good for exporting the SL default character.

Special Notes for Second Life users:

- Please use the Operator presets. All other export settings will not work for Second Life.
- The character orientation needs to be such that the character looks towards positive X.
- Scale&Rotation must be applied before export!


Export Data Options
===================

Apply Modifiers
^^^^^^^^^^^^^^^

All active Modifiers will be applied in a non destructive mode. That is,
the modifiers will be applied to copies of the meshes.
Thus you no longer need to apply your modifiers before exporting.
That is now done automatically in the background.


.. note:: Preview/Render mode

   Some Modifiers provide a Preview mode and a Render mode with different mesh settings. We now support both modes when applying the modifiers.


Selection Only
^^^^^^^^^^^^^^

When selection only is enabled, then only the selected objects will be exported.
Otherwise the entire scene is exported with all visible and all invisible objects.


Include Children
^^^^^^^^^^^^^^^^

When this option is enabled then all children of the selected objects will also be exported
regardless of their selection state.


.. note:: Example

   You now can select only(!) an armature,
   then in the exporter enable "include children" then all rigged meshes attached to the armature will also be exported.


Include Armatures
^^^^^^^^^^^^^^^^^

When this option is enabled, then all armatures related to the selected objects will also be
exported regardless of their selection state.


.. note:: Example

   You now can just select your objects, then in the exporter enable "include armatures" then the armature data is also exported.


Include Shape keys
^^^^^^^^^^^^^^^^^^

.. note:: Shape keys

   This option also includes the application of Shape keys! So now you can export your meshes with the current shape key configuration baked in.


Texture Options
===============

Only Active UV layer
^^^^^^^^^^^^^^^^^^^^

When your mesh contains multiple UV layers, then Blender exports all layers by default.
This option allows you to only export the active UV layers.


Include Textures
^^^^^^^^^^^^^^^^

Blender supports 2 ways to texturise your objects.


- By using directly assigned surface textures
- By using material based image textures

While the material based image textures offer much more flexibility,
using surface textures can be done very quickly without need to first render textures.
Until now blender did only export material based image textures.
The new option allows to directly export render results.


.. note:: Texture export needs materials

   For using surface textures, you will still have to create a material for each texture face.
   Then all you need to do is assign your images to the correct faces of your mesh.
   And finally when your object looks as you expect, just export it with "Include UV Textures".
   See also the "Copy" option below.

Copy
^^^^

When you export images either material based image textures or surface textures,
then we create absolute file references in the export file.

But if the "Copy" option is enabled,
we will create copies of the images instead and place the copies besides the export file.
In that case the file references are made relative.


Armature Options
================

Deform Bones Only
^^^^^^^^^^^^^^^^^

When this option is enabled,
then the exporter strips all non deformiung bones from the exported armatures. This option is
useful when your armatures contain control bones which are not actually part of the charater
skeleton. For example you can now export the Avastar rig with this option enabled.
The resulting exported rig is compatible to Second life.
But please note the restrictions further down.


Export for Second Life
^^^^^^^^^^^^^^^^^^^^^^

This option is very special. In fact some issues with bone orientation are calculated
differently when this option is enabled. This is only relevant for rigged meshes.
I hope that this option will eventually be replaced by something more meaningful
(and still compatible to Second Life)    Hint:
This option is only important when you want to export rigged meshes.
For static meshes it just does nothing at all.


Collada Options
===============

Triangulate
^^^^^^^^^^^

The Mesh con be triangulated on the Fly. The triangulation is based on the same function which
is used in the User interface for triangulating the current selection of faces.
For full control over the triangulation you can do this manually before exporting.
However this option allows to do the triangulation only for the exported data.
The mesh itself is not affected.


Use Object Instances
^^^^^^^^^^^^^^^^^^^^

In Blender you can reuse the same mesh for multiple Objects.
This is named "object instanciation". When you enable this option,
then Blender will propagate object instantiation to the Collada file.


Transformation Type
^^^^^^^^^^^^^^^^^^^

Collada supports 2 types of Transformation matrix specifications.
Either as <Matrix> or as a set of transformation decompositions (for Translate,
Rotate and Scale). Note that the exporter will not strictly follow this option setting,
but will rather take it as a hint to use the option if ever possible. This is so because some
of the exported data types hae specific rules about how the transformation matrix has to be
exported.
This is ongoing development and we may provide a less ambiguous method in the future.


Sort by Object Name
^^^^^^^^^^^^^^^^^^^

The export order of data is bound to internal object order and it can not be influenced in a
reliable way. this option ensures that the Geometry nodes and the Object nodes are both
exported in alphabetical order.


The Collada Importer
====================

The Collada Importer is mostly driven by the imported Data.
We only have added one option for controlling the Import units:


- Import Units

If not enabled the imported data will be rescaled according to the currently used unit system.
We assume that the Blender unit is 1 meter. if this option is enabled,
then Blender will adjust itself to the unit system as provided by the Collada file.


Technical details
*****************

Mesh

----


Import
------

Supported geometry types are

- tris (not tested)
- polylist
- polygons
- ngons
- trifans (not tested)
- lines


Export
------

Mesh data is exported as <polylist>, <lines> and <vertices>.


Light
=====

Import
------

Blender does a best effort on importing lights from a .dae.
If a Blender profile is detected for lights, all values from these will be used instead.
This ensures 100% reimport from a Blender exported .dae. <extra>
support has been added in Blender 2.57.


Export
------

A Blender profile for lights has been added through the <extra> tag.
The entire Lamp struct from Blender will be exported through this profile,
with the exception of Light curve falloff .


Material & Effect
=================

Export
------

Since Blender 2.57 some changes to export of effects have been made. Most notably <
lambert> is exported if and only if specularity is 0.


Animation
=========

Export&Import
-------------

- Support for Object(Mesh, Camera, Light) transform Animations. Only euler rotations, which is the default option for Objects, can be exported for now. For armature bone animations euler and quaternion rotation types are supported.
- Import and export of animations for the following parameters are supported:-
  - Light
  - Camera
  - Material Effects
- Non Skin controlling armature bone animation.
- Animations of Armatures with skin deforming bones.
- Animations of Armatures in Object mode.
- Fully rigified Armature animations. For export of rigified Armature animations
  - Select Bake Action. ( press space in 3d view and Type Bake Action )
  - If you have only the deform bones selected check "only selected". This will give smaller dae. Otherwise uncheck "Only Selected".
  - Check "Clear Constraints".
  - Bake Action.
  - Select the mesh and the deform bones. Then export to COLLADA while checking only selected option. ( Selecting only the Mesh and bones is not strictly necessary. Selecting and export only selected will give smaller dae.)
  - `Demonstration <http://www.youtube.com/watch?v=GTlmmd13J1w>`__


Nodes
=====

On import parent transformations for <instance_node>s is properly propagated to child
node instances. Blender materials are exported with the following mapping:

- phong
- blinn
- lambert

For bone nodes which are leaf nodes in the armature tree,
or if a bone has more than one children a blender profile for tip with an <extra> tag,
is added for those joint nodes. To correctly derive the bone→tail location on re-import.


Important things to remember
============================

- object and datablock names are constrained to 21 characters (bytes).
- uv layer names are constrained to 32 characters (bytes).
- only armature animation on mesh, single skin controller
- no support for modifiers yet

When importing a .dae that has <instance_node>s on exporting this information is
essentially lost and these nodes will be <node>s.
