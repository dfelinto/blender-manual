.. index:: Modifiers; Modeling Modifiers
.. index:: Modeling Modifiers

************
Introduction
************

Modifiers are automatic operations that affect an object's geometry in a non-destructive way.
With modifiers, you can perform many effects automatically that would otherwise be too tedious to do manually
(such as subdivision surfaces) and without affecting the base geometry of your object.

They work by changing how an object is displayed and rendered, but not the geometry which you can edit directly.
You can add several modifiers to a single object to form `The Modifier Stack`_
and *Apply* a modifier if you wish to make its changes permanent.

.. figure:: /images/modeling_modifiers_introduction_menu.png

   Modifiers menu.

They can be added to the active object using the *Add Modifier* drop-down menu at the top of their properties tab.
New modifiers are always added at the bottom of the :ref:`stack <modifier-stack>` (i.e. will be applied last).

There are four categories of modifiers:

Modify
   These are tools similar to the *Deform* ones (see below),
   however, they usually do not directly affect the geometry of the object,
   but some other data, such as vertex groups.
Generate
   These are constructive/destructive tools that will affect the whole :term:`Topology` of the mesh.
   They can change the general appearance of the object, or add new geometry to it...
Deform
   Unlike *Generate* ones above, these only change the shape of an object, without altering its topology.
Simulate
   Those represent :doc:`physics simulations </physics/index>`. In most cases, they are automatically added to
   the modifiers stack whenever a *Particle System* or *Physics* simulation is enabled. Their only role is to define
   the position in the modifier stack from which is taken the base data for the simulation they represent.
   As such, they typically have no attributes, and are controlled by settings exposed in
   separate sections of the :doc:`Properties </editors/properties_editor>`.


.. _bpy.types.Modifier.show:

Interface
=========

.. _fig-modifiers-panel-layout:

.. figure:: /images/modeling_modifiers_introduction_panel-layout.png
   :align: center

   Panel layout (Subdivision Surface as an example).

Each modifier's interface shares the same basic components, see Fig. :ref:`fig-modifiers-panel-layout`.

At the top is the panel header.
The icons each represent different settings for the modifier (left to right):

Expand (down/right arrow icon)
   Collapse modifier to show only the header and not its options.

Type
   An icon as a quick visual reference of the modifier's type.

.. _bpy.types.Modifier.name:

Name
   Every modifier has a unique name per object. Two modifiers on one object must have unique names,
   but two modifiers on different objects can have the same name. The default name is based on the modifier type.

.. _bpy.types.Modifier.show_on_cage:

Show on Cage (vertices triangle icon) -- Meshes only
   Depends on the previous setting, if enabled, the modified geometry can also be edited directly,
   instead of the original one.

   .. warning::

      While it shows edited items in their final, modified positions, you are still actually editing original data.
      This can lead to strong and unpredictable effects with some tools,
      and should be disabled whenever you need to perform complex or precise editing on the mesh.

.. _bpy.types.Modifier.show_in_editmode:

Show in Edit Mode (vertices square icon)
   Display the modified geometry in Edit Mode, as well as the original geometry which you can edit.

.. _bpy.types.Modifier.show_viewport:

Show in Viewport (screen icon)
   Toggle visibility of the modifier's effect in the 3D Viewport.

.. _bpy.types.Modifier.show_render:

Render (camera icon)
   Toggle visibility of the modifier's effect in the render.

   .. note::

      The *Square*, *Triangle* and *Surface* icons may not be available,
      depending on the type of object and modifier.

.. _bpy.types.Modifier.use_apply_on_spline:

Apply On Spline Points (point surface icon) -- Curves, surfaces and texts only
   Apply the whole modifier stack up to and including that one on the curve or surface control points,
   instead of their tessellated geometry.

   .. note::

      By default, curves, texts and surfaces are always converted to mesh-like geometry
      before that the modifier stack is evaluated on them.

.. _bpy.ops.object.modifier_apply:

Extras
   Apply :kbd:`Ctrl-A`
      Makes the modifier "real": converts the object's geometry to match the applied modifier's results,
      and deletes the modifier.

      When applying a modifier to an object that shares Object Data between multiple objects,
      the object must first be made a :ref:`Single User <data-system-datablock-make-single-user>`
      which can be performed by confirming the pop-up message.

      .. warning::

         Applying a modifier that is not first in the stack will ignore the stack order
         (it will be applied as if it was the first one), and may produce undesired results.

   .. _bpy.ops.object.modifier_apply_as_shapekey:

   Apply as Shape Key
      Stores the result of that modifier in a new relative :doc:`shape key </animation/shape_keys/introduction>`
      and then deletes the modifier from the modifier stack.
      This is only available with modifiers that do not affect the topology (typically, *Deform* modifiers only).

      .. note::

         Even though it should work with any geometry type that supports shape keys,
         currently it will only work with meshes.

   Save as Shape Key
      Stores the result of that modifier in a new relative :doc:`shape key </animation/shape_keys/introduction>`
      and keeps the modifier in the modifier stack.
      This is only available with modifiers that do not affect the topology (typically, *Deform* modifiers only).

   .. _bpy.ops.object.modifier_copy:

   Duplicate :kbd:`Shift-D`
      Creates a duplicate of the modifier just below current one in the stack.

   .. _bpy.ops.object.modifier_copy_to_selected:

   Copy to Selected
      Copies the modifier from the :term:`Active` object to all selected objects.

   .. _bpy.ops.object.modifier_move_to_index:

   Move to First/Last
      Moves the modifier to the first or last position in the modifier stack.

.. _bpy.ops.object.modifier_remove:

Delete :kbd:`X`, :kbd:`Delete`
   Delete the modifier.

Move ``::::``
   Move the modifier up/down in the :ref:`stack <modifier-stack>`,
   changing the evaluation order of the modifiers.

Below this header, all of the options unique to each modifier will be displayed.


.. _modifier-stack:

The Modifier Stack
------------------

Modifiers are a series of non-destructive operations which can be applied on top of an object's geometry.
You can be apply them in almost any order.
This kind of functionality is often referred to as a "modifier stack"
and is also found in several other 3D applications.

In a modifier stack, the order in which modifiers are applied has an effect on the result.
Therefore the modifiers can be re-arranged by clicking the grab widget (``::::``) in the top right,
and moving the selected modifier up or down.
For example, the image below shows :doc:`Subdivision Surface </modeling/modifiers/generate/subdivision_surface>`
and :doc:`Mirror </modeling/modifiers/generate/mirror>` modifiers that have switched places.

.. list-table:: Modifier Stack example.

   * - .. figure:: /images/modeling_modifiers_introduction_mirror-subdiv2.png
          :width: 320px

          The Mirror modifier is the last item in the stack and
          the result looks like two surfaces.

     - .. figure:: /images/modeling_modifiers_introduction_mirror-subdiv1.png
          :width: 320px

          The Subdivision Surface modifier is the last
          item in the stack and the result is a single merged surface.

Modifiers are calculated from top to bottom in the stack.
In this example, the desired result (on right) is achieved by first mirroring the object,
and then calculating the subdivision surface.


.. _modifier-stack-active:

Active Modifier
^^^^^^^^^^^^^^^

A modifier in the stack can be selected to mark in as :term:`Active`,
the active modifier displays an outline around the modifier's panel.
To set an active modifier, select an area of the modifier's panel background,
the modifier's icon, or, select a modifier in the :doc:`/editors/outliner/index`.

The active modifier is used by the :doc:`/editors/geometry_node`
to determine which node group is being modified.


Example
=======

.. figure:: /images/modeling_modifiers_introduction_stack-example-3.png

   In this example a simple subdivided cube has been transformed into a rather complex object using
   a stack of modifiers.

`Download example file <https://wiki.blender.org/wiki/File:25-Manual-Modifiers-example.blend>`__.
