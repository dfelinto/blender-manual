
Wave Modifier
*************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Panel:    :guilabel:`Modifiers`


Description
===========

The :guilabel:`Wave` modifier adds an ocean-like motion to the Z coordinate of the object's
vertices/control points. This modifier is available for meshes, lattices, curves,
surfaces and texts, with a few restrictions for non-\ *mesh* objects:

- Activating :guilabel:`Normals` or typing a name in :guilabel:`VGroup` will simply deactivate the modifier.
- Even worse, selecting :guilabel:`UV` as texture coordinates will make Blender crash at once!


Options
=======

.. figure:: /images/25-Manual-Modifiers-Wave.jpg

   Wave modifier


.. figure:: /images/25-Manual-Modifiers-Wave-example-Circular.jpg

   Circular wave front


.. figure:: /images/25-Manual-Modifiers-Wave-example-Linear.jpg

   Linear wave front


.. figure:: /images/25-Manual-Modifiers-Wave-example-normals.jpg

   Motion enabled for X and Normals enabled for Y


:guilabel:`Motion`
   :guilabel:`X`, :guilabel:`Y`, :guilabel:`Cyclic`: The wave effect deforms vertices/control points in the Z direction, originating from the given starting point and propagating along the object with circular wave fronts (both :guilabel:`X` and :guilabel:`Y` activated), or with rectilinear wave fronts, then parallel to the axis corresponding to the :guilabel:`X` or :guilabel:`Y` button activated.  :guilabel:`Cyclic` repeats the waves cyclically, rather than a single pulse.

:guilabel:`Normals`
   For meshes only.  Displaces the mesh along the surface normals (instead of the object's Z-axis).

:guilabel:`Time`
   Settings to control time parameters.

   :guilabel:`Offset`
      Time offset in frames.  The frame at which the wave begins (if :guilabel:`Speed` is positive), or ends (if :guilabel:`Speed` is negative). Use a negative frame number to prime and pre-start the waves.
   :guilabel:`Life`
      Duration of animation in frames. Set to zero, loops the animation forever.
   :guilabel:`Damping`
      An additional number of frames in which the wave slowly damps from the :guilabel:`Height` value to zero after :guilabel:`Life` is reached. The dampening occurs for all the ripples and begins in the first frame after the :guilabel:`Life` is over. Ripples disappear over :guilabel:`Damping` frames.

:guilabel:`Position`
   :guilabel:`X` and :guilabel:`Y` coordinates of the center of the waves, in the object's local coordinates.  :guilabel:`Falloff` controls how fast the waves fade out as they travel away from the coordinates above.  Note that selecting a :guilabel:`Start Position Object` effectively cancels the coordinates chosen above, but retains the :guilabel:`Falloff` value.

:guilabel:`Start Position Object`
   Use another object as the reference for the starting position of the wave. Leave blank to disable. Note that you then can animate this object's position, to change the wave's origin across time.

:guilabel:`Vertex Group`
   For meshes only. A vertex group name, used to control the parts of the mesh affected by the wave effect, and to what extent (using vertex weights).

:guilabel:`Texture`
   Use this texture to control the object's displacement level. Animated textures can give very interesting results here.

:guilabel:`Texture Coordinates`
   This menu lets you choose the texture's coordinates for displacement:

   :guilabel:`Local`
      Object's local coordinates.
   :guilabel:`Global`
      Global coordinates.
   :guilabel:`Object`
      Adds an additional field just below, to type in the name of the object from which to get the texture coordinates.
   :guilabel:`UV`
      Adds an extra :guilabel:`UV Layer` drop-down list, to select the UV layer to be used. **Warning:** do not activate this option with non-mesh objects; it seems to make Blender crash.

:guilabel:`Speed`
   The speed, in BU (for "Blender Units") per frame, of the ripple.

:guilabel:`Height`
   The height or amplitude, in BU, of the ripple.

:guilabel:`Width`
   Half of the width, in BU, between the tops of two subsequent ripples (if :guilabel:`Cycl` is enabled). This has an indirect effect on the ripple amplitude - if the pulses are too near to each other, the wave may not reach the **0** Z-position, so in this case Blender actually lowers the whole wave so that the minimum is zero and, consequently, the maximum is lower than the expected amplitude. See
   FIXME(TODO: Internal Link; [[#Technical Details and Hints|technical details]]) below.

:guilabel:`Narrowness`
   The actual width of each pulse: the higher the value the narrower the pulse. The actual width of the area in which the single pulse is apparent is given by ``4/Narrowness``. That is, if :guilabel:`Narrowness` is **1** the pulse is **4** units wide, and if :guilabel:`Narrowness` is **4** the pulse is **1** unit wide.


.. admonition:: Warning
   :class: note

   All the values described above must be multiplied with the corresponding :guilabel:`Scale` values of the object to get the real dimensions.  For example, if the value of :guilabel:`Scale Z` is **2** and the value of :guilabel:`Height` of the waves is **1**, it gives us final waves with a height of **2 BU** !


Technical Details and Hints
===========================

The relationship of the above values is described here:


+--------------------------------------------------------+
+.. figure:: /images/Blender3D_WaveModifierParameters.jpg+
+   :width: 600px                                        +
+   :figwidth: 600px                                     +
+                                                        +
+   Wave front characteristics.                          +
+--------------------------------------------------------+


To obtain a nice wave effect similar to sea waves and close to a sinusoidal wave,
make the distance between following ripples and the ripple width equal; that is,
the :guilabel:`Narrowness` value must be equal to ``2/Width``. E.g.
for :guilabel:`Width` =\ **1**, set :guilabel:`Narrow` to **2**.


