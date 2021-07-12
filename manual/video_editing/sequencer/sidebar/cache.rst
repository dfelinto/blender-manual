
*****
Cache
*****

The Cache is used to save frames in memory for preview,
so they can be later displayed much faster than rendered from scratch.
Cache capacity can be set in :doc:`System tab </editors/preferences/system>` of the Preferences.

In order for this tab to be visible, enable :ref:`Developer Extras <prefs-interface-dev-extras>`.

.. seealso::

   Which frames are cached can be visualized by enabling :ref:`Show Cache <bpy.types.SequenceEditor.show_cache>`.


Cache Settings
==============

.. reference::

   :Panel:     :menuselection:`Sidebar --> Cache --> Cache Settings`

In this panel you can set up types of images that will be cached for all strips.

Cache
   Raw
      Cache raw images read from drive, for faster tweaking of strip parameters at the cost of memory usage.
   Pre-processed
      Cache preprocessed images, for faster tweaking of effects at the cost of memory usage.
   Composite
      Cache intermediate composited images, for faster tweaking of stacked strips at the cost of memory usage.
   Final
      Cache final image for each frame.


Strip Cache
===========

.. reference::

   :Panel:     :menuselection:`Sidebar --> Cache --> Cache Settings`

This panel sets the types of images that will be cached for the active strip.
Enable overriding the cache defaults, when disabled, `Cache Settings`_ will be used.

Cache
   Raw
      Cache raw images read from drive, for faster tweaking of strip parameters at the cost of memory usage.
   Pre-Processed
      Cache preprocessed images, for faster tweaking of effects at the cost of memory usage.
   Composite
      Cache intermediate composited images, for faster tweaking of stacked strips at the cost of memory usage.
