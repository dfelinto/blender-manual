
*********
UV Layout
*********

.. reference::

   :Category:  Import-Export
   :Menu:      :menuselection:`UV Editor --> UV --> Export UV Layout`


Usage
=====

Using your favorite image painting program, you could use an exported UV layout to create a texture.
Then save your changes, and back in Blender, use the :menuselection:`Image --> Open`
to load it as your UV image for the mesh in Edit Mode for the desired (and active) UV map.

As a way of communicating to an artist who is painting your UV Texture for you,
Blender has a tool called *UV Layout* (:menuselection:`UV Editor --> UV --> Export UV Layout`)
that saves an image as a ``Targa`` (``.tga``), ``EPS``, or ``SVG`` format for the object you have selected.

The image will be lines defining the UV edges that are within the image area of the UV mapping area.
Edges outside the boundary, even if selected, will not be shown in the saved graphic.
The artist will use this as a transparent layer in their paint program as a guide when painting your texture.
The example below shows Blender in the background, and the Gimp working on the texture,
using the saved layout as a guide. Note that ``targa`` format supports the Alpha channel,
so you can paint transparent areas of the mesh. For using images as textures, see the page on
:doc:`Image Textures </render/materials/legacy_textures/types/image_movie>`.

.. list-table::

   * - .. figure:: /images/addons_import-export_mesh-uv-layout_uv-editor.png
          :width: 320px

          A UV layout in the UV Editor.

     - .. figure:: /images/addons_import-export_mesh-uv-layout_export.png
          :width: 320px

          A UV layout in a paint program.


Properties
==========

.. figure:: /images/addons_import-export_mesh-uv-layout_export-panel.png

   Export options.

All UVs
   if disabled, then only the UV faces selected will be outlined.
Modified
   Export UVs from the modified mesh.
Format
   Select the type of image file to save (``.png``, ``.eps``, ``.svg``).
Size
   Select the size of the image in pixels.
Fill Opacity
   Set the opacity of the fill.
