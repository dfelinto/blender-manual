Weight Tools
************

.. figure:: /images/26-Manual-Modeling-Meshes-weight-paint-tools.jpg

   Weight Paint Tools


Blender provides a set of helper tools for Weight Painting.
The tools are accessible from the Tool Shelf in Weight Paint mode.
And they are located in the weight tools panel.


The Subset Option
=================

Some of the tools also provide a Subset parameter (in the Operator panel,
displayed after the tool is called) with following options:


- Active Group
- Selected Pose Bones
- Deform pose Bones
- All Groups

All tools also work with Vertex Selection Masking and Face Selection masking.
In these modes the tools operate only on selected verts or faces.


.. tip:: About the Blend tool
 
   The Blend tool only works when "Vertex selection masking for painting" is enabled. Otherwise the tool button is grayed out.


Normalize All
=============

For each vertex,
this tool makes sure that the sum of the weights across all Vertex Groups is equal to 1.
This tool normalizes all of the vertex groups, except for locked groups,
which keep their weight values untouched.


Operator parameters
-------------------

.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-normalize-all.jpg

   Normalize All Options


Lock Active
   Keep the values of the active group while normalizing all the others.

Please note: Currently this tool normalizes ALL vertex groups except the locked vertex groups.


Normalize
=========

.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-normalize.jpg

   Normalize All Options

This tool only works on the active Vertex Group. All vertices keep their relative weights, but the entire set of weights is scaled up such that the highest weight value is 1.0


Operator parameters
-------------------

None


Mirror
======

.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-mirror.jpg

   Normalize All Options


This tool mirrors the weights from one side of the mesh to the opposite side
(only mirroring along x-axis is supported). But note,
the weights are not transferred to the corresponding opposite bone weight group.
The mirror only takes place within the selected Vertex Group.


Operator parameters
-------------------

.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-mirror-options.jpg

   Mirror Options


Mirror Weights
   Mirrors the weights of the active group to the other side. Note, this only affects the active weight group.
Flip Group Names
   Exchange the names of left and right side. This option only renames the groups.
All Groups
   Operate on all selected bones.
Topology Mirror
   Mirror for meshes which are not 100% symmetric (approximate mirror).


.. tip:: Mirror to opposite bone

   If you want to create a mirrored weight group for the opposite bone (of a symmetric character), then you can do this:

   - Delete the target Vertex Group (where the mirrored weights will be placed)
   - Create a copy of the source bone Vertex Group (the group containing the weights which you want to copy)
   - Rename the new Vertex Group to the name of the target Vertex Group (the group you deleted above)
   - Select the Target Vertex Group and call the Mirror tool (use only the Mirror weights option and optionally Topology Mirror if your mesh is not symmetric)


Invert
======

.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-invert.jpg

   Invert


Replaces each Weight of the selected weight group by 1.0 - weight.

Examples:


- original 1.0 converts to 0.0
- original 0.5 remains 0.5
- original 0.0 converts to 1.0

Note: Please see how the parameter settings change the behavior.


Operator parameters
-------------------

.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-invert-operator.jpg

   Mirror Options


Subset
   Restrict the tool to a subset. See above (:guilabel:`The Subset Option`) about how subsets are defined.
Add Weights
   Add verts that have no weight before inverting (these weights will all be set to 1.0)
Remove Weights
   Remove verts from the Vertex Group if they are 0.0 after inverting.

Note: Locked vertex Groups are not affected.


Clean
=====

.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-clean.jpg

   Invert


Removes weights below a given threshold.
This tool is useful for clearing your weight groups of very low (or zero-) weights.

In the example shown, I used a cutoff value of 0.139 (see operator options below)
so all blue parts (left side) are cleaned out (right side).

Note, the images use the :guilabel:`Show Zero weights` =Active option so that unreferenced
Weights are shown in Black.


Operator parameters
-------------------

.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-clean-operator.jpg

   Mirror Options


Subset
   Restrict the tool to a subset. See above (:guilabel:`The Subset Option`) for how subsets are defined.
Limit
   This is the minimum weight value that will be kept in the Group. Weights below this value will be removed from the group.
Keep Single
   Ensure that the Clean tool will not create completely unreferenced verts (verts which are not assigned to any Vertex Group), so each vertex will keep at least one weight, even if it is below the limit value!


Levels
======
.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-levels.jpg

   Invert


Adds an offset and a scale to all weights of the selected Weight Groups.
with this tool you can raise or lower the overall "heat" of the weight group.

Note: No weight will ever be set to values above 1.0 or below 0.0 regardless of the settings.


Operator parameters
-------------------

.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-levels-operator.jpg

   Mirror Options


Subset
   Restrict the tool to a subset. See above (:guilabel:`The Subset Option`) for how subsets are defined.
Offset
   A value from the range [-1.0,1.0]) to be added to all weights in the Vertex Group.
Gain
   All weights in the Subset are multiplied with the gain. The drag sliders of this value allow only a range of [-10.0, 10.0]. However, you can enter any factor you like here by typing from the keyboard.

Note: Whichever Gain and Offset you choose,
in all cases the final value of each weight will be clamped to the range [0.0, 1.0].
So you will never get negative weights or overheated areas (weight > 1.0) with this tool.


Blend
=====

Blends the weights of selected vertices with adjacent unselected vertices.
This tool only works in vertex select mode.


.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-blend1.jpg

   Blending


To understand what the tool really does, let's take a look at a simple example.
The selected vertex is connected to 4 adjacent vertices
(marked with a gray circle in the image). All adjacent vertices are unselected.
Now the tool calculates the average weight of all connected **and** unselected verts.
In the example this is

(1 + 0 + 0 + 0) / 4 = 0.25

This value is multiplied by the factor given in the Operator parameters (see below).

- If the factor is 0.0 then actually nothing happens at all and the vertex just keeps its value.
- If the factor is 1.0 then the calculated average weight is taken (0.25 here).
- Dragging the factor from 0 to 1 gradually changes from the old value to the calculated average.


.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-blend2.jpg

   Blending


Now let's see what happens when we select all but one of the neighbors of the selected vert as
well. Again all connected and unselected verts are marked with a gray circle.
When we call the Blend tool now and set the Factor to 1.0,
then we see different results for each of the selected verts:


- The topmost and bottommost selected verts:

 are surrounded by 3 unselected verts, with an average weight of (1 + 0 + 0) / 3 = 0.333  So their color has changed to light green.

- The middle vertex:

 is connected to one unselected vert with weight =  1.  So the average weight is 1.0 in this case, thus the selected vert color has changed to red.

- The right vert:

 is surrounded by 3 unselected verts with average weight = (0+0+0) / 3 = 0 So the average weight is 0, thus the selected vert color has not changed at all (it was already blue before blend was applied).


.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-blend3.jpg

   Blending


Finally let's look at a practical example (and explain why this tool is named Blend).
In this example I have selected the middle edge loop.
And I want to use this edge loop for blending the left side to the right side of the area.


- All selected vertices have 2 unselected adjacent verts.
- The average weight of the unselected verts is (1 + 0) / 2  = 0.5
- Thus when the Blend Factor is set to 1.0 then the edge loop turns to green and finally does blend the cold side (right) to the hot side (left).


Operator parameters
-------------------

.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-blend-operator.jpg

   Blend Options


Factor
   The effective amount of blending (range [0.0, 1.0]). When Factor is set to 0.0 then the Blend tool does not do anything. For Factor > 0 the weights of the affected vertices gradually shift from their original value towards the average weight of all connected **and** unselected verts (see examples above).


Transfer Weights
================

Copy weights from other objects to the vertex groups of the active Object.
By default this tool copies all vertex groups contained in the selected objects to the target
object. However you can change the tool's behavior in the operator redo panel (see below).


Prepare the copy
----------------

.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-transfer-wrong.jpg

   Blending


.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-transfer-ok.jpg

   Blending


You first select all source objects, and finally the target object
(the target object must be the active object).

It is important that the source objects and the target object are at the same location.
If they are placed side by side, then the weight transfer won't work.
You can place the objects on different layers,
but you have to ensure that all objects are visible when you call the tool.

Now ensure that the Target Object is in Weight Paint mode.


Call the tool
-------------

Open the Tool Shelf and locate the Weight Tools panel.
From there call the "Transfer weights" tool.
The tool will initially copy all vertex groups from the source objects.
However the tool also has an operator redo panel
(which appears at the bottom of the tool shelf).
From the redo panel you can change the parameters to meet your needs.
(The available Operator parameters are documented below.)


Redo Panel Confusion
~~~~~~~~~~~~~~~~~~~~

You may notice that the Operator Redo Panel (see below)
stays available after the weight transfer is done.
The panel only disappears when you call another Operator that has its own redo Panel. This can
lead to confusion when you use Transfer weights repeatedly after you changed your vertex
groups. If you then use the still-visible redo panel, then Blender will reset your work to its
state right before you initially called the Transfer Weights tool.


Workaround
~~~~~~~~~~

When you want to call the Transfer Weights tool again after you made some changes to your
vertex groups, then always use the "Transfer Weights" Button,
even if the operator panel is still available.
Unless you really want to reset your changes to the initial call of the tool.


Operator parameters
~~~~~~~~~~~~~~~~~~~

Defaults are marked in boldface:


.. figure:: /images/26-Manual-Modeling-Meshes-wp-tools-transfer-operator.jpg

   Blend Options


Group:

- Active: Only copy to the Active Group in the active Object. This option only works when the active Object has an active Vertex Group set. Otherwise the Weight transfer will not do anything.
- **All** : Copy all Vertex groups from the selected objects to the Active Object.

Method:

- **Nearest vertex In face** : TODO
- Nearest Face: TODO
- Nearest vertex: TODO
- Vertex Index (verbatim copy, works only for meshes with identical index count)

Replace

- Empty: Only copy a weight to the active object if the vertex has not yet had a weight set in the group.
- **All** : delete all previous content of the target vertex group before copying the group from the source object.

.. note::

   If a vertex group is contained in 2 or more of the selected objects,
   then the result depends on the order in which the selected objects are processed.
   However, the order of processing cannot be influenced.


Limit total
===========

Reduce the number of weight groups per vertex to the specified Limit.
The tool removes lowest weights first until the limit is reached.

Hint: The tool can only work reasonably when more than one weight group is selected.


Operator parameters
-------------------

Subset
   Restrict the tool to a subset. See above (:guilabel:`The Subset Option`) for how subsets are defined.
Limit
   Maximum number of weights allowed on each vertex (default:4)


Weight Gradient (wip)
=====================

.. figure:: /images/WeightGradient_266.jpg
   :width: 200px
   :figwidth: 200px

   example of the gradient tool being used with selected vertices.


This is an interactive tool for applying a linear/radial weight gradient;
this is useful at times when painting gradual changes in weight becomes difficult.

The gradient tool can be accessed from the Toolbar as a key shortcut:

- Linear: :kbd:`alt-LMB` and drag
- Radial: :kbd:`alt-ctrl-LMB` and drag

The following weight paint options are used to control the gradient:

- Weight - The gradient starts at the current selected weight value, blending out to nothing.
- Strength  - Lower values can be used so the gradient mixes in with the existing weights (just like with the brush).
- Curve - The brush falloff curve applies to the gradient too, so you can use this to adjust the blending.

Blends the weights of selected vertices with unselected vertices.
Hint: this tool only works in vertex select mode.


Operator parameters
-------------------

Type:

- Linear
- Radial

X Start:
X End:
Y Start:
Y End:
