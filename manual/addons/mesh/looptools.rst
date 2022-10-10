
**********
Loop Tools
**********

Todo.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Mesh then Loop Tools to enable the script.


Description
===========

Bridge
------

There are two main ways to use the Bridge tool.
The first method is to select two groups of faces and then run the tool.
The second method is to select two (closed) loops of edges.
Both methods can be mixed and you can even Bridge multiple groups at the same time.
The script will try to make an educated guess on which groups should be connected.

Bridge shares its settings with the *Loft* tool, so changing a setting for one of the tools,
will also change it for the other tool.

Segments
   The number of faces used to bridge the distance between two loops.
   One segment means that only faces will be created.
   Two (or more) segments means that an intermediary line (or lines) of vertices is created,
   so two or more faces can be defined between the loops. If the value is set to zero,
   the script automatically calculates the best amount of segments in order to keep the faces as square as possible.
Minimum Width
   This option has no label, but is located directly to the right of the segments setting.
   The simple explanation: 0% lot of triangles, 100% mostly square faces. There is a bit more to it though.
   It determines when a new vertex has to be created, or when to use the vertex next to it.
   It does this based on the distance between these vertices compared to the distance between
   the vertices in the original loops. So 50% means that if the distance between two vertices
   that will be newly created is smaller than half the distance between two vertices in the original loop,
   they will be merged together, resulting in only a single new vertex.
Interpolation
   This can be set to either cubic or linear. Linear is just a flat interpolation,
   while cubic tries to retain the surface tangents, resulting in more fluid curves.
Strength
   The strength option is only available when the interpolation mode is set to cubic.
   Setting the strength to zero gives a result very similar to linear interpolation,
   while higher strengths result in more fluid curves.
   Setting a negative strength changes the direction of the curve. Or described in a more visual way:
   it makes deflated volumes inflate and vice versa. The soft limits of this option are set to range from -3 to +3,
   but you can easily assign bigger or smaller values by manually entering a number, instead of using the slider.
   This works just the same as with normal sliders in Blender.
Remove Faces
   When using a face-selection input, the inner faces will be removed after bridging.

   Because of some limitations in Blender the weight values assigned to
   the Bevel modifier might be slightly altered (by about 0.01) when this option is enabled.
Twist
   Determines which vertices in both loops are connected to each other.
   This might be used for artistic reasons or to correct a wrong result given by the script.
Reverse
   This option should only be used if the script gives a wrong result.
   It reverses the order in which vertices are connected and can fix problems
   when the script gives a result that looks inverted. It's a bit hard to describe,
   but just try it once and you'll immediately understand what it does.


Creating Holes
^^^^^^^^^^^^^^

You can additionally create holes in an object via the Bridge tool.
Select two or more faces and run the Bridge tool.


Circle
------

There are two correct inputs for the circle tool: selecting a single vertex,
or selecting a closed or open loop of edges.
You can also have the tool operate on multiple inputs at the same time and mix the input types.

Method
   Best Fit
      When *Best Fit* is selected a circle is calculated using a nonlinear least squares method.
      This basically means that the circle that is calculated with this option best fits the vertices you selected.

   Fit Inside
      Selecting *Fit Inside* will calculate the circle in such a way
      that none of the vertices will be moved away from the center of the calculated circle.
      This is useful when you want to retain the topology of the surrounding mesh.
Flatten
   When enabled, the input will be flattened to an optimal plane.
   This includes the center vertex, if the input consisted of a single vertex.
   When disabled the input will be projected onto the existing mesh.
Radius
   This overrides the radius calculated by the script.
   Useful if you wish to create several circles of the same size, or if you need more precision.
Regular
   When this option is selected, the vertices on the circle will all have the same distance between each other.
Influence
   The force of the tool. Zero percent influence means no changes will be made to the mesh.
   100% influence means that the input will be fully transformed into a circle.


Curve
-----

There are two valid input methods for the curve tool.
The first is to select two or more vertices on the same loop.
You can do this for multiple loops simultaneously to save time.

The second method is to select one or more entire loops.
If a full loop is selected, the curve tool won't operate on that loop,
but on all loops perpendicular to it and use the vertices on the selected loop(s) as control points.

Interpolation
   Cubic gives a smooth curve, calculated using a natural cubic spline algorithm.
   Linear calculates straight lines through the control points.
Restriction
   This restricts the movement of the vertices to only one direction.
   Indent only allows movement toward the mesh,
   while extrude only allows movement away from the mesh (in the direction of the normal).
Boundaries
   If enabled, the curve won't stretch beyond the input vertices.
   This limits the tool to only a subsection of the mesh.
Regular
   This will evenly distribute the vertices along the curve. Sometimes this can create weird results,
   as an even distribution isn't always possible (since the selected input vertices aren't moved).
   If that is the case, simply uncheck this checkbox.
Influence
   The force of the tool. Zero percent influence means no changes will be made to the mesh.
   100% influence means the tool will have the maximum effect.


Flatten
-------

Any selection is considered acceptable input for the flatten tool.

Plane
   The method used to calculate the plane on which the input is flattened.

   Best Fit
      Calculates a plane so that on average the vertices will have to be moved the least to be flattened.
   Normal
      Is identical to scaling the input to zero on local Z when the orientation is set to normal (so :kbd:`G Z Z 0`).
      It's mainly included for making an easy comparison between the flatten methods.
   View
      Flattens the input on a plane perpendicular to the viewport angle. So when you run the tool,
      it will appear nothing has changed, but when you rotate the viewport, you'll see what has happened.
Influence
   The force of the tool. Zero percent influence means no changes will be made to the mesh.
   100% influence means the input will be fully flattened.


Loft
----

For loft you can use the same input method as for *Bridge*: selecting groups of faces, or selecting (closed) loops.
You can mix input methods. Contrary to Bridge, you can select more than two input groups,
and have them bridged consecutively.

Loft shares its settings with the Bridge tool, so changing a setting for one of the tools,
will also change it for the other tool. For a full discussion of all the settings take a look at the Bridge settings.
Below you'll find some specific information for the loft tool.

Segments
   This is identical to the *Segments* setting of the Bridge tool,
   but setting it to automatic (segments = 0) has an advantage for the loft tool.
   When letting the script determine the number of segments needed,
   it might create different numbers of segments between different loops.
Loop
   Connects the first and the last loop to each other.


Relax
-----

The input of the relax tool consists of a single (partial) loop.

Interpolation
   Determines how the final position of the vertices is calculated.
   Cubic uses a natural cubic spline to project the vertices on, linear projects the vertices on straight lines.

   A word of caution: when you use the relax tool on a closed loop
   (a loop where all vertices are connected to two other vertices in the same loop)
   you can better use cubic interpolation instead of the linear.
   If you use linear interpolation, the volume of the loop will quickly diminish.
Input
   Selection
      When set to *Selection* the tool will only operate on the selected vertices.
   Parallel (all)
      Setting it to *Parallel (all)*, will also include the vertices of all parallel loops.
Iterations
   The number of times the tool is run. A higher number gives a smoother result.
Regular
   If this option is selected, the vertices will be distributed evenly along the loop.


Space
-----

The input of the space tool consists of a single (partial) loop.

Interpolation
   Cubic distributes the vertices along a natural cubic spline through,
   while linear projects the vertices on the already existing edges.
Input
   Selection
      When set to *Selection* the tool will only operate on the selected vertices.
   Parallel (all)
      Setting it to *Parallel (all)*, will also include the vertices of all parallel loops.
Influence
   The force of the tool. Zero percent influence means no changes will be made to the mesh.
   100% influence means the tool will have the maximum effect.

.. seealso::

   For an illustrated explanation of all the tool settings visit
   the `script home page <https://sites.google.com/site/bartiuscrouch/looptools>`__.

   Please see the
   `old Wiki <https://archive.blender.org/wiki/index.php/Extensions:2.6/Py/Scripts/Modeling/LoopTools/>`__
   for the archived original docs.


.. reference::

   :Category:  Mesh
   :Description: Mesh modeling toolkit. Several tools to aid modeling.
   :Location: :menuselection:`3D Viewport --> Sidebar --> Edit tab`,
              :menuselection:`3D Viewport Edit Mode --> context menu`
   :File: mesh_looptools.py
   :Author: Bart Crouch
   :License: GPL
   :Note: This add-on is bundled with Blender.
