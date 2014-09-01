
Solidify Modifier
*****************

.. admonition:: Reference
   :class: refbox

   | Mode:     Any mode
   | Panel:    :guilabel:`Modifiers`


Description
===========

The :guilabel:`Solidify` modifier takes the surface of any mesh and adds a depth to it.


Options
=======

.. figure:: /images/25-Manual-Modifiers-Solidify.jpg

   Solidify modifier


.. figure:: /images/26-Manual-Modifiers-Solidify-Clamp.jpg

   Clamp Offset


:guilabel:`Thickness`
   The depth to be solidified.
:guilabel:`Offset`
   A value between ``-1`` and ``1`` to locate the solidified output inside or outside the original mesh.  Set to zero, :guilabel:`Offset` will center the solidified output on the original mesh.
:guilabel:`Clamp`
   A value between ``0`` and ``2`` to clamp offsets to avoid self intersection.
:guilabel:`Vertex Group`
   Restrict the modifier to only this vertex group.

   :guilabel:`Invert`
      Inverts the previous selection.


.. figure:: /images/25-Manual-Modifiers-Solidify-Rims.jpg
   :width: 350px
   :figwidth: 350px

   Rim and edges.  In this example, the object was assigned a second material used to color the rim red.


:guilabel:`Crease`
   These options are intended for usage with the :doc:`Subdivision Surface </modifiers/generate/subsurf>` modifier.

   :guilabel:`Inner`
      Assign a crease to the inner edges.
   :guilabel:`Outer`
      Assign a crease to the outer edges.
   :guilabel:`Rim`
      Assign a crease to the rim.
:guilabel:`Even Thickness`
   Maintain thickness by adjusting for sharp corners.  Sometimes improves quality but also increases computation time.
:guilabel:`High Quality Normals`
   Normals are calculated to produce a more even thickness.  Sometimes improves quality but also increases computation time.
:guilabel:`Fill Rim`
   Fills the gap between the inner and outer edges.
:guilabel:`Rim Material`
   Uses the object's second material for the rim; this is applied as an offset from the current material.


Hints
=====

- The modifier thickness is applied before object scale; if maintaining a fixed thickness is important use unscaled objects (or account for the scale).


- Solidify thickness is an approximation. While "Even Thickness" and "High Quality Normals", should yield good results, the architectural/CAD modeling the final wall thickness isn't guaranteed, depending on the mesh topology. To look at it differently - maintaining precise wall thickness in some cases would need to add / remove faces on the offset shell - something this modifier doesn't do since this would add a lot of complexity and slow down the modifier.


