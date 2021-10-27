.. _object-proxy:
.. _bpy.ops.object.proxy_make:
.. _files-library_proxies:

*******
Proxies
*******

Proxies were the historical way in Blender to allow some local editing of linked data-blocks.
This was mostly aimed at character animation.

They are now fully deprecated as of Blender 3.0, replaced by the new
:doc:`Library Overrides </files/linked_libraries/library_overrides>`.

Existing proxies in older .blend files will be converted to library overrides when
opening it in Blender 3.0.

.. note::

   It is currently possible to keep existing proxies when opening an older .blend file,
   by disabling the :doc:`Proxy to Override Auto Conversion </editors/preferences/experimental>`
   experimental option in the Preferences.
   
   Existing Proxies will still work as expected in Blender 3.0.
   
   Removal of this option and the full proxy code is scheduled for Blender 3.1.

