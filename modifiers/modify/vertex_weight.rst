
WeightVGroup Modifiers
======================

.. admonition:: Reference
   :class: refbox

   | Mode:     Any mode
   | Panel:    :guilabel:`Modifiers` (:guilabel:`Modifiers` properties)


Description
-----------

The WeightVGroup modifiers work on a vertex group of the affected object,
by modifying its weights and/or which vertices belong to this group.


 .. warning::

   FIXME - warning body below

 Those modifiers do implicit clamping of weight values in the standard ``[0.0, 1.0]`` range. So all values below **0.0** /above **1.0** will be lost!

There are currently three WeightVGroup modifiers:

-

FIXME(TODO: Internal Link;
[[#Vertex Weight Edit Modifier|Vertex Weight Edit]]
).

-

FIXME(TODO: Internal Link;
[[#Vertex Weight Mix Modifier|Vertex Weight Mix]]
).

-

FIXME(TODO: Internal Link;
[[#Vertex Weight Proximity Modifier|Vertex Weight Proximity]]
).


Common Settings
---------------

.. figure:: /images/ManModifiersWeightVG_mask.jpg
   :width: 300px
   :figwidth: 300px

   The influence/masking part of WeightVGroup modifiers.


The three WeightVGroup modifiers share a few settings,
controlling their influence on the affected vertex group.

:guilabel:`Global Influence`
   The overall influence of the modifier (**0.0** will leave the vertex group's weights untouched, **1.0** is standard influence).

 .. warning::

   FIXME - warning body below

Note that influence only affects weights, adding/removing of vertices to/from vertex group is not prevented by setting this value to **0.0** !

:guilabel:`Vertex Group Mask`
   An additional vertex group, which weights will be pre-multiplied with the global influence value, for each vertex. If a vertex is not in the masking vertex group, its masking weight (and hence its influence) will be null.

:guilabel:`Texture`
   An additional texture, which values will be pre-multiplied with the global influence value, for each vertex. You can choose which channel of the texture to use as values.
   This is a standard texture ID control. When set, it reveals other settings:

   :guilabel:`Texture Coordinates`
      How the texture is mapped to the mesh… You have four choices:

      - :guilabel:`Local`: use local vertices coordinates.
      - :guilabel:`Global`: use the vertices coordinates in the global space.
      - :guilabel:`Object`: use the vertices coordinates in another object's space.
      - :guilabel:`UV`: use an UV layer's coordinates.

   :guilabel:`Use Channel`
      Which channel to use as weight factor source (intensity, RGB, HSV, alpha - the options are quite self-explanatory, I guess…).

   :guilabel:`Object`
      The object to be used as reference for :guilabel:`Object` mapping…

   :guilabel:`UV Layer`
      The UV layer to be used for :guilabel:`UV` mapping…


Viewing Modified Weights
~~~~~~~~~~~~~~~~~~~~~~~~

You will now view the modified weights in :guilabel:`WeightPaint` mode. This also implies that
you'll have to disable the Vertex Weight modifiers if you want to see the original weights of
the vertex group you are editing (provided it is affected by some modifier, obviously).


Vertex Weight Edit Modifier
---------------------------

.. figure:: /images/ManModifiersWeightVGEdit.jpg
   :width: 300px
   :figwidth: 300px

   The WeightVGEdit modifier panel.


This modifier is intended to edit the weights of one vertex group.

The general process is the following, for each vertex:

- [Optional] It does the mapping, either through one of the predefined functions, or a custom mapping curve.
- It applies the influence factor, and optionally the vertex group or texture mask (null values mean original weight, **1.0** ones mean fully mapped weight).
- It applies back the weight to the vertex, and/or it might optionally remove the vertex from the group if its weight is below a given threshold, or add it if it's above a given threshold.


Options
~~~~~~~

:guilabel:`Vertex Group`
   The vertex group to affect.

:guilabel:`Default Weight`
   The default weight to assign to all vertices not in the given vertex group.

:guilabel:`Falloff Type`
   Type of mapping:

   - :guilabel:`Linear` - No mapping.
   - :guilabel:`Custom Curve` - Enables the the curve mapping. This shows up a curve control.
   - :guilabel:`Sharp`, :guilabel:`Smooth`, :guilabel:`Root` and :guilabel:`Sphere` are classical mapping functions, from spikiest to roundest.
   - :guilabel:`Random` - Fully randomizes the weights!
   - :guilabel:`Median Step` - Creates binary weights (**0.0** or **1.0**), with **0.5** as cutting value.

:guilabel:`Group Add`
   Adds vertices with a final weight over :guilabel:`Add Threshold` to the vertex group.

:guilabel:`Group Remove`
   Removes vertices with a final weight below :guilabel:`Rem Threshold` from the vertex group.


Vertex Weight Mix Modifier
--------------------------

.. figure:: /images/ManModifiersWeightVGMix.jpg
   :width: 300px
   :figwidth: 300px

   The WeightVGMix modifier panel.


This modifier mixes a second vertex group (or a simple value) into the affected vertex group,
using different operations.

It also has an option to choose which vertices to work on (all,
only those of the first or second vertex group, etc.).


 .. warning::

   FIXME - warning body below

This implies that it *might* add vertices to the affected vertex group (it will never remove vertices, though); see below for details.‏


Options
~~~~~~~

:guilabel:`Vertex Group A`
   The vertex group to affect.

:guilabel:`Default Weight A`
   The default weight to assign to all vertices not in the given vertex group.

:guilabel:`Vertex Group B`
   The second vertex group to mix into the affected one. Leave it empty if you only want to mix in a simple value.

:guilabel:`Default Weight B`
   The default weight to assign to all vertices not in the given second vertex group.

:guilabel:`Mix Mode`
   How the vertex group weights are affected by the other vertex group's weights. You have seven choices:

   - :guilabel:`Replace weights` just replaces affected weights by the second weights.
   - :guilabel:`Add to weights` adds both values.
   - :guilabel:`Subtract from weights` subtracts the second weights from the affected weights.
   - :guilabel:`Multiply weights` multiplies both weights.
   - :guilabel:`Divide weights` divides the affected weights by the second weights.
   - :guilabel:`Difference` computes the difference between affected weights and second weights (it's just the absolute value of the subtract operation).
   - :guilabel:`Average` computes the average value of both weights.

:guilabel:`Mix Set`
   Which vertices to work on. You have five options:

   - :guilabel:`All vertices` affects all vertices, disregarding the vertex groups content. *This option might add vertices to the affected vertex group.*
   - :guilabel:`Vertices from group A` affects only vertices belonging to the affected vertex group.
   - :guilabel:`Vertices from group B` affects only vertices belonging to the second vertex group. *This option might add vertices to the affected vertex group.*
   - :guilabel:`Vertices from one group` affects only vertices belonging to at least one of the vertex groups. *This option might add vertices to the affected vertex group.*
   - :guilabel:`Vertices from both groups` affects only vertices belonging to both vertex groups.


Vertex Weight Proximity Modifier
--------------------------------

.. figure:: /images/ManModifiersWeightVGProximity.jpg
   :width: 300px
   :figwidth: 300px

   The WeightVGProximity modifier panel.


This modifier sets the weights of the given vertex group,
based on the distance between the object (or its vertices), and another target object
(or its geometry).


Options
~~~~~~~

:guilabel:`Vertex Group`
   The vertex group to affect.

:guilabel:`Target Object`
   The object from which to compute distances.

Proximity mode

   - :guilabel:`Object Distance` will use the distance between the modified mesh object and the target object as weight for all vertices in the affected vertex group.
   - :guilabel:`Geometry Distance` will use the distance between each vertex and the target object, or its geometry.

The :guilabel:`Geometry Distance` mode has three additional options,
to use the target object's geometry instead of its center location
(if you enable more than one of them, the shortest computed distance will be used).
If the target object has no geometry (e.g. an empty or camera one),
it will silently fall back to the default :guilabel:`Object Distance` behavior.

:guilabel:`Vertex`
   This will set each vertex's weight from its distance to the nearest vertex of the target object.

:guilabel:`Edge`
   This will set each vertex's weight from its distance to the nearest edge of the target object.

:guilabel:`Face`
   This will set each vertex's weight from its distance to the nearest face of the target object.

:guilabel:`Lowest Dist`
   Distance mapping to **0.0** weight. It can be above :guilabel:`Highest Dist` for reversed mapping effects.

:guilabel:`Highest Dist`
   Distance mapping to **1.0** weight. It can be below :guilabel:`Lowest Dist` for reversed mapping effects.

:guilabel:`Falloff Type`
   Some predefined mapping functions, see
   FIXME(TODO: Internal Link; [[#Vertex Weight Edit|the Vertex Weight Edit part above]]).


Examples
--------

Using Distance from a Target Object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a first example,
let's dynamically control a :guilabel:`Wave` modifier with a modified vertex group.

Add a :guilabel:`Grid` mesh, with many vertices (e.g. a **100×100** vertices),
and **10** BU side-length. Switch to :guilabel:`Edit` mode (:kbd:`tab`),
and in the :guilabel:`Object Data` properties, :guilabel:`Vertex Groups` panel,
add a vertex group. Assign to it all your mesh's vertices (with e.g. a **1.0** weight).
Go back to :guilabel:`Object` mode.

Then, go to the :guilabel:`Modifiers` properties,
and add a :guilabel:`Vertex Weight Proximity` modifier.
Set the mode to :guilabel:`Object Distance`. Select your vertex group,
and the target object you want (here I used the lamp).

You will likely have to adjust the linear mapping of the weights produced by the
:guilabel:`Vertex Weight Proximity` modifier. To do so, edit :guilabel:`Lowest Dist` and
:guilabel:`Highest Dist` so that the first corresponds to the distance between your target
object and the vertices you want to have lowest weight,
and similarly with the second and highest weight…

Now add a :guilabel:`Wave` modifier, set it to your liking,
and use the same vertex group to control it.

Animate your target object, making it move over the grid. As you can see, the waves are only
visible around the reference object! Note that you can insert a :guilabel:`Vertex Weight Edit`
modifier before the :guilabel:`Wave` one,
and use its :guilabel:`Custom Curve` mapping to get larger/narrower "wave influence's slopes".


FIXME(Tag Unsupported:vimeo;
<vimeo>30187079</vimeo>
)

`The Blender file <http://wiki.blender.org/index.php/Media:ManModifiersWeightVGroupEx.blend>`__, ``TEST_1`` scene.


Using Distance from a Target Object's Geometry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We're going to illustrate this with a :guilabel:`Displace` modifier.

Add a **10×10** BU **100×100** vertices grid, and in :guilabel:`Edit` mode,
add to it a vertex group containing all of its vertices, as above.
You can even further sub-divide it with a first :guilabel:`Subsurf` modifier.

Now add a curve circle, and place it **0.25** BU above the grid. Scale it up a bit (e.g.
**4.0**).

Back to the grid object, add to it a :guilabel:`Vertex Weight Proximity` modifier,
in :guilabel:`Geometry Distance` mode. Enable :guilabel:`Edge`
(if you use :guilabel:`Vertex` only, and your curve has a low U definition,
you would get wavy patterns, see (*Wavy patterns*)).


+---------------------------------------------------------------+--------------------------------------------------------------------------+
+**Wavy patterns.**                                                                                                                        +
+---------------------------------------------------------------+--------------------------------------------------------------------------+
+.. figure:: /images/ManModifiersWeightVGroupGeometryEX1.0PF.jpg|.. figure:: /images/ManModifiersWeightVGroupGeometryEX1.0PFWavyWeights.jpg+
+   :width: 300px                                               |   :width: 300px                                                          +
+   :figwidth: 300px                                            |   :figwidth: 300px                                                       +
+                                                               |                                                                          +
+   Distance from edges.                                        |   Distance from vertices.                                                +
+---------------------------------------------------------------+--------------------------------------------------------------------------+


Set the :guilabel:`Lowest Dist` to **0.2**, and the :guilabel:`Highest Dist` to **2.0**,
to map back the computed distances into the regular weight range.

Add a third :guilabel:`Displace` modifier and affect it the texture you like. Now,
we want the vertices of the grid nearest to the curve circle to remain undisplaced.
As they will get weights near zero,
this means that you have to set the :guilabel:`Midlevel` of the displace to **0.0**.
Make it use our affected vertex group,
and that's it! Your nice mountains just shrink to a flat plane near the curve circle.

As in the previous example,
you can insert a :guilabel:`Vertex Weight Edit` modifier before the :guilabel:`Displace` one,
and play with the :guilabel:`Custom Curve` mapping to get a larger/narrower "valley"…


+----------------------------------------------------------------+---------------------------------------------------------------+---------------------------------------------------------------+
+:guilabel:`Curve Map` **variations.**                                                                                                                                                           +
+----------------------------------------------------------------+---------------------------------------------------------------+---------------------------------------------------------------+
+.. figure:: /images/ManModifiersWeightVGroupGeometryEX-5.0PF.jpg|.. figure:: /images/ManModifiersWeightVGroupGeometryEX1.0PF.jpg|.. figure:: /images/ManModifiersWeightVGroupGeometryEX5.0PF.jpg+
+   :width: 200px                                                |   :width: 200px                                               |   :width: 200px                                               +
+   :figwidth: 200px                                             |   :figwidth: 200px                                            |   :figwidth: 200px                                            +
+                                                                |                                                               |                                                               +
+   Concave-type mapping curve.                                  |   No mapping curve (linear).                                  |   Convex-type mapping curve.                                  +
+----------------------------------------------------------------+---------------------------------------------------------------+---------------------------------------------------------------+


.. figure:: /images/ManModifiersWeightVGroupGeometryEXRemVerts.jpg
   :width: 200px
   :figwidth: 200px

   Vertices with a computed weight below 0.1 removed from the vertex group.


You can also add a fifth :guilabel:`Mask` modifier,
and enable :guilabel:`Vertex Weight Edit` 's :guilabel:`Group Remove` option,
with a :guilabel:`Rem Threshold` of **0.1**, to see the bottom of your valley disappear.


FIXME(Tag Unsupported:vimeo;
<vimeo>30188564</vimeo>
)

`The Blender file <http://wiki.blender.org/index.php/Media:ManModifiersWeightVGroupEx.blend>`__, ``TEST_2`` scene.


Using a Texture and the Mapping Curve
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we are going to create a sort of strange alien wave (yes,
another example with the :guilabel:`Wave` modifier… but it's a highly visual one;
it's easy to see the vertex group effects on it…).

So as above, add a **100×100** grid. This time, add a vertex group,
but without assigning any vertex to it - we'll do this dynamically.

Add a first :guilabel:`Vertex Weight Mix` modifier,
set the :guilabel:`Vertex Group A` field with a :guilabel:`Default Weight A` of **0.0**,
and set :guilabel:`Default Weight B` to **1.0**.
Leave the :guilabel:`Mix Mode` to :guilabel:`Replace weights`,
and select :guilabel:`All vertices` as :guilabel:`Mix Set`. This way,
all vertices are affected. As none are in the affected vertex group,
they all have a default weight of **0.0**, which is replaced by the second default weight
(**1.0**). And all those vertices are also added to the affected vertex group.

Now, select or create a masking texture - here I chose a default :guilabel:`Magic` one.
The values of this texture will control how much of the "second weight" (**1.0**)
replaces the "first weight" (**0.0**)… In other words, they are taken as weight values!

You can then select which texture coordinates and channel to use.
Leave the mapping to the default :guilabel:`Local` option, and play with the various channels…


+--------------------------------------------------------------+--------------------------------------------------------+---------------------------------------------------------------+
+**Texture channel variations.**                                                                                                                                                        +
+--------------------------------------------------------------+--------------------------------------------------------+---------------------------------------------------------------+
+.. figure:: /images/ManModifiersWeightVGroupTexExIntensity.jpg|.. figure:: /images/ManModifiersWeightVGroupTexExRed.jpg|.. figure:: /images/ManModifiersWeightVGroupTexExSaturation.jpg+
+   :width: 200px                                              |   :width: 200px                                        |   :width: 200px                                               +
+   :figwidth: 200px                                           |   :figwidth: 200px                                     |   :figwidth: 200px                                            +
+                                                              |                                                        |                                                               +
+   Using intensity.                                           |   Using Red.                                           |   Using Saturation.                                           +
+--------------------------------------------------------------+--------------------------------------------------------+---------------------------------------------------------------+


Don't forget to add a :guilabel:`Wave` modifier, and select your vertex group in it!

You can use the weights created this way directly,
but if you want to play with the curve mapping,
you must add the famous :guilabel:`Vertex Weight Edit` modifier,
and enable its :guilabel:`Custom Curve` mapping.

By default, it's a one-to-one linear mapping - in other words,
it does nothing! Change it to something like in (*A customized mapping curve*),
which maps ``[0.0, 0.5]`` to ``[0.0, 0.25]`` and ``[0.5,
1.0]`` to ``[0.75, 1.0]``, thus producing nearly only weights below **0.25**,
and above **0.75** : this creates great "walls" in the waves…


+--------------------------------------------------------------+--------------------------------------------------------+------------------------------------------------------------+
+**Custom mapping curve.**                                                                                                                                                           +
+--------------------------------------------------------------+--------------------------------------------------------+------------------------------------------------------------+
+.. figure:: /images/ManModifiersWeightVGroupTexExCMapCurve.jpg|.. figure:: /images/ManModifiersWeightVGroupTexExRed.jpg|.. figure:: /images/ManModifiersWeightVGroupTexExRedCMap.jpg+
+   :width: 200px                                              |   :width: 200px                                        |   :width: 200px                                            +
+   :figwidth: 200px                                           |   :figwidth: 200px                                     |   :figwidth: 200px                                         +
+                                                              |                                                        |                                                            +
+   A customized mapping curve.                                |   Custom Mapping disabled.                             |   Custom Mapping enabled.                                  +
+--------------------------------------------------------------+--------------------------------------------------------+------------------------------------------------------------+


FIXME(Tag Unsupported:vimeo;
<vimeo>30188814</vimeo>
)

`The Blender file <http://wiki.blender.org/index.php/Media:ManModifiersWeightVGroupEx.blend>`__, ``TEST_4`` scene.


See Also
--------

- The `Development page <http://wiki.blender.org/index.php/User:Mont29/WeightVGroup/Dev>`__.
