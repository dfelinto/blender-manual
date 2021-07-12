
*******
Options
*******

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Options`

Display
   Fast Navigate
      For multiresolution models, shows low resolution while navigating in the viewport.
   Delay Viewport Updated
      Update the geometry when it enters view. This provides for faster navigation.
   Use Deform Only
      Limits the activated modifiers on the active object to Deform Modifiers, and Multiresolution.
      Constructive modifiers (like Subdivision Surface, Mirror and other) get deactivated,
      because they could give inaccurate results.

Auto-Masking
   These settings automatically mask geometry based on geometric properties of the mesh.
   Note, these options are applied across all sculpt brushes, however, they can also be configured
   per brush in the :ref:`Advanced Brush Settings <sculpt-tool-settings-brush-settings-advanced>`.
   These options can be accessed via a :ref:`bpy.types.UIPieMenu` by pressing :kbd:`Alt-A`.

   Topology
      Brush affects only vertices connected to the active vertex under the brush.
   Face Sets
      Affect only vertices that share face sets with active vertex.
   Mesh Boundary
      Does not affect non-manifold boundary edges.
   Face Sets Boundary
      Does not affect vertices which belong to a face set boundary.

.. seealso::

   See the :ref:`Display <sculpt-paint-brush-display>` options.


Gravity
=======

.. _bpy.types.Sculpt.gravity:

Factor
   Setting the factor allows you to add gravity to your brush strokes,
   giving it a draping effect.

.. _bpy.types.Sculpt.gravity_object:

Orientation
   Using another object, the gravity can be oriented to the set object's local Z axis,
   changing the direction of the gravity.
