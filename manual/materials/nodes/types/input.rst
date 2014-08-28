
Material Input Nodes
********************

A starting material is created in the Materials Panel. The :guilabel:`Nodes` button is enabled
to add that material to the list of noded materials shown in the Node Editor window header.
Other inputs to the node map include:

- A value
- A color
- A texture
- Geometry
- Material
- Camera Data
- Lamp Data


Material Node
=============

.. admonition:: Reference
   :class: refbox

   | Panel:    :doc:`Node Editor </materials/nodes/editor>` → :doc:`Material Nodes </materials/nodes>`
   | Menu:     :kbd:`shift-A` → Input → Material


.. figure:: /images/26-Manual-Material-Node.jpg

   Material node


The Material node is used to add a material to the node program.
Materials can be anything from pure shading to fully layered with textures.
It inputs the main attributes of a material (color, alpha and normal vector) into the map.


Output
------

Materials can output color (which includes shading and any textures assigned to it), alpha,
and the final normal calculated from any textures it has.


- :guilabel:`Color` - value of the color, combined by the node.
- :guilabel:`Alpha` - value of the alpha, combined by the node.
- :guilabel:`Normal` - direction of the normal, combined by the node.


Input
-----

Materials can take inputs for colors, inputs for diffuse color and specularity color,
a value for reflectivity, and a normal.


- :guilabel:`Color` - The base color of the paint. Can be set
  - manually by :kbd:`lmb` clicking on the color swatch applet next to the socket, choosing a color using the control panel that pops up, and pressing :kbd:`Enter`
  - based on an Active Material which is specified using the material panels, or
  - plugged in from an RGB color generator.
- :guilabel:`Spec` - The color that is reflected as you get perpendicular to the light source reflecting off the surface. The color can be
  - plugged in from another node or
  - set manually by :kbd:`lmb` clicking on and using the color swatch applet.
- :guilabel:`Refl:` - The degree to which the material reflects light and gives off its color. The value can be provided by another node or set manually.
- :guilabel:`Normal` - The lighting condition.


Controls
--------

:guilabel:`Material` field
   You can browse and select materials here.
:guilabel:`Diffuse` toggle
   Turn on/off Diffuse Color.
:guilabel:`Specular` toggle
   Turns on/off Specularity calculation.
:guilabel:`Invert Normal` toggle
   Inverts the material input normal when activated (which, of course, is a combination of the 3D normal given to it by the 3D object plus the normal input point).


.. admonition:: Normal Override
   :class: note

   The normal input socket does not in any way blend the source normal with the underlying geometry. Any plugged in Geometry here overrides the Normal lighting conditions.


Using the Material Node with Specularity
----------------------------------------

.. figure:: /images/26-Manual-Material-Node-Specular.jpg
   :width: 250px
   :figwidth: 250px

   Material Node using Specularity


To make a material node actually generate a color,
you have to specify at least a basic input color, and optionally a specularity color.
The specularity color is the color that shines under intense light.

For example, consider the mini-map to the right. The base color, a dark blue,
is connected from an RGB color generator node to the :guilabel:`Color` input socket.
The specular color, yellow, is connected to the :guilabel:`Spec` input.
Under :guilabel:`Normal` lighting conditions on a flat surface,
this material will produce a deep blue color and,
as you approach a spot perpendicular to the light,
you will see the yellow specular color mix in.

.. admonition:: Enable Spec
   :class: note

   To see specularity, you have to enable it by clicking the blue Spec button located just below the material color swatch in the node.


Extended Material Node
======================

.. figure:: /images/26-Manual-Extended-Material-Node.jpg
   :width: 200px
   :figwidth: 200px

   Extended Material node


Adds additional input and output channels to the material node.


Input
-----

:guilabel:`Color`
   Includes a color swatch, allowing you to select the color directly on the node.
:guilabel:`Mirror Color`
   Color of mirrored reflection.
:guilabel:`Ambient`
   Amount of global ambient color the material receives.
:guilabel:`Emit`
   Amount of light to emit.
:guilabel:`SpecTra`
   Alpha for the specular color.
:guilabel:`Ray Mirror`
   Amount of reflectiveness of the object.
:guilabel:`Alpha`
   Transparency of the material by setting all pixels in the alpha channel to the given value.
:guilabel:`Translucency`
   Amount of diffuse shading on the back side


Output
------

Materials can additionaly output the followings:

- :guilabel:`Diffuse` - value of the diffuse color, combined by the node.
- :guilabel:`Spec` - value of the specular color, combined by the node.
- :guilabel:`AO` - value of the Ambient Occlusion, combined by the node.


Camera Data Node
================

.. figure:: /images/26-Manual-Camera-Data-Node.jpg

   Camera Data node


:guilabel:`View Vector`
   A Camera space vector from the camera to the shading point.
:guilabel:`View Z Depth`
   How far away each pixel is from the camera
:guilabel:`View Distance`
   Distance from the camera to the shading point.


Lamp Data Node
==============

.. figure:: /images/26-Manual-Lamp-Data-Node.jpg
   :width: 180px
   :figwidth: 180px

   Lamp Data node


The Lamp Data node is used to obtain information related to a specified lamp object.
Select a lamp object listed in the Lamp field, then the following outputs will be available:

:guilabel:`Color`
   Lamp color multiplied by the lamp energy.
:guilabel:`Light Vector`
   An unit vector in the direction from the shading point to the lamp.
:guilabel:`Distance`
   Distance from the shading point to the lamp.
:guilabel:`Shadow`
   Shadow color that the other objects cast on the shading point.
:guilabel:`Visibility Factor`
   Light falloff ratio at the shading point.

The light textures and the shadow textures affect the Color and Shadow outputs, respectively.


.. admonition:: Portability to Various Scenes
   :class: note

   If multiple materials use a Lamp Data node linking to the same lamp object, including the Lamp Data node into a node group is recommended. Otherwise, when the mesh objects are imported to the other scene, all the materials may need to be modified.


Value Node
==========

.. figure:: /images/26-Manual-Value-Node.jpg

   Value node


The Value node has no inputs; it just outputs a numerical value
(floating point spanning 0.00 to 1.00)
currently entered in the NumButton displayed in its controls selection.

Use this node to supply a constant, fixed value to other nodes' value or factor input sockets.


RGB Node
========

.. figure:: /images/26-Manual-RGB-Node.jpg

   RGB node


The RGB node has no inputs.
It just outputs the value Color currently selected in its controls section.


Material Node "Texture"
=======================

.. figure:: /images/26-Manual-Texture-Node.jpg

   Texture node


A texture, from the list of textures available in the current blend file,
is selected and introduced through the value and/or color socket.


.. figure:: /images/26-Manual-Texture-Node-Example.jpg
   :width: 500px
   :figwidth: 500px

   Example of the applying Texture node


Input
-----

:guilabel:`Vector`
   Uses for map the texture to a specific geometric space.


Outputs
-------

:guilabel:`Value`
   Straight black-and-white value of the texture, combined by the node.
:guilabel:`Color`
   Texture color output, combined by the node.
:guilabel:`Normal`
   Direction of normal texture, combined by the node.

In the example to the right, a cloud texture, as it would appear to a viewer,
is added to a base purple material, giving a velvet effect.

Note that you can have multiple texture input nodes. With nodes,
you simply add the textures to the map and plug them into the map.


Geometry Node
=============

.. figure:: /images/26-Manual-Geometry-Node.jpg

   Geometry node


The geometry node is used to specify how light reflects off the surface.
This node is used to change a material's Normal response to lighting conditions.

Use this node to feed the Normal vector input on the Material node,
to see how the material will look (i.e. shine, or reflect light)
under different lighting conditions. Your choices are:

:guilabel:`Global`
   Global position of the surface.
:guilabel:`Local`
   Local position of the surface.
:guilabel:`View`
   Viewed position of the surface.
:guilabel:`Orco`
   Using the Original Coordinates of the mesh.
:guilabel:`UV`
   Using the UV coordinates of the mesh, selected in the field in bottom node.
:guilabel:`Normal`
   Surface Normal; On a flat plane with one light above and to the right reflecting off the surface.
:guilabel:`Vertex Color`
   Allows for output value of group vertex colors, selected in the field in bottom node.
:guilabel:`Vertex Alpha`
   Allows for output alpha value of vertex.
:guilabel:`Front/Back`
   Allows for output to take into account front or back of surface is light relative the camera.


.. admonition:: Note
   :class: note

   These are exactly the same settings as in the :doc:`Mapping </textures/mapping>` panel for :doc:`Textures </textures>`, though a few settings - like :guilabel:`Stress` or :guilabel:`Tangent` - are missing here. Normally you would use this node as input for a
   FIXME(TODO: Internal Link;
   [[#Texture Node|Texture Node]]
   ).


Geometry Node Example using a UV image
--------------------------------------

.. figure:: /images/26-Manual-Geometry-Node-Example.jpg
   :width: 500px
   :figwidth: 500px

   Setup to render an UV-Mapped Image Texture.


E.g.: To render an UV-mapped image, you would use the :guilabel:`UV` output and plug it into
the :guilabel:`Vector` Input of a texture node. Then you plug the color output of the texture
node into the color input of the material node - which corresponds to the setting on the
:guilabel:`Map To` panel.

