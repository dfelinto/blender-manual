


Armature Editing
================


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit mode`
   | Hotkey:   :kbd:`tab`


As with any other object, you edit your armature in :guilabel:`Edit mode` (\ :kbd:`Tab`\ ).

Editing an armature means two main domains of action:

- :doc:`Editing the bones <rigging/armatures/editing/bones>` - i.e. adding/inserting/deleting/extruding/sub-dividing/joining them…
- :doc:`Editing the bones' properties <rigging/armatures/editing/properties>` - this includes key features, like transform properties (i.e. grab, scale, etc…) and relationships between bones (parenting and connecting), as well as bones' names, influence, behavior in :guilabel:`Pose` mode, etc.

These are standard editing methods, quite similar for example to :doc:`meshes <modeling/meshes/editing>` editing. Blender also features a more advanced "armature sketching" tool, called :doc:`Etch-a-Ton <rigging/armatures/editing/sketching>`\ . The same tool might also be used in :doc:`templating <rigging/armatures/editing/templating>`\ , i.e. using another armature as template for the current one…


FIXME(Template Unsupported: Template:Warning/Important;
{{Template:Warning/Important}}
)
One important thing to understand about armature editing is that you **edit the rest position
of your armature**\ , i.e. its "default state". An armature in its *rest position* has all
bones with no rotation and scaled to **1.0** in their own local space.

The different :doc:`poses <rigging/posing>` you might create afterwards are based on this rest position - so if you modify it in :guilabel:`Edit mode`\ , all the poses already existing will also be modified. Thus you should in general be sure that your armature is definitive before starting to :doc:`skin <rigging/skinning>` and :doc:`pose <rigging/posing>` it!


FIXME(Template Unsupported: Template:Warning/Important;
{{Template:Warning/Important}}
)
Please note that some tools work on bones' ends, while others work on bones themselves.
Be careful not to get confused.


