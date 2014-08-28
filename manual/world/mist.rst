
Mist
****

Description
===========

Mist can greatly enhance the illusion of depth in your rendering. To create mist,
Blender makes objects farther away more transparent (decreasing their Alpha value)
so that they mix more of the background color with the object color. With Mist enabled,
the further the object is away from the camera the less it's alpha value will be.


Option
======

.. figure:: /images/25-Manual-World-MistPanel.jpg
   :width: 305px
   :figwidth: 305px

   Mist panel


Mist check box
   Toggles mist on and off
Minimum
   An overall minimum intensity, or strength, of the mist.
Start
   The distance from the camera at which the mist starts to fade in
Depth
   The distance from :guilabel:`Start` of the mist, that it fades in over. Objects further from the camera than :guilabel:`Start+Depth` are completely hidden by the mist.


.. figure:: /images/25-Manual-World-MistFalloff.jpg
   :width: 197px
   :figwidth: 197px

   Mist Falloff popup menu


Height
   Makes the mist intensity decrease with height, for a more realistic effect. If greater than 0, it sets, in Blender units, an interval around z=0 in which the mist goes from maximum intensity (below) to zero (above).
Falloff
   The decay rate of the mist (:guilabel:`Quadratic` / :guilabel:`Linear` / :guilabel:`Inverse Quadratic`). These settings control the rate of change of the mist's strength further and further into the distance.


.. admonition:: Mist distances
   :class: note

   To visualize the mist distances in the 3D View, select your camera, go to the camera menu, and enable :guilabel:`Show Mist`.

   The camera will show mist limits as a line projecting from the camera starting from
   :guilabel:`Start` and of distance :guilabel:`Depth`.

   To get a better view to evaluate the :guilabel:`Mist` visualization,
   :kbd:`Shift-pad1` with the camera selected
   (:kbd:`pad5` to toggle perspective view on and off).
   This will place the 3D view right over the camera looking down.


Transparency
============

Because :guilabel:`Mist` works by adjusting transparency,
this can sometimes cause objects to be partially transparent when they shouldn't be.
One workaround is to set the Mist settings as desired, but turn Mist off.
The Mist data is still available for compositing even though it is off.  Use :doc:`Do Composite </composite_nodes>`
and the :doc:`Nodes Editor </composite_nodes/editor>` to feed the Mist pass to an
:doc:`AlphaOver </composite_nodes/types/color#alphaover_node>` to blend the background color
(or a render layer with just the sky) with the rendered image.
This produces the mist effect but since Mist is off the object transparency (or lack of) is preserved.


Examples
========

.. figure:: /images/25-Manual-World-Mist-Example1.jpg

   Mist example


In this example (`.blend <http://wiki.blender.org/index.php/:File:25-Manual-World-Mist-Example1.blend>`__)
the :guilabel:`Mist` :guilabel:`Height` options has been limited to create smoke covering the floor.


This simple scene was inspired by [http://stefan-morrell.cgsociety.org/gallery/536375/ Stefan
Morell's *Arc Sci-Fi Corridor* ].

