
*******
Shading
*******

.. _bpy.ops.object.shade_smooth:

Shade Smooth
============

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Shade Smooth`

The easiest way is to set an entire object as smooth or faceted by selecting a mesh object,
and in *Object Mode*, select *Shade Smooth* in the *Object* menu.
This forces the assignment of the "smoothing" attribute to each face in the mesh,
including when you add or delete geometry.

Notice that the outline of the object is still strongly faceted.
Activating the smoothing features does not actually modify the object's geometry;
it changes the way the shading is calculated across the surfaces (normals will be interpolated),
giving the illusion of a smooth surface.

Select the *Shade Flat* item in the *Object* menu
to revert the shading back (normals will be constant)
to that shown in the first image above.

.. seealso::

   The :ref:`Auto Smooth <auto-smooth>` mesh property.


.. _bpy.ops.object.shade_flat:

Shade Flat
==========

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Shade Flat`

As seen in the previous sections, polygons are central to Blender.
Most objects are represented by polygons and truly curved objects
are often approximated by polygon meshes. When rendering images,
you may notice that these polygons appear as a series of small, flat faces.
Sometimes this is a desirable effect for hard surfaces,
but for organic surfaces you usually want your objects to look smooth.

.. list-table:: Example mesh flat (left) and smooth-shaded (right).
   `Sample blend-file <https://wiki.blender.org/wiki/File:25-manual-meshsmooth-example.blend>`__.

   * - .. figure:: /images/scene-layout_object_editing_shading_example-flat.png
          :width: 200px

     - .. figure:: /images/scene-layout_object_editing_shading_example-smooth.png
          :width: 200px
