.. _bpy.types.SceneEEVEE.gtao:

*****************
Ambient Occlusion
*****************

Ambient occlusion is computed using :abbr:`GTAO (Ground Truth Ambient Occlusion)` and applied to indirect lighting.
The bent normal option will make the diffuse lighting come from only the least occluded direction.

Ambient occlusion can be rendered as a separate pass in the Render Layers panel.

.. note::

   This effect needs to be enabled for the :doc:`Ambient Occlusion </render/shader_nodes/input/ao>` node to work.

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Render --> Ambient Occlusion`

Distance
   Distance of object that contributes to the ambient occlusion effect.

Factor
   Blend factor for the ambient occlusion effect.

Trace Precision
   Increases precision of the effect but introduces more noise and lowers the maximum trace distance.
   Increased precision also increases the performance cost.
   Lower precision will also miss occluders and lead to undershadowing.

Bent Normals
   Compute the least occluded direction.
   This direction can be used to sample the diffuse irradiance in a more realistic way.

Bounce Approximation
   An approximation to simulate light bounces giving less occlusion on brighter objects.
   It only takes into account the surface color and not its surroundings.
   This is not applied to the ambient occlusion pass.

.. seealso:: :ref:`Limitations <eevee-limitations-ao>`.
