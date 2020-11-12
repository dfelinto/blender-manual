
*******
Strokes
*******

Strokes are the final rendered lines. Yet you can tweak them, for example,
by removing the ones longer/shorter than some threshold,
chaining lines into a single stroke or breaking a stroke into several ones based on angles,
dashed pattern, etc.

.. figure:: /images/render_freestyle_parameter-editor_line-style_strokes_tab.png
   :align: center
   :width: 50%

   Line Style: Strokes


Chaining
========

By default all retrieved lines from the line set are chained together.
There are two basic chaining methods:

Plain
   The default chaining method; it creates simple chains.

Sketchy
   This chaining option allows for generating chains of feature edges with sketchy multiple strokes.
   Basically, it generates *Round* strokes instead of a single one.
   It is only really useful if you use some random-driven modifiers in the line style!

Rounds
   It specifies the number of rounds in sketchy strokes.

Chaining can also be turned off to render each line separately,
which can be useful for line styles which depend on accurate representation of the line set.


Splitting
=========

You can split up chains of Freestyle lines by checking one of the following:

Min, Max 2D Angle
   Splits chains of feature edges when they make a 2D angle above (or below) a minimum (or maximum) threshold.
2D Length
   Splits chains when they are longer than the given value.
Material Boundary
   Splits chains of feature edges if they cross from one material to another.

Split Dash, Gap
   Splits the chains using the given dashed pattern
   ("D" stands for "dash", "G" stands for "gap"; see also `Dashed Line`_).

   D1, G1, D2, G2, D3, G3


Sorting
=======

You can sort the order of your strokes, allowing the lines to stack in the order given.

Sort Key
   A sort key is used to determine the stacking order of lines.

   Distance from Camera
      Lines closer to the camera lie on top of further lines.
   2D Length
      Longer lines lie on top of shorter lines.
   Projected X, Y
      Sort by the projected X or Y value in the image coordinate system.
Integration Type
   Use in tandem with the Sort Key to determine the range for sorting.
   Since the distance of a line from the camera may vary over vertices,
   this option computes the sort key for a line from the values computed at
   individual vertices. The value computed for the line is:

   Mean
      The mean of the values obtained for the vertices.
   Min
      The minimum of the values obtained for the vertices.
   Max
      The maximum of the values obtained for the vertices.
   First
      The value obtained for the first vertex.
   Last
      The value obtained for the last vertex.
Sort Order
   With the given result you can choose to "Reverse" the sort order.


Selection
=========

You can also choose to only render selected chains.

Minimal, Maximal 2D Length
   Chains longer and/or shorter than *2D Length*.
Chain Count
   Allows the selection of first N chains.


Caps
====

You can choose between three types of line caps:

Butt
   Flat cap, exactly at the point the line ends.
Round
   A half circle centered on the end point of the line.
Square
   A square centered on the end point of the line
   (hence, like the circle, the drawn end of the line is slightly extended compared to its computed value).

.. figure:: /images/render_freestyle_parameter-editor_line-style_strokes_caps-example.png
   :align: center

   Line caps example.


Dashed Line
===========

By enabling the *Dashed Line* checkbox,
you can specify three pairs of dash and gap lengths.
Dash values define the lengths of dash strokes,
while gap values specify intervals between two dashes.

If a zero gap is specified,
then the corresponding dash is ignored even if it has a non-zero value.

Dashes are treated as separate strokes, meaning that you can apply line caps,
as well as color, alpha and thickness modifiers.
