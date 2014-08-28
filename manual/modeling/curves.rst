
Curves
******

.. figure:: /images/Manual-Part-II-LogoFinal.jpg

   Bird logo made from Bezier curves.


Curves and :doc:`Surfaces </modeling/surfaces>` are particular types of Blender Objects. They are expressed by mathematical functions rather than a series of points. Blender offers both
FIXME(TODO: Internal Link;
[[#Beziers|Bezier]]
) curves and
FIXME(TODO: Internal Link;
[[#NURBS|NURBS]]
) curves and surfaces. NURBS stands for "Non-Uniform Rational B-Splines". Both Bezier curves and NURBS curves and surfaces are defined in terms of a set of "control points" (or "control vertices") which define a "control polygon".

The main advantage to using curves instead of polygonal meshes is that curves are defined by
less data and so can produce excellent results using less memory and storage space at modeling
time. However, this procedural approach to surfaces can increase demands at render time.

Certain modeling techniques, such as :doc:`extruding a profile along a path </modeling/curves/editing/advanced#curve_extrusion>`, are possible only using curves. On the other hand, when using curves, vertex-level control is more difficult and if fine control is necessary, :doc:`mesh editing </modeling/meshes/editing>` may be a better modeling option.

Bezier curves are the most commonly used curves for designing letters or logos. They are also widely used in animation, both as :doc:`paths </animation/techs/object/path>` for objects to move along and as :doc:`F-curves </animation/editors/graph/fcurves>` to change the properties of objects as a function of time.


Tutorials
---------

:doc:`Create the bird logo with Bezier Curves » </ls/modeling/curves/bézier>`

:doc:`Skinning: Making a surface with two or more curves » </ls/modeling/surfaces/skinning>`


Curve Primitives
================

.. figure:: /images/Modeling_Curves_add-curve-menu.jpg

   Add Curve menu.


In Object mode, the :guilabel:`Add Curve` menu,
Blender provides five different curve primitives:

:guilabel:`Bezier Curve`
   Adds an open 2D Bezier curve with two control points.
:guilabel:`Bezier Circle`
   Adds a closed, circle-shaped 2D Bezier curve (made of four control points).
:guilabel:`NURBS Curve`
   Adds an open 2D NURBS curve, with four control points, with :guilabel:`Uniform` knots.
:guilabel:`NURBS Circle`
   Adds a closed, circle-shaped 2D NURBS curve (made of eight control points).
:guilabel:`Path`
   Adds a NURBS open 3D curve made of five aligned control points, with :guilabel:`Endpoint` knots and the :guilabel:`CurvePath` setting enabled.


Bezier Curves
=============

The main elements used in editing Bezier Curves are the Control Points and Handles. A Segment
(the actual Curve) is found between two Control Points. In the image below, the Control Points
can be found in the middle of the pink line while the Handles comprise the extensions from the
Control Point. By default the arrows on the Segment represents the direction and
**relative** speed and direction of movement Objects will have when moving along the curve.
This can be altered by defining a custom :guilabel:`Speed` Ipo.


.. figure:: /images/Modeling_Curves_control-points-handles.jpg

   Bezier Curve in Edit mode.


Editing Bezier Curves
---------------------

A Bezier curve can be edited by moving the locations of the Control Points and Handles.

- Add a Curve by :kbd:`shift-a` to bring up the :guilabel:`Add` menu, followed by :menuselection:`Curve --> Bezier`.
- Press :kbd:`TAB` to enter :guilabel:`Edit mode`.
- Select one of the Control Points and move it around. Use :kbd:`LMB` to confirm the new location of the Control Point, or use :kbd:`RMB` to cancel.
- Now select one of the Handles and move it around. Notice how this changes the curvature of the curve.

To add more Control Points

- Select at least two adjacent Control Points.
- Press :kbd:`W` and select :guilabel:`Subdivide`.
- Optionally, you can press :kbd:`F6` immediately after the subdivision to modify the number of subdivisions.

Note that while in :guilabel:`Edit mode` you cannot directly select a Segment. To do so,
select all of the Control Points that make up the Segment you want to move.

There are four Bezier curve handle types.
They can be accessed by pressing :kbd:`V` and selecting from the list that appears,
or by pressing the appropriate hotkey combination. Handles can be rotated, moved,
scaled and shrunk/fattened like any vertex in a mesh.


+-----------------------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
+**Bezier Curve Handle Types**                                                                                                                                                                                                                                                                                                                                +
+-----------------------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
+:guilabel:`Type`             |:guilabel:`Shortcut`|:guilabel:`Usage`                                                                                                                                                                                                                               |:guilabel:`Appearance`                                   +
+-----------------------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
+Automatic                    |:kbd:`V-A`          |This handle has a completely automatic length and direction which is set by Blender to ensure the smoothest result. These handles convert to :guilabel:`Aligned` handles when moved.                                                            |.. figure:: /images/Modeling_Curves_automatic-handles.jpg+
+-----------------------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
+Vector                       |:kbd:`V-V`          |Both parts of a handle always point to the previous handle or the next handle which allows you to create curves or sections thereof made of straight lines or with sharp corners. Vector handles convert to :guilabel:`Free` handles when moved.|.. figure:: /images/Modeling_Curves_vector-handles.jpg   +
+-----------------------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
+Aligned                      |:kbd:`V-L`          |These handles always lie in a straight line, and give a continuous curve without sharp angles.                                                                                                                                                  |.. figure:: /images/Modeling_Curves_aligned-handles.jpg  +
+-----------------------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
+Free                         |:kbd:`V-F`          |The handles are independent of each other.                                                                                                                                                                                                      |.. figure:: /images/Modeling_Curves_free-handles.jpg     +
+-----------------------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+


Additionally,
the :kbd:`V-T` shortcut can be used to toggle between Free and Aligned handle types.


----


Curve Properties
================

Curve Properties can be set from the :guilabel:`Object Data` option in the
:guilabel:`Properties Header` (shown below in blue).


.. figure:: /images/Icon-library_Properties_header-curve.jpg


Shape
-----

.. figure:: /images/Modeling_Curves_shape-panel.jpg

   Curves Shape panel.


:guilabel:`2D and 3D Curves`
   By default, new curves are set to be 3D, which means that Control Points can be placed anywhere in 3D space.
   Curves can also be set to 2D which constrain the Control Points to the Curve's local XY axis.

:guilabel:`Resolution`
   The *resolution* property defines the number of points that are computed between every pair of Control Points.
   Curves can be made more or less smooth by increasing and decreasing the resolution respectively.
   The :guilabel:`Preview U` setting determines the resolution in the 3D viewport while the :guilabel:`Render U` setting
   determines the Curve's render resolution. If :guilabel:`Render U` is set to zero (0),
   then the :guilabel:`Preview U` setting is used for both the 3D viewport and render resolution.



.. figure:: /images/Modeling_Curves_shape-resolution.jpg

   Curves with a resolution of 3 (left) and 12 (right).


:guilabel:`Twisting`
   A 3D Curve has Control Points that are not located on the Curve's local XY plane. This gives the Curve a twist which can affect the Curve normals. You can alter how the twist of the Curve is calculated by choosing from :guilabel:`Minimum, Tangent` and :guilabel:`Z-Up` options from the drop-down menu.


.. figure:: /images/Modeling_Curves_shape-twist.jpg

   Curves with a twist of minimum (left) and tangent (right).


:guilabel:`Fill`
   Fill determines the way a Curve is displayed when it is Beveled (see below for details on Beveling). When set to :guilabel:`Half` (the default) the Curve is displayed as half a cylinder. The :guilabel:`Fill Deformed` option allows you to indicate whether the Curve should be filled before or after (default) applying any Shape Keys or Modifiers.


.. figure:: /images/Modeling_Curves_shape-fill.jpg

   Curves with a fill of half (left) and full (right).


:guilabel:`Path/Curve-Deform`
   These options are primarily utilized when using a Curve as a Path or when using the Curve Deform property. The :guilabel:`Radius, Stretch` and :guilabel:`Bounds Clamp` options control how Objects use the Curve and are dealt with in more detail in the appropriate links below.

:doc:`Read more about Basic Curve Editing » </modeling/curves/editing>`
:doc:`Read more about Paths » </animation/techs/object/path>`
:doc:`Read more about Curve Deform » </modeling/curves/editing/advanced>`


Geometry
--------

.. figure:: /images/Modeling_Curves_geometry-panel.jpg

   Curves Geometry panel.


:guilabel:`Modification`
   :guilabel:`Offset`
      By default, text Objects are treated as curves. The Offset option will alter the space between letters.
   :guilabel:`Extrude`
      Will extrude the curve along both the positive and negative local Z axes.
:guilabel:`Bevel`
   :guilabel:`Depth`
      Changes the size of the bevel


.. figure:: /images/Modeling_Curves_geometry-bevel-depth.jpg

   A Curve with different Bevel depths applied.


   :guilabel:`Resolution`
      Alters the smoothness of the bevel


.. figure:: /images/Modeling_Curves_geometry-bevel-resolution.jpg

   A Curve with different resolutions applied.


:guilabel:`Taper Object`
   Tapering a Curve causes it to get thinner towards one end. You can also alter the proportions of the Taper throughout the tapered object by moving/scaling/rotating the Control Points of the Taper Object. The Taper Object can only be another Curve. Editing the Handles and Control Points of the Taper Object will cause the original Object to change shape.


.. figure:: /images/Modeling_Curves_geometry-taper.jpg

   A Curve before (left) and after (right) a Bezier Curve Taper Object was applied.


:guilabel:`Bevel Object`
   Beveling a Bezier Curve with a Bezier Curve as the Bevel Object generally gives it the appearance of a plane, while using a Bezier Circle as the Bevel Object will give it the appearance of a cylinder. The Bevel Object can only be another Curve. Editing the Handles and Control Points of the Bevel Object will cause the original Object to change shape. Given the options available, it is best to experiment and see the results of this operation.


.. figure:: /images/Modeling_Curves_geometry-bevel.jpg

   A Curve with the Bevel Object as a Bezier Curve (left) and as a Bezier Circle (right).


:guilabel:`Fill Caps`
   Seals the ends of a beveled Curve.
:guilabel:`Map Taper`
   For Curves using a Taper Object and with modifications to the :guilabel:`Start/End Bevel Factor`
   the :guilabel:`Map Taper` option will apply the taper to the beveled part of the Curve (not the whole Curve).


.. figure:: /images/Modeling_Curves_geometry-map-taper.jpg

   A Curve without (left) and with (right) Map Taper applied.


:guilabel:`Start Bevel Factor` and :guilabel:`End Bevel Factor`
   These options determine where to start the Bevel operation on the Curve being beveled.
   Increasing the :guilabel:`Start Bevel Factor` to 0.5 will start beveling the Curve 50% of the distance from the start
   of the Curve (in effect shortening the Curve).
   Decreasing the :guilabel:`End Bevel Factor` by 0.25 will start beveling the Curve 25% of the distance from the end
   of the Curve (again, shortening the Curve).



.. figure:: /images/Modeling_Curves_geometry-bevel-start-end-factor.jpg

   A Curve with no Bevel factor applied (left), with a 50% Start Bevel Factor (middle) and with a 25% End Bevel Factor (right).


:doc:`Read more about Advanced Curve Editing » </modeling/curves/editing/advanced>`


Path Animation
--------------

The Path Animation settings can be used to determine how Objects move along a certain path.
See the link below for further information.

:doc:`Read more about utilizing Curves for paths during animation » </animation/techs/object/path>`


Active Spline
-------------

.. figure:: /images/Modeling_Curves_active-spline-panel.jpg

   Curves Active Spline panel.


The :guilabel:`Active Spline` panel becomes available during :guilabel:`Edit mode`.

:guilabel:`Cyclic`
   Closes the Curve.
:guilabel:`Resolution`
   Alters the smoothness of of each segment by changing the number of subdivisions.
:guilabel:`Interpolation`
   :guilabel:`Tilt`
      Alters how the tilt of a segment is calculated.
   :guilabel:`Radius`
      Alters how the radius of a Beveled Curve is calculated. The effects are easier to see after Shrinking/Fattening a control point :kbd:`alt-s`.
   :guilabel:`Smooth`
      Smooths the normals of the Curve


----


Non-Uniform Rational B-Splines (NURBS)
======================================

One of the major differences between Bezier Objects and NURBS Objects is that Bezier Curves
are approximations. For example, a Bezier circle is an *approximation* of a circle,
whereas a NURBS circle is an *exact* circle.
NURBS theory can be a *very* complicated topic. For an introduction,
please consult the `Wikipedia page. <http://en.wikipedia.org/wiki/NURBS>`__ In practice,
many of the Bezier curve operations discussed above apply to NURBS curves in the same manner.
The following text will concentrate only on those aspects that are unique to NURBS curves.


Editing NURBS Curves
--------------------

A NURBS Curve is edited by moving the location of the Control Points.

- Place a Curve by :kbd:`shift-a` to bring up the Add menu, followed by :menuselection:`Curve --> NURBS curve`.
- Press :kbd:`TAB` to enter :guilabel:`Edit mode`.
- Select one of the Control Points and move it around. Use :kbd:`LMB` to confirm the new location of the Control Point, or use :kbd:`RMB` to cancel.
- If you want to add additional Control Points, select both of them, press :kbd:`W` and select :guilabel:`Subdivide`. Press :kbd:`F6` immediately after to determine how many subdivisions to make.


Active Spline
-------------

.. figure:: /images/Modeling_Curves_nurbs-active-spline-panel.jpg

   NURBS Active Spline panel.


One of the characteristics of a NURBS object is the *knot vector*. This is a sequence of
numbers used to determine the influence of the control points on the curve.
While you cannot edit the knot vectors directly, you can influence them through the
:guilabel:`Endpoint` and :guilabel:`Bezier` options in the Active Spline panel. Note that the
:guilabel:`Endpoint` and :guilabel:`Bezier` settings only apply to open NURBS curves.

:guilabel:`Cyclic`
   Makes the NURBS curve cyclic.


.. figure:: /images/Modeling_Curves_nurbs-cyclic.jpg

   A NURBS curve with Cyclic applied.


:guilabel:`Bezier`
   Makes the NURBS curve act like a Bezier curve.
:guilabel:`Endpoint`
   Makes the curve contact the end control points. Cyclic must be disabled for this option to work.


.. figure:: /images/Modeling_Curves_nurbs-endpoint.jpg
   :width: 511px
   :figwidth: 511px

   A NURBS curve with Endpoint enabled.


:guilabel:`Order`
   The order of the NURBS curve determines the area of influence of the control points over the curve. Higher order values means that a single control point has a greater influence over a greater relative proportion of the curve. The valid range of :guilabel:`Order` values is 2-6 depending on the number of control points present in the curve.


.. figure:: /images/Modeling_Curves_nurbs-order.jpg
   :width: 511px
   :figwidth: 511px

   NURBS curves with orders of 2 (left), 4 (middle) and 6 (right).


Path

----


As mentioned above, Curves are often used as :doc:`paths </animation/techs/object/path>`. Any curve can be used as a Path if the :guilabel:`Path Animation` option is selected.

The Path option available from the :guilabel:`Add Curve` menu is identical to a 3D NURBS
curve, except that you do not have access to the :guilabel:`Active Spline` panel.

