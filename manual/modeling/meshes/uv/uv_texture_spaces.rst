
*******************
UVs & Texture Space
*******************

.. _uv-maps-panel:

UV Maps
=======

.. reference::

   :Mode:      All Modes
   :Panel:     :menuselection:`Properties --> Object Data --> UV Maps`

.. figure:: /images/modeling_meshes_uv_uv-texture-spaces_uv-maps.png

   The UV Maps panel in the Mesh tab.

If you have an active object, inside the Properties Editor, on the Object Data tab,
the UV maps panel contains a :ref:`List view <ui-list-view>`
that lists the UV maps created for this mesh.

If you have the UV Editor open, you will see the currently selected UV map.

Active Render
   Click the camera icon to enable that UV texture for rendering.
   If no other map is explicitly specified.

Add ``+``
   Clicking the *Add* button duplicates the selected UV map or creates a new UV map if the list is empty.

Remove ``-``
   Clicking the *Remove* button will remove the selected UV map.

.. seealso::

   Note that each texture can be mapped to a specific UV layout.

   .. TODO2.8 link to docs on UV mapping textures.


.. _bpy.types.*texspace:
.. _bpy.types.Mesh.texture_mesh:
.. _bpy.ops.curve.match_texture_space:
.. _properties-texture-space:

Texture Space
=============

.. reference::

   :Mode:      All Modes
   :Panel:     :menuselection:`Properties --> Object Data --> Texture Space`

These are settings of the :term:`Texture Space` used by generated texture mapping.
The visualization of the texture space can be activated in the :doc:`/scene_layout/object/properties/display`.

Auto Texture Space
   Adjusts the active object's texture space automatically when transforming the object.

   Location, Size
      If the texture space is not calculated automatically then you can define
      the location and size of the texture space relative to the base object.
      These can also be adjusted from the 3D Viewport, see `Editing`_ for more information.

----

Texture Mesh
   Use another mesh for texture indices, the vertex of the two objects must be perfectly aligned.
   Otherwise the UV map will be distorted. Note that, this is only for mesh objects.
Match Texture Space
   Modifies the *Location* and *Size* to match the objects bounding box.
   This disables Auto Texture Space. Note that, this is only for curve objects.

   .. is Match Texture Space the same thing as Auto Texture Space?


.. _properties-texture-space-editing:

Editing
-------

.. reference::

   :Mode:      Object Mode and Edit Mode
   :Menu:      :menuselection:`Object --> Transform --> Scale/Move Texture Space`

To modify the texture space from the 3D Viewport, enable
:ref:`Edit Texture Space <modeling_transform_edit-texture-space>` while transforming an object.


Accessing
---------

The automatically calculated UV map can be accessed by an object's material through
the *Generated* output of the :doc:`/render/shader_nodes/input/texture_coordinate`.
This output can then be used to map any texture onto an object.

.. tip::

   Generated texture spaces do not have rotation support, to overcome this,
   a :doc:`/render/shader_nodes/vector/mapping` can be used to rotate the UV map.
