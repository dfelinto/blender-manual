.. _bpy.types.Bone.hide:

****************
Viewport Display
****************

.. admonition:: Reference
   :class: refbox

   :Mode:      Object and Pose Mode
   :Panel:     :menuselection:`Bone --> Viewport Display`

.. figure:: /images/animation_armatures_bones_properties_display_custom-shape-field.png

   Viewport Display panel.

Display panel lets you customize the look of your bones taking the shape of another existing object.

Hide
   Hides the selected bone.


.. _bpy.types.PoseBone.custom_shape:
.. _bpy.types.Bone.show_wire:

Custom Shape
============

Blender allows you to give to each bone of an armature a specific shape
(in *Object Mode* and *Pose Mode*), using another object as "template".
In order to be visible the *Shapes* checkbox has to be enabled
(:menuselection:`Armature --> Viewport Display` panel).

Custom Object
   Object that defines the custom shape of the selected bone.
Override Transform
   Bone that defines the display transform of the custom shape.
Scale
   Additional scaling factor to apply to the custom shape.
Scale to Bone Length
   Option not to use bones length, so that changes in Edit Mode don't resize the custom shape.
Wireframe
   When enabled, bone is displayed in wireframe mode regardless of the viewport display mode.
   Useful for non-obstructive custom bone chains.


Workflow
--------

To assign a custom shape to a bone, you have to:

#. Switch to *Pose Mode* :kbd:`Ctrl-Tab`.
#. Select the relevant bone by clicking on it.
#. Go to the *Display* panel *Custom Shape* field and select the 3D object previously created in the scene;
   in this example we are using a cube and a cone. You can optionally set the *At* field to another bone.

.. figure:: /images/animation_armatures_bones_properties_display_custom-shape-example.png

   The armature with shape assigned to bone. Note the origin of the Cone object.

.. note::

   - These shapes will never be rendered, like any bone, they are only visible in 3D Views.
   - Even if any type of object seems to be accepted by the *Object* field (meshes, curves, even metas...),
     only meshes really work. All other types just make the bone invisible.
   - The origin of the shape object will be at the *root of the bone*
     (see the :doc:`bone page </animation/armatures/bones/index>` for root/tip).
   - The object properties of the shape are ignored
     (i.e. if you make a parallelepiped out of a cube by modifying its dimensions in *Object Mode*,
     you will still have a cube-shaped bone...).
   - The "along bone" axis is the Y one,
     and the shape object is always scaled so that one unit stretches along the whole bone length.
   - If you need to remove the custom shape of the bone,
     just right-click in the *Custom Shape* field and select *Reset to default value* in the pop-up menu.

So to summarize all this, you should use meshes as shape objects,
with their center at their lower -Y end, and an overall Y length of 1.0 unit.
