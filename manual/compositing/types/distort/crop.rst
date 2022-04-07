.. _bpy.types.CompositorNodeCrop:

*********
Crop Node
*********

.. figure:: /images/compositing_node-types_CompositorNodeCrop.webp
   :align: right
   :alt: Crop Node.

The Crop node crops an input image to a selected region
by either making the cropped area transparent or by resizing the input image.


Inputs
======

Image
   Standard color input. If no image is selected, an image filled with the selected color is used.
   You can use and crop this image in combination with another background image.


Properties
==========

Crop Image Size
   When disabled, the image remains the same size, but the cropped areas become transparent pixels.
   When enabled, the image size is cropped to the specified region and gets a new width or height or both.

   Note that this will probably reposition the image in the render output
   because the cropped image is automatically centered.

Relative
   When enabled, crop dimensions are a percentage of the input image's width and height.
   When disabled, the range of the *Crop Region Values* are the width and height of the image in pixels.

Crop Region Values
   Define borders of the crop region; *Left* or *Right* can vary between 0 and the width of the image.
   *Up* or *Down* can vary between 0 and the height of the image.

.. note::

   The terminology (*Left*, *Right*, *Up*, *Down*) can be misunderstood easily.
   First, the numbers do not represent the amount of cropping,
   e.g. *Left* is set to 50 and *Right* to 50 does not mean that you will be
   cropping the image for 50 pixels on both the left and right side.
   In fact, it will result in zero-sized image because you are cropping from pixel 50 to pixel 50.
   So, the numbers defines a position in the input image.

   Secondly, depending on which one is bigger, *Left* should be interpreted as *Right* and vice versa.
   If *Left* is greater than *Right* then both values are switched and *Left* gets the value of *Right*
   and vice versa. The same operation is done for *Up* and *Down*, where you can think of them as the top
   and bottom of the image.

   Thirdly, the terms *Up* and *Down* are ambiguous and suggest an action; e.g. "Crop down".
   The values, however, are not amounts but positions.
   The term *Down* should be interpreted as "Bottom" and *Up* as "Top".


Outputs
=======

Image
   Standard color output.


Usage
=====

The following workflow removes some possible confusion:

#. Uncheck *Crop Image Size* for this step, so that you can see the borders of the input image.
   To see this border, you have to select the Viewer node.
#. If you don't need pixel-perfect cropping, check *Relative* so that
   you do not have to consider the exact dimensions of the input image.
#. Set *Left* and *Down* to zero. Set *Right* and *Up* to one, or to the width and height of the input image.
   You should see now the entire input image in the backdrop. *Up* is thus interpreted as the top of the image.
   The origin of the image (0, 0) is at the bottom (down) left corner.
#. To crop from the left, change the *Left* value. To crop from the right, change the *Right* value.
   To crop from the top, change the *Up* value. To crop from the bottom, change the *Down* value.
