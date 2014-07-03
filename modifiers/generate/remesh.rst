


Remesh Modifier
===============


.. admonition:: Reference
   :class: refbox

   | Mode:     Object mode
   | Panel:    Properties Window → Context Button :guilabel:`Modifiers`

   .. figure:: /images/CZ_Modifier_ContextButton.jpg


Description
-----------


The Remesh modifier is a tool for generating new mesh topology based on an input surface.
The output follows the surface curvature of the input, but its topology contains only quads.


.. figure:: /images/Remesh-modifier-screenshot-00.jpg
   :width: 600px
   :figwidth: 600px


Usage
~~~~~


In the modifier panel, add a Remesh modifier. (This modifier is only available for meshes.)
The input mesh should have some thickness to it; if the input is completely flat,
add a solify modifier above the remesh modifier.


Mode
____


There are three basic modes available in the remesh modifier: Blocks, Smooth and Sharp.


.. figure:: /images/Remesh-mode-cone-example.jpg
   :width: 600px
   :figwidth: 600px

   This example shows a cone with each of the different remesh modes. From left to right: original cone, Blocks, Smooth, and Sharp


Note that the output topology is almost identical between the three modes;
what changes is the smoothing. In Blocks mode, there is no smoothing at all.
The Smooth and Sharp modes generate similar output in places where the mesh is already smooth,
but Sharp mode preserves sharp details better. In this example, the circular bottom of the
cone and the top point of the cone are accurately reproduced in Sharp mode.


Octree Depth and Scale
______________________


The Octree Depth sets the resolution of the output.
Low values will generate larger faces relative the input,
higher values generate a denser output.
The result can be tweaked further by setting the Scale;
lower values effectively decrease the output resolution.


.. figure:: /images/Remesh-depth-cone-example.jpg
   :width: 600px
   :figwidth: 600px

   Input mesh, and the low to high resolution output meshes


Disconnected Pieces
___________________


To filter out small disconnected pieces of the output, enabled Remove Disconnected and set the
threshold to control how small a disconnected component must be to be removed.


.. figure:: /images/Remesh-remove-disconnected-example.jpg
   :width: 600px
   :figwidth: 600px

   The input mesh (left) is fairly noisy, so the initial output of the remesh modifier (center) contains small disconnected pieces. Enabling Remove Disconnected Pieces (right) deletes those faces.


Sharpness
_________


In Sharp mode,
set the Sharpness value to control how closely the output follows sharp edges in the input
(use lower values to filter out noise).


Demo Videos
~~~~~~~~~~~


FIXME(Tag Unsupported:div;
<div style="text-align: center !important;">
<youtube width="640" height="360">TvNHiHdrjUw</youtube>

<youtube width="640" height="360">Mh-gUnS2c0Y</youtube>

<youtube width="640" height="360">dker8gRuww4</youtube>

<youtube width="640" height="360">5njU1nIyC6I</youtube>

<vimeo width="640" height="360" >21096739</vimeo>

<vimeo width="640" height="360" >21330126</vimeo>
</div>
)


.. figure:: /images/Remesh-text-00.jpg
   :width: 640px
   :figwidth: 640px

   Remesh modifier applied to text to improve topology


