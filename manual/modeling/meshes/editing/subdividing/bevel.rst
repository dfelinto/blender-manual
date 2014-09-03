
..    TODO/Review: {{review|}} .


Bevel
*****

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Edges --> Bevel` or :menuselection:`[Ctrl][E] --> Bevel`
   | Hotkey:   :kbd:`Ctrl-B` or :menuselection:`[W] --> Bevel`


.. figure:: /images/Manual-PartII-Bevel-Cubes.jpg

   With bevel and without bevel.


The bevel tool allows you to create chamfered or rounded corners to geometry.
A bevel is an effect that smooths out edges and corners.
True world edges are very seldom exactly sharp.
Not even a knife blade edge can be considered perfectly sharp.
Most edges are intentionally beveled for mechanical and practical reasons.

Bevels are also useful for giving realism to non-organic models. In the real world,
the blunt edges on objects catch the light and change the shading around the edges.
This gives a solid, realistic look,
as opposed to un-beveled objects which can look too perfect.


Bevel Modifier
==============

The :doc:`Bevel Modifier </modifiers/generate/bevel>` is a non destructive alternative to the bevel tool.
It gives you the same options, with additional goodies, like the bevel width controlled by the vertices weight,
and all the modifiers general enhancements (non-destructive operations, ...).
Note that the :guilabel:`Bevel` modifier has no recursive option. To overcome this,
you can add additional modifiers to multiply the effect.


Usage
=====

The :guilabel:`Bevel` tool works only on selected edges.
It will recognize any edges included in a vertex or face selection as well,
and perform the bevel the same as if those edges were explicitly selected.
The :guilabel:`Bevel` tool smooths the edges and/or "corners" (vertices)
by "subdividing" them a specified number of times
(see the options below for details about the bevel algorithm).

Use :kbd:`Ctrl-B` or a method listed above to run the tool.
Move the mouse to interactively specify the bevel offset,
and scroll the :kbd:`wheel` to increase or decrease the number of segments. (see below)


.. figure:: /images/Bevel1.jpg
   :width: 300px
   :figwidth: 300px

   Selected edge before beveling


.. figure:: /images/Bevel2.jpg
   :width: 300px
   :figwidth: 300px

   Result of bevel


Options
=======

.. figure:: /images/BevelOptions.jpg

:guilabel:`Offset`
   You can change the bevel width by moving the mouse towards and away from the object, a bit like with transform tools. As usual, the scaling can be controlled to a finer degree by  holding :kbd:`shift` to scale in 0.001 steps. :kbd:`lmb` finalizes the operation, :kbd:`rmb` or :kbd:`Esc` aborts the action.


.. figure:: /images/Bevel3.jpg
   :width: 300px
   :figwidth: 300px

   Bevel with 4 segments


:guilabel:`Segments`
   The number of segments in the bevel can be defined by scrolling the mouse :kbd:`wheel` to increase or decrease this value. The greater the number of recursions, the smoother the bevel.


   Alternatively, you can manually enter a scaling value while using the tool, or in the Mesh Tool options panel after using the tool.


Examples
========

.. figure:: /images/Bevel4.jpg
   :width: 300px
   :figwidth: 300px

   Result of beveling multiple edges


.. figure:: /images/Bevel5.jpg
   :width: 300px
   :figwidth: 300px

   Another example of beveling multiple edges


