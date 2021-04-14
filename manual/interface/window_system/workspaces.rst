
**********
Workspaces
**********

Workspaces are essentially predefined window layouts.
Blender's flexibility with :doc:`Areas </interface/window_system/areas>`
lets you create customized workspaces for different tasks such as
modeling, animating, and scripting. It is often useful to quickly switch between
different workspaces within the same file.

.. figure:: /images/interface_window-system_workspaces_screen.png
   :align: center

   Workspaces are located at the Topbar.


.. _workspaces-controls:

Controls
========

Tabs
   Click on the tabs titles to switch between the workspaces.
   To cycle between workspaces use :kbd:`Ctrl-PageUp` and :kbd:`Ctrl-PageDown`.
   Double click to rename the workspace.
Add ``+``
   Click on the *Add* button to add a new workspace.
Context menu :kbd:`RMB`
   The context menu contains options to duplicate, delete and reorder workspaces.


Default Workspaces
==================

Blender's default startup shows the "Layout" workspace in the main area.
This workspace is a general workspace to preview your scene and objects
and contains the following :doc:`/editors/index`:

- 3D Viewport on top left.
- Outliner on top right.
- Properties on bottom right.
- Timeline on bottom left.

.. figure:: /images/interface_window-system_workspaces_layout.png
   :align: center

   Blender's 'Layout' Workspace with four editors.

   3D Viewport (yellow), Outliner (green), Properties (blue) and Timeline (red).

Blender also has several other workspaces added by default:

:Modeling: For modification of geometry by modeling tools.
:Sculpting: For modification of meshes by sculpting tools.
:UV Editing: Mapping of image texture coordinates to 3D surfaces.
:Texture Paint: Tools for coloring image textures in the 3D Viewport.
:Shading: Tools for specifying material properties for rendering.
:Animation: Tools for making properties of objects dependent on time.
:Rendering: For viewing and analyzing rendering results.
:Compositing: Combining and post-processing of images and rendering information.
:Geometry Nodes: For procedural modeling using :doc:`/modeling/geometry_nodes/index`.
:Scripting: Programming workspace for writing scripts.


Additional Workspaces
---------------------

Blender has a couple additional Workspaces to choose from when adding a new Workspace:


.. rubric:: 2D Animation

:2D Animation: General workspace to work with Grease Pencil.
:2D Full Canvas: Similar to "2D Animation" but contains a larger canvas.


.. rubric:: VFX

:Masking: Tools to create 2D masks for compositing.
:Motion Tracking: Tools to motion track and stabilize footage.


.. rubric:: Video Editing

:Video Editing: Sequence together media into one video.


Save and Override
=================

The workspaces are saved in the blend-file.
When you open a file, enabling the *Load UI* in the File Browser indicates that Blender should
use the file's screen layouts and overriding the current layout.
See :ref:`Load UI <file-load-ui>`.

A custom set of workspaces can be saved as a part of the :doc:`/getting_started/configuration/defaults`.


Workspace Settings
==================

.. admonition:: Reference
   :class: refbox

   :Editor:    Properties
   :Menu:      :menuselection:`Active Tool and Workspace Settings --> Workspace`

.. _bpy.types.WorkSpace.object_mode:

Mode
   Switch to this :doc:`Mode </editors/3dview/modes>` when activating the workspace.


.. _bpy.ops.wm.owner_enable:
.. _bpy.ops.wm.owner_disable:
.. _bpy.types.WorkSpace.use_filter_by_owner:

Filter Add-ons
--------------

Filters which :doc:`Add-ons </addons/index>` are enabled in the active workspace.
Keeping the checkbox in the header enables all global add-ons,
enabling the checkbox allows you to individually enable add-ons from the list.
