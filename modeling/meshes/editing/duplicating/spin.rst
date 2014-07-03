
..    TODO/Review: {{review|text=reorganize, elaborate}} .


Spin
====

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Mesh Tools` (\ :guilabel:`Editing` context)


Use the :guilabel:`Spin` tool to create the sort of objects that you would produce on a lathe
(this tool is often called a "lathe"-tool or a "sweep"-tool in the literature,
for this reason). In fact, it does a sort of circular extrusion of your selected elements,
centered on the 3D cursor, and around the axis perpendicular to the working view…


- The point of view will determine around which axis the extrusion spins…
- The position of the 3D cursor will be the center of the rotation.

Here are its settings:
:guilabel:`Steps`
   Specifies how many copies will be extruded along the "sweep".
:guilabel:`Dupli`
   When enabled, will keep the original selected elements as separated islands in the mesh (i.e. unlinked to the result of the spin extrusion).
:guilabel:`Angle`

   specifies the angle "swept" by this tool, in degrees (e.g. set it to **180 - ** for half a turn).

:guilabel:`Center`
   Specifies the center of the spin. By default it uses the cursor position.
:guilabel:`Axis`
   Specify the spin axis as a vector. By default it uses the view axis.


Example
=======

.. figure:: /images/Spin1.jpg
   :width: 300px
   :figwidth: 300px

   Glass profile.


First, create a mesh representing the profile of your object.
If you are modeling a hollow object, it is a good idea to thicken the outline.
(\ *Glass profile*\ ) shows the profile for a wine glass we will model as a demonstration.

Go to the :guilabel:`Edit` mode and select all the vertices of the Profile with :kbd:`A`\ .

We will be rotating the object around the cursor in the top view,
so switch to the top view with :kbd:`pad7`\ .


.. figure:: /images/Spin2.jpg
   :width: 300px
   :figwidth: 300px

   Glass profile, top view in Edit mode, just before spinning.


Place the cursor along the center of the profile by selecting one of the vertices along the
center, and snapping the 3D cursor to that location with :menuselection:`[shift][S] --> Cursor →
Selection`\ . (\ *Glass profile, top view in* :guilabel:`Edit` *mode, just before spinning*\ )
shows the wine glass profile from top view, with the cursor correctly positioned.


Click the :guilabel:`Spin` button. If you have more than one 3D view open, the cursor will
change to an arrow with a question mark and you will have to click in the window containing
the top view before continuing. If you have only one 3D view open,
the spin will happen immediately. (\ *Spun profile*\ ) shows the result of a successful spin.


Angle
-----

.. figure:: /images/Spin3.jpg
   :width: 300px
   :figwidth: 300px

   Spun profile using an angle of 360


.. figure:: /images/Spin4.jpg
   :width: 300px
   :figwidth: 300px

   Spun profile using an angle of 120


Dupli
-----

.. figure:: /images/Spin6.jpg
   :width: 300px
   :figwidth: 300px

   Result of spin operation


.. figure:: /images/Spin7.jpg
   :width: 300px
   :figwidth: 300px

   Result of Dupli enabled


Merge Duplicates
----------------

.. figure:: /images/Spin8.jpg
   :width: 300px
   :figwidth: 300px

   Duplicate vertices


The spin operation leaves duplicate vertices along the profile.
You can select all vertices at the seam with Box select (\ :kbd:`B`\ ) shown in
(\ *Seam vertex selection*\ ) and perform a :guilabel:`Remove Doubles` operation.


Notice the selected vertex count before and after the :guilabel:`Remove Doubles` operation
(\ *Vertex count after removing doubles*\ ). If all goes well, the final vertex count
(38 in this example) should match the number of the original profile noted in
(\ *Mesh data - Vertex and face numbers*\ ). If not,
some vertices were missed and you will need to weld them manually. Or, worse,
too many vertices will have been merged.


.. admonition:: Merging two vertices in one
   :class: note

   To merge (weld) two vertices together, select both of them by :kbd:`shift-rmb` clicking on them. Press :kbd:`S` to start scaling and hold down :kbd:`ctrl` while scaling to scale the points down to 0 units in the X, Y and Z axis. :kbd:`lmb` to complete the scaling operation and click the :guilabel:`Remove Doubles` button in the :guilabel:`Buttons` window, :guilabel:`Editing` context (also available with :menuselection:`[W] --> Remove Doubles`\ ).


   Alternatively,
   you can use :menuselection:`[W] --> Merge` from the same :guilabel:`Specials` menu
   (or :kbd:`alt-M`\ ). Then, in the new pop-up menu, choose whether the merged vertex will
   be at the center of the selected vertices or at the 3D cursor.
   The first choice is better in our case!


Recalculate Normals
-------------------

All that remains now is to recalculate the normals to the outside by selecting all vertices,
pressing :kbd:`ctrl-N` and validating :guilabel:`Recalc Normals Outside` in the pop-up
menu.


