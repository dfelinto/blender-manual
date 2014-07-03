


Warp
====


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` and :guilabel:`Edit` modes
   | Menu:     :menuselection:`Object/Mesh/Curve/Surface --> Transform --> Warp`
   | Hotkey:   :kbd:`shift-W`


.. figure:: /images/Doc26-warp.jpg

   warp tool options


In :guilabel:`Edit mode`\ , the :guilabel:`Warp` transformation takes selected elements and
warps them around the 3D cursor by a certain angle.
Note that this transformation is always dependent on the location of the 3D cursor.
The Pivot Point is not taken into account.
The results of the :guilabel:`Warp` transformation are also view dependent.

In :guilabel:`Object mode`\ , the :guilabel:`Warp` transformation takes the selected Objects and
causes them to move in an orbit-like fashion around the 3D cursor.
Similar to :guilabel:`Edit mode`\ ,
the Pivot Point is not taken into account and the results are view dependent.


Usage
-----


.. figure:: /images/3D-interaction_Transformation_Advanced_Warp_warp-mesh.jpg
   :width: 350px
   :figwidth: 350px

   In this example, a plane is warped around the 3D cursor by the indicated number of degrees.


..    Comment: <!--[[File:3D-interaction_Transformation_Advanced_Warp_warp-toolshelf-f6.png|thumb|right|300px|{{Literal|Warp}} Angle Slider.]]--> .

Select the elements you want to operate on and activate the :guilabel:`Warp` transform
function. The :guilabel:`Warp` option can be invoked from the
:menuselection:`Object/Mesh/Curve/Surface --> Transform --> Warp` menu option or by pressing
:kbd:`shift-w`\ . The amount of warping given to the selection can be determined
interactively by moving the mouse or by typing a number.
Pressing :kbd:`Enter` will confirm the transformation. The confirmed transformation can
be further edited by pressing :kbd:`F6` or by going into the Toolshelf (\ :kbd:`T`\ )
and altering the Angle slider provided that no other actions take place between the
:guilabel:`Warp` transform confirmation and accessing the slider.


Cursor position and view
~~~~~~~~~~~~~~~~~~~~~~~~


The location of the 3D cursor can be used to alter the results of the :guilabel:`Warp`
transformation. As can be seen from the example in this section, the :guilabel:`Warp` radius
is dependent on the distance of the cursor from the selected elements.
The greater the distance, the greater the radius.

The result of the :guilabel:`Warp` transform is also influenced by your current view. The
example in this section shows the results of a 180 degree :guilabel:`Warp` transform applied
to the same Suzanne mesh when in different views. A 3D render is also provided for comparison.


.. figure:: /images/3D-interaction_Transformation_Advanced_Warp_warp-cursor-view.jpg
   :width: 500px
   :figwidth: 500px

   The left side of this image shows how the Warp transform is influenced by the location of the cursor. The right hand side shows the influence of the current view.


.. admonition:: Warping text
   :class: note

   If you want to warp text, you will need to convert it from a Text Object to Mesh by pressing :kbd:`alt-c` and selecting the :guilabel:`Mesh from Curve/Meta/Surf/Text` option.


Example
-------


.. figure:: /images/3D-interaction_Transformation_Advanced_Warp_warp-text.jpg

   Text wrapped around logo. This was made by creating the Blender logo and text as separate Objects. The text was  converted to a mesh and then warped around the Blender logo.


