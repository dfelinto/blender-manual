
Vertex Painting
***************

Vertex Painting is a simple way of painting color onto an object,
by directly manipulating the color of vertices, rather than textures,
and is fairly straightforward.

When a vertex is painted,
the colour of the vertex is modified according to the rules of the 'brush'. The color of all
visible planes and edges attached to the vertex are then modified with a gradient to the color
of the other connected vertices. (Note that the color of non-visible faces are not modified).

Vertex colors can be painted by first going into Edit Mode, then switching to :guilabel:`Vertex Paint Mode`; however, it will not show up in the render unless you check "Vertex Color Paint" in the Materials  `Options <http://wiki.blender.org/index.php/User:Sculptorjim/Materials/Properties/Options>`__ Panel.


.. figure:: /images/Doc_2.6_Materials_VertexPaint0.jpg

   Vertex Painting Mode


.. figure:: /images/vertexpaintmat.jpg

   Check this box


Settings
********

The Tools Shelf, shortcut :kbd:`T` contains most of the options for vertex painting.
The following sections describe the controls in each of the available panels.


.. figure:: /images/Doc-2.6-Materials-VertexPaint-ToolShelf-Tools.jpg
   :width: 600px
   :figwidth: 600px

   Settings for vertex painting


Brush
=====

Brush Datablock
   The image, name panel and color selector at the top allows you to select brush presets, rename brushes, as well as add custom brushes, and delete them.
Radius
   Set the radius of the brush
Strength
   Set the strength of the brush's effect.


.. figure:: /images/mix.jpg

   Mix overlay with full strength


**Blend** menu

   Mix
      Mixes RGB values. When set to a strength of 1.0, it will cover the underlying "paint".
   Add
      Adds RGB values. Will eventually turn the entire object white as RGB values accumulate to 1.0-1.0-1.0: Pure White.
   Subtract
      Subtracts RGB values. Usually results in Black.
   Multiply
      Multiplies brush colors by the vertex colors.
   Blur
      Blurs vertex colors.
   Lighten
      Lightens the color of the vertices.


.. figure:: /images/sub.jpg

   Subtract with full strength


   Darken
      Darkens the color of the vertices.


..    Comment: <!--[[Don't delete this space]]--> .


Texture
=======

Use the texture selector at the bottom of the paint panel to select a pre-loaded image or
procedural texture to use as your brush pattern. Note that in order to use it,
you must have a placeholder material defined,
and that particular texture defined using the Material and Texture buttons.
It is not necessary to have that material or texture applied to any mesh anywhere;
it must only be defined.

Brush Mapping Mode
   Sets how the texture is applied to the brush

   View Plane
      In 2D painting, the texture moves with the brush
   Tiled
      The texture is offset by the brush location
   3D
      Same as tiled mode
   Stencil
      Texture is applied only in borders of the stencil.
   Random
      Random applying of texture.

Angle
   This is the rotation angle of the texture brush. It can be changed interactively via :kbd:`ctrl-F` in the 3D view. While in the interactive rotation you can enter a value numerically as well. Can be set to:

   User
      Directly input the angle value.
   Rake
      Angle follows the direction of the brush stroke. Not available with :guilabel:`3D` textures.
   Random
      Angle is randomized.

Offset
   Offset the texture in x, y, and z.

Size
   Set the scale of the texture in each axis.


Stroke
------

Stroke Method
   Allows set the way applying strokes.

   Airbrush
      Flow of the brush continues as long as the mouse click is held, determined by the :guilabel:`Rate` setting.
      If disabled, the brush only modifies the color when the brush changes its location.

      Rate
         Interval between paints for airbrush
   Space
      Creates brush stroke as a series of dots, whose spacing is determined by the :guilabel:`Spacing` setting.

      Spacing
         Represents the percentage of the brush diameter. Limit brush application to the distance specified by spacing.
   Dots
      Apply paint on each mouse move step
   Jitter
      Jitter the position of the brush while painting
Smooth stroke
   Brush lags behind mouse and follows a smoother path. When enabled, the following become active:

   Radius
      Sets the minimun distance from the last point before stroke continues.
   Factor
      Sets the amount of smoothing.
Input Samples
   Average multiple input samples together to smooth the brush stroke.


.. figure:: /images/brushcurves.jpg
   :width: 200px
   :figwidth: 200px

   Various brush curves


Curve
=====

Brush Curves affect how strongly the color is applied depending on distance from the center of
the brush. In other words, they allow you to edit the Falloff of the brush intensity.


Options
*******

.. figure:: /images/Doc-2.6-Materials-VertexPaint-ToolShelf-Options.jpg
   :width: 600px
   :figwidth: 600px

   Options for vertex painting


Overlay
=======

Allows you to customize the display of curve and texture that applied to the brush.


Appearance
==========

Allows you to customize the color of the brush radius outline,
as well as specify a custom icon.


Options
=======

Normals
   Applies the Vertex Normal before painting. This does not usually affect painting.
Spray
   Continues painting for as long as the mouse is held.

Unified Settings
   Size
      All brushes use the same size.
   Strength
      All brushes use the same strength.


