
***************
Edit Mesh Tools
***************

Mesh Edit Tool adds several tools to Blender that are not available in the built-in tools or
provide different methods for similar tasks.
Each Menu: Vertex, Edge, Face and Utility is a sub panel that is closed
by default in the :menuselection:`Sidebar --> Edit tab`.
The Icons in the closed panel headers contain some new/different selection tools and
Edit Mode vertex/edge/face selection modes for quick access to some tools, before opening the sub panels.

In the UI there are a variety of tools in each category, most tools have a tooltip to provide
some usage information to help users understand each tools basic requirements.
The most significant hotkey is in Edit Mode double :kbd:`RMB` brings up the Vertex/Edge/Face menus
depending on vertex/edge/face selection mode.
Menu Integration is main tools into the Edit Mode context menu, selection tools into the Edit Mode select menu.

- Face Inset Fillet: based completely on add-on by zmj100
- Vertex Align: by zmj100
- Edge Fillet Plus: by Gert De Roost -- original by zmj100
- Split Solidify: by zmj100, updated by zeffii to BMesh
- Pen Tool: by zmj100
- Mesh Cut Faces: by Stanislav Blinov (Stan Pancakes)
- Vertex/Edge/Face Context Menu: by Stanislav Blinov (Stan Pancakes)
- Edge Roundifier: by Piotr Komisarczyk (komi3D), PKHG
- PKHG Face Extrude: by PKHG, based on Geodesic Domes add-on "faces function"
- Set Edges Length: by "Giuseppe De Marco [BlenderLab] inspired by NirenYang"
- Edge Tools: by Paul Marshall (brikbot)
- Extrude and Reshape: by Germano Cavalcante (mano-wii)
- Fast Loop: by Andy Davies (metalliandy)
- Multi Extrude: by Liero, Jimmy Hazevoet
- Offset Edges: by Hidesato Ikeya
- Mesh to Wall: by luxuy_BlenderCN
- Vertex Chamfer: by Andrew Hale (TrumanBlending)
- Random Vertices: by Oscurart
- Select Tools: by dustractor
- Thanks to Macouno and CoDEmanX


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Mesh then Edit Mesh Tools to enable the script.


Description
===========

Todo.

.. seealso::

   Please see the
   `old Wiki <https://archive.blender.org/wiki/index.php/Extensions:2.6/Py/Scripts/Modeling/Extra_Tools/>`__
   for the archived original docs.


Extrude & Reshape
-----------------

You can select a face and extrude it inwards or outwards, creating new faces to accommodate the extrusions.
Note: Also known as *Push/Pull Face*.


.. reference::

   :Category:  Mesh
   :Description: Mesh modeling toolkit. Several tools to aid modeling.
   :Location: :menuselection:`3D Viewport --> Sidebar --> Edit tab`,
              :menuselection:`3D Viewport Edit Mode --> context menu`
   :File: mesh_tools folder
   :Author: Multiple Authors, Meta-Androcto
   :Maintainer: meta-androcto, lijenstina
   :License: GPL
   :Note: This add-on is bundled with Blender.
