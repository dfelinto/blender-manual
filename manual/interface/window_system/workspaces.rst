
**********
Workspaces
**********

Workspaces are essentially predefined window layouts.
Each Workspace consists of a set of :doc:`Areas </interface/window_system/areas>`
containing :doc:`Editors </editors/index>`, and is geared towards a specific task such as
modeling, animating, or scripting. You'll typically switch between
multiple Workspaces while working on a project.

.. figure:: /images/interface_window-system_workspaces_screen.png
   :align: center

   Workspaces are located at the Topbar.


.. _workspaces-controls:

Controls
========

Tabs
   Click on the tabs to switch between the workspaces.
   You can also use the keyboard shortcuts :kbd:`Ctrl-PageUp` and :kbd:`Ctrl-PageDown`.
   Double-click a tab to rename the workspace.
Add ``+``
   Click on the *Add* button to add a new workspace.
Context menu :kbd:`RMB`
   The context menu contains options to duplicate, delete and reorder workspaces.


Default Workspaces
==================

Blender's default startup shows the "Layout" workspace in the main area.
This workspace is a general workspace to preview your scene
and contains the following Editors:

- :doc:`3D Viewport </editors/3dview/introduction>` on top left.
- :doc:`Outliner </editors/outliner/introduction>` on top right.
- :doc:`Properties </editors/properties_editor>` on bottom right.
- :doc:`Timeline </editors/timeline>` on bottom left.

.. figure:: /images/interface_window-system_workspaces_layout.png
   :align: center

   Blender's 'Layout' Workspace with four editors.

   3D Viewport (yellow), Outliner (green), Properties (blue) and Timeline (red).

Blender also has several other workspaces added by default:

:Modeling: For modification of geometry by modeling tools.
:Sculpting: For modification of meshes by sculpting tools.
:UV Editing: For mapping of image texture coordinates to 3D surfaces.
:Texture Paint: For coloring image textures in the 3D Viewport.
:Shading: For specifying material properties for rendering.
:Animation: For making properties of objects dependent on time.
:Rendering: For viewing and analyzing rendering results.
:Compositing: For combining and post-processing of images and rendering information.
:Geometry Nodes: For procedural modeling using :doc:`/modeling/geometry_nodes/index`.
:Scripting: For interacting with Blender's Python API and writing scripts.


Additional Workspaces
---------------------

Blender has a couple additional Workspaces to choose from when adding a new Workspace:


.. rubric:: 2D Animation

:2D Animation: General workspace to work with Grease Pencil.
:2D Full Canvas: Similar to "2D Animation" but contains a larger canvas.


.. rubric:: VFX

:Masking: For creating 2D masks for compositing or video editing.
:Motion Tracking: For calculating camera motion and stabilizing video footage.


.. rubric:: Video Editing

:Video Editing: For sequencing together media into one video.


Save and Override
=================

The workspaces are saved in the blend-file.
When you open a file, enabling :ref:`Load UI <file-load-ui>` in the File Browser indicates that Blender should
use the file's screen layout rather than the current one.

A custom set of workspaces can be saved as a part of the :doc:`/getting_started/configuration/defaults`.


Workspace Settings
==================

.. reference::

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

Determines which :doc:`Add-ons </addons/index>` are enabled in the active workspace.
When unchecked, the global add-ons will be used.
When checked, you can enable individual add-ons in the list below.
