.. _object-proxy:
.. _bpy.ops.object.proxy_make:
.. _files-library_proxies:

*******
Proxies
*******

Proxies are the historical way in Blender to allow some local editing of linked data-blocks.
This is mostly aimed at character animation.

One of their most important restrictions is that you can only have one proxy
of any linked object in a given blend-file.

A new system, more powerful and flexible, is currently being implemented:
:doc:`Library Overrides </files/linked_libraries/library_overrides>`.


Make Proxy
==========

.. reference::

   :Editor:    3D Viewport
   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Relations --> Make Proxy...`

This makes the active linked object into a local proxy, appending "_proxy" to its name.
It allows you to make changes locally over an object (or collection) linked from an external library.

Possible changes are restricted, you can mainly edit and animate transformations of the proxy object,
and its constraints.
Those changes remain local, they are not sent back to the external library.

.. hint::

   Another way to transform a linked object locally is with
   the use of :doc:`Collection Instancing </scene_layout/object/properties/instancing/collection>`.
   Instead of linking objects directly, it is often more useful to link in *collections*,
   which can be assigned to empties and moved, while maintaining the link to the original file.

   It is also useful to be able to add/remove objects from the collection (from within the library blend-file)
   without having to manage re-linking of multiple objects.


Proxy Armatures
---------------

On rigged models, proxy objects allow you to edit and animate their poses.

It is also possible, in the source (library) blend-file, to protect some bone layers from being editable in proxies.
This helps keeping complex rigs usage sensible, by only exposing some 'public' bone layers as editable by users.

Set the *Protected Layers* in the source file using the *Skeleton* panel of the *Armatures* properties.
See :ref:`Armature Layers <bpy.types.Armature.layers>`.
