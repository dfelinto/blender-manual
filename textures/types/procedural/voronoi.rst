
Procedural textures: Voronoi
============================


.. figure:: /images/25-Manual-Textures-Procedural-Voronoi.jpg
   :width: 307px
   :figwidth: 307px

   Voronoi Texture Panels


**Often used for**
   Very convincing Metal, especially the "Hammered" effect. Organic shaders (e.g. scales, veins in skin).
**Result(s)**
   Intensity (default) and Color


Options
-------

Distance Metric
   This procedural texture has seven Distance Metric options. These determine the algorithm to find the distance between cells of the texture. These options are:

   - :guilabel:`Minkovsky`
   - :guilabel:`Minkovsky 4`
   - :guilabel:`Minkovsky 1/2`
   - :guilabel:`Chebychev`
   - :guilabel:`Manhattan`
   - :guilabel:`Distance Squared`
   - :guilabel:`Actual Distance`

   The :guilabel:`Minkovsky` setting has a user definable value (the :guilabel:`Exponent` button) which determines the Minkovsky exponent (\ ``e``\ ) of the distance function ``(x``\ :sup:`e` ``+ y``\ :sup:`e` ``+ z``\ :sup:`e`\ ``)``\ :sup:`1/e`\ . A value of one produces the :guilabel:`Manhattan` distance metric, a value less than one produces stars (at **0.5**\ , it gives a :guilabel:`Minkovsky 1/2`\ ), and higher values produce square cells (at **4.0**\ , it gives a :guilabel:`Minkovsky 4`\ , at **10.0**\ , a :guilabel:`Chebychev`\ ). So nearly all Distance Settings are basically the same - variations of :guilabel:`Minkowsky`\ .
    You can get irregularly-shaped rounded cells with the :guilabel:`Actual Distance`\ /\ :guilabel:`Distance Squared` options.

+-------------------------------------------+------------------------------------------+-------------------------------------------------------+
+.. figure:: /images/VoronoyMinkovsky0.5.jpg|.. figure:: /images/VoronoyMinkovsky1.jpg |.. figure:: /images/VoronoiMinkovsky2.jpg              +
+   :width: 200px                           |   :width: 200px                          |   :width: 200px                                       +
+   :figwidth: 200px                        |   :figwidth: 200px                       |   :figwidth: 200px                                    +
+                                           |                                          |                                                       +
+   Minkovsky Exponent : 0.5 (Minkovsky 1/2)|   Minkovsky Exponent : 1 (Manhattan)     |   Minkovsky Exponent : 2 (Actual Distance)            +
+-------------------------------------------+------------------------------------------+-------------------------------------------------------+
+.. figure:: /images/VoronoyMinkovsky4.jpg  |.. figure:: /images/VoronoyMinkovsky10.jpg|.. figure:: /images/VoronoyDistanceSquared.jpg         +
+   :width: 200px                           |   :width: 200px                          |   :width: 200px                                       +
+   :figwidth: 200px                        |   :figwidth: 200px                       |   :figwidth: 200px                                    +
+                                           |                                          |                                                       +
+   Minkovsky Exponent : 4 (Minkovsky 4)    |   Minkovsky Exponent : 10 (Chebychev)    |   Distance Squared (More contrast than ActualDistance)+
+-------------------------------------------+------------------------------------------+-------------------------------------------------------+


:guilabel:`Feature Weights`
   These four sliders at the bottom of the Voronoi panel represent the values of the four Worley constants, which are used to calculate the distances between each cell in the texture based on the distance metric. Adjusting these values can have some interesting effects on the end result...    Comment: <!-- (no gallery yet) Check the Samples Gallery for some examples of these settings and what textures they produce. --> .

:guilabel:`Coloring`
   Four settings (\ :guilabel:`Intensity`\ , :guilabel:`Position`\ , :guilabel:`Position and Outline`\ , and :guilabel:`Position, Outline, and Intensity`\ ) that can use four different noise basis as methods to calculate color and intensity of the texture output. This gives the Voronoi texture you create with the "Worley Sliders" a completely different appearance and is the equivalent of the noise basis setting found on the other textures.


Technical Details
-----------------

For a more in depth description of the Worley algorithm, see:
`Worley Documentation <http://www.ypoart.com/Downloads/Worley.htm>`__\ (dead link).

