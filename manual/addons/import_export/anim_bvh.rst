
******************************
BioVision Motion Capture (BVH)
******************************

.. admonition:: Reference
   :class: refbox

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Import/Export --> Motion Capture (.bvh)`


Usage
=====

Used for import/export of .bvh or files with Biovision Hierarchical data
or data of skeleton (rig) with the animation in it
Useful for importing data from motion capture devices.


Properties
==========

Import
------

Target
   The motion capture data type.

   :Armature: The bvh-file contains an animated rigged skeleton such as a walking motion capture.
   :Object: The bvh-file contains a static (not animated) mesh object such as a character model.


Transform
^^^^^^^^^

Scale
   Factor to increase the physical size of the BVH.
Rotation
   .. todo:: |TODO|
Forward / Up
   Since many applications use a different axis for pointing upwards, these are axis conversion for these settings,
   Forward and up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y forward, Z up (since the front view looks along the +Y direction).
   For example, its common for applications to use Y as the up axis, in that case -Z forward, Y up is needed.


Animation
^^^^^^^^^

Start Frame
   The start frame, in Blender, to start playback of the BVH animation.
Scale FPS
   Scales the frame rate from the BVH file to the scene frame rate set in Blender,
   otherwise each BVH frame maps directly to a frame in Blender.
Loop
   Cycles the animation playback.
Update Scene FPS
   Set the scene's frame rate to match the frame rate of the BVH file.
Update Scene Duration
   Extend the scene's duration to match the BVH's duration.


Export
------

Transform
^^^^^^^^^

Scale
   Factor to increase the physical size of the BVH.
Rotation
   TODO.
Root Translation Only
   Only write the translation animation channels for the root bone.


Animation
^^^^^^^^^

Start / End
   Sets the range of animation to export to the BVH file.
