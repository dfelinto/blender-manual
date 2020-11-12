
*****
Masks
*****

Layers List
===========

.. figure:: /images/grease-pencil_properties_masks_layers-panel.png
   :align: right

   Layer list with masked layers.

In Grease Pencil there are no special mask layers, any layer can act as a mask for other layers.
The mask system is flexible enough to allow top-bottom and bottom-top masking.

Layers used as mask can use all the blend modes and different opacity values like any other layer.

.. note::

   If you want to make a full transparent masking
   you will have to set the mask layer(s) opacity to 0.

By activating the mask toggle (mask icon) next to the layer name or
using the checkbox on the masks panel header
the layer becomes prepared to be masked by other layer(s).

.. figure:: /images/grease-pencil_properties_masks_panel.png
   :align: right

   Masks list view.


Masks List
==========

The layer/s that will act as mask of the current layer could be added
to the Mask :ref:`list view <ui-list-view>`.

In the Masks list next to the layers name there are two icons buttons that control
common properties of the layer mask:

Invert (mask icon)
   Inverts the mask.

Viewport/Render Visibility (eye icon)
   Toggle layer visibility in the viewport and in render.


Example
=======

.. list-table:: Mask (green circle) samples.

   * - .. figure:: /images/grease-pencil_properties_masks_example-01.png
          :width: 200px

          Original image (Blend: Regular, Opacity: 1).

     - .. figure:: /images/grease-pencil_properties_masks_example-02.png
          :width: 200px

          Blend: Hard Light, Opacity: 1.

     - .. figure:: /images/grease-pencil_properties_masks_example-03.png
          :width: 200px

          Blend: Regular, Opacity: 1.
