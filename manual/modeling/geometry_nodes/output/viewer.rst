.. index:: Geometry Nodes; Viewer
.. _bpy.types.GeometryNodeViewer:

***********
Viewer Node
***********

.. figure:: /images/node-types_GeometryNodeViewer.webp
   :align: right
   :alt: The Viewer node.

The *Viewer* node allows viewing data from inside a geometry node group in the
:doc:`Spreadsheet Editor </editors/spreadsheet>` and the 3D Viewport.

Any geometry connected can be visualized in the viewport and its attribute values
can be read in the spreadsheet. 


Activation and Deactivation
---------------------------

Using :kbd:`Shift-Ctrl-LMB` on any node or socket connects it to the viewer and makes it active.
Using the same shortcut on empty space in the node editor makes deactivates the active viewer.
When the active viewer is not visible anymore (e.g. another object is selected, or the current
node group is exited), it is deactivated. The icon in the viewer node header can also be used
to activate and deactivate it.

.. _bpy.types.SpaceView3D.show_viewer:

In the viewport, the *Show Viewer* option can turn off the viewer node visualization completely
in order to see the final output of the object's evaluation instead.

Attribute Visualization
-----------------------

When the viewer has a geometry and a separate value input connected, the values can be visualized
with a :doc:`viewport overlays </editors/3dview/display/overlays>`. When possible, the
:ref:`attribute domain <attribute-domains>` used to visualize the data is determined automatically.
Otherwise, the viewer node falls back to the face corner domain on meshes and the point domain
on curves. When necessary, the domain can be chosen manually.

.. _bpy.types.View3DOverlay.show_viewer_attribute:
.. _bpy.types.View3DOverlay.viewer_attribute_opacity:

The attribute overlay opacity can be controlled with the *Viewer Node* setting in the overlays popover.

The spreadsheet now only shows the "Viewer" column for the domain that is selected in the Viewer node.

Pinning
-------

It can be helpful to pin a specific viewer node in the spreadsheet. When pinned, the spreadsheet
still references the viewer node even when it becomes inactive.


Inputs
======

Geometry
   Geometry that will be displayed in the Spreadsheet.

Value
   Field to be evaluated on the geometry.
   The type for this value is chosen automatically when the keyboard shortcut to link
   an output is pressed. However, if the type must be adjusted manually,
   it is available in the node editor Sidebar.


Properties
==========

Data Type
   The data type used to evaluate the *Value* input, visible in the node side-bar.

Domain
   The :ref:`attribute domain <attribute-domains>` used to evaluate the *Value* input.
   The *Auto* option chooses the domain automatically based on the connected nodes.


Outputs
=======

This node has no outputs.
