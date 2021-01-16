
********
Geometry
********

.. figure:: /images/modeling_curves_properties_geometry_panel.png
   :align: center

   Geometry panel.

.. _bpy.types.Curve.offset:

Offset
   Moves the extrusion parallel to the curve normals.

   .. figure:: /images/modeling_curves_properties_geometry_extrude-offset.png
      :width: 50%

      Bézier Circle -1 offset, 0.5 extrusion, 0.25 Bevel Depth, 10 Bevel resolution.

.. _bpy.types.Curve.extrude:

Extrude
   Will extrude the curve along both the positive and negative local Z axes.
   Turns a one-dimensional curve into a two-dimensional curve by giving it height.
   With a scale is the sum of both directions, perpendicular to the curve's normals.

   .. list-table::

      * - .. figure:: /images/modeling_curves_properties_geometry_extrude-bezier-circle.png
             :width: 320px

             Bézier Circle 0.0 extrude (Edit Mode).

        - .. figure:: /images/modeling_curves_properties_geometry_extrude-after.png
             :width: 320px

             Extruded by 0.5 (Object Mode).

.. _bpy.types.Curve.taper_object:

Taper Object
   Tapering a curve causes it to get thinner towards one end.
   You can also alter the proportions of the Taper throughout the tapered object
   by moving/scaling/rotating the control points of the Taper Object.
   The taper curve is evaluated along the local X axis, using the local Y axis for width control.
   In order for this to work the Taper Object can only be another *open curve*.

   The details are:

   - The taper is applied independently to all curves of the extruded object.
   - Only the first curve in a *Taper Object* is evaluated, even if you have several separated segments.
   - The scaling starts at the first control point on the left
     and moves along the curve to the last control point on the right.
   - Negative scaling, (e.g. negative local Y on the taper curve) is possible as well.
     However, rendering artifacts may appear.
   - You may need to increase the curve resolution to see more detail of the taper.
   - The Taper Object is distributed by control points.
     Therefor unevenly spaced control points may likelier to stretch the shape of the taper.
     Subdividing segments causes those points to use a larger fraction of the overall taper shape.
   - With closed curves, the taper curve in *Taper Object* acts along the whole curve (perimeter of the object),
     not just the length of the object, and varies the extrusion depth. In these cases,
     you want the relative height of the *Taper Object*
     Taper curve at both ends to be the same, so that the cyclic point
     (the place where the endpoint of the curve connects to the beginning) is a smooth transition.

   .. hint::

      Editing the handles and control points of the Taper Object
      will instantly change the shape of the original object.

.. _bpy.types.Curve.use_map_taper:

Map Taper
   For curves using a Taper Object and with modifications to the *Start/End Bevel Factor*
   the *Map Taper* option will apply the taper to the beveled part of the curve (not the whole curve).


.. _bpy.types.Curve.bevel:

Bevel
=====

Round
-----

.. _bpy.types.Curve.bevel_depth:

Depth
   Changes the size of the bevel.

   .. list-table::

      * - .. figure:: /images/modeling_curves_properties_geometry_bevel-depth.png
             :width: 320px

             A curve with different Bevel depths applied (Depth of 0.05).

        - .. figure:: /images/modeling_curves_properties_geometry_bevel.png
             :width: 320px

             A curve with different Bevel depths applied (Depth of 0.25).

.. _bpy.types.Curve.bevel_resolution:

Resolution
   Alters the smoothness of the bevel.

   .. list-table::

      * - .. figure:: /images/modeling_curves_properties_geometry_bevel-resolution.png
             :width: 320px

             A curve with different resolutions applied (Resolution of 1).

        - .. figure:: /images/modeling_curves_properties_geometry_bevel.png
             :width: 320px

             A curve with different resolutions applied (Resolution of 12).

.. _bpy.types.Curve.use_fill_caps:

Fill Caps
   Seals the ends of a beveled curve.


Object
------

.. _bpy.types.Curve.bevel_object:

Object
   Here you can specify a curve object (opened or closed) which will be extruded along the curve.
   If your object's :ref:`shape <bpy.types.Curve.dimensions>` is 3D,
   it will be projected to its local XY plane before the extrusion.
   You can check how the projected Object looks like by switching its shape to 2D.

   .. important::

      Make sure the shape you want to extrude is in the Object's local XY plane.
      If it is in the local XZ or YZ plane, it will be reduced to a line when it is projected to the local XY plane.
      Because of this, the extruded shape will be a flat plane.

   .. list-table::

      * - .. figure:: /images/modeling_curves_properties_geometry_bevel-object.png
             :width: 320px

             A curve with a Bézier curve as the Bevel Object.

        - .. figure:: /images/modeling_curves_properties_geometry_extrude-bevel-object.png
             :width: 320px

             A curve with a Bézier circle as the Bevel Object.


Profile
-------

.. figure:: /images/modeling_modifiers_generate_bevel_profile-widget.png
   :align: right
   :width: 300px

   The custom profile widget.

This widget allows the creation of a user-defined profile with more complexity than
with the single profile parameter. The modal tool allows toggling the custom profile,
but the shape of the profile is only editable in the options panel after the operation is confirmed.

The profile starts at the bottom right of the widget and ends at the top left, as if it
were between two edges intersecting at a right angle. Control points are created in the widget and
then the path is sampled with the number of segments from the Bevel modifier.

.. note::

   The *Profile* slider stays active when miters are enabled
   because it still controls the shape of the miter profiles.

Presets
   The *Support Loops* and *Steps* presets are built dynamically depending on
   the number of segments in the bevel. If the number of segments is changed,
   the preset will have to be re-applied.

Sampling
   Samples will first be added to each control point, then if there are enough samples,
   they will be divided evenly between the edges. The *Sample Straight Edges* option toggles whether
   the samples are added to edges with sharp control points on either side. If there aren't enough samples
   to give each edge the same number of samples, they will just be added to the most curved edges.
   So it is recommended to use at least as many segments as there are control points.


Start & End Mapping
===================

.. _bpy.types.Curve.bevel_factor_start:
.. _bpy.types.Curve.bevel_factor_end:

Factor Start, End
   These options determine where to start/end the geometry of the curve.
   This allows to make a curve which is not fully covered with geometry.

   Increasing the start value to 0.5 will start the geometry at 50%
   of the distance from the start of the curve (in effect shortening the curve).
   Decreasing the end value by 0.25 will start the geometry at 25%
   of the distance from the end of the curve (again, shortening the curve).

   .. list-table::

      * - .. figure:: /images/modeling_curves_properties_geometry_bevel.png
             :width: 320px

             A curve with no *Factor Start, End*.

        - .. figure:: /images/modeling_curves_properties_geometry_bevel-start-end-factor.png
             :width: 320px

             A curve with a 0.6 End factor.

.. _bpy.types.Curve.bevel_factor_mapping_start:
.. _bpy.types.Curve.bevel_factor_mapping_end:

Mapping Start, End
   Allows to control the relation between the *Factor Start, End* (number between 0 and 1)
   and the rendered start and end point of the spline's geometry.

   Resolution
      Maps the start and end factor to the number of subdivisions of a spline (U resolution).
   Segments
      Maps the start and end factor to the length of its segments.
      Mapping to segments treats the subdivisions in each segment
      of a curve as if they would have all the same length.
   Spline
      Maps the start and end factor to the length of a spline.


Examples
========

.. TODO Add some "simple" extrusion examples.
        Add some "bevel" extrusion with *Radius* examples.


Open 2D Curve
-------------

The extrusion will create a "wall" or "ribbon" following the curve shape. If using a *Bevel Depth*,
the wall becomes a sort of slide or gutter.
If your normals are facing the wrong way you can switch their direction as shown
:ref:`here <curve-switch-direction>`.

.. figure:: /images/modeling_curves_properties_geometry_extrude-open-curve.png
   :width: 320px

   Open 2D Curve with :kbd:`Alt-C`, fill set to none,
   zero offset, 0.5 extrusion, 0.25 Bevel Depth, 10 Bevel resolution.


Closed 2D Curve
---------------

This is probably the most useful situation, as it will quickly create a volume, with (by default)
two flat and parallel surfaces filling the two sides of the extruded "wall". You can remove one or both of these
faces by choosing the fill mode: both, front, back, or none.

The optional bevel depth will always create a 90 degree bevels here.

.. figure:: /images/modeling_curves_properties_geometry_extrude-closed-curve.png
   :width: 320px

   Closed 2D Curve, 0.5 extrude, 0.25 Bevel Depth, 10 Bevel resolution, Fill: Both.


3D Curve
--------

Here the fact that the curve is closed or not has no importance --
you will never get a volume with an extruded 3D curve, only a wall or ribbon, like with open 2D curves.

However, there is one more feature with 3D curves: the *Tilt* of the control points (see above).
It will make the ribbon twist around the curve to create a Möbius strip, for example.


Taper
-----

Let us taper a simple curve circle extruded object using a taper curve. Add a curve,
then exit *Edit Mode*. Add another one (a closed one, like a circle); call it "BevelCurve",
and enter its name in the *Bevel Object* field of the first curve
(*Curve* tab). We now have a pipe.
Add a third curve while in *Object Mode* and call it "TaperCurve".
Adjust the left control point by raising it up about 5 units.

Now return to the Object tab,
and edit the first curve's *Taper Object* field in the Geometry panel to reference the new taper curve
which we called "TaperCurve".
When you hit enter the taper curve is applied immediately,
with the results shown in Fig. :ref:`fig-curves-extrude-taper-curve`.

.. list-table::

   * - .. _fig-curves-extrude-taper-curve:

       .. figure:: /images/modeling_curves_properties_geometry_extrude-bevel-object.png
          :width: 320px

          Circle curve set as Bevel Object.

     - .. figure:: /images/modeling_curves_properties_geometry_extrude-taper-object.png
          :width: 320px

          Taper extruded curve.

You can see the *taper curve* being applied to the *extruded object*.
Notice how the pipe's volume shrinks to nothing as the taper curve goes from left to right.
If the taper curve went below the local Y axis the pipe's inside would become the outside,
which would lead to rendering artifacts.
Of course as an artist that may be what you are looking for!

.. _fig-curves-extrude-taper1:

.. figure:: /images/modeling_curves_properties_geometry_extrude-taper-curve-closer.png

   Taper example 1.

In Fig. :ref:`fig-curves-extrude-taper1`
you can clearly see the effect the left taper curve has on the right curve object.
Here the left taper curve is closer to the object origin and
that results in a smaller curve object to the right.

.. _fig-curves-extrude-taper2:

.. figure:: /images/modeling_curves_properties_geometry_extrude-taper-curve-away.png

   Taper example 2.

In Fig. :ref:`fig-curves-extrude-taper2` a control point in the taper curve to the left is moved away from
the origin and that gives a wider result to the curve object on the right.

.. _fig-curves-extrude-taper3:

.. figure:: /images/modeling_curves_properties_geometry_extrude-taper-curve-irregular.png

   Taper example 3.

In Fig. :ref:`fig-curves-extrude-taper3` we see the use of a more irregular taper curve applied to a curve circle.

.. figure:: /images/modeling_curves_properties_geometry_extrude-bevel-curve-tilt.png

   Bevel extrusion with Tilt example.
