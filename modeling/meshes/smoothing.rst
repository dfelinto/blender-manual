
Mesh Shading
============


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
+.. figure:: /images/25-manual-meshsmooth-example-2rrflat.jpg                                                                                                                                                                  |.. figure:: /images/25-manual-meshsmooth-example-05edgesplit.jpg|.. figure:: /images/25-manual-meshsmooth-example-10edgeloops.jpg+
+   :width: 200px                                                                                                                                                                                                              |   :width: 200px                                                |   :width: 200px                                                +
+   :figwidth: 200px                                                                                                                                                                                                           |   :figwidth: 200px                                             |   :figwidth: 200px                                             +
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
+Example mesh rendered flat, smoothed using edge split, and using Subdivision Surface.  Note how edges are rendered differently. `Sample .blend <http://wiki.blender.org/index.php/:File:25-manual-meshsmooth-example.blend>`__                                                                                                                                  +
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+----------------------------------------------------------------+

As seen in the previous sections, polygons are central to Blender. Most objects are
represented by polygons and truly curved objects are often approximated by polygon meshes.
When rendering images, you may notice that these polygons appear as a series of small,
flat faces.

Sometimes this is a desirable effect, but usually we want our objects to look nice and smooth.
This section shows you how to visually smooth an object, and how to apply the :guilabel:`Auto
Smooth` filter to quickly and easily combine smooth and faceted polygons in the same object.

The last section on this page shows possibilities for smoothing a mesh's geometry,
not only its appearance.


Smooth shading
--------------


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` and :guilabel:`Object` mode
   | Panel:    :guilabel:`Mesh Tools` (\ :guilabel:`Editing` context)
   | Menu:     :menuselection:`Mesh --> Faces --> Shade Smooth / Shade Flat`
   | Hotkey:   :menuselection:`[ctrl][F] --> Shade Smooth / Shade Flat`


+----------------------------------------------------+---------------------------------------------------------------+
+.. figure:: /images/25-manual-meshsmooth-shading.jpg|.. figure:: /images/25-manual-meshsmooth-example-03rrsmooth.jpg+
+   :width: 80px                                     |   :width: 220px                                               +
+   :figwidth: 80px                                  |   :figwidth: 220px                                            +
+----------------------------------------------------+---------------------------------------------------------------+
+Same mesh smooth shaded                                                                                             +
+----------------------------------------------------+---------------------------------------------------------------+

The easiest way is to set an entire object as smooth or faceted by selecting a mesh object,
and in :guilabel:`Object` mode, click :guilabel:`Smooth` in the :guilabel:`Tool Shelf`\ .
This button does not stay pressed;
it forces the assignment of the "smoothing" attribute to each face in the mesh,
including when you add or delete geometry.

Notice that the outline of the object is still strongly faceted.
Activating the smoothing features doesn't actually modify the object's geometry;
it changes the way the shading is calculated across the surfaces,
giving the illusion of a smooth surface. Click the :guilabel:`Flat` button in the
:guilabel:`Tool Shelf`\ 's :guilabel:`Shading panel` to revert the shading back to that shown in
the first image above.


Smoothing parts of a mesh
~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, you can choose which edges to smooth by entering :guilabel:`Edit mode`\ ,
then selecting some faces and clicking the :guilabel:`Smooth` button.
The selected edges are marked in yellow.

When the mesh is in :guilabel:`Edit mode`\ ,
only the selected edges will receive the "smoothing" attribute. You can set edges as flat
(removing the "smoothing" attribute)
in the same way by selecting edges and clicking the :guilabel:`Flat` button.


Auto Smooth
-----------


.. admonition:: Reference
   :class: refbox

   | Panel:    :guilabel:`Properties` (\ :guilabel:`Object Data` context)


+-------------------------------------------------------------------+
+.. figure:: /images/25-manual-meshsmooth-example-04rrautosmooth.jpg+
+   :width: 180px                                                   +
+   :figwidth: 180px                                                +
+-------------------------------------------------------------------+
+.. figure:: /images/25-manual-meshsmooth-autosmooth.jpg            +
+   :width: 180px                                                   +
+   :figwidth: 180px                                                +
+-------------------------------------------------------------------+
+Example mesh with :guilabel:`Auto Smooth` enabled                  +
+-------------------------------------------------------------------+

It can be difficult to create certain combinations of smooth and solid faces using the above
techniques alone. Though there are workarounds
(such as splitting off sets of faces by selecting them and pressing :kbd:`Y`\ ),
there is an easier way to combine smooth and solid faces, by using :guilabel:`Auto Smooth`\ .

Auto smoothing can be enabled in the mesh's panel in the :guilabel:`Properties` window. Angles
on the model that are smaller than the angle specified in the :guilabel:`Angle` button will be
smoothed during rendering (i.e. not in the 3D view)
when that part of the mesh is set to smooth. Higher values will produce smoother faces,
while the lowest setting will look identical to a mesh that has been set completely solid.

Note that a mesh, or any faces that have been set as :guilabel:`Flat`\ ,
will not change their shading when :guilabel:`Auto Smooth` is activated: this allows you extra
control over which faces will be smoothed and which ones won't by overriding the decisions
made by the :guilabel:`Auto Smooth` algorithm.


Edge Split Modifier
-------------------

With the :doc:`Edge Split Modifier <modifiers/generate/edge_split>` we get a result similar to :guilabel:`Auto Smooth` with the ability to choose which edges should be split, based on angle—those marked as sharp.


+----------------------------------------------------------------+----------------------------------------------------------------+----------------------------------------------------------------+
+.. figure:: /images/25-manual-meshsmooth-example-05edgesplit.jpg|.. figure:: /images/25-manual-meshsmooth-example-07marksharp.jpg|.. figure:: /images/25-manual-meshsmooth-example-06marksharp.jpg+
+   :width: 200px                                                |   :width: 200px                                                |   :width: 200px                                                +
+   :figwidth: 200px                                             |   :figwidth: 200px                                             |   :figwidth: 200px                                             +
+                                                                |                                                                |                                                                +
+   Edge Split modifier enabled, based on angle                  |   Edges marked as sharp                                        |   Resulting render with sharp edge weighting                   +
+----------------------------------------------------------------+----------------------------------------------------------------+----------------------------------------------------------------+


----


Smoothing the mesh geometry
---------------------------

The above techniques do not alter the mesh itself, only the way it is displayed and rendered.
Instead of just making the mesh look like a smooth surface,
you can also physically smooth the geometry of the mesh with these tools:


Mesh editing tools
~~~~~~~~~~~~~~~~~~

You can apply one of the following in :guilabel:`Edit mode`\ :
:doc:`Smooth <modeling/meshes/editing/deforming/smooth>`
   This relaxes selected components, resulting in a smoother mesh.
:doc:`Laplacian Smooth <modeling/meshes/editing/deforming/smooth>`
   Smooths geometry by offers controls for better preserving larger details.
:doc:`Subdivide Smooth <modeling/meshes#specials>`
   Adjusting the :guilabel:`smooth` parameter after using the :guilabel:`subdivide` tool results in a more organic shape. This is similar to using the subdivide modifier.
:doc:`Bevel <modeling/meshes/editing>`
   This Bevels selected edged, causing sharp edges to be flattened.


Modifiers
~~~~~~~~~

Alternatively,
you can smooth the mesh non-destructively with one or several of the following modifiers:
:doc:`Smooth Modifier <modifiers/deform/smooth>`
   Works like the :guilabel:`Smooth` tool in :guilabel:`Edit mode`\ ; can be applied to specific parts of the mesh using vertex groups.
:doc:`Laplactian Smooth Modifier <modifiers/deform/laplacian_smooth>`
   Works like the :guilabel:`Laplacian Smooth` tool in :guilabel:`Edit mode`\ ; can be applied to specific parts of the mesh using vertex groups.
:doc:`Bevel Modifier <modifiers/generate/bevel>`
   Works like the :guilabel:`Bevel` tool in :guilabel:`Edit mode`\ ; Bevel can be set to work on an angle threshold, or on edge weight values.
:doc:`Subdivision Surface Modifier <modifiers/generate/subsurf>`
   Catmull-Clark subdivision produces smooth results. Sharp edges can be defined with :doc:`subdivision creases <modifiers/generate/subsurf#weighted_creases_for_subdivision_surfaces>` or by setting certain edges to "sharp" and adding an :doc:`EdgeSplit modifier <modifiers/generate/edge_split>` (set to :guilabel:`From Marked As Sharp`\ ) before the :guilabel:`Subsurf` modifier.




.. figure:: /images/25-manual-meshsmooth-example-08subsurf.jpg
   :width: 150px
   :figwidth: 150px

   Subsurf


.. figure:: /images/25-manual-meshsmooth-example-09edgecrease.jpg
   :width: 150px
   :figwidth: 150px

   Using creased edges, and resulting subsurf artifacts


.. figure:: /images/25-manual-meshsmooth-example-10edgeloops.jpg
   :width: 150px
   :figwidth: 150px

   Extra edge loops added


.. figure:: /images/25-manual-meshsmooth-example-11edgeloops.jpg
   :width: 150px
   :figwidth: 150px

   3D view showing creased edges (pink) and added edges loops (yellow)


