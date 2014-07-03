
..    TODO/Review: {{review|}} .


EdgeSplit Modifier
==================

.. admonition:: Reference
   :class: refbox

   | Mode:     Any mode
   | Panel:    Properties Window → Context Button :guilabel:`Modifiers`

   .. figure:: /images/CZ_Modifier_ContextButton.jpg


Description
-----------

The :guilabel:`EdgeSplit` modifier splits edges within a mesh.
The edges to split can be determined from the edge angle (i.e.
angle between faces forming this edge), and/or edges marked as sharp.

Splitting an edge affects vertex normal generation at that edge, making the edge appear sharp. Hence, this modifier can be used to achieve the same effect as the :guilabel:`Autosmooth` button, making edges appear sharp when their angle is above a certain threshold. It can also be used for manual control of the smoothing process, where the user defines which edges should appear smooth or sharp (see :doc:`Mesh Smoothing <modeling/meshes/smoothing>` for other ways to do this). If desired, both modes can be active at once. The output of the :guilabel:`EdgeSplit` modifier is available to export scripts, making it quite useful for creators of game content.


Options
-------

.. figure:: /images/Reference-Panels-Modifier-EdgeSplit-2.5.jpg

   EdgeSplit modifier.


:guilabel:`From Edge Angle`
   If this button is enabled, edges will be split if their edge angle is greater than the :guilabel:`Split Angle` setting.

   - The edge angle is the angle between the two faces which use that edge.
   - If more than two faces use an edge, it is always split.
   - If fewer than two faces use an edge, it is never split.

:guilabel:`Split Angle`

   This is the angle above which edges will be split if the :guilabel:`From Edge Angle` button is selected, from **0- ** (all edges are split) to **180- ** (no edges are split). This performs the same action as the :menuselection:`Edge Specials --> Edge Split` menu item (\ :kbd:`ctrl-E`\ , in :guilabel:`Edit mode`\ )

:guilabel:`From Marked As Sharp`
   If this button is enabled, edges will be split if they are marked as sharp, using the :menuselection:`Edge Specials --> Mark Sharp` menu item (\ :kbd:`ctrl-E`\ , in :guilabel:`Edit mode`\ ).


Examples
--------

.. figure:: /images/Manual-Modifier-EdgeSplit-Example01.jpg
   :width: 600px
   :figwidth: 600px

   EdgeSplit modifier output with From Marked As Sharp selected.


.. figure:: /images/Edge_Split_to_improve_Smooth_Shading.jpg
   :width: 600px
   :figwidth: 600px

   (From Left to right): Flat Shading, Smooth Shading, Smooth Shading with Edge Split.


