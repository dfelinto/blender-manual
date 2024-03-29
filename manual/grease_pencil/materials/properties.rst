
**********
Properties
**********

Surface
=======

.. figure:: /images/grease-pencil_materials_properties_panel.png
   :align: right

   Shader panel with only Stroke component activated.


.. _bpy.types.MaterialGPencilStyle.show_stroke:
.. _bpy.types.MaterialGPencilStyle.color:
.. _bpy.types.MaterialGPencilStyle.use_overlap_strokes:

Stroke
------

When enabled, the shader use the stroke component.
The *Stroke* component controls how to render the edit lines.

.. _bpy.types.MaterialGPencilStyle.mode:

Line Type
   Defines how to display or distribute the output material over the stroke.

   :Line:
      Connects every points in the strokes showing a continuous line.
   :Dots:
      Use a disk shape at each point in the stroke.
      The dots are not connected.
   :Squares:
      Use a square shape at each point in the stroke.
      The squares are not connected.

.. _bpy.types.MaterialGPencilStyle.stroke_style:

Style
   The type of the material.

   :Solid:
      Use a solid color.

      Base Color
         The base color of the stroke.

   :Texture:
      Use an image texture.

      Base Color
         The base color of the stroke.

      Image
         The image data-block used as an image source.

      Blend
         Texture and Base Color mixing amount.

      UV Factor
         The image size along the stroke.

.. _bpy.types.MaterialGPencilStyle.use_stroke_holdout:

Holdout
   Removes the color from strokes underneath the current by using it as a mask.

.. _bpy.types.MaterialGPencilStyle.alignment_mode:

Alignment
   Defines how to align the *Dots* and *Squares* along the drawing path and with the object's rotation.

   :Path:
      Aligns to the drawing path and the object's rotation.
   :Object:
      Aligns to the object's rotation; ignoring the drawing path.
   :Fixed:
      Aligns to the screen space; ignoring the drawing path and the object's rotation.

Rotation
   Rotates the points of *Dot* and *Square* strokes.

   .. note::

      The *Rotation* option is limited to a range of -90 to 90 degrees.

Self Overlap
   Disables stencil and overlap self-intersections with alpha materials.

.. list-table:: Samples of different material strokes mode types and styles.

   * - .. figure:: /images/grease-pencil_materials_properties_stroke-solid-line.png
          :width: 130px

          Mode Type: Line, Style: Solid.

     - .. figure:: /images/grease-pencil_materials_properties_stroke-texture-line.png
          :width: 130px

          Mode Type: Line, Style: Texture.

     - .. figure:: /images/grease-pencil_materials_properties_stroke-solid-dot.png
          :width: 130px

          Mode Type: Dot, Style: Solid.

     - .. figure:: /images/grease-pencil_materials_properties_stroke-texture-dot.png
          :width: 130px

          Mode Type: Dot, Style: Texture.


.. _bpy.types.MaterialGPencilStyle.show_fill:
.. _bpy.types.MaterialGPencilStyle.fill_style:
.. _bpy.types.MaterialGPencilStyle.fill_color:
.. _bpy.types.MaterialGPencilStyle.mix_color:
.. _bpy.types.MaterialGPencilStyle.mix_factor:
.. _bpy.types.MaterialGPencilStyle.flip:
.. _bpy.types.MaterialGPencilStyle.pattern:
.. _bpy.types.MaterialGPencilStyle.texture:
.. _bpy.types.MaterialGPencilStyle.use_fill_texture_mix:

Fill
----

When enabled, the shader use the fill component.
The *Fill* component control how to render the filled areas determined by closed edit lines.

Style
   The type of material.

   Solid
      Use solid color.

      Base Color
         The base color of the fill.

   Gradient
      Use a color gradient.

      Gradient Type
         Linear
            Mix the colors along a single axis.

         Radial
            Mix the colors radiating from a center point.

      Base Color
         The primary color.

      Secondary Color
         The secondary color.

      Blend
         Base Color and Secondary Color mixing amount.

      Flip Colors
         Flips the gradient, inverting the Base Color and Secondary Color.

      Location
         Shifts the gradient position.

         X, Y

      Rotation
         Rotates the gradient.

      Scale
         Scales the gradient.

         X, Y

   Texture
      Use an image texture.

      Base Color
         The base color of the fill.

      Image
         The image data-block used as an image source.

      Blend
         Texture and Base Color mixing amount.

      Location
         Shifts the image position.

         X, Y

      Rotation
         Rotates the image.

      Scale
         Scales the image.

         X, Y

      Clip Image
         When enabled, show one image instance only (do not repeat).

.. _bpy.types.MaterialGPencilStyle.use_fill_holdout:

Holdout
   Removes the color from strokes underneath the current by using it as a mask.

.. list-table:: Samples of different material fill styles.

   * - .. figure:: /images/grease-pencil_materials_properties_fill-solid.png
          :width: 130px

          Style: Solid.

     - .. figure:: /images/grease-pencil_materials_properties_fill-gradient.png
          :width: 130px

          Style: Gradient (Linear).

     - .. figure:: /images/grease-pencil_materials_properties_fill-gradient-radial.png
          :width: 130px

          Style: Gradient (Radial).

     - .. figure:: /images/grease-pencil_materials_properties_fill-texture.png
          :width: 130px

          Style: Texture.


Settings
========

.. _bpy.types.MaterialGPencilStyle.pass_index:

Pass Index
   This index can be used with some modifiers to restrict changes to only a certain material.
   See :doc:`Modifiers </grease_pencil/modifiers/introduction>` for more information.
