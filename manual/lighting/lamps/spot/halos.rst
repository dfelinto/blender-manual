
..    TODO/Review: {{review|}} .


Spot Volumetric Effects
***********************

.. figure:: /images/25-Manual-Lighting-Lamps-Spot-HaloOptions.jpg
   :width: 310px
   :figwidth: 310px

   Spot lamps's Halo options


:guilabel:`Spot` lights also can produce "volumetric" effects. See :doc:`Volumetric Light </lighting/volumetric_lights>` for more information about what it means.

:guilabel:`Halo`
   The :guilabel:`Halo` button allows a :guilabel:`Spot` lamp to have a volumetric effect applied to it. This button must be active if the volumetric effect is to be visible. Note that if you are using buffered shadows, you have extra options described in the :doc:`Spot Buffered Shadows </lighting/lamps/spot/buffered_shadows>` page.

:guilabel:`Intensity`
   The :guilabel:`Intensity` slider controls how intense/dense the volumetric effect is that is generated from the light source. The lower the value of the :guilabel:`Intensity` slider, the less visible the volumetric effect is, while higher :guilabel:`Intensity` values give a much more noticeable and dense volumetric effect.
:guilabel:`Step`
   This field can have a value between ``0`` and ``12``. It is used to determine whether this :guilabel:`Spot` will cast volumetric shadows, and what quality those volumetric shadows will have.
   If :guilabel:`Step` is set to a value of ``0``, then no volumetric shadow will be generated.
   Unlike most other controls, as the :guilabel:`Step` value increases, the quality of volumetric shadows decreases (but take less time to render), and *vice versa*.

.. tip:: :guilabel:`Step` values

   A value of ``8`` for :guilabel:`Halo Step` is usually a good compromise between speed and accuracy.


   Blender only simulates volumetric lighting in :guilabel:`Spot` lamps when using its internal renderer. This can lead to some strange results for certain combinations of settings for the light's :guilabel:`Energy` and the halo's :guilabel:`Intensity`.
   For example, having a :guilabel:`Spot` light with null or very low light :guilabel:`Energy` settings but a very high halo :guilabel:`Intensity` setting can result in a dark/black halo, which would not happen in the real world. Just be aware of this possibility when using halos with the internal renderer.


.. admonition:: Note
   :class: note

   The halo effect can be greatly enhanced when using buffered shadows: when the halo's :guilabel:`Step` is not null, they can create "volumetric shadows". See the page about :guilabel:`Spot` :doc:`Buffered Shadows </lighting/lamps/spot/buffered_shadows>` for more information.


See Also
========

- :doc:`Shadows </lighting/shadows>`
- :doc:`Spot Lamp </lighting/lamps/spot>`
- :doc:`Spot Buffered Shadows </lighting/lamps/spot/buffered_shadows>`


