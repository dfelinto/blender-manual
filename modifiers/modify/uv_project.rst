
UV Project Modifier
===================

.. admonition:: Reference
   :class: refbox

   | Mode:     Any mode
   | Panel:    :guilabel:`Modifiers` (:guilabel:`Generate`)


.. figure:: /images/Uvproject.jpg

   Projecting the Blender logo onto Suzanne.


The :guilabel:`UV Project` Modifier acts like a slide projector.
It emits a UV map from the -Z axis of 'Projector' objects,
and applies it to the object as the "light" hits it.
It can optionally override the object's face texture.


- `Download an example <http://wiki.blender.org/index.php/File:Uvproject.blend>`__


Options
-------

.. figure:: /images/Uvproject_ui.jpg


:guilabel:`UV layer`
   Which UV layer to modify. Defaults to the active rendering layer.

:guilabel:`Image`
   The image associated with this modifier. Not required; you can just project a UV for use elsewhere. *Override Image*, below, defines how the image is used.

Override Image

   - When true, the Face Texture of all vertices on the mesh is replaced with the Image. This will cause the image to repeat, which is usually undesirable.
   - When false, the modifier is limited to faces with the Image as their Face Texture.

:guilabel:`Projectors`
   Up to ten projector objects are supported. Each face will choose the closest and aligned projector with its surface normal.
   Projections emit from the -Z axis (i.e. straight down a camera or lamp).
   If the projector is a camera, the projection will adhere to its perspective/orthographic setting.

:guilabel:`Objects`
   Specify the projector Object

:guilabel:`Aspect X/Y and Scale X/Y`
   These allow simple manipulation of the image. Only apply when a camera is used as projector Object.


Usage
-----

General
~~~~~~~

UV Project is great for making spotlights more diverse,
and also for creating decals to break up repetition.

The modifier's Image property is not generally used: instead,
a Texture mapped to the UV layer that the modifier targets is added to the object's Material.
This allows you to prevent the image from repeating by setting *Texture → Image Mapping →
Extension* to *Clip*.


Perspective Cameras
~~~~~~~~~~~~~~~~~~~

When using perspective cameras or spot lamps,
you will likely want to enable the **UV Project** Material Option
(available in the materials panel),
This uses a different UV interpolation to prevent distortion.

*Note: This option is not yet available for Cycles*

