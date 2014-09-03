
..    TODO/Review: {{review|partial=X|im=some screenshots are correct, but taken from the 2.4|fixes=[[User:Fade/Doc:2.6/Manual/Modeling/Curves/Editing/Advanced|WIP fix here]]}} .


Curve Deform
************

:guilabel:`Curve Deform` provides a simple but efficient method of defining a deformation on a mesh. By parenting a mesh object to a curve, you can deform the mesh up or down the curve by moving the mesh along, or orthogonal to, the dominant axis. This is a most useful tool to make an object follow a complex path, like e.g. a sheet of paper inside a printer, a film inside a camera, the water of a canal...

The :guilabel:`Curve Deform` works on a (global) dominant axis, X, Y, or Z.
This means that when you move your mesh in the dominant direction,
the mesh will traverse along the curve. Moving the mesh in an orthogonal direction will move
the mesh object closer or further away from the curve.
The default settings in Blender map the Y axis to the dominant axis. When you move the object
beyond the curve endings the object will continue to deform based on the direction vector of
the curve endings.

If the "curve path" is :guilabel:`3D`, the :guilabel:`Tilt` value of its control points will be used (see the
FIXME(TODO: Internal Link;
[[#Extrusion|Extrusion]]
) section above) to twist the "curved" object around it. Unfortunately, the other :guilabel:`Radius` property is not used (it would have been possible, for example, to make it control the size of the "curved" object...).


.. tip::

   Try to position your object over the curve immediately after you have added it,
   before adding the curve deform. This gives the best control over how the deformation works.


.. note:: Use modifiers!

   The :guilabel:`Curve Deform` relationship is now also a modifier, called :doc:`Curve </modifiers/deform/curve>`. The :guilabel:`Curve` modifier function acts the same as its counterpart, except that when the modifier is used, the "dominant axis" is set inside its properties - and the :guilabel:`Track X` / :guilabel:`Y` / :guilabel:`Z` buttons no longer have an effect on it. And you have some goodies, like the possibility, if "curving" a mesh, to only curve one of its vertex groups...


Interface
=========

.. figure:: /images/2.5_Manual-Part-II-curvesDeform_parentMenu.jpg

   Make Parent menu.


When parenting an object (mesh, curve, meta, ...) to a curve (:kbd:`ctrl-P`),
you will be presented with a menu (:guilabel:`Make Parent` *menu*).

By selecting :guilabel:`Curve Deform`, you enable the curve deform function on the mesh object.


.. figure:: /images/2.5_Manual-Part-II-curvesDeform_animPanel.jpg

   Anim settings panel.


The dominant axis setting is set on the mesh object.
By default the dominant axis in Blender is :guilabel:`Y`.
This can be changed by selecting one of the :guilabel:`Track X`,
:guilabel:`Y` or :guilabel:`Z` buttons in the :guilabel:`Anim` Panel,
(:guilabel:`Anim settings` *panel*), in :guilabel:`Object` context (:kbd:`F7`).


.. figure:: /images/2.5_Manual-Part-II-curvesDeform_curveAndSurfacePanel.jpg

   Curve and Surface panel.


Cyclic (or closed)
curves work as expected where the object deformations traverse along the path in cycles.
Note however that when you have more than one curve in the "parent" object,
its "children" will only follow the first one.

The :guilabel:`Stretch` curve option allows you to let the mesh object stretch, or squeeze,
over the entire curve. This option is in :guilabel:`Editing` Context (:kbd:`F9`),
for the "parent" curve. See (:guilabel:`Curve and Surface` *panel*).


Example
=======

Let's make a simple example:


.. figure:: /images/2.5_Manual-Part-II-curvesDeform_exampleAddMonkey.jpg

   Add a Monkey!


- Remove default cube object from scene and add a Monkey (:menuselection:`[shift][A] --> Add --> Mesh --> Monkey`, *Add a Monkey!*)!
- Press :kbd:`tab` to exit :guilabel:`Edit` mode.


.. figure:: /images/2.5_Manual-Part-II-curvesDeform_exampleAddCurve.jpg

   Add a Curve.


- Now add a curve (:menuselection:`[shift][A] --> Add --> Curve --> Bezier Curve`, *Add a Curve*).


.. figure:: /images/2.5_Manual-Part-II-curvesDeform_exampleEditCurve.jpg

   Edit Curve.


- While in :guilabel:`Edit` mode, move the control points of the curve as shown in (*Edit Curve*), then exit :guilabel:`Edit` mode (:kbd:`tab`).


.. figure:: /images/2.5_Manual-Part-II-curvesDeform_exampleMonkeyOnCurve1.jpg

   Monkey on a Curve.


- Now, you can use the new, modern, modifier way of "curving" the Monkey:
  - Select the Monkey (:kbd:`rmb`).
  - In the :guilabel:`Editing` context (:kbd:`F9`), :guilabel:`Modifiers` panel, add a :guilabel:`Curve` modifier.
  - Type the name of the curve (should be "\ ``Curve`` ") in the :guilabel:`Ob` field of the modifier, and optionally change the dominant axis to :guilabel:`Y`.
- Or you can choose the old, deprecated method (note that it creates a "virtual" modifier...):
  - Select the Monkey (:kbd:`rmb`), and then shift select the curve (:kbd:`shift-rmb`).
  - Press :kbd:`ctrl-P` to open up the :guilabel:`Make Parent` menu.
  - Select :guilabel:`Curve Deform` (:guilabel:`Make Parent` *menu*).
- The Monkey should be positioned on the curve, as in (*Monkey on a Curve*).
- Now if you select the Monkey (:kbd:`rmb`), and move it (:kbd:`G`), in the Y-direction (the dominant axis by default), the monkey will deform nicely along the curve.


.. tip::

   If you press :kbd:`mmb` (or one of the :kbd:`X` / :kbd:`Y` / :kbd:`Z` keys)
   while moving the Monkey you will constrain the movement to one axis only.


- In (*Monkey deformations*), you can see the Monkey at different positions along the curve. To get a cleaner view over the deformation I have activated :guilabel:`SubSurf` with :guilabel:`Subdiv` to **2**, and :guilabel:`Set Smooth` on the Monkey mesh (:kbd:`F9` to get :guilabel:`Editing` context).


.. tip::

   Moving the Monkey in directions other than the dominant axis will create some odd deformations.
   Sometimes this is what you want to achieve, so you'll need to experiment and try it out!


.. figure:: /images/2.5_Manual-Part-II-curvesDeform_exampleMonkeyOnCurve2.jpg
   :width: 650px
   :figwidth: 650px

   Monkey deformations.


Curve Extrusion
***************

This section covers methods for extruding curves, or giving them thickness,
and how to control the thickness along the path.


Extrusion
=========

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` or :guilabel:`Edit` mode
   | Panel:    :guilabel:`Curve and Surface` (:guilabel:`Editing` context, :kbd:`F9`)


Ah! The extrusion! Probably the most interesting tool of the curves for modeling, especially with the bevel/taper/\
:guilabel:`Tilt` / :guilabel:`Radius` options? Note that this has nothing to do with the :guilabel:`Extrude`
(:kbd:`E`) command, described in the :doc:`previous page </modeling/curves/editing#adding_new_segments>` !


We will see the different settings, depending on their scope of action:

Width
   This controls the position of the extruded "border" of the curve, relative to the curve itself.
   With closed 2D curves (see below),
   it is quite simple to understand - with a :guilabel:`Width` greater than **1.0**, the extruded volume is wider,
   with a :guilabel:`Width` of **1.0**, the border tightly follows the curve,
   and with a :guilabel:`Width` lower than **1.0**,
   the volume is narrower? The same principle remains for open 2D and 3D curves,
   but the way the "outside" and "inside" of the curve is determined seems a bit odd?

   It has the same effect with extruded "bevel" objects...

Tilt
   This setting - unfortunately, you can never see its value anywhere in Blender - controls the "twisting angle" around the curve for each point - so it is only relevant with 3D curves!
   You set it using the :guilabel:`Tilt` transform tool (:kbd:`T`, or :menuselection:`Curve --> Transform --> Tilt`), and you can reset it to its default value (i.e. perpendicular to the original curve plane) with :kbd:`alt-T` (or :menuselection:`Curve --> Control Points --> Clear Tilt`).
   With NURBS, the tilt is always smoothly interpolated. However, with Bézier, you can choose the interpolation algorithm to use in the :guilabel:`Tilt Interpolation` drop-down list of the :guilabel:`Curve Tools` panel (you will find the classical :guilabel:`Linear`, :guilabel:`Cardinal`, :guilabel:`B Spline` and :guilabel:`Ease` options...).


Simple Extrusion
----------------

Let's first see the "simple" extrusion of curves, without additional bevel/taper objects.

Extrude
   This controls the width (or height) of the extrusion.
   The real size is of course dependent on the scale of the underlying object, but with a scale of one,
   an :guilabel:`Extrusion` of **1.0** will extrude the curve one BU in both directions,
   along the axis perpendicular to the curve's plane (see below for specifics of 3D curves?).

   If set to **0.0**, there is no "simple" extrusion!

Bevel Depth
   This will add a bevel to the extrusion. See below for its effects...
   Note that the bevel makes the extrusion wider and higher.
   If set to **0.0**, there is no bevel (max value: **2.0**).

Bev Resol
   Controls the resolution of the bevel created by a :guilabel:`Bevel Depth` higher than zero.
   If set the **0** (the default), the bevel is a simple "flat" surface.
   Higher values will smooth, round off the bevel, similar to the resolution settings of the curve itself...

We have three sub-classes of results, depending on whether the curve is open or closed or 3D:

Open 2D Curve
   The extrusion will create a "wall" or "ribbon" following the curve shape. If using a :guilabel:`Bevel Depth`,
   the wall becomes a sort of slide or gutter.
   Note the direction of this bevel is sometimes strange and unpredictable, often the reverse of what you would get
   with the same curve closed? You can inverse this direction by
   :doc:`switching the direction </modeling/curves/editing#switch_direction>` of the curve.

   This allows you, e.g., to quickly simulate a marble rolling down a complex slide,
   by combining an extruded beveled curve,
   and a sphere with a :guilabel:`Follow Path` constraint set against this curve?

Closed 2D Curve
   This is probably the most useful situation, as it will quickly create a volume, with (by default)
   two flat and parallel surfaces filling the two sides of the extruded "wall". You can remove one or both of these
   faces by disabling the :guilabel:`Back` and/or :guilabel:`Front` toggle buttons next to the :guilabel:`3D` one.

   The optional bevel will always be "right-oriented" here, allowing you to smooth out the "edges" of the volume.

3D Curve
   Here the fact that the curve is closed or not has no importance - you will never get a volume with an extruded 3D
   curve, only a wall or ribbon, like with open 2D curves.

   However, there is one more feature with 3D curves: the :guilabel:`Tilt` of the control points (see above).
   It will make the ribbon twist around the curve ? to create a M?bius strip, for example!



Advanced Extrusion
------------------

These extrusions use one or two additional curve objects,
to create very complex organic shapes.

To enable this type of extrusion, you have to type a valid curve object name in the
:guilabel:`BevOb` field of the curve you are going to use as the "spinal column" of your
extrusion. The "bevel" curve will control the cross section of the extruded object.
Whether the :guilabel:`BevOb` curve is 2D or 3D has no importance, but if it is closed,
it will create a "tube-like" extrusion;
otherwise you will get a sort of gutter or slide object...

The object is extruded along the whole length of all internal curves. By default,
the width of the extrusion is constant, but you have two ways to control it,
the :guilabel:`Radius` property of control points, and the "taper" object.

The :guilabel:`Radius` of the points is set using the :guilabel:`Shrink/Fatten Radius`
transform tool (:kbd:`alt-S`, or :menuselection:`Curve --> Transform --> Shrink/Fatten Radius`),
or with the :guilabel:`Set Radius` entry in the :guilabel:`Specials` menu (:kbd:`W`).
Here again,
you unfortunately cannot visualize anywhere the :guilabel:`Radius` of a given control point...

The :guilabel:`Radius` allows you to directly control the width of the extrusion along the
"spinal" curve. As for :guilabel:`Tilt` (see above),
you can choose the interpolation algorithm used for Bézier curves,
in the :guilabel:`Radius Interpolation` drop-down list of the :guilabel:`Curve Tools` panel.

But you have another, more precise option: the "taper" object. As for the "bevel" one, you set
its name in the :guilabel:`TaperOb` field of the main curve - it must be an *open curve*.
The taper curve is evaluated along *the local X axis*,
using *the local Y axis* for width control. Note also that:

- The taper is applied independently to all curves of the extruded object.
- Only the first curve in a :guilabel:`TaperOb` is evaluated, even if you have several separated segments.
- The scaling starts at the first control-point on the left and moves along the curve to the last control-point on the right.
- Negative scaling, (negative local Y on the taper curve) is possible as well. However, rendering artifacts may appear.
- It scales the width of normal extrusions based on evaluating the taper curve,
  which means sharp corners on the taper curve will not be easily visible.
  You'll have to heavily level up the resolution (:guilabel:`DefResolU`) of the base curve.
- With closed curves, the taper curve in :guilabel:`TaperOb` acts along the whole curve (perimeter of the object),
  not just the length of the object, and varies the extrusion depth. In these cases,
  you want the relative height of the :guilabel:`TaperOb`
  Taper curve at both ends to be the same, so that the cyclic point
  (the place where the endpoint of the curve connects to the beginning) is a smooth transition.

Last but not least, with 3D "spinal" curves, the :guilabel:`Tilt` of the control points can
control the twisting of the extruded "bevel" along the curve!


Examples
--------

TODO: add some "simple" extrusion examples.

TODO: add some "bevel" extrusion with :guilabel:`Radius` examples.

Let's taper a simple curve circle extruded object using a taper curve. Add a curve,
then exit :guilabel:`Edit`
mode. Add another one (a closed one, like a circle); call it "\ ``BevelCurve`` ",
and enter its name in the :guilabel:`BevOb` field of the first curve
(:guilabel:`Editing` context :kbd:`f9`, :guilabel:`Curve and Surface` panel).
We now have a pipe.
Add a third curve while in :guilabel:`Object` mode and call it "\ ``TaperCurve`` ".
Adjust the left control-point by raising it up about 5 units.

Now return to the :guilabel:`Editing` :doc:`context </interface/contexts>`,
and edit the first curve's :guilabel:`TaperOb` field in
:doc:`Curve and Surface </ce/panels/editing/curves/curve_and_surface>` panel to reference the new taper curve
which we called "\ ``TaperCurve`` ". When you hit enter the taper curve is applied immediately,
with the results shown in (*Taper extruded curve*).


+-------------------------------------------------------------+-------------------------------------------------------------------+
+.. figure:: /images/Manual-Part-II-Curves-Simple-Taper-Ex.jpg|.. figure:: /images/Manual-Part-II-Curves-Simple-Taper-Ex-Solid.jpg+
+                                                             |                                                                   +
+   Taper extruded curve.                                     |   Taper solid mode.                                               +
+-------------------------------------------------------------+-------------------------------------------------------------------+

You can see the **taper curve** being applied to the **extruded object**.
Notice how the pipe's volume shrinks to nothing as the taper curve goes from left to right.
If the taper curve went below the local Y axis the pipe's inside would become the outside,
which would lead to rendering artifacts.
Of course as an artist that may be what you are looking for!


.. figure:: /images/Manual-Part-II-curvesTaper02.jpg

   Taper example 1.


In (*Taper example 1*)
you can clearly see the effect the left taper curve has on the right curve object. Here the
left taper curve is closer to the object center and that results in a smaller curve object to
the right.


.. figure:: /images/Manual-Part-II-curvesTaper03.jpg

   Taper example 2.


In (*Taper example 2*) a control point in the taper curve to the left is moved away from the
center and that gives a wider result to the curve object on the right.


.. figure:: /images/Manual-Part-II-curvesTaper04.jpg

   Taper example 3.


In (*Taper example 3*),
we see the use of a more irregular taper curve applied to a curve circle.


TODO: add some "bevel" extrusion with :guilabel:`Tilt` examples.


