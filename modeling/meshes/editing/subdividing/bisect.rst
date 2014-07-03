


Mesh Bisect
===========


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Bisect`


The bisect tool is a quick way to cut a mesh in-two along a custom plane.

There are three important differences between this and the knife tool.


- The plane can be numerically adjusted in the operator panel for precise values.
- Cuts may remove geometry on one side.
- Cuts can optionally fill in the holes created, with materials and UV's & vertex-colors based on the surrounding geometry.

This means the bisect tool can cut off parts of a mesh without creating any holes.


.. figure:: /images/Mesh_bisect.jpg
   :width: 300px
   :figwidth: 300px

   Example of a common use of bisect


.. figure:: /images/Mesh_bisect_uv.jpg
   :width: 300px
   :figwidth: 300px

   Example of bisect with fill option


