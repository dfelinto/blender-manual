
********************
Copy Attributes Menu
********************

This add-on extends the *Copy Objects* :kbd:`Ctrl-C` hotkey to include many extra copy types.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Interface then Copy Attributes Menu to enable the script.


Description
===========

Object Mode
-----------

Select more than one object, press :kbd:`Ctrl-C` to copy attributes from active to selected,
you'll see the following menu:

Each item on the menu will copy some attributes from the *active* (last selected object) to
all the other *selected* items:

Copy Location
   Copies the object location in world coordinates.
Copy Rotation
   Copies the object rotation in world coordinates.
Copy Scale
   Copies the object scale in world coordinates.
Copy Draw Options
   Copies draw options: for instance wireframe draw, empty draw shape, empty draw size, etc.
Copy Time Offset
   Copies the animation stack time offset.
Copy Instancing
   Copies the objects instancing group/vertex/face settings.
Copy Object Color
   (Self-explanatory)
Copy Mass (physics setting)
   (Self-explanatory)
Copy Protected Transform
   Duplicates the transform locks.
Copy Object Constraints
   Currently deletes all constraints on the selected objects and
   replaces them with the constraints on the active object.
Copy Texture Space
   (Self-explanatory)
Copy Pass Index
   (Self-explanatory)
Copy Modifiers
   Currently behaves like constraints, all you original modifiers will be replaced by the ones on the active item.
Copy Vertex Weights
   (Self-explanatory)


Mesh Edit Mode
--------------

With a mesh object selected, enter Edit Mode and press :kbd:`Ctrl-C` to copy texture face attributes.
The following menu appears:

Some of the items may not appear, depending on the number of UV texture or vertex color layers on the mesh.

The first group of options copies attributes from the active face to
all other selected faces in the same UV texture or vertex color layer.

Copy Material
   Copy material index to selected faces.
Copy Image
   Copy image assignment to selected faces.
Copy UV Coordinates
   Copy UV coordinates to selected faces.
Copy Vertex Colors
   Copy Vertex Colors to selected faces.

The second group of options copies attributes to selected faces in
the active UV texture or vertex color layer from their corresponding faces in
a different UV texture or vertex color layer.

Copy Image from Layer
   Copy image assignment from another layer for selected faces.
Copy UV Coordinates from Layer
   Copy UV coordinates from another layer for selected faces.
Copy Vertex Colors from Layer
   Copy Vertex Colors from another layer for selected faces.


Pose Mode
---------

Select more than one bone, press :kbd:`Ctrl-C` to copy attributes from *active* (last selected bone) to
all other *selected* bones. The following menu appears:

Copy Local Location
   Copies the location coordinate (as seen in the transform panel) to the selected bones.
Copy Local Rotation
   Copies the rotation coordinate (as seen in the transform panel) to the selected bones.
Copy Local Scale
   Copies the scale coordinate (as seen in the transform panel) to the selected bones.

Copy Visual Location
   Copies the actual location of the bone (as seen in the screen) to the selected bones.
Copy Visual Rotation
   Copies the actual rotation of the bone (as seen in the screen) to the selected bones.
Copy Visual Scale
   Copies the actual size of the bone (as seen in the screen) to the selected bones.

Copy Bone Shape
   (Self-explanatory)
Copy Protected Transform
   (Self-explanatory)
Copy Pose Constraints
   (Self-explanatory)
Copy IK Limits
   (Self-explanatory)
Copy Pose
   Is what was originally mapped to :kbd:`Ctrl-C` before installing the add-on.


Distinction between Local and Visual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Local transformation of bones is relative the each bone's own rest position;
if they do not match in Edit Mode, they will not match in Pose Mode,
even though the numbers appear the same in the bone's transformation panel.
They also do not take into account constraints, or parenting.

Visual transformation of bones copies the visual transform (on screen) of
the active bone to the selected bones, regardless of parenting or constraints.
The result should look exactly the same even if the bone's numbers do not match.
Constraints on the selected bones may prevent this from working (or drivers for that matter):


.. admonition:: Reference
   :class: refbox

   :Category:  Interface
   :Description: Copy Attributes Menu.
   :Location: 3D Viewport :kbd:`Ctrl-C`
   :File: space_view3d_copy_attributes.py
   :Author: Bassam Kurdali, Fabian Fricke, Adam Wiseman
   :Maintainer: to do
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
