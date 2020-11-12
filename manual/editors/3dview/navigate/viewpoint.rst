.. _bpy.ops.view3d.view_axis:

*********
Viewpoint
*********

Blender uses a right-angled "Cartesian" coordinate system with the Z axis pointing upwards.

:X axis: Left / Right
:Y axis: Front / Back
:Z axis: Top / Bottom

You can select the viewing direction for a 3D Viewport with the *View* menu entries,
:ref:`Navigation Gizmo <navigation-gizmo>`, or by pressing the hotkeys.

These operators change the view to be aligned with the specified global axes:

:Top: :kbd:`Numpad7`
:Front: :kbd:`Numpad1`
:Right: :kbd:`Numpad3`

Holding :kbd:`Ctrl` shows the other side of the same axis:

:Bottom: :kbd:`Ctrl-Numpad7`
:Back: :kbd:`Ctrl-Numpad1`
:Left: :kbd:`Ctrl-Numpad3`

Holding :kbd:`Shift` aligns the view relative to the active selection.
So you can for example, view a rotated objects side, or align the view to the active face in mesh Edit Mode.

The view can also be aligned by holding :kbd:`Alt-MMB` and moving the mouse towards the view to align to.
