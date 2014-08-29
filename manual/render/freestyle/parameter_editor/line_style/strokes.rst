
Stroke
******

.. figure:: /images/Manual-2.6-Render-Freestyle-Stroke_UI.jpg
   :width: 300px
   :figwidth: 300px

   Stroke Line Style


Strokes are the final rendered lines. Yet you can tweaks them, for example,
by removing the ones longer/shorter than some threshold,
chaining lines into a single stroke or breaking a stroke into several ones based on angles,
dashed pattern, etc.


Chaining
========

By default all retrieved lines from the line set are chained together.
There are two basic chaining methods:

:guilabel:`Plain`
   The default chaining method; it creates simple chains.

:guilabel:`Sketchy`
   This chaining option allows for generating chains of feature edges with sketchy multiple strokes.
   Basically, it generates :guilabel:`Round` strokes instead of a single one.
   It is only really useful if you use some random-driven modifiers in the line style!

:guilabel:`Rounds`
   It specifies the number of rounds in sketchy strokes.

Chaining can also be turned off to render each line separately,
which can be useful for line styles which depend on accurate representation of the line set.


.. figure:: /images/Manual-2.6-Render-Freestyle-Chaining_UI.jpg
   :width: 300px
   :figwidth: 300px

   Chaining


Splitting
=========

You can split up chains of Freestyle lines by checking one of the following:

:guilabel:`Material Boundary`
   Splits chains of feature edges if they cross from one material to another.

:guilabel:`Min 2D Angle` and :guilabel:`Max 2D Angle`
   Splits chains of feature edges when they make a 2D angle above (or below) a minimum (or maximum) threshold.


.. figure:: /images/Manual-2.6-Render-Freestyle-Splitting_UI.jpg
   :width: 300px
   :figwidth: 300px

   Splitting


:guilabel:`2D Length`
   Splits chains when they are longer than the given value.

:guilabel:`D1` / :guilabel:`G1` / :guilabel:`D2` / :guilabel:`G2` / :guilabel:`D3` / :guilabel:`G3`
   Splits the chains using the given dashed pattern ("D" stands for "dash", "G" stands for "gap"; see also
   FIXME(TODO: Internal Link; [[#Dashed Line|below]])).


Selection
=========

.. figure:: /images/Manual-2.6-Render-Freestyle-Selection_Length_UI.jpg
   :width: 300px
   :figwidth: 300px

   Selection


You can also choose to only select (i.e. render)
chains longer than :guilabel:`Min 2D Length` and/or shorter than :guilabel:`Max 2D Length`.


Caps

----


You can choose between three types of line caps:

:guilabel:`Butt`
   Flat cap, exactly at the point the line ends.


.. figure:: /images/Manual-2.6-Render-Freestyle-Caps_UI.jpg
   :width: 300px
   :figwidth: 300px

   Line tip caps


:guilabel:`Round`
   A half circle centered on the end point of the line.

:guilabel:`Square`
   A square centered on the end point of the line (hence, like the circle,
   the drawn end of the line is slightly extended compared to its computed value).


Dashed Line
===========

.. figure:: /images/Manual-2.6-Render-Freestyle-Dashes_UI.jpg
   :width: 300px
   :figwidth: 300px

   Dashes Line UI


By enabling the :guilabel:`Dashed Line` check box,
you can specify three pairs of dash and gap lengths.
Dash values define the lengths of dash strokes,
while gap values specify intervals between two dashes.

If a zero gap is specified,
then the corresponding dash is ignored even if it has a non-zero value.

Dashes are treated as separate strokes, meaning that you can apply line caps,
as well as color, alpha and thickness modifiers.
..    Comment: <!--The image below shows a few examples of dashed lines on the default cube.--> .
