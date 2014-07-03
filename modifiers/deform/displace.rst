
Displace Modifier
=================

.. admonition:: Reference
   :class: refbox

   | Mode:     Any mode
   | Panel:    :guilabel:`Modifiers`


Description
-----------

The :guilabel:`Displace` modifier displaces vertices in a mesh based on the intensity of a
texture. Either procedural or image textures can be used.
The displacement can be along a particular local axis, along the vertex normal,
or the separate RGB components of the texture can be used to displace vertices in the local X,
Y and Z directions simultaneously.


Options
-------

.. figure:: /images/25-Manual-Modifiers-Displace.jpg

   Displace modifier


:guilabel:`Texture`
   The name of the texture from which the displacement for each vertex is derived.
    If this field is empty, the modifier defaults to 1.0 (white).

:guilabel:`Vertex Group`
   The name of a vertex group which is used to control the influence of the modifier.
    If :guilabel:`VGroup` is empty, the modifier affects all vertices equally.

:guilabel:`Midlevel`
   The texture value which will be treated as no displacement by the modifier. Texture values below this value will result in negative displacement along the selected direction, while texture values above this value will result in positive displacement. This is achieved by the equation ``(displacement) = (texture value) - Midlevel``\ .
    Recall that color/luminosity values are typically between **0.0** and **1.0** in Blender, and not between **0** and **255**\ .

:guilabel:`Direction`
   The direction along which to displace the vertices.
    Can be one of the following:

   - :guilabel:`X` - displace along local X axis.
   - :guilabel:`Y` - displace along local Y axis.
   - :guilabel:`Z` - displace along local Z axis.
   - :guilabel:`RGB → XYZ` - displace along local XYZ axes individually using the RGB components of the texture.
   - :guilabel:`Normal` - displace along vertex normal.

:guilabel:`Texture Coordinates`
   The texture coordinate system to use when retrieving values from the texture for each vertex.
    Can be one of the following:


   - :guilabel:`UV` - take texture coordinates from face UV coordinates.

      :guilabel:`UV Layer`
         The UV coordinate layer from which to take texture coordinates.
          If the object has no UV coordinates, it uses the :guilabel:`Local` coordinate system. If this field is blank, but there is an UV coordinate layer available (e.g. just after adding the first UV layer to the mesh), it will be overwritten with the currently active UV layer.

.. admonition:: Note
   :class: note

   Since UV coordinates are specified per face, the UV texture coordinate system currently determines the UV coordinate for each vertex from the first face encountered which uses that vertex; any other faces using that vertex are ignored. This may lead to artifacts if the mesh has non-contiguous UV coordinates.


   - :guilabel:`Object` - take the texture coordinates from another object's coordinate system (specified by the :guilabel:`Object` field).

      :guilabel:`Object`
         The object from which to take texture coordinates. Moving the object will therefore alter the coordinates of the texture mapping.  Take note that moving the original object will **also** result in a texture coordinate update.  As such, if you need to maintain a displacement coordinate system while moving the object to which the displacement is set, you will also have to move the related object at the same rate and direction.
         If this field is blank, the :guilabel:`Local` coordinate system is used.


   - :guilabel:`Global` - take the texture coordinates from the global coordinate system.


   - :guilabel:`Local` - take the texture coordinates from the object's local coordinate system.

:guilabel:`Strength`
   The strength of the displacement. After offsetting by the :guilabel:`Midlevel` value, the displacement will be multiplied by the :guilabel:`Strength` value to give the final vertex offset. This is achieved by the equation ``(vertex_offset) = (displacement) × Strength``\ .
   A negative strength can be used to invert the effect of the modifier.


See also
========

- Blender artists post: `Displace modifier tutorial <http://blenderartists.org/forum/showthread.php?t=77026>`__ (September 2006)


