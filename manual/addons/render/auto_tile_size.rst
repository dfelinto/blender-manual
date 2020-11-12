
**************
Auto Tile Size
**************

This add-on gives you some quick controls to get the best possible tile sizes for the fastest possible Cycles render.
Usually it's a good idea to stick to powers of 2 (16, 64, 256...) to get fast renders,
however in the case of tile sizes it's even more important to keep the tiles fairly square and of consistent size.
Having some tiles smaller than the rest due to the borders of the image makes for longer renders.

So this add-on allows you to choose a target size and then automatically calculates the actual tile dimensions
to ensure squareness and consistency.

As a rule of thumb, GPUs like bigger tiles (256 × 256 usually) and CPUs like smaller ones (often 32 square),
thus the two target values are stored separately in case you switch between them often.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Render then Auto Tile Size to enable the script.


Usage
=====

At the bottom of the :menuselection:`Render --> Performance panel` are the target tile sizes.
The best tile size will be calculated and the add-on will attempt to stick as close to the target as possible.

In a previous version it was necessary to *Set* the tile size, however it is now done automatically.
After enabling the add-on, you can probably forget about tile sizes altogether,
though some strange resolutions cannot have nice consistent tile sizes and you may wish to set it manually.

If for some reason you want to set the tile size to exactly the target, resulting in perfectly square tiles
but probably some rectangular ones on the edges, disable *Consistent Tiles*.

.. seealso::

   The most recent documentation and info can be found at
   the `authors site <http://gregzaal.github.io/auto-tile-size/>`__.

.. admonition:: Reference
   :class: refbox

   :Category:  Render
   :Description: Estimate and set the tile size that will render the fastest.
   :Location: :menuselection:`Properties --> Render --> Performance`
   :File: render_auto_tile_size.py
   :Author: Greg Zaal
   :License: GPL
   :Note: This add-on is bundled with Blender.
