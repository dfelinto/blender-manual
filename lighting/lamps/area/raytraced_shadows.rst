
..    TODO/Review: {{review|}} .

Area Raytraced Shadows
======================


.. figure:: /images/25-Manual-Lighting-Lamps-Area-AdapQMC.jpg
   :width: 300px
   :figwidth: 300px

   Adaptive QMC settings


The :guilabel:`Area` light source can only cast ray-traced shadows. The ray-traced shadows settings of this lamp are mostly shared with other lamps, as described in :doc:`Raytraced Properties <lighting/shadows/raytraced_properties>`\ . However, there are some specifics with this lamp, which are detailed below:


Shadow Samples
--------------

:guilabel:`Samples`
   This have the same role as with other lamps, but when using a :guilabel:`Rectangle` :guilabel:`Area` lamp, you have two samples settings: :guilabel:`Samples X` and :guilabel:`Samples Y`\ , for the two axes of the area plane.
    Note also that when using the :guilabel:`Constant Jittered` sample generator method, this is more or less equivalent to the number of virtual lamps in the area. With QMC sample generator methods, it behaves similarly to with :guilabel:`Lamp` or :guilabel:`Spot` lamps.


Sample Generator Types
----------------------

:guilabel:`Adaptive QMC`\ ;\ :guilabel:`Constant QMC`
   These common setting are described in :doc:`Shadow Properties <lighting/shadows/properties>`\ .


.. figure:: /images/25-Manual-Lighting-Lamps-Area-ContJitt.jpg
   :width: 300px
   :figwidth: 300px

   Constant Jittered settings


:guilabel:`Constant Jittered`
    The :guilabel:`Area` lamp has a third sample generator method, :guilabel:`Constant Jittered`\ , which is more like simulating an array of lights. It has the same options as the old one: :guilabel:`Umbra`\ , :guilabel:`Dither` and :guilabel:`Jitter`\ .

    The following three parameters are only available when using the :guilabel:`Constant Jittered` sample generator method, and are intended to artificially boost the "soft" shadow effect, with possible loss in quality:

   :guilabel:`Umbra`
      Emphasizes the intensity of shadows in the area fully within the shadow rays. The light transition between fully shadowed areas and fully lit areas changes more quickly (i.e. a sharp shadow gradient). You need :guilabel:`Samples` values equal to or greater than **2** to see any influence of this button.

   :guilabel:`Dither`
      Applies a sampling over the borders of the shadows, similar to the way anti-aliasing is applied by the :guilabel:`OSA` button on the borders of an object. It artificially softens the borders of shadows; when :guilabel:`Samples` is set very low, you can expect poor results, so :guilabel:`Dither` is better used with medium :guilabel:`Samples` values. It is not useful at all with high :guilabel:`Samples` values, as the borders will already appear soft.

   :guilabel:`Jitter`
      Adds noise to break up the edges of solid shadow samples, offsetting them from each other in a pseudo-random way. Once again, this option is not very useful when you use high :guilabel:`Samples` values where the drawback is that noise generates quite visible graininess.


Technical Details
-----------------


.. figure:: /images/Manual-Part-V-AreaLightConcept.jpg
   :width: 250px
   :figwidth: 250px

   Principles behind the Area light


The (\ *Principles behind the* :guilabel:`Area` *light*\ )
picture helps to understand how the soft shadows are simulated.

``(a)`` is the :guilabel:`Area` light as defined in Blender. If its shape is :guilabel:`Square`\ , then the softness of the shadow is defined by the number of light :guilabel:`Samples` in each direction of the shape. For example, ``(b)`` illustrates the equivalent case of an :guilabel:`Area` light (\ :guilabel:`Square` shape), with :guilabel:`Samples` set at **3** on the :guilabel:`Shadow and Spot` panel.

The :guilabel:`Area` lamp is then considered as a grid with a resolution of three in each
direction, and with a light "dupliverted" at each node for a total of nine lights.

In case ``(a)``\ , the energy (\ ``E``\ ) is ``E/1``\ , and in case
``(b)``\ , the energy of each individual pseudo-light is equal to ``E/
(Nbr of lights)``\ . Each pseudo-light produces a faint shadow
(proportional to its energy), and the overlay of the shadows produces the soft shadow
(it is darker where the individual shadows overlap, and lighter everywhere else).


Hints
-----

You will note that changing the :guilabel:`Size` parameter of your area lamp doesn't affect
the lighting intensity of your scene. On the other hand, rescaling the lamp using the
:kbd:`S` in the 3D View could dramatically increase or decrease the lighting intensity
of the scene. This behavior has been coded this way so that you can fine tune all your light
settings and then decide to scale up (or down)
the whole scene without suffering from a drastic change in the lighting intensity.
If you only want to change the dimensions of your :guilabel:`Area` lamp,
without messing with its lighting intensity,
you are strongly encouraged to use the :guilabel:`Size` button(s) instead.

If your computer isn't very fast,
when using the :guilabel:`Constant Jittered` sample generator method,
you could find it useful to set a low :guilabel:`Samples` value (like **2**\ )
and activate :guilabel:`Umbra`\ , :guilabel:`Dither`\ ,
and/or :guilabel:`Jitter` in order to simulate slightly softer shadows. However,
these results will never be better than the same lighting with high :guilabel:`Samples` values.
