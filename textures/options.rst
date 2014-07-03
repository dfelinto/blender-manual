
Textures common options
=======================

In the Properties editor, choose the Texture context: this will show the Texture panel.


Textures Stack
--------------

.. figure:: /images/Doc-26-Manual-Textures-Stack.jpg
   :width: 300px
   :figwidth: 300px

   Textures Stack


The list below these buttons represents the :guilabel:`Stack` of textures that we can manage.
It can have up to eighteen :guilabel:`Texture Slots`\ :


- Tick or untick a texture to enable/disable it.
- Use the three buttons on the right side to move individual textures up and down in the stack or to copy/paste material's settings between slots.

The order in the Stack Textures defines how textures overlay each other for finally result
image.


Texture Datablock
-----------------

.. figure:: /images/Doc-26-Manual-Textures-Datablock.jpg
   :width: 300px
   :figwidth: 300px

   Active Texture Datablock


Select a slot in the Textures Stack to see its settings.

The first group of buttons below the stack displays the texture currently selected in the
stack.

:guilabel:`Browse`
    The first button below the stack displays the all available textures in the current file. Textures are stored globally, and can be linked to more than one material. If you have already created a texture that you want to reuse, select from this list.

:guilabel:`Name`
    A name field where the name of the material can be changed.

:guilabel:`Number of users`
    If the active texture is used by another material, a :guilabel:`2` button appears that can be used to make a single-user copy of the active texture.  Use this button to quickly create a new texture based on an existing texture.

:guilabel:`Fake`
    The :guilabel:`F` button assigns the active texture to a "Fake" material, so that the texture is saved with the file even if it has no "real" users.

:guilabel:`Add`
    Replaces the texture of the active slot with a new texture.

:guilabel:`Unlink`
    Removes the texture from the active slot.


Texture Type
------------

.. figure:: /images/Doc-26-Manual-Textures-Types.jpg
   :width: 300px
   :figwidth: 300px

   Texture Types


Choose the type of texture that is used for the current texture datablock.


- :doc:`Procedural Textures <textures/types/procedural>`
- :doc:`Image <textures/types/image>` and :doc:`Video <textures/types/video>` Textures
- :doc:`Environment Map <textures/mapping/environment>`
- :doc:`Volume Textures <textures/types/volume>`
- Ocean Texture

These types are described in detail :doc:`in this section <textures/types>`\ .


Preview
-------

.. figure:: /images/25-Manual-Textures-preview-panel.jpg
   :width: 300px
   :figwidth: 300px

   Preview panel


The texture preview panel provides a quick pre-visualisation of how the texture looks on its
own, without mapping.

:guilabel:`Texture`\ , :guilabel:`Material`\ , or :guilabel:`Both`
    Choose to display only the texture, only the material, or both.

:guilabel:`Show Alpha`
   Show alpha in preview.
   If Alpha: Use is checked in the :doc:`Image Sampling <textures/types/image>` panel, the image's alpha channel is displayed.
   If Alpha: Use is unchecked, an alpha channel based on averaged rgb values is displayed like it would be used by the Alpha slider in the :doc:`Influence <textures/influence/material>` panel.


Colors
------

.. figure:: /images/25-Manual-Textures-color-panel.jpg
   :width: 300px
   :figwidth: 300px

   Colors panel


The :guilabel:`Ramp` button activates a color ramp which allows you to remap the colors of a texture to new ones. See :doc:`Ramps <materials/properties/ramps>` for information on using ramps.

The color of a texture can be modified with the :guilabel:`Brightness`\ , :guilabel:`Contrast`\ ,
and  :guilabel:`Saturation` buttons. All textures with RGB-Values — including
:guilabel:`Images` and  :guilabel:`Environment Maps` — may be modified with the RGB
sliders.

:guilabel:`R`\ ,  :guilabel:`G`\ ,  :guilabel:`B`
   Tint the color of a texture by brightening each red, green and blue channel.
:guilabel:`Brightness`
   Change the overall brightness/intensity of the texture
:guilabel:`Contrast`
   Change the contrast of the texture
:guilabel:`Saturation`
   Change the saturation of the texture


Mapping
-------

Here you can control how the texture will be mapped on the object.


.. admonition:: Brushes
   :class: note

   These options are not available for brushes because they wouldn't make sense


See :doc:`Mapping <textures/mapping>` section for details.


Influence
---------

Here you can control what properties the texture will affect, and by how much.

They are detailed on the :doc:`Influence <textures/influence/material>` section.


.. admonition:: Brushes
   :class: note

   These options are not available for brushes because they wouldn't make sense


