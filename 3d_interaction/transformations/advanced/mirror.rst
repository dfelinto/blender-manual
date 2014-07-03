
Mirror
======


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` and :guilabel:`Edit` modes
   | Menu:     :menuselection:`Object/Mesh --> Mirror`
   | Hotkey:   :kbd:`ctrl-M`


Description
-----------


.. figure:: /images/3D-interaction_Transformations_Advanced_Mirror_mirror-example.jpg

   Mirroring a selection.


Mirroring an Object or Mesh selection will create a reversed version of the selection. The
position of the mirrored version of the selection is determined by the :guilabel:`Pivot
Point.` A common use of mirroring is to model half an object, duplicate it and then use the
mirror transform to create a reversed version to complete the model.
Note that mirrored duplicates can also be created with a :guilabel:`Mirror modifier.`


:doc:`Read more about the Pivot Point » <3d_interaction/transform_control/pivot_point>`

:doc:`Read more about the Mirror Modifier » <modifiers/generate/mirror>`


Usage
~~~~~


To mirror a selection along a particular global axis press:


:kbd:`ctrl-M`\ , followed by :kbd:`x`\ , :kbd:`y` or :kbd:`z`\ .


The image :guilabel:`Mirroring a selection` shows the results of this action after a mesh
element has been duplicated.


----

In Mesh mode, you can mirror the selection on the currently selected Transform Orientation by
pressing the appropriate axis key a second time. For example,
if the Transform Orientation is set to :guilabel:`Normal`\ , pressing:


:kbd:`ctrl-m`\ , followed by :kbd:`x` and then :kbd:`x` again


will mirror the selection along the X-axis of the :guilabel:`Normal Orientation.`

:doc:`Read more about Transform Orientations » <3d_interaction/transform_control/transform_orientations>`


.. figure:: /images/3D-interaction_Transformations_Advanced_Mirror_interactive-mirror.jpg

   Interactive mirror.


----

You can alternatively hold the :kbd:`mmb` to interactively mirror the object by moving
the mouse in the direction of the mirror axis.

