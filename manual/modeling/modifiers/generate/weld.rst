.. index:: Modeling Modifiers; Weld Modifier
.. _bpy.types.WeldModifier:

*************
Weld Modifier
*************

The *Weld* modifier looks for groups of vertices within a threshold and merges them,
collapsing the surrounding geometry.


Options
=======

.. figure:: /images/modeling_modifiers_generate_weld_panel.png
   :align: right
   :width: 300px

   The Weld modifier.

Distance
   Maximum distance that the vertices must have each other to be merged.

Duplicate Limit
   For a better performance, limits the number of elements found per vertex.
   0 makes it infinite.

Vertex Group
   When the *Vertex Group* option is selected, only vertices with weight above zero will be affected by the modifier.

   Invert ``<->``
      Inverts the influence of the selected vertex group, meaning that the group
      now represents vertices that will not be deformed by the modifier.

      The setting reverses the weight values of the group.
