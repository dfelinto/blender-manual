
**********************
Freestyle SVG Exporter
**********************

This add-on can export your :ref:`Freestyle Renders <bpy.types.Freestyle>` into an SVG file.
It can fill contours with their material color and can also export SVG animations.

.. figure:: /images/addons_render_render-freestyle-svg_suzanne.svg
   :align: center

   An example of an SVG result produced by the Freestyle SVG Exporter.


Activation
==========

This add-on can be enabled via :menuselection:`Preferences --> Add-ons --> Render --> Freestyle SVG Exporter`.
The interface for the exporter should now be visible as a new panel in the Render tab.

.. admonition:: Reference
   :class: refbox

   :Category:  Render
   :Panel:     :menuselection:`Properties --> Render --> Freestyle SVG Export`


Usage
=====

Activate :doc:`Freestyle rendering </render/freestyle/introduction>` and then render your scene with *Render Image*.
Your render will be displayed, and the SVG version will be saved to the default output path
:menuselection:`Properties --> Output --> Output`.


Options
=======

.. figure:: /images/addons_render_render-freestyle-svg_panel.png
   :align: right

   Freestyle SVG Export panel.

Mode
   Option between Frame and Animation. Frame will render a single frame,
   Animation will bundle all rendered frames into a single ``.svg`` file.
Split at Invisible
   By default the exporter will not take invisible vertices into account and export them like they are visible.
   Some stroke modifiers, like Blueprint, mark vertices as invisible to achieve a certain effect. Enabling this
   option will make the paths split when encountering an invisible vertex, which leads to a better result.
Fill Contours
   The contour of objects is filled with their material color.

   .. note::

      This feature is somewhat unstable -- especially with animations.

Stroke Cap Style
   Defines the style the stroke caps will have in the SVG output.

   Miter
      Corners with sharp edges.
   Round
      Corners are smoothed.
   Bevel
      Corners are beveled.


Exportable Properties
=====================

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Properties --> View Layers --> Freestyle Line Style SVG Export`

Because the representation of Freestyle strokes and SVG path objects is fundamentally different, a one-on-one
translation between Freestyle and SVG is not possible. The main shortcoming of SVG compared to Freestyle is that
Freestyle defines style per-point, where SVG defines it per-path. This means that Freestyle can produce much more
complex results that are impossible to achieve in SVG.

There are extended options for the exporter,
located at the specific panels of the Freestyle renderer at the View Layers tab of the Properties.
Those options are located at the Freestyle Line Style SVG Export panel, at the bottom of the tab.

The properties (no modifiers applied) that can be exported are:

- Base color
- Base alpha
- Base thickness
- Dashes


Animations
==========

The exporter supports the creation of SVG animations. When the Mode is set to Animation, all frames from a render --
one when rendering a frame (:kbd:`F12`)
or all when rendering an animation (:kbd:`Shift-F12`) -- are saved into a single file.
Most modern browsers support the rendering of SVG animations.

.. figure:: /images/addons_render_render-freestyle-svg_cube.svg
   :align: center

   An SVG animation rendered with the exporter.


Exporting Fills
---------------

Fills are colored areas extracted from a Freestyle render result. Specifically, they are defined by a combination of
the Contour and External Contour edge type, combined with some predicates. The fill result can be unexpected,
when the SVG renderer cannot correctly render the path that the exporter has generated.
This problem is extra apparent in animations.

.. figure:: /images/addons_render_render-freestyle-svg_pallet.svg
   :align: center

   An example of an SVG result produced by the Freestyle SVG Exporter.
   Model by `Julien Deswaef <https://github.com/xuv>`__.

Fills support holes and layering. When using layers, the exporter tries to render objects with the same material as
the patch. The exporting of fills and especially the order in which they are layered is by no means perfect.
In most cases, these problems can be easily solved in Inkscape or a text editor.
