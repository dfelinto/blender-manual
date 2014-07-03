
Viewmaps
========

There is only one viewmap per render layer. It controls the edge detection parameters. Which detected edges are actually rendered, and how, can be controlled either through the user-friendly :doc:`parameter editor <render/freestyle/parameter_editor>`\ , or powerful but complex :doc:`Python scripting <render/freestyle/python>`\ .

:guilabel:`Face Smoothness`
   When enabled, Face Smoothness will be taken into account for edges calculation.


.. figure:: /images/Manual-2.6-Render-Freestyle-Parameter_Editor_Mode.jpg
   :width: 200px
   :figwidth: 200px

   Parameter Editor Mode UI


:guilabel:`Crease Angle`
   If two adjacent faces form an angle less than the defined :guilabel:`Crease Angle`\ , the edge between them will be rendered when using :guilabel:`Crease` edge type selection in a line set. The value also affects :guilabel:`Silhouette` edge type selection.

:guilabel:`Culling`
   Ignore the edges that are out of view (saves some processing time and memory, but may reduce the quality of the result in some cases).


Advanced Options
----------------


.. figure:: /images/Manual-2.6-Render-Freestyle-Advanced_Options.jpg
   :width: 200px
   :figwidth: 200px

   Advanced Options


:guilabel:`Sphere Radius`
It affects the calculation of curvatures for :guilabel:`Ridge`\ ,
:guilabel:`Valley` and :guilabel:`Suggestive Contour` edge type selection in a line set.

:guilabel:`Kr Derivative Epsilon`
   It provides you with control over the output of :guilabel:`Suggestive Contour` and :guilabel:`Silhouette` edge type selection (further information in `this pdf <http://wiki.blender.org/index.php/file:Manual-2.6-Render-Freestyle-PrincetownLinestyle.pdf>`__\ ).