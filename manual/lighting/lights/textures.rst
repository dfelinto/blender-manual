
Lamps Textures
**************

.. figure:: /images/25-Manual-Lighting-Lights-Texture-Panels.jpg
   :width: 307px
   :figwidth: 307px

   Lamp Texture panels


When a new lamp is added, it produces light in a uniform, flat color.
While this might be sufficient in simple renderings,
more sophisticated effects can be accomplished through the use of :doc:`textures </textures>`.
Subtle textures can add visual nuance to a lamp, while hard textures can be used to simulate more pronounced effects,
such as a disco ball, dappled sunlight breaking through treetops, or even a projector.
These textures are assigned to one of ten channels, and behave exactly like material textures,
except that they affect a lamp's color and intensity, rather than a material's surface characteristics.


Options
=======

The lamp textures settings are grouped into two panels. Here we will only talk about the few things that differ from object material textures; see the :doc:`Materials </materials>` and :doc:`Textures </textures>` chapters for details about the standard options.

The texture-specific and the :guilabel:`Mapping` panels remain the same. However, you'll note
there are much fewer :guilabel:`Mapping` options - you can only choose between
:guilabel:`Global`,
:guilabel:`View` or another :guilabel:`Object` 's texture :guilabel:`coordinates`
(since a lamp has no texture coordinates by itself), and you can scale or offset the texture.

The :guilabel:`Mapping` panel is also a subset of its regular material's counterpart.
You can only map a lamp texture to its regular,
basic :guilabel:`Color` and/or to its :guilabel:`Shadow` color. As you can only affect colors,
and a lamp has no texture coordinates on its own, the :guilabel:`Diffuse`,
:guilabel:`Specular`, :guilabel:`Shading`, and :guilabel:`Geometry` options have disappeared.


