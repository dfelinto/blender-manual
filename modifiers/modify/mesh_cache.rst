
Mesh Cache Modifier
===================


.. admonition:: Reference
   :class: refbox

   | Mode:     Any mode
   | Panel:    :guilabel:`Modifiers`


Description
-----------

The :guilabel:`Mesh Cache` modifier is used so animated mesh data can be applied to a mesh and
played back, deforming the mesh.

This works in a similar way to shape-keys but is aimed at playing back external files and is
often used for interchange between applications.

When using this modifier, the vertex locations are overwritten.


Options
-------


.. figure:: /images/26-Manual-Modifiers-MeshCache.jpg

   Mesh Cache modifier


:guilabel:`Format`
   The input file format (currently **MDD** and **PC2** are supported).

:guilabel:`File Path`
   Path to the cache file.

:guilabel:`Influence`
   Factor to adjust the influence of the modifiers deformation, useful for blending in/out from the cache data.
:guilabel:`Deform Mode`
   This setting defaults to 'Overwrite' which will replace the vertex locations with those in the cache file.
However you may want to use shape-keys, for example, and mix them with the mesh-cache. In this case you can select the 'Deform' option which integrates deformations with the mesh-cache result.
*Note - this feature is limited to making smaller, isolated edits and won't work for re-posing limbs, for example.*
:guilabel:`Interpolation`
   None or Linear which will blend between frames; use linear when the frames in the cache file don't match up exactly with the frames in the blend file.

Time Mapping:
:guilabel:`Time Mode`
   Select how time is calculated.

- **Frame:** Allows you to control the frames, which will ignore timing data in the file but is often useful since it gives simple control.
- **Time:** Evaluates time in seconds, taking into account timing information from the file (offset and frame-times).
- **Factor:** Evaluates the entire animation as a value from [0 - 1].

:guilabel:`Play Mode`
   Select how playback operates.

- **Scene:** Use the current frame from the scene to control playback.
  - **Frame Start:** Play the cache starting from this frame.
  - **Frame Scale:** Scale time by this factor (applied after the start value).
- **Custom:** Control animation timing manually.
  - **Evaluation Value:** Property used for animation time, this gives more control of timing - typically this value will be animated.

Axis Mapping:
Axis transformation for the input coordinates.

:guilabel:`Forward/Up Axis`
   The axis for forward and up used in the source file.
*Often different applications have different axis defaults for up/down front/back, so it's common to have to switch these on import.*
:guilabel:`Flip Axis`
   In rare cases you may also need to flip the coordinates on an axis.


Hints
-----


- Both MDD and PC2 depend on the vertex order on the mesh remaining unchanged; this is a limitation with the method used so take care not to add/remove vertices once this modifier is used.


