.. _bpy.ops.view3d.localview:
.. _editors-3dview-navigate-views-local:

**********
Local View
**********

Toggle Local View
=================

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Local View --> Toggle Local View`
   :Shortcut:  :kbd:`NumpadSlash`, :kbd:`Slash`

Global view shows all 3D objects in the scene. Local view isolates the selected object or
objects, so that they are the only ones visible in the viewport. This is useful for working on
objects that are obscured by other ones, or to speed up the viewport performance in heavy scenes.
Local view is contextual meaning that is can be set per 3D Viewport.

You can toggle between *Global* and *Local View* by selecting the option
from the *View Menu* or using the shortcut :kbd:`NumpadSlash`.

.. list-table::

   * - .. figure:: /images/editors_3dview_navigate_local-view_local1.png
          :width: 320px

          Global View.

     - .. figure:: /images/editors_3dview_navigate_local-view_local2.png
          :width: 320px

          Local View.

.. note::

   These notes cover changes in local view which are not immediately obvious.

   3D Cursor
      In local view the 3D cursor is not locked to the scene.
      Instead, each view has an independent cursor location.
   Layers
      Local view bypasses layers, using only the selected objects when entering local view.
      Although new objects can be added while in local view.

.. tip::

   Accidentally pressing :kbd:`NumpadSlash` can happen rather often if you are new to Blender,
   so if a bunch of the objects in your scene seem to have mysteriously vanished, try turning off local view.


.. _bpy.ops.view3d.localview_remove_from:

Remove from Local View
----------------------

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Local View --> Remove from Local View`
   :Shortcut:  :kbd:`M`

Objects can be removed from Local View by selecting them and using the *Remove from Local View* operator.
This will move the selected object back to global view and all other objects will remain in local view.
If the last remaining object is removed,
the local view will be left empty and you will have to exit local view to see any objects.
