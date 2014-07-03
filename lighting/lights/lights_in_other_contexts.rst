


Lamps Related Settings
======================

Here are some options closely related to light sources, without being lamps settings.


Lighting Groups
---------------


Materials
~~~~~~~~~


.. figure:: /images/25-Manual-Lighting-LightGr-Mat.jpg
   :width: 317px
   :figwidth: 317px

   Light Group options for Materials


By default, materials are lit by all lamps in all visible layers, but a material (and thus all objects using that material) can be limited to a single group of lamps. This sort of control can be incredibly useful, especially in scenes with complex lighting setups. To enable this, navigate to the :guilabel:`Material` menu's :guilabel:`Options` panel and select a group of lamps in the :guilabel:`Light Group` field. Note that a :doc:`light group <modeling/objects/groups_and_parenting>` must be created first.

If the :guilabel:`Exclusive` button is enabled,
lights in the specified group will *only* affect objects with this material.


Render Layers
~~~~~~~~~~~~~


.. figure:: /images/25-Manual-Lighting-LightGr-RenLay.jpg
   :width: 317px
   :figwidth: 317px

   Light Group options for Render Layers


There's a similar control located in the :guilabel:`Layer panel` of the context :doc:`Render Layers <render/post_process/layers>`\ . If a light group name is selected in this :guilabel:`Light` field, the scene will be lit exclusively by lamps in the specified group.


See Also
--------


- :doc:`Lamps Introduction <lighting/lamps>`
- :doc:`Shadows <lighting/shadows>`
- :doc:`Materials Introduction <materials>`


