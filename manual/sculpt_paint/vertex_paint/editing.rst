
*******
Editing
*******

.. admonition:: Reference
   :class: refbox

   :Mode:      Vertex Paint Mode
   :Menu:      :menuselection:`Paint`

Set Vertex Colors :kbd:`Shift-K`
   Fill the active vertex color layer with the current paint color.
Smooth Vertex Colors
   Smooth colors across vertices.
Dirty Vertex Colors
   Blur Strength
      Blur strength per iteration.
   Blur Iterations
      Number of times to blur the colors (higher blurs more).
   Highlight Angle
      Clamps the angle for convex areas of the mesh.
      Lower values increase the contrast but can result in clamping.
      90 means flat, 180 means infinitely pointed.
   Dirt Angle
      Clamps the angle for concave areas of the mesh.
      Higher values increase the contrast but can result in clamping.
      90 means flat, 0 means infinitely deep.
   Dirt Only
      When active it won't calculate cleans for convex areas.
   Normalize
      Choose optimal contrast by effectively lowering
      *Highlight Angle* and increasing *Dirt Angle* automatically.
      Disabling *Normalize* allows getting consistent results across multiple
      objects.

Vertex Color from Weight
   Converts the active weight into grayscale vertex colors.
Invert
   Invert RGB values.
Levels
   Adjust levels of vertex colors.
Hue Saturation Value
   Adjust vertex color HSV values.
Bright/Contrast
   Adjust vertex color brightness/contrast.
