
..    TODO/Review: {{review|im= add images}} .


Explode Modifier
================

.. admonition:: Reference
   :class: refbox

   | Mode:     Any Mode
   | Panel:    Editing Context → Modifiers
   | Hotkey:    :kbd:`none`


The Explode Modifier is used to alter the mesh geometry (by moving/rotating its faces)
in a way that (roughly)
tracks underlying emitted particles that makes it look as if the mesh is being exploded
(broken apart and pushed outward).

For the Explode Modifier to have a visible effect on the underlying mesh it has to be applied
to a mesh which has a particle system on it,
in other words it has to be a mesh which outputs particles.
This is because the particle system on the mesh is what controls how a mesh will be exploded,
and therefore without the particle system the mesh wont appear to alter.  Also both the number
of emitted particles and number of faces determine how granular the Explode Modifier will be.
With default settings the more faces and particles the more detailed the mesh exploding will
be, because there are more faces and particles to affect detachment/movement of faces.

Here is a link to an Ogg Theora Movie showing a cube with a particle system and Explode
Modifier applied:


+------------------------------------------------------------------------------------------------------------------------------------------------------------+
+`File:Manual - Explode Modifier - Exploding Cube - 2.5.ogg <http://wiki.blender.org/index.php/Media:Manual - Explode Modifier - Exploding Cube - 2.5.ogg>`__+
+------------------------------------------------------------------------------------------------------------------------------------------------------------+


Here is a link to the original Blender file which has an Exploding cube setup, just free the
particle cache by pressing the Free Bake button in the bake panel and then press the Animate
button to see the animation:


+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
+`File:Manual_-_Explode_Modifier_-_Exploding_Cube_-_2.5.blend <http://wiki.blender.org/index.php/Media:Manual_-_Explode_Modifier_-_Exploding_Cube_-_2.5.blend>`__+
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+


Stacking Order Importance
-------------------------

This modifier is highly affected by its position within the modifier stacking order.  If it is
applied before a Particle System modifier it will not be affected by particles and therefore
appear to do nothing.  The Particle System Modifier must appear before the Explode Modifier
because the Particle System Modifier has the information needed to drive the Explode Modifier.


Options
-------

.. figure:: /images/Doc26-explodeModifier.jpg

   Explode Modifier panel with Particle System Modifier above it


:guilabel:`Vertex group`
   If a mesh that has an Explode Modifier on it also has vertex groups assigned to it then this field will allow the selection of one of those vertex groups.  This will indicate to the Explode Modifier that it should take into account the weight values assigned to areas of the selected vertex group.
:guilabel:`Protect`
   Clean vertex group edges. Depending on the weights assigned to that vertex group; either completely protect those faces from being affected by the Explode Modifier (which would happen if the faces had a weight value of 1) or completely remove protection from those faces (which would happen if the faces had a weight value 0).

:guilabel:`Particle UV`
   UV map to change with particle age.

:guilabel:`Cut Edges`
   Cut face edges for nicer shrapnel

:guilabel:`Unborn`
   Show mesh when particles are unborn
:guilabel:`Alive`
   Show mesh when particles are alive
:guilabel:`Dead`
   Show mesh when particles are dead
:guilabel:`Size`
   Use particle size for shrapnel

:guilabel:`Refresh`
   Refresh data in the explode modifier


