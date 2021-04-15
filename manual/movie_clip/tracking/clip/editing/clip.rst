
****
Clip
****

.. _bpy.ops.clip.open:

Open Clip
=========

.. admonition:: Reference
   :class: refbox

   :Mode:      All modes
   :Menu:      :menuselection:`Clip --> Open Clip`
   :Shortcut:  :kbd:`Alt-O`

Todo.


.. _bpy.ops.clip.set_scene_frames:

Set Scene Frames
================

.. admonition:: Reference
   :class: refbox

   :Mode:      Tracking
   :Menu:      :menuselection:`Clip --> Set Scene Frames`

Sets end scene frame to match current clip duration.


.. _bpy.ops.clip.set_center_principal:

Set Principal to Center
=======================

.. admonition:: Reference
   :class: refbox

   :Mode:      Tracking
   :Menu:      :menuselection:`Clip --> Set Principal to Center`

Changes the :ref:`Optical Center <bpy.types.MovieTrackingCamera.principal>` values to the center of image.


.. _bpy.ops.clip.prefetch:

Prefetch
========

.. admonition:: Reference
   :class: refbox

   :Mode:      All modes
   :Menu:      :menuselection:`Clip --> Prefetch`
   :Shortcut:  :kbd:`P`

Fills cache with frames. As many frames as fits into cache are load form the drive.
This allows to fill in the cache as fast as possible when you really need to track something,
but this keeps CPU and drive bandwidth idle if you've got a Clip editor opened but not actually interacting with it.


.. _bpy.ops.clip.reload:

Reload Clip
===========

.. admonition:: Reference
   :class: refbox

   :Mode:      All modes
   :Menu:      :menuselection:`Clip --> Open Clip`
   :Shortcut:  :kbd:`Alt-O`

Force reload the currently loaded movie clip. Is mainly useful when the clip gets edited outside of Blender.


Proxy
=====

Todo.


.. _bpy.ops.clip.set_viewport_background:

Set as Background
=================

.. admonition:: Reference
   :class: refbox

   :Mode:      Tracking
   :Menu:      :menuselection:`Clip --> Set as Background`

Sets the clip currently being edited as the camera background for all visible 3D Viewports.
If there is no visible 3D Viewports or the Clip Editor is open in full screen, nothing will happen.


.. _bpy.ops.clip.setup_tracking_scene:

Setup Tracking Scene
====================

.. admonition:: Reference
   :class: refbox

   :Mode:      Tracking
   :Menu:      :menuselection:`Clip --> Setup Tracking Scene`

Performs all usual steps to set up a VFX scene:

- Create reference objects for floor and test object.
- Create node set up for combining CG with an actual clip.
