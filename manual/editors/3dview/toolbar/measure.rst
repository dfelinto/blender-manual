.. _bpy.ops.view3d.ruler:
.. _tool-measure:

*******
Measure
*******

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Tool:      :menuselection:`Toolbar --> Measure`

The *Measure* tool is an interactive tool where you can drag lines in the scene to measure distances or angles.
Snapping to geometry could be activated for better accuracy or to measure wall thickness.
The *Measure* tool can be accessed from the Toolbar.

.. figure:: /images/editors_3dview_toolbar_measure_ruler-example.png

   Examples of the Measure tool.


Usage
=====

Here are some common steps for using the *Measure* tool:

#. Activate the *Measure* tool from the Toolbar.
#. Click and drag in the viewport to define the initial start and end point for the ruler.
   You can add multiple rulers in the viewport.
#. Click on either end of the ruler to select it and move the endpoints.

   - Holding :kbd:`Ctrl` while moving enables snap to edges and vertices.
     A small circle appears when the end point is snapped to a vertex or edge.
     This way you can place the endpoints more accurately.
   - Holding :kbd:`Shift` while moving lets you measure the distance between faces.
     This works well only with parallel faces, e.g. walls.

   You can always navigate (pan, zoom, ...)
   or change the view (orthogonal, perspective) in the viewport to have better access to the ruler.

#. Click on the midpoint of a created ruler to convert it to a protractor.
   Move this midpoint to set the vertex of the angle.
   Holding down :kbd:`Ctrl` enables snap to edges and vertices.
   Move the endpoints to change the angle size.
#. A selected ruler can be deleted with :kbd:`Delete` or  :kbd:`X`.
   To delete all measurements, make the :menuselection:`Sidebar --> View --> Annotations` panel visible.
   Delete the "RulerData3D" layer (see image above).

All measurements are hidden when another tool is selected.
They are shown when the *Measure* tool is selected again.
Yet you can do editing operations while the ruler is active.
For example, you can edit the rotation or dimension of the selected object in the Sidebar.
The measurement values do not appear in the Render output.

Unit settings and scale from the scene are used for displaying dimensions.
Changing the units system (metric, imperial), or the units of length (cm, m, ...),
or angle (degrees, radians) will update the measurements.

.. tip::

   In Edit Mode only, there is also a *Measurement* setting in the *Viewport Overlays* popover.
   Edge length, edge angle, face area and face angle can be displayed through this setting.
