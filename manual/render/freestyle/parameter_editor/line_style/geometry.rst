
Geometry
********

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Geometry_UI.jpg
   :width: 300px
   :figwidth: 300px

   Line Style Geometry Overall UI


In this tab you control the geometry of your strokes.


Modifiers
=========

There are thirteen geometry modifiers available.
These modifiers have no mix nor influence settings,
as they always completely apply to the strokes' geometry (like object modifiers do). They take
the resulting two-dimensional strokes from the Freestyle line set and displace or deform them
in various ways.

As with other modifier stacks in Blender, they are applied from top to bottom.


2D Offset
---------

The :guilabel:`2D Offset` modifier adds some two-dimensional offsets to the stroke backbone
geometry. It has two sets of independent options/effects:


.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Geometry_2D_Offset.jpg
   :width: 200px
   :figwidth: 200px

   Line Style Geometry's 2D Offset modifier


Start and End
   These two options add the given amount of offset to the start (or end) point of the stroke, along the (2D)
   normal at those points. The effect is blended over the whole stroke, so if you, for example,
   set only :guilabel:`Start` to **50**, the start of the stroke is offset 50 pixels along its normal,
   the middle of the stroke, 25 pixels along its own normal, and the end point isn't moved.

X and Y
   These two options simply add a constant horizontal and/or vertical offset to the whole stroke.


2D Transform
------------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Geometry_2D_Transform.jpg
   :width: 200px
   :figwidth: 200px

   Line Style Geometry's 2D Transform modifier


The :guilabel:`2D Transform` modifier applies two-dimensional scaling and/or rotation to the
stroke backbone geometry. Scale is applied before rotation.

The center (pivot point) of these 2D transformations can be:

Stroke Center
   The median point of the stroke.
Stroke Start
   The beginning point of the stroke.
Stroke End
   The end point of the stroke.
Stroke Point Parameter
   The :guilabel:`Stroke Point Parameter` factor controls where along the stroke the pivot point is
   (``0.0`` means start point; ``1.0`` end point).
Absolute 2D Point
   The :guilabel:`Pivot X` and :guilabel:`Pivot Y` allows you to define the position of the pivot point in the final
   render (from the bottom left corner). **WARNING** : Currently,
   you have to take into account the *real* render size, i.e. resolution **and** resolution percentage!

Scale X and Scale Y
   The scaling factors, in their respective axes.

Rotation Angle
   The rotation angle.


.. figure:: /images/2D_Transform.jpg
   :width: 400px
   :figwidth: 400px

   2D Transform modifier
   `File:Toycar_Three_Contours.zip <http://wiki.blender.org/index.php/File:Toycar_Three_Contours.zip>`__


Backbone Stretcher
------------------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Geometry_Backbone_Stretcher.jpg
   :width: 200px
   :figwidth: 200px

   Line Style Geometry's Backbone Stretcher modifier


The :guilabel:`Backbone Stretcher` modifier stretches (adds some length to)
the beginning and end of the stroke.

Backbone Length
   Length to add to the strokes' ends.


Bezier Curve
------------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Geometry_Bezier_Curve.jpg
   :width: 200px
   :figwidth: 200px

   Line Style Geometry's Bezier Curve modifier


The :guilabel:`Bezier Curve` modifier replaces the stroke by a Bezier approximation of it.

Error
   The maximum distance allowed between the new Bezier curve and the original stroke.


.. figure:: /images/toycar_bezier.jpg
   :width: 400px
   :figwidth: 400px

   Bezier Curve modifier demo by T.K.
   `File:toycar_bezier.zip <http://wiki.blender.org/index.php/File:toycar_bezier.zip>`__


Blueprint
---------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Geometry_Blueprint.jpg
   :width: 200px
   :figwidth: 200px

   Line Style Geometry's Blueprint modifier


The :guilabel:`Blueprint` modifier produces blueprint-like strokes using either circular,
elliptical, or square contours. A blueprint here refers to those lines drawn at the beginning
of free-hand drawing to capture the silhouette of objects with a simple shape such as circles,
ellipses and squares.

Shape
   Which base shapes to use for this blueprint: :guilabel:`Circles`, :guilabel:`Ellipses` or :guilabel:`Squares`.

Rounds
   How many rounds are generated, as if the pen draws the same stroke several times
   (i.e. how many times the process is repeated).

Random Radius and Random Center
   For the :guilabel:`Circles` and :guilabel:`Ellipses` shapes.
   Adds some randomness to each round in the relevant aspect.
   Using more than one round with no randomness would be meaningless, as they would draw over each other exactly.

Backbone Length and Random Backbone
   For the :guilabel:`Squares` shapes.
   The first adds some extra length to each edge of the generated squares (also affected by the second parameter).
   The second adds some randomness to the squares.

Note that the :guilabel:`Min 2D Length` feature from the :guilabel:`Strokes` settings is quite
handy here, to avoid the noise generated by small strokes...


Guiding Lines
-------------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Geometry_Guiding_Lines.jpg
   :width: 200px
   :figwidth: 200px

   Line Style Geometry's Guiding Lines modifier


The :guilabel:`Guiding Lines` modifier replaces a stroke by a straight line connecting both of
its ends.

Offset
   Offset the start and end points along the original stroke, before generating the new straight one.

This modifier will produce reasonable results when strokes are short enough,
because shorter strokes are more likely to be well approximated by straight lines. Therefore,
it is recommended to use this modifier together with one of the splitting options
(by 2D angle or by 2D length) from the :guilabel:`Strokes` panel.


.. figure:: /images/Toycar_Guiding_Line.jpg
   :width: 400px
   :figwidth: 400px

   Guiding Lines modifier Demo by T.K.
   `File:Toycar_Guiding_Line.zip <http://wiki.blender.org/index.php/File:Toycar_Guiding_Line.zip>`__


Perlin Noise 1D
---------------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Geometry_Perlin_Noise_1D.jpg
   :width: 200px
   :figwidth: 200px

   Line Style Geometry's Perlin Noise 1D modifier


The :guilabel:`Perlin Noise 1D` modifier adds one-dimensional Perlin noise to the stroke.

Frequency
   How dense the noise is (kind of a scale factor along the stroke).

Amplitude
   How much the noise distorts the stroke in the :guilabel:`Angle` direction.

Seed
   The seed of the random generator (the same seed over a stroke will always give the same result).

Octaves
   The "level of detail" of the noise.

Angle
   In which direction the noise is applied (``0.0`` is fully horizontal).


Perlin Noise 2D
---------------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Geometry_Perlin_Noise_2D.jpg
   :width: 200px
   :figwidth: 200px

   Line Style Geometry's Perlin Noise 2D modifier


The :guilabel:`Perlin Noise 2D` modifier adds one-dimensional Perlin noise to the stroke.

Its settings are exactly the same as the :guilabel:`Perlin Noise 1D` modifier.

TODO: What's the difference between those two modifiers?


Polygonization
--------------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Geometry_Polygonization.jpg
   :width: 200px
   :figwidth: 200px

   Line Style Geometry's Polygonization modifier


The :guilabel:`Poligonization` modifier simplifies strokes as much as possible
(in other words, it transforms smooth strokes into jagged polylines).

Error
   The maximum distance allowed between the new simplified stroke and the original one
   (the larger this value is, the more jagged/approximated the resulting polylines are).


Sampling
--------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Geometry_Sampling.jpg
   :width: 200px
   :figwidth: 200px

   Line Style Geometry's Sampling modifier


The :guilabel:`Sampling` modifier changes the definition, precision of the stroke,
for the following modifiers.

Sampling
   The smaller this value, the more precise are the strokes.
   Be careful; too small values will require a huge amount of time and memory during render!


Sinus Displacement
------------------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Geometry_Sinus_Displacement.jpg
   :width: 200px
   :figwidth: 200px

   Line Style Geometry's Sinus Displacement modifier


The :guilabel:`Sinus Displacement` modifier adds a sinusoidal displacement to the stroke.

Wavelength
   How wide the undulations are along the stroke.

Amplitude
   How high the undulations are across the stroke.

Phase
   Allows "offsetting" ("moving") the undulations along the stroke.


.. figure:: /images/Toycar_Sinus_Displacement.jpg
   :width: 400px
   :figwidth: 400px

   Sinus Displacement modifier demo by T.K.
   `File:Toycar_Sinus.zip <http://wiki.blender.org/index.php/File:Toycar_Sinus.zip>`__


Spatial Noise
-------------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Geometry_Spatial_Noise.jpg
   :width: 200px
   :figwidth: 200px

   Line Style Geometry's Spatial Noise modifier


The :guilabel:`Spatial Noise` modifier adds some spatial noise to the stroke.

TODO: definition of "spatial  noise"!

Amplitude
   How much the noise distorts the stroke.

Scale
   How wide the noise is along the stroke.

Octaves
   The level of detail of the noise.

Smooth
   When enabled, apply some smoothing over the generated noise.

Pure Random
   When disabled, the next generated random value depends on the previous one;
   otherwise they are completely independent. Disabling this setting gives a more "consistent" noise along a stroke.


Tip Remover
-----------

.. figure:: /images/Manual-2.6-Render-Freestyle-Line_Style_Geometry_Tip_Remover.jpg
   :width: 200px
   :figwidth: 200px

   Line Style Geometry's Tip Remover modifier


The :guilabel:`Tip Remover` modifier removes a piece of the stroke at its beginning and end.

Tip Length
   Length of stroke to remove at both of its tips.
