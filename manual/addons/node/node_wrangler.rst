
*************
Node Wrangler
*************

This add-on gives you several tools that help you work with nodes quickly and efficiently.
Many functions work for both the Compositor and shader nodes, and some functions bring features
already in the Compositor to the shader nodes as well. Some tools are made for a specific function,
however we have made it our goal to allow complete flexibility for you to use the tools in every situation,
even where we did not intend.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Node then Node Wrangler to enable the script.


Usage
=====

Use panel in Sidebar of node editor or :kbd:`Ctrl-Spacebar` keyboard shortcut or individual shortcuts for tools.


Description
===========

Lazy Connect
------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Ctrl-RMB`-drag, :kbd:`Shift-Ctrl-RMB`

Make links between the nodes without having to precisely select the sockets.
Just drag from one node to another while holding :kbd:`Ctrl-RMB`.
The nodes nearest the mouse are used, so you don't even have to click on one precisely.

Also, use :kbd:`Shift-Ctrl-RMB` to show a menu of inputs and outputs to make a more accurate connection.
This is useful when working with a large node tree,
since you can easily make connections without having to zoom in and out a lot.


Lazy Mix
--------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Alt-RMB`-drag

Merge outputs of two nodes using a Mix node or Mix Shader node by dragging from one node to another
while holding down :kbd:`Alt-RMB`. A Mix node or Mix Shader node will be added and
the outputs of the nodes will be connected to it.


Merge
-----

Quickly add Mix, Math, Z-Combine, Alpha Over, Mix Shader or Add Shader nodes
that will merge outputs of selected nodes.


Merge with Automatic Type Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Ctrl-0`, :kbd:`Shift-Ctrl-=`, :kbd:`Ctrl-Minus`, :kbd:`Shift-Ctrl-8`, :kbd:`Ctrl-Slash`,
               :kbd:`Shift-Ctrl-Comma`, :kbd:`Shift-Ctrl-Period`

Selected nodes' outputs will be merged using Mix, Math, Mix Shader or Add Shader nodes,
depending on types of selected nodes.

Add :kbd:`Shift-Ctrl-=`
   Sets the blend mode or math operation to Add. When shaders are selected an Add Shader will be used.
Multiply :kbd:`Shift-Ctrl-8`
   Multiply blend mode or math operation.
Subtract :kbd:`Ctrl-Minus`
   Subtract blend mode or math operation.
Divide :kbd:`Ctrl-Slash`
   Divide blend mode or math operation.
Mix :kbd:`Ctrl-0`
   Mix blend mode or when shaders are selected a Mix Shader node will be used.
Greater than :kbd:`Shift-Ctrl-Comma`
   Greater than math operation.
Less than :kbd:`Shift-Ctrl-Period`
   Less than math operation.


Merge Using Mix Node
^^^^^^^^^^^^^^^^^^^^

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Shift-Ctrl-Alt-=`, :kbd:`Ctrl-Alt-Minus`, :kbd:`Shift-Ctrl-Alt-8`, :kbd:`Ctrl-Alt-Slash`

Using :kbd:`Ctrl-Alt` with proper keys will force to use Mix node for merging
no matter what types of nodes are selected.


Merge Using Z-Combine Node
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Ctrl-NumpadPeriod`

Z-Combine nodes will be used for merging. If possible -- image and Z-Depth outputs will be linked.


Merge Using Alpha Over Node
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Ctrl-Alt-0`

Alpha Over nodes will be used for merging.


Merge Using Math Node
^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Shift-Ctrl-=`, :kbd:`Shift-Ctrl-Minus`, :kbd:`Shift-Ctrl-8`,
               :kbd:`Shift-Ctrl-Slash`, :kbd:`Shift-Ctrl-Comma`, :kbd:`Shift-Ctrl-Period`

Using :kbd:`Shift-Ctrl` with proper keys will force to use Math node for merging
no matter what types of nodes are selected.


Batch Change Blend Mode / Math Operation
----------------------------------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Alt-Up`, :kbd:`Alt-Down`, :kbd:`Alt-0`, :kbd:`Shift-Alt-=`, :kbd:`Alt-Minus`,
               :kbd:`Shift-Alt-8`, :kbd:`Alt-Slash`, :kbd:`Shift-Alt-Comma`, :kbd:`Shift-Alt-Period`

Select Mix nodes or Math nodes and change their blend mode or math operation at the same time.
Use keys specified above. They will change the blend mode or operation accordingly to:
Mix, Add, Subtract, Divide, Less than, Greater than.
Use :kbd:`Alt-Up` or  :kbd:`Alt-Down` to go through all available blend modes or math operations.


Change Mix Factor
-----------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Alt-Left`, :kbd:`Shift-Alt-Left`, :kbd:`Alt-Right`, :kbd:`Shift-Alt-Right`

Change Factor of selected Mix nodes or Mix Shader nodes.

- Use :kbd:`Alt-Right` to increase it by 0.1.
- Use :kbd:`Alt-Left` to decrease it by 0.1.
- Use :kbd:`Shift-Alt-Right` to increase it by 0.01.
- Use :kbd:`Shift-Alt-Left` to decrease it by 0.01.
- Use :kbd:`Shift-Ctrl-Alt-Left` to set factor to 0.0. Additional shortcut is :kbd:`Shift-Ctrl-Alt-0`.
- Use :kbd:`Shift-Ctrl-Alt-Right` to set factor to 1.0. Additional shortcut is :kbd:`Shift-Ctrl-Alt-1`.


Delete Unused Nodes
-------------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Alt-X`

Clean your node tree. Delete all of the nodes that don't contribute to the final result.


Swap Links
----------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Alt-S`

Select two nodes that have something linked to their outputs. :kbd:`Alt-S` will swap the outputs.
What originally was linked to output of the first node will now be linked to
output of the second node and vice versa.

Or, select one node with a single linked input --
:kbd:`Alt-S` will cycle the link through the available input sockets.
Or, select one node with two linked inputs -- :kbd:`Alt-S` will swap the two links.
If more than two inputs are linked, the two with matching types will be swapped
(such as a Mix node's two color inputs).


Reset Backdrop
--------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Z`

Reset position and scale of the backdrop.


Add UV Layout Attribute Node
----------------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Header --> Add menu`

Add Attribute node with the attribute set to UV Layout.


Add Vertex Color Attribute Node
-------------------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Header --> Add menu`

Add an Attribute node with the attribute set to vertex color.


Shader Viewer
-------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Shift-Ctrl-LMB`

Viewer Node for shaders. :kbd:`Shift-Ctrl-LMB` and the output of the node will be linked to
newly created Emission shader and Material Output. This is an easy way of previewing textures.


Frame Selected
--------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Shift-P`

Select nodes and "wrap" them in Frame node by hitting :kbd:`Shift-P`.
Immediately after that hit :kbd:`F6` to set the color and label of the Frame.


Reload Images
-------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Alt-R`

All of the images used in the node tree (Image inputs, textures) can be reloaded by hitting :kbd:`Alt-R`.


Switch Node Type
----------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Shift-S`

Change the type of selected node(s) to any other type. Hit :kbd:`Shift-S` and
you'll get the menu ordered exactly the same as :menuselection:`Add --> Node` menu. Choose the new type.


Copy Settings
-------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Shift-C`

Copy settings of active node to all selected nodes of the same type.


Copy Label
----------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Shift-C`

Copy labels all selected nodes based on various criteria.
Labels can be copied from labels (names) of active node :kbd:`Shift-V`,
or from names (labels) of nodes that are linked to selected ones or
from the names of sockets that the selected nodes are linked to.
All options will be revealed in submenu after hitting :kbd:`Shift-C`.


Clear Label
-----------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Alt-L`

Clear labels of selected nodes.


Modify Label
------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Shift-Alt-L`

Batch change labels of selected nodes.
Add text to beginning, to end, replace parts of text.


Add Texture Setup
-----------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Ctrl-T`

Select any shader node, :kbd:`Ctrl-T` and an image texture with nodes controlling coordinates will be added.
If you select any texture node, only the Texture Coordinate and Mapping nodes will be added.
A background shader will get an Environment Texture node with generated mapping.


Add Reroutes to Outputs
-----------------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Slash`

Reroute nodes will be added and linked to each output of each selected node.


Link Active to Selected
-----------------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Backslash`, :kbd:`K`, :kbd:`Shift-K`, :kbd:`'`, :kbd:`Shift-'`, :kbd:`;`, :kbd:`Shift-;`

Link active node to selected nodes basing on various criteria.

- :kbd:`Backslash` -- Call main *Link Active to Selected* menu.
- :kbd:`K` -- Link active to all selected. Use :kbd:`Shift-K` to force to replace existing links.
- :kbd:`Shift-'` -- Link only to selected nodes that have the same name/label as active node
  (:kbd:`Shift-'` to replace existing links).
- :kbd:`;` -- Link selected when name of output matches the name or label of selected node.
  Handy for replacing sources. For example Render Layer to image (multi-layer EXR).


Align Nodes
-----------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Shift-=`

Align nodes horizontally or vertically. Same as :kbd:`S X 0` or :kbd:`S Y 0`,
but with even spacing between the nodes.


Select within Frame (Parent/Children)
-------------------------------------

- :kbd:`]` -- Select all nodes wrapped in selected Frame node.
- :kbd:`[` -- Select frame node that selected nodes are wrapped in.


Detach Outputs
--------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Shift-Alt-D`

Detach output of selected node leaving linked inputs.


Link to Output Node
-------------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`O`

In compositing -- link to Composite output.
In materials -- link to Material Output node.


Add Image Sequence
------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Add --> Input` menu for composite nodes,
               or :menuselection:`Add --> Texture` menu for shader nodes

Select just one image from a sequence in the File Browser and
it will automatically detect the length of the sequence and set the node appropriately.


Add Multiple Images
-------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Add --> Input` menu for composite nodes,
               or :menuselection:`Add --> Texture` menu for shader nodes

Simply allows you to select more than one image and adds a node for each.
(Useful for importing multiple render passes or renders for image stacking.)


.. seealso::

   Please see the
   `old Wiki <https://archive.blender.org/wiki/index.php/Extensions:2.6/Py/Scripts/Nodes/Nodes_Efficiency_Tools/>`__
   for the archived original docs.


.. admonition:: Reference
   :class: refbox

   :Category:  Node
   :Description: Various tools to enhance and speed up node-based workflow.
   :Location: :menuselection:`node editor --> Sidebar` or see the hotkeys of individual tools.
   :File: node_wrangler.py
   :Author: Bartek Skorupa, Greg Zaal, Sebastian Koenig, Christian Brinkmann, Florian Meyer
   :License: GPL
   :Note: This add-on is bundled with Blender.
