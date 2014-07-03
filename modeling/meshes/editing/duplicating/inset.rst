
Inset
=====

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Faces --> Inset` or :menuselection:`[ctrl][F] --> Inset`
   | Hotkey:   :kbd:`I`


This tool takes the currently selected faces and creates an inset of them,
with adjustable thickness and depth. The tool is modal, such that when you activate it,
you may adjust the thickness with your mouse position. You may also adjust the depth of the
inset during the modal operation by holding :kbd:`ctrl`\ .


+----------------------------------------------+---------------------------------------------+
+.. figure:: /images/mesh_tool_inset_before.jpg|.. figure:: /images/mesh_tool_inset_after.jpg+
+   :width: 300px                              |   :width: 300px                             +
+   :figwidth: 300px                           |   :figwidth: 300px                          +
+                                              |                                             +
+   Selection to inset                         |   Selection with inset                      +
+----------------------------------------------+---------------------------------------------+


Options
-------

+------------------------------------------------+
+.. figure:: /images/mesh_tool_inset_settings.jpg+
+   :width: 200px                                +
+   :figwidth: 200px                             +
+                                                +
+   Inset Operator Settings                      +
+------------------------------------------------+


:guilabel:`Boundary`
    Determines whether open edges will be inset or not.
:guilabel:`Offset Even`
   Scale the offset to give more even thickness.
:guilabel:`Offset Relative`
   Scale the offset by surrounding geometry.
:guilabel:`Thickness`
   Set the size of the inset.
:guilabel:`Depth`
   Raise or lower the newly inset faces to add depth.
:guilabel:`Outset`
   Create an outset rather than an inset.
:guilabel:`Select Outer`
   Toggle which side of the inset is selected after operation.

