
Overview
********

:guilabel:`Sculpt` Mode is similar to :guilabel:`Edit` Mode in that it is used to alter the shape of a model, but Sculpt Mode uses a very different workflow: instead of dealing with individual elements (vertices, edges, and faces), an area of the model is altered using a brush. In other words, instead of selecting a group of vertices, Sculpt Mode automatically selects vertices based on where the brush is, and modifies them accordingly.


Sculpt Mode
***********

Sculpt mode is selected from the mode menu of the :guilabel:`3D View` header.

Once sculpt mode is activated the :guilabel:`Toolbar` of the :guilabel:`3D View` will change
to sculpt mode specific panels.  The panels in the toolbar will be :guilabel:`Brush`,
:guilabel:`Texture`, :guilabel:`Tool`, :guilabel:`Symmetry`, :guilabel:`Stroke`,
:guilabel:`Curve`, :guilabel:`Appearance`, and :guilabel:`Options`.
Also a red circle will appear that follows the location of the cursor in the 3d view.


.. figure:: /images/2.5_Sculpt_mode_drop_down.jpg

   Sculpt Mode Dropdown.


.. figure:: /images/2.5_Sculpt_brush_circle.jpg

   The cursor in Sculpt Mode.


Sculpt Brushes
**************

Brushes are brush presets.  They are a combination of a 'tool', along with stroke, texture,
and options.

:guilabel:`Sculpt` Mode has sixteen brushes, each of which operates on the model in a unique way. Many can be toggled to have an additive or subtractive effect. They can be selected in the :guilabel:`Tool` menu. The current Brush presets are: Blob, Clay, Crease, Draw, Fill/Deepen, Flatten/Contrast, Grab, Inflate/Deflate, Layer, Nudge, Pinch/Magnify, Rotate, Scrape/Peak, Smooth, Snake Hook, Thumb:


.. figure:: /images/Sculpt_draw_various_size_and_strength.jpg

   Drawing in various sizes and strengths.


:guilabel:`Blob`
   Pushes mesh outward or inward into a spherical shape with settings to control the amount of pinching at the edge of the sphere.

:guilabel:`Clay` (:kbd:`C`)
   Similar to the :guilabel:`Draw` brush, but includes settings to adjust the plane on which the brush acts.

:guilabel:`Clay Strips`
   Similar to the :guilabel:`Clay` brush, but it uses a cube test to define the brush area of influence rather than a sphere.

:guilabel:`Crease`
   Creates sharp indents or ridges by pushing or pulling the mesh, while pinching the vertices together.

:guilabel:`Draw` (:kbd:`D`)
   Moves vertices inward or outward, based the average normal of the vertices contained within the drawn brush stroke.

:guilabel:`Fill`
   The :guilabel:`Fill` brush works like the Flatten brush, but only brings vertices below the brush plane upwards.  The inverse of the Scrape brush is to :guilabel:`Deepen` by pushing vertices above the plane downward.

:guilabel:`Flatten` (:kbd:`T`)
   The :guilabel:`Flatten` brush finds an 'area plane' located by default at the average height above/below the vertices within the brush area.  The vertices are then pulled towards this plane.  The inverse of the Flatten brush is the :guilabel:`Contrast` brush which pushes vertices up or down away from the brush plane.

:guilabel:`Grab` (:kbd:`G`)
   :guilabel:`Grab` is used to drag a group of points around. Unlike the other brushes, :guilabel:`Grab` does not modify different points as the brush is dragged across the model. Instead, :guilabel:`Grab` selects a group of vertices on mousedown, and pulls them to follow the mouse. The effect is similar to moving a group of vertices in :guilabel:`Edit mode` with proportional-editing enabled, except that :guilabel:`Grab` can make use of other Sculpt Mode options (like textures and symmetry).

:guilabel:`Inflate` (:kbd:`I`)
   Similar to :guilabel:`Draw`, except that vertices in :guilabel:`Inflate` mode are displaced in the direction of their own normals.

:guilabel:`Layer` (:kbd:`L`)
   This brush is similar to :guilabel:`Draw`, except that the height of the displacement layer is capped. This creates the appearance of a solid layer being drawn. This brush does not draw on top of itself; a brush stroke intersects itself. Releasing the mouse button and starting a new stroke will reset the depth and paint on top of the previous stroke.

:guilabel:`Nudge`
   Moves vertices in the direction of the brush stroke.

:guilabel:`Pinch` (:kbd:`P`)
   :guilabel:`Pinch` pulls vertices towards the center of the brush. The inverse setting is :guilabel:`Magnify`, in which vertices are pushed away from the center of the brush.

:guilabel:`Rotate`
   Rotates vertices within the brush in the direction the cursor is moved.

:guilabel:`Scrape`
   The :guilabel:`Scrape` brush works like the Flatten brush, but only brings vertices above the plane downwards.  The inverse of the Scrape brush is to :guilabel:`Peak` by pushing vertices above the plane up away from the plane.

:guilabel:`Smooth` (:kbd:`S`)
   As the name suggests, eliminates irregularities in the area of the mesh within the brush's influence by smoothing the positions of the vertices.

:guilabel:`Snake Hook`
   Pulls vertices along with the movement of the brush to create long, snake-like forms.

:guilabel:`Thumb`
   Similar to the :guilabel:`Nudge` brush, this one flattens the mesh in the brush area, while moving it in the direction of the brush stroke.


Sculpting with the Multires Modifier
************************************

...


Sculpt Properties Panel
***********************

This panel appears in the tool palette on the left side of the 3D viewport.


Brush Menu
==========

:guilabel:`Radius`
   This option controls the radius of the brush, measured in pixels. :kbd:`F` in the 3D view allows you to change the brush size interactively by dragging the mouse and then left clicking (the texture of the brush should be visible inside the circle). Typing a number then enter while in :kbd:`F` sizing allows you to enter the size numerically. Brush size can be affected by enabling the pressure sensitivity icon, if a supported tablet is being used.

:guilabel:`Strength`
   :guilabel:`Strength` controls how much each application of the brush affects the model. For example, higher values cause the :guilabel:`Draw` brush to add depth to the model more quickly, and cause the :guilabel:`Smooth` brush to smooth the model more quickly. This setting is not available for :guilabel:`Grab`, :guilabel:`Snake Hook`, or :guilabel:`Rotate`.

If the range of strengths doesn't seem to fit the model (for example,
if even the lowest strength setting still makes too large of a change on the model)
then you can scale the model (in :guilabel:`Edit` Mode, not :guilabel:`Object` Mode).
Larger sizes will make the brush's effect smaller, and vice versa. You can change the brush
strength interactively by pressing :kbd:`shift-F` in the 3D view and then moving the
brush and then left clicking.
You can enter the size numerically also while in :kbd:`shift-F` sizing.
Brush strength can be affected by enabling the pressure sensitivity icon,
if a supported tablet is being used.

:guilabel:`Autosmooth`
   Sets the amount of smoothing to be applied to each stroke.

:guilabel:`Sculpt Plane`
   Use this menu to set the plane in which the sculpting takes place.

:guilabel:`Plane Offset`
   Adjusts the plane on which the brush acts toward or away from the viewer.

:guilabel:`Trim`
   Enables trimming of the sculpt plane, determined by the :guilabel:`Distance` setting.

:guilabel:`Front Faces Only`
   When enabled, the brush only affects vertices that are facing the viewer.

:guilabel:`Accumulate`
   Causes stroke dabs to accumulate on top of each other.


Stroke Menu
===========

:guilabel:`Stroke Method`
   Defines the way brush strokes are applied to the mesh:

:guilabel:`Dots`
   Standard brush stroke.

:guilabel:`Drag Dot`
   Creates a single displacement in the brush shape. Click then drag on mesh to desired location, then release.

:guilabel:`Space`
   Creates brush stroke as a series of dots, whose spacing is determined by the :guilabel:`Spacing` setting. :guilabel:`Spacing` represents the percentage of the brush diameter.

:guilabel:`Anchored`
   Creates a single displacement at the brush location. Clicking and dragging will resize the brush diameter. When :guilabel:`Edge to Edge` the brush location and orientation is determined by a two point circle, where the first click is one point, and dragging places the second point, opposite from the first.

:guilabel:`Airbrush`
   Flow of the brush continues as long as the mouse click is held, determined by the :guilabel:`Rate` setting. If disabled, the brush only modifies the model when the brush changes its location. This option is not available for the :guilabel:`Grab` brush.

The following parameters are available for the :guilabel:`Dots`, :guilabel:`Space`,
and :guilabel:`Airbrush` strokes:

:guilabel:`Smooth stroke`
   Brush lags behind mouse and follows a smoother path. When enabled, the following become active:

   :guilabel:`Radius`
      Sets the minimum distance from the last point before stroke continues.
   :guilabel:`Factor`
      Sets the amount of smoothing
:guilabel:`Jitter`
   Jitters the position of the brush while painting.


Curve Menu
==========

The :guilabel:`Curve` section allows you to use a curve control to the right to modify the
intensity of the brush from its centre (left part of the curve) towards its borders
(right part of the curve).


Texture Menu
============

A texture can be used to determine the strength of brush effects as well.
Select an existing texture from the texture box,
or create a new one by selecting the :guilabel:`New` button

:guilabel:`Brush Mapping`
   Sets the way the texture is mapped to the brush stroke:

   :guilabel:`Fixed`
      If :guilabel:`Fixed` is enabled, the texture follows the mouse, so it appears that the texture is being dragged across the model.
   :guilabel:`Tiled`
      The :guilabel:`Tile` option tiles the texture across the screen, so moving the brush appears to move separately from the texture. The :guilabel:`Tile` option is most useful with tileable images, rather than procedural textures.
   :guilabel:`3D`
      The :guilabel:`3D` option allows the brush to take full advantage of procedural textures. This mode uses vertex coordinates rather than the brush location to determine what area of the texture to use.

:guilabel:`Angle`
   This is the rotation angle of the texture brush. It can be changed interactively via :kbd:`ctrl-F` in the 3D view. While in the interactive rotation you can enter a value numerically as well. Can be set to:

   :guilabel:`User`
      Directly input the angle value.
   :guilabel:`Rake`
      Angle follows the direction of the brush stroke. Not available with :guilabel:`3D` textures.
   :guilabel:`Random`
      Angle is randomized.

:guilabel:`Offset`
   Fine tunes the texture map placement in the x, y, and z axes.
:guilabel:`Size`
   This setting allows you to modify the scaling factor of the texture. Not available for :guilabel:`Drag` textures.
:guilabel:`Sample Bias`
   Value added to texture samples.
:guilabel:`Overlay`
   When enabled, the texture is shown in the viewport, as determined by the ;\ :guilabel:`Alpha` value.


Symmetry Menu
=============

Mirror the brush strokes across the selected local axes.
Note that if you want to alter the directions the axes point in,
you must rotate the model in :guilabel:`Edit` Mode, not :guilabel:`Object` Mode.

:guilabel:`Feather`
   Reduces the strength of the stroke where it overlaps the planes of symmetry.
:guilabel:`Radial`
   These settings allow for radial symmetry in the desired axes. The number determines how many times the stroke will be repeated within 360 degrees around the central axes.


Options Menu
============

:guilabel:`Threaded Sculpt`
   Takes advantage of multiple CPU processors to improve sculpting performance.
:guilabel:`Fast Navigation`
   For ;\ :guilabel:`Multires` models, show low resolution while navigation the viewport.
:guilabel:`Show Brush`
      Shows the brush shape in the viewport.
Unified Settings:

   ;\ :guilabel:`Size`
      Forces the brush size to be shared across brushes.
   ;\ :guilabel:`Strength`
      Forces the brush strength to be shared across brushes.
:guilabel:`Lock`
   These three buttons allow you to block any modification/deformation of your model along selected local axes, while you are sculpting it.


Appearance Menu
===============

You can set the color of the brush depending on if it is in additive or subtractive mode.

You can also set the brush icon from an image file.


Tool Menu
=========

Here you can select the type of brush preset to use.
:guilabel:`Reset Brush` will return the settings of a brush to its defaults.
You can also set Blender to use the current brush for :guilabel:`Vertex Paint` mode,
:guilabel:`Weight Paint` mode, and :guilabel:`Texture Paint` mode using the toggle buttons.


Hiding and Revealing Mesh
*************************

It is sometimes useful to isolate parts of a mesh to sculpt on. To hide a part of a mesh,
press :kbd:`H` then click & drag around the part you want to hide.
To reveal a hidden part of a mesh,
press :kbd:`shift-H` then click & drag around the part you want to reveal.
To reveal all hidden parts, just hit :kbd:`alt-H`.


.. figure:: /images/Hide_before_and_after.jpg
   :width: 610px
   :figwidth: 610px

   Before and after Hiding.


Keyboard Shortcuts
******************

These shortcuts may be customized under File > User preferences > Input > 3D View > Sculpt
Mode.


+----------------------------------------------------------------+-------------------------------------------------------------+
+**Action**                                                      |**Shortcut**                                                 +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Hide mesh inside selection                                      |:kbd:`H` then click & drag                                   +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Reveal mesh inside selection                                    |:kbd:`Shift-H` then click & drag                             +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Show entire mesh                                                |:kbd:`alt-H`                                                 +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Interactively set brush size                                    |:kbd:`F`                                                     +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Increase/decrease brush size                                    |:kbd:`[` and :kbd:`]`                                        +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Interactively set brush strength                                |:kbd:`shift-F`                                               +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Interactively rotate brush texture                              |:kbd:`ctrl-F`                                                +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Brush direction toggle (:guilabel:`Add` / :guilabel:`Sub`)      |:kbd:`Ctrl` pressed while sculpting                          +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Set stroke method (airbrush, anchored, ..)                      |:kbd:`A`                                                     +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Smooth stroke toggle                                            |:kbd:`shift-S`                                               +
+----------------------------------------------------------------+-------------------------------------------------------------+
+:guilabel:`Draw` brush                                          |:kbd:`D`                                                     +
+----------------------------------------------------------------+-------------------------------------------------------------+
+:guilabel:`Smooth` brush                                        |:kbd:`S`                                                     +
+----------------------------------------------------------------+-------------------------------------------------------------+
+:guilabel:`Pinch/Magnify` brush                                 |:kbd:`P`                                                     +
+----------------------------------------------------------------+-------------------------------------------------------------+
+:guilabel:`Inflate/Deflate` brush                               |:kbd:`I`                                                     +
+----------------------------------------------------------------+-------------------------------------------------------------+
+:guilabel:`Grab` brush                                          |:kbd:`G`                                                     +
+----------------------------------------------------------------+-------------------------------------------------------------+
+:guilabel:`Layer` brush                                         |:kbd:`L`                                                     +
+----------------------------------------------------------------+-------------------------------------------------------------+
+:guilabel:`Flatten/Contrast` brush                              |:kbd:`shift-T`                                               +
+----------------------------------------------------------------+-------------------------------------------------------------+
+:guilabel:`Clay` brush                                          |:kbd:`C`                                                     +
+----------------------------------------------------------------+-------------------------------------------------------------+
+:guilabel:`Crease` brush                                        |:kbd:`shift-C`                                               +
+----------------------------------------------------------------+-------------------------------------------------------------+
+:guilabel:`Snake Hook` brush                                    |:kbd:`K`                                                     +
+----------------------------------------------------------------+-------------------------------------------------------------+
+:guilabel:`Mask` brush                                          |:kbd:`M`                                                     +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Mask clear                                                      |:kbd:`alt-M`                                                 +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Mask invert                                                     |:kbd:`ctrl-I`                                                +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Set brush by number                                             |:kbd:`0` - :kbd:`9` and :kbd:`shift-0` to :kbd:`shift-9`     +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Sculpt options panel toggle                                     |:kbd:`T`                                                     +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Step up one multires level                                      |:kbd:`Page Up`                                               +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Step down one multires level                                    |:kbd:`Page Down`                                             +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Set multires level                                              |:kbd:`Ctrl-0` to :kbd:`Ctrl-5`                               +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Dynamic topology toggle                                         |:kbd:`Ctrl-D`                                                +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Set texture angle type                                          |:kbd:`R`                                                     +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Translate/scale/rotate stencil texture                          |:kbd:`RMB`, :kbd:`shift-RMB`, :kbd:`ctrl-RMB`                +
+----------------------------------------------------------------+-------------------------------------------------------------+
+Translate/scale/rotate stencil mask                             |:kbd:`alt-RMB`, :kbd:`alt-shift-RMB`, :kbd:`alt-ctrl-RMB`    +
+----------------------------------------------------------------+-------------------------------------------------------------+


