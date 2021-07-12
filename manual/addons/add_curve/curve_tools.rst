
***********
Curve Tools
***********

This add-on provides an extensive set of tools for the manipulating
and editing of curves. Several :abbr:`CAD (Computer-Aided Design)` style curve tools are included.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Add Curve then Curve Tools to enable the script.


Interface
=========

This add-on is split into sub panels with each panel having it's own specific set of tools.


Curve Info
----------

.. reference::

   :Mode:      All Modes
   :Tool:      :menuselection:`Sidebar --> Edit --> Curve Info`

Curve
   Print splines, segments and empty splines information to the Info header and Info editor.
Spline
   Print splines information to the Info header and Info editor.
Segment
   Print segments information to the Info header and Info editor.
Length
   Calculate the length of the curve and show in the add-on's panel.


Curve Edit
----------

.. reference::

   :Mode:      All Modes
   :Tool:      :menuselection:`Sidebar --> Edit --> Curve Edit`

Fillet/Chamfer
   Round or chamfer Bézier point fillets.
Outline
   Create an outline around a selected curve object.
Recursive Offset
   Create an offsetted array.
Separate Offset/Selected
   Separate the outline mesh from the original.

Subdivide
   Subdivide selection or filleted corners.
Multi Subdivide
   Subdivide with level of details.
Split at Vertex
   Cuts the selected points creating openings.
Discretize Curve
   Disconnect the selected points.
Array Splines
   Create an array of the selected curves in Edit Mode.


Intersect
---------

.. reference::

   :Mode:      All Modes
   :Tool:      :menuselection:`Sidebar --> Edit --> Intersect`

2D Curve Boolean
   Boolean selected curves on a 2D plane.
Intersect Curves
   Create an intersection between flat curves on the same plane.


Surfaces
--------

.. reference::

   :Mode:      All Modes
   :Tool:      :menuselection:`Sidebar --> Edit --> Surfaces`

Birail
   It creates a surface from a profile and two paths.
   The order in which you select the curves and its direction is important to make this function properly.
Convert Bézier to Surface
   Convert the selected curve to a NURBS surface.
Convert Faces to Bézier
   Select faces and convert them to Bézier curves.


Loft
^^^^

.. reference::

   :Mode:      All Modes
   :Tool:      :menuselection:`Sidebar --> Edit --> Surfaces --> Loft`

Loft
   Loft a mesh object between two Bézier curves.
Auto Loft
   Turn on to store the loft data if you move or edit the curves.
Update Auto Loft
   Press this button to update the new loft mesh position after moving or editing parent curves.


Sanitize
--------

.. reference::

   :Mode:      All Modes
   :Tool:      :menuselection:`Sidebar --> Edit --> Sanitize`

Set Origin to Spline Start
   Move the origin of the curve to the first point.
Reset Scale
   Reset the objects scale to (1, 1, 1).


.. rubric:: Cleanup:

Remove Doubles
   Remove doubled points.
Short Splines
   Remove selected splines based on a threshold.


.. rubric:: Join Splines:

Join Neighboring Splines
   Join selected splines based on a threshold.


Utilities
---------

.. reference::

   :Mode:      All Modes
   :Tool:      :menuselection:`Sidebar --> Edit --> Utilities`


.. rubric:: Curve Resolution:

Show [ESC]
   Display the resolution in the interface with a colored overlay.


.. rubric:: Spline Order:

Show [ESC]
   Display and arrange the sequence.


Path Finder
^^^^^^^^^^^

.. reference::

   :Mode:      All Modes
   :Tool:      :menuselection:`Sidebar --> Edit --> Utilities --> Path Finder`

Tools for paths.


.. reference::

   :Category:  Add Curve
   :Description: Adds functionality for Bézier/NURBS curve/surface modeling.
   :Location: :menuselection:`Sidebar --> Edit tab`
   :File: curve_tools folder
   :Authors: MacKracken, cwolf3d, Alexander Meißner (Lichtso)
   :Contributors: guy lateur, Alexander Meißner (Lichtso), Dealga McArdle (zeffii), Marvin K. Breuer (MKB)
   :Maintainer: Vladimir Spivak (cwolf3d)
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
