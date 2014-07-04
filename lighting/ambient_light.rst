
..    TODO/Review: {{review|partial=X}} .


Environment Lighting
--------------------

Environment light provides light coming from all directions.

Light is calculated with a ray-traced method which is the same as that used by Ambient
Occlusion. The difference is that Environment lighting takes into account the "ambient"
parameter of the material shading settings,
which indicates the amount of ambient light/color that that material receives.


.. figure:: /images/27x-Manual-Lighting-EL.jpg
   :width: 500px
   :figwidth: 500px

   Environment Lighting panel.


Also, you can choose the environment color source (white, sky color, sky texture)
and the light energy.

:guilabel:`Energy`
   Defines the strength of environment light.
:guilabel:`Environment Color`
   Defines where the color of the environment light comes from.

Using both settings simultaneously produces better global lighting.

It's good for mimicking the sky in outdoor lighting.
Environment lighting can be fairly noisy at times.