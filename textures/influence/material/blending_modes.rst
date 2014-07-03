
Texture Blending Modes
======================

Blending Modes are different methods of controlling how the texture influences material
properties. While a blending mode defines the specific operation performed,
blending factor controls the amount, the overall "strength" of this operation.
For textures such blending factor is set via sliders in the Influence panel.
Throughout this section,
the term :guilabel:`base layer` refers to the base material color being manipulated
(as defined by texture's Influence) and :guilabel:`blend layer` refers to the texture.
Following is a list of available texture blending modes:


Linear Light
~~~~~~~~~~~~

Brightens base layer depending on blend layer. If blend layer is more than 50% bright,
base layer is brightened by the blend layer values,
otherwise it is darkened by the blend layer values.


Soft Light
~~~~~~~~~~

Lightens or darkens base layer depending on the blend layer brightness.
The effect is softer than that of Linear Light or Overlay modes,
with pure white and pure black blend layers not yielding pure white/black results.


Color
~~~~~

Mixes hue and saturation of the blend layer into the base layer.


Value
~~~~~

Mixes value of the blend layer into the base layer.


Saturation
~~~~~~~~~~

Mixes saturation of the blend layer into the base layer.


Hue
~~~

Mixes hue of the blend layer into the base layer.


Overlay
~~~~~~~

Combines Multiply and Screen modes. The darker the base layer,
the more the blend layer influences the mix.


Lighten
~~~~~~~

Any fragments of the base layer that are darker than those of the blend layer are replaced by
the blend layer fragments.


Darken
~~~~~~

Any fragments of the base layer that are lighter than those of the blend layer are replaced by
the blend layer fragments.


Difference
~~~~~~~~~~

Mixes with absolute value of the difference between base and blend layers.


Divide
~~~~~~

Base layer is divided by the blend layer.


Screen
~~~~~~

Inverse of the base layer is multiplied by the blend layer.


Subtract
~~~~~~~~

Blend layer is subtracted from the base layer.


Multiply
~~~~~~~~

Base layer is multiplied by the blend layer.


Add
~~~

Blend layer is added to the base layer.


Mix
~~~

Linear interpolation between base and blend layers.


