
Wireframe Modifier
******************

.. admonition:: Reference
   :class: refbox

   | Mode:     Any mode
   | Panel:    :guilabel:`Modifiers`


Description
===========

.. figure:: /images/Wireframe_Modifier_Panel.jpg

   Wireframe Modifier


The :guilabel:`Wireframe` modifier transforms a mesh into a wireframe by iterating over its
faces, collecting all edges and turning those edges into 4 sided polygons.
Be aware of the fact that your mesh needs to have faces to be wireframed.
You can define the thickness, the material and several other parameters of the generated
wireframe dynamically via the given  modifier options.

When you got more Faces that meet at one point they are forming a star like pattern like seen
in the examples below.


.. figure:: /images/CubeWireframes.jpg

   Original / Wireframe / Original+Wireframe


.. figure:: /images/Wireframe_Modifier_Suzanne.jpg

   VGroup weighting: One half 0 weighted, one half 1 weighted


.. figure:: /images/Wireframe_Modifier_CreaseWeight.jpg

   Cube+Subsuf with 0 / 0.5 / 1 crease weight


Options
=======

:guilabel:`Thickness`
   The depth or size of the wireframes.
:guilabel:`Offset`
   A value between **-1** and **1** to change whether the wireframes are generated inside or outside the original mesh. Set to zero, :guilabel:`Offset` will center the wireframes around the original edges.
:guilabel:`Vertex Group`
   Restrict the modifier to only this vertex group.

   :guilabel:`Invert`
      Inverts the vertex group weights.


.. figure:: /images/Wireframe_Mod_Result.jpg
   :width: 350px
   :figwidth: 350px

   Wireframes on a displaced plane. In this example, the wireframes carry a second (dark) material while the displaced plane uses its original one.


:guilabel:`Crease Edges`
   This option is intended for usage with the :doc:`Subdivision Surface </modifiers/generate/subsurf>` modifier.
   Enable this option to crease edges on their junctions and prevent large curved intersections.

   :guilabel:`Crease Weight`
      Define how much crease (between **0** = no and **1** = full) the junctions should receive.
:guilabel:`Even Thickness`
   Maintain thickness by adjusting for sharp corners.  Sometimes improves quality but also increases computation time.
:guilabel:`Relative Thickness`
   Determine edge thickness by the length of the edge - longer edges are thicker.
:guilabel:`Boundary`
   Creates wireframes on mesh island boundaries.
:guilabel:`Replace Original`
   If this option is enabled, the original mesh is replaced by the generated wireframe. If not, the wireframe is generated on top of it.
:guilabel:`Material Offset`
   Uses the chosen material index as as the material for the wireframe; this is applied as an offset from the first material.


Hints
=====

- Wireframe thickness is an approximation. While **Even Thickness** should yield good results in many cases, skinny faces can cause ugly spikes, in this case you can either reduce the extreme angles in the geometry or disable the **Even Thickness** option.


