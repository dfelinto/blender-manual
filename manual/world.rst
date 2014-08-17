
..    TODO/Review: {{review|partial=X|text=missing some words on options that are explain in lighting and no explanation about Gather}} .


World
*****

.. figure:: /images/25-Manual-World-WorldPanel.jpg

   World panel


Blender provides a number of very interesting settings to complete your renderings by adding a
nice background, and some interesting 'depth' effects.
These are accessible via the :guilabel:`World` context.
By default a very plain uniform world is present. You can edit it or add a new World.

You have:

:doc:`Background <world/background>`
   The color and texture of the world background, with special settings for mapping coordinates.

:doc:`Mist <world/mist>`
   Add a mist to your scene to enhance the feeling of depth.

:doc:`Stars <world/stars>`
   Randomly covers the background with halo-like dots.

While these world settings offers a simple way of adding effects to a scene, :doc:`compositing nodes <composite_nodes>` are often preferred, though more complex to master, for the additional control and options they offer.  For example, filtering the Z value (distance from camera) or normals (direction of surfaces) through compositing nodes can further increase the depth and spacial clarity of a scene.


.. admonition:: Note
   :class: note

   Some of the settings under the World panel in Blender affect lighting so you find them under the :doc:`Lighting <lighting>` chapter (see :doc:`Ambient Light <lighting/environment>`, :doc:`Exposure <render/exposure>` and :doc:`Ambient Occlusion <lighting/ambient_occlusion>`).  When using a :guilabel:`Sun Lamp` options for :guilabel:`Sky & Atmosphere` are available in the :guilabel:`Lamp` menu.


