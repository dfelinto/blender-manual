.. _bpy.types.GPencilLayer:

*********
2D Layers
*********

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Panel:     :menuselection:`Object Data tab --> Layers`
   :Hotkey:    :kbd:`Y`


Layers List
===========

.. figure:: /images/grease-pencil_properties_layers_panel.png
   :align: right

   Grease Pencil Layers panel.

Grease Pencil objects each have a list of 2D layers for grouping and arranging strokes
in a :ref:`List view <ui-list-view>`. Any stroke can only belong to a single 2D layer.
There is always only one active layer in the list (the selected one).
When you draw, the new strokes are added to the active layer.
By default the view order of the layers in the viewport is top to bottom.

Every layer correspond to a channel in the Dope Sheet editor (in Grease Pencil mode).
See :doc:`Dope Sheet </editors/dope_sheet/grease_pencil>` for more information.
Layers can also be used together with Modifiers to only affects part of your drawing.
See :doc:`Modifiers </grease_pencil/modifiers/introduction>` for more information.

.. tip::

   Sometimes the layers you are not working on can be a distraction.
   Activate *Fade Layers* in overlays to control the opacity of the non-active layers.
   See :doc:`Overlays </editors/3dview/display/overlays>` for more information.

.. _bpy.types.GPencilLayer.mask_layer:
.. _bpy.types.GPencilLayer.lock:
.. _bpy.types.GPencilLayer.hide:
.. _bpy.types.GPencilLayer.use_onion_skinning:

Next to the layer name there are four icons buttons that control common properties of the layer:

.. _bpy.types.GPencilLayer.use_solo_mode:

Mask (mask icon)
   Toggle the :doc:`Masks </grease_pencil/properties/masks>` visibility in the layer.

Onion Skinning (onion skin icon)
   Toggle the use the layer for :doc:`Onion Skinning </grease_pencil/properties/onion_skinning>`.

Viewport/Render Visibility (eye icon)
   Toggle layer visibility in the viewport and in render.

Lock (padlock icon)
   Toggle layer from being editable.

.. _bpy.types.GPencilLayer.blend_mode:
.. _bpy.types.GPencilLayer.opacity:

Below the layers list there are additional common settings:

Blend
   The layer blending operation to perform. See :term:`Color Blend Modes`.

Opacity
   Used to set the opacity of the layer.

Use Lights
   When enabled, the layer is affected by lights.


Specials
--------

Duplicate Layer
   Makes an exact copy of the selected layer appending a number to differentiate its name.

Show All
   Turns on the visibility of every layer in the list.

Hide Others
   Turns off the visibility of every layer in the list except the active one.

Lock All
   Locks edition of all the layers in the list.

Unlock All
   Unlocks edition of all the layers in the list.

Autolock Inactive Layer
   Locks automatically the edition of every layer in the list except the active one.
   This way you avoid to make unwanted changes in other layers without the need to lock them every time.

Merge Down
   Merge the selected layer with the layer below, the new layer keeps the name of the lower layer.

Copy Layer to Object
   Makes a copy of the layer and move it to the selected Grease Pencil object.


Lock & Visibility General Controls
----------------------------------

Lock (padlock icon)
   Toggle whether the active layer is the only one that can be edited.

Visibility (screen icon)
   Toggle whether the active layer is the only one that can be edited and is visible.


Masks
=====

In a :ref:`List view <ui-list-view>` of layers affected by a layer mask.
See :doc:`Masks </grease_pencil/properties/masks>` for more information.


Adjustments
===========

.. figure:: /images/grease-pencil_properties_layers_adjustment.png
   :align: right

   Layers adjustment panel.

Tint Color/Factor
   Color that tint any material colors used in the layer.
   The *Factor* controls the amount of tint color to apply.

Stroke Thickness
   Thickness value that override the strokes thickness in the layer.

Pass Index
   The layer index number can be used with some modifiers to restrict changes to only certain areas.

   See :doc:`Modifiers </grease_pencil/modifiers/introduction>` for more information.

View Layer
   Defines the View Layer to use for the Grease Pencil layer.
   If empty, the layer will be included in all View Layers.
   This is useful to separate drawings parts for :doc:`compositing </compositing/introduction>`.

Disallow Locked Materials Editing
   Avoids editing locked materials in the layer. When disabled,
   any material can be edited even if they are locked in the material list.


Relations
=========

Parent/Type
   Select a Parent object and Type to manipulate the layer.
   The layer will inherit the transformations of the parent,
   this is especially useful when rigging for cut-out animation.


Display
=======

Custom Channel Color
   Sets the color to use in the channel region of the :doc:`Dope Sheet </editors/dope_sheet/grease_pencil>`.

Show Only On Keyframed
   Makes the layer visible in the viewport only if it has a keyframe in the actual frame.
   This helps for example when you are in the inking process using the *Fill* tool and want to only see
   the strokes that are in the actual frame to avoid fill in unwanted regions.
