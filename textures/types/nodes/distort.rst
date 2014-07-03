

..    TODO/Review: {{review|text=examples}} .


Distort Nodes
=============

These nodes allow you to change the mapping of a texture.

Rotate
------


.. figure:: /images/Doc26-textureNodes-rotate.jpg

   Rotate node


Rotate the texture coordinates of an image or texture.

:guilabel:`Turns`
   The number of times to rotate the coordinates 360 degrees about the specified axis.
:guilabel:`Axis`
   The axis to rotate the mapping about


Translate
---------


.. figure:: /images/Doc26-textureNodes-translate.jpg

   Translate node


Translate the texture coordinates of an image or texture.
:guilabel:`Offset`
   The amount to offset the coordinates in each of the 3 axes.


Scale
-----


.. figure:: /images/Doc26-textureNodes-scale.jpg

   Scale node


Scale the texture coordinates of an image or texture.
:guilabel:`Scale`
   The amount to scale the coordinates in each of the 3 axes.


At
--


.. figure:: /images/Doc26-textureNodes-at.jpg

   At node


Returns the color of a texture at the specified coordinates.
If the coordinates are not spatially varying, the node will return a single color.

:guilabel:`Coordinates`
   The point at which to sample the color. For images, the space is between -1 and 1 for x and y.