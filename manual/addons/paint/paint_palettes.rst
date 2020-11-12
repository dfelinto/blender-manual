
**************
Paint Palettes
**************

Todo.

.. seealso::

   Please see the
   `old Wiki <https://archive.blender.org/wiki/index.php/Extensions:2.6/Py/Scripts/Paint/Palettes/>`__
   for the archived original docs.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Paint then Paint Palettes to enable the script.


Interface
=========

Located in the :menuselection:`3D Viewport --> Sidebar --> Color Palette or Weight Palette` depending on the mode.
Located in the :menuselection:`Image editor --> Sidebar --> Color Palette` while in Paint Mode.


Usage
=====

Go into any paint mode (Image Painting, Texture Paint, Vertex Paint, Weight Paint) and
look for the Palette panel corresponding to that mode.


Color Palette
-------------

This add-on can read and write Gimp's palette format.
The first thing to do is to determine your "Palettes Folder". This can be the Gimp's palette folder,
or it can be a specific one for your project. Select the palette with the select menu.
You can save your palette with the ``+`` button.
Add as many colors as you need with the ``+`` button at the left of the index number field.
Sample the current brush color with the small color wheel button.
Select a palette color with the small button under the colors.


Weight Palette
--------------

Select the weight value from the eleven values. These can be adjusted with the *Weight* slider.


.. admonition:: Reference
   :class: refbox

   :Category:  Paint
   :Description: Palettes for color and weight paint modes.
   :Location: :menuselection:`Image Editor, 3D View Paint Modes --> Color Palette or Weight Palette panel`
   :File: paint_palette.py
   :Author: Dany Lebel (Axon D)
   :License: GPL
   :Note: This add-on is bundled with Blender.
