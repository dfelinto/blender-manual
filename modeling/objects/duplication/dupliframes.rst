
DupliFrames
===========

DupliFrames is a tool to duplicate objects at frames distributed along a path.
This is a useful tool to quickly arrange objects.


Examples
--------


.. figure:: /images/25-Manual-Modeling-Dupliframes-example01.jpg
   :width: 300px
   :figwidth: 300px

   Settings for the curve


:kbd:`Shift-A` to add a :guilabel:`Bezier Circle` and scale it up.  In the :guilabel:`Curve` menu under :guilabel:`Path Animation` enable :guilabel:`Follow` and set :guilabel:`Frames` to something more reasonable than 100 (say 16).


.. figure:: /images/25-Manual-Modeling-Dupliframes-example02.jpg
   :width: 300px
   :figwidth: 300px

   Settings for the object


Add a :guilabel:`Monkey`\ .  In the :guilabel:`Object` menu under :guilabel:`Duplication` enable
:guilabel:`Frames` and disable :guilabel:`Speed`\ .


.. admonition:: Speed
   :class: note

   The :guilabel:`Speed` option is used when the parent-child relationship is set to :guilabel:`Follow Path` (see below).  In this example, the monkey will then travel along the circle over 16 frames.


.. figure:: /images/25-Manual-Modeling-Dupliframes-example03.jpg
   :width: 300px
   :figwidth: 300px

   Parenting


To parent the monkey to the Bezier circle, first select the monkey then the curve
(so that the curve is the active object) and :kbd:`Ctrl-P`\ .
Select the monkey and :kbd:`Alt-O` to reset its origin.


.. figure:: /images/25-Manual-Modeling-Dupliframes-example04.jpg
   :width: 300px
   :figwidth: 300px

   Orientation tweaks


You can now change the orientation of the monkey by either rotating it
(either in :guilabel:`Edit mode` or :guilabel:`Object mode`\ )
or by changing the :guilabel:`Tracking Axes` under :guilabel:`Animation Hacks`
(with the monkey selected).  The arrangement of monkeys can, of course,
be further enhanced by editing the curve.


To transform all monkeys into real objects,
first :kbd:`Ctrl-Shift-A` to :guilabel:`Make Duplicates Real`\ .
All monkeys are now real objects, but still linked copies.  To change this,
:guilabel:`Object`\ →\ :guilabel:`Make Single User`\ →\ :guilabel:`Object&Data` then choose
:guilabel:`All`\ .


.. admonition:: Note
   :class: note

   There are many alternatives to Dupliframes.  Which tool to use depends on context.

   - To use a small curve as a profile and a larger curve as a path, simply use the former as a :guilabel:`Bevel Object` to the latter.
   - To arrange objects along a curve, combining an :guilabel:`Array Modifier` and a :guilabel:`Curve Modifier` is often useful.
   - :guilabel:`Dupliverts` can be used to arrange objects, for example, along a circle or across a subdivided plane.


External links
==============


- `Blender Artists: Dupliframes in 2.5 <http://blenderartists.org/forum/showthread.php?t=181911&page=1>`__


