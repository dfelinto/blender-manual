
Curve Modifier
**************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Panel:    :guilabel:`Modifiers`


The :guilabel:`Curve` Modifier provides a simple but efficient method of defining a
deformation on a mesh based on the position of an curve object.

The :guilabel:`Curve` Modifier works on a (global) dominant axis, X, Y, or Z.
This means that when you move your mesh in the dominant direction,
the mesh will traverse along the curve. Moving the mesh in an orthogonal direction will move
the mesh object closer or further away from the curve.
The default settings in Blender map the Y axis to the dominant axis. When you move the object
beyond the curve endings the object will continue to deform based on the direction vector of
the curve endings.


Options
=======

.. figure:: /images/25-Manual-Modifiers-Curve.jpg

   Curve modifier


:guilabel:`Object`
   The name of the curve object that will affect the deformed object.

:guilabel:`Vertex Group`
   A vertex group name within the deformed object. The modifier will only affect vertices assigned to this group.

:guilabel:`Deformation Axis`
   :guilabel:`X`, :guilabel:`Y`, :guilabel:`Z`, :guilabel:`-X`, :guilabel:`-Y`, :guilabel:`-Z`: This is the axis that the curve deforms along.


Example
=======

Let's make a simple example:


- Remove default cube object from scene and add a Monkey (:kbd:`shift-A` → :guilabel:`Add` → :guilabel:`Mesh` → :guilabel:`Monkey`, *Add a Monkey!*)!
- Now add a curve (:kbd:`shift-A` → :guilabel:`Add` → :guilabel:`Curve` → :guilabel:`Bezier Curve`, *Add a Curve*).

..    Comment: <!--[[File:Manual-Part-II-curvesDeform_exampleAddMonkey.png|frame|left|Add a Monkey!]]
   [[File:Manual-Part-II-curvesDeform_exampleAddCurve.png|frame|left|Add a Curve.]]--> .


.. figure:: /images/Manual-Part-II-curvesDeform_exampleEditCurve.jpg
   :width: 300px
   :figwidth: 300px

   Edit Curve.


- While in :guilabel:`Edit mode`, move the control points of the curve as shown in (*Edit Curve*), then exit :guilabel:`Edit mode` (:kbd:`tab`).


- Select the Monkey (:kbd:`Rmb`) in :guilabel:`Object mode`
- Assign the curve to the modifier, as shown below. The Monkey should be positioned on the curve:


.. figure:: /images/25-Manual-Modifiers-Curve.jpg

   Assign the Bezier curve to the Curve modifier (for Monkey)


.. figure:: /images/Manual-Part-II-curvesDeform_exampleMonkeyOnCurve1.jpg
   :width: 200px
   :figwidth: 200px

   Monkey on a Curve.


- Now if you select the Monkey (:kbd:`Rmb`), and move it (:kbd:`G`), in the Y-direction, the monkey will deform nicely along the curve.

.. tip::

   If you press :kbd:`Mmb` while moving the Monkey you will constrain the movement to one axis only.


.. figure:: /images/Manual-Part-II-curvesDeform_exampleMonkeyOnCurve2-2.65.gif
   :width: 250px
   :figwidth: 250px

   Monkey deformations.


- In the image to the right you can see the Monkey at different positions along the curve. To get a cleaner view over the deformation :guilabel:`SubSurf` got applied with :guilabel:`Subdiv` to ``2``, and :guilabel:`Set Smooth` on the Monkey mesh.


