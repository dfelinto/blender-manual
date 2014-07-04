
To Sphere
=========

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Transform --> To Sphere`
   | Hotkey:   :kbd:`shift-alt-s`


Description
-----------

The :guilabel:`To Sphere` transformation will give the selection spherical qualities. The
*Suzanne with increasing sphericity* image below shows the results of applying the
:guilabel:`To Sphere` transformation to the Suzanne mesh.


.. figure:: /images/3D_interaction-Transformations-Advanced-To_Sphere_suzanne-spherical.jpg
   :width: 640px
   :figwidth: 640px

   Suzanne with inceasing sphericity. The sequence above shows a Suzanne mesh with a 0, 0.25 (25%), 0.5 (50%) and 1 (100%) To Sphere transform applied.


Usage
~~~~~

.. figure:: /images/3D_interaction-Transformations-Advanced-To_Sphere_toolshelf-f6.jpg
   :width: 150px
   :figwidth: 150px

   To Sphere Factor.


Select the elements you want to operate on and activate the :guilabel:`To Sphere` transform
function. The :guilabel:`To Sphere` option can be invoked from the :menuselection:`Mesh --> Transform --> To
Sphere` menu option or by pressing :kbd:`shift-alt-s`. The amount of sphericity given
to the selection can be determined interactively by moving the mouse or by typing a number
between 0 and 1. Pressing :kbd:`Enter` will confirm the transformation. The confirmed
transformation can be further edited by pressing :kbd:`F6` or by going into the
:guilabel:`Toolshelf` (:kbd:`T`) and altering the :guilabel:`Factor` slider provided
that no other actions take place between the :guilabel:`To Sphere` transform confirmation and
accessing the slider.


----

Note that the result of the :guilabel:`To Sphere` transform is also dependant on the number of
selected mesh elements (vertices, faces etc). As can be seen in the below image, the result
will be smoother and more spherical when there are more mesh elements available to work with.


.. figure:: /images/3D_interaction-Transformations-Advanced-To_Sphere_cubes-spherical.jpg
   :width: 640px
   :figwidth: 640px

   To Sphere applied to cubes with different subdivision levels. In this image sequence, To Sphere was applied to the entire cube at levels of 0, 0.25 (25%), 0.5 (50%) and 1 (100%) respectively.


The :guilabel:`To Sphere` transform will generate different results depending on the number
and arrangement of elements that were selected (as shown by the below image).


.. figure:: /images/3D_interaction-Transformations-Advanced-To_Sphere_other-spherical.jpg
   :width: 640px
   :figwidth: 640px

   To Sphere applied to different selections.


