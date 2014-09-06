
..    TODO/Review: {{review
   |text=
   Needs clarification & updates.

   |fixes=[[User:Rking/Doc:2.6/Manual/Animation/Editors/NLA|X]]
   }} .


Non-Linear Animation Editor
***************************

The NLA editor can manipulate and repurpose actions,  without the tedium of keyframe handling.
Its often used to make broad, significant changes to a scene's animation, with relative ease.
It can also repurpose, and 'layer' actions, which make it easier to organize,
and version-control your animation.


Tracks
======

Tracks are the layering system of the NLA.  At its most basic level,
it can help organize strips.  But it also
layers motion much like an image editor layers pixels - the bottom layer first, to the top,
last.


.. figure:: /images/NLA_track.jpg


Strips
======

There's three kinds of strips - Action, Transition, and Meta.
Actions contain the actual keyframe data,
Transitions will perform calculations between Actions,
and Meta will group strips together as a whole.


Creating Action Strips
----------------------

Any action used by the NLA first must be turned into an Action strip.  This is done so by clicking the

.. figure:: /images/NLA_Snowflake.jpg


 next to the action listed in the NLA.  Alternatively, you can go to

.. admonition:: Reference
   :class: refbox

   | Menu:     Add → Action


.. figure:: /images/NLA_Action_Strip.jpg
   :width: 200px
   :figwidth: 200px

   Action Strip.


Creating Transition Strips
--------------------------

Select two or more strips on the same track, and go to

.. admonition:: Reference
   :class: refbox

   | Menu:     Add → Transition


.. figure:: /images/Manual_NLA-Basics_Transition.jpg
   :width: 200px
   :figwidth: 200px

   Transition Strip.


Grouping Strips into Meta Strips
--------------------------------

If you find yourself moving a lot of strips together, you can group them into a Meta strip.
A meta strip can be moved and duplicated like a normal strip.

.. admonition:: Reference
   :class: refbox

   | Menu:     Add → Add Meta-Strips
   | Hotkey:   :kbd:`shift-G`


+------------------------------------------+------------------------------------------+
+.. figure:: /images/NLA_meta_strips_01.jpg|.. figure:: /images/NLA_meta_strips_02.jpg+
+   :width: 200px                          |   :width: 200px                          +
+   :figwidth: 200px                       |   :figwidth: 200px                       +
+                                          |                                          +
+   Shift-select two or more strips..      |   Combine them into a meta strip.        +
+------------------------------------------+------------------------------------------+

A meta strip still contains the underlying strips. You can ungroup a Meta strip.

.. admonition:: Reference
   :class: refbox

   | Menu:     Add → Remove Meta-Strips
   | Hotkey:   :kbd:`alt-G`


Editing Strips
==============

The contents of Action strips can be edited, but you must be in 'Tweak Mode' to do so.


.. admonition:: Reference
   :class: refbox

   | Menu:     View → Enter Tweak Mode
   | Hotkey:   :kbd:`Tab`


+------------------------------------------+------------------------------------------+
+.. figure:: /images/NLA_strip_NLA_Mode.jpg|.. figure:: /images/NLA_strip_EditMode.jpg+
+   :width: 200px                          |   :width: 200px                          +
+   :figwidth: 200px                       |   :figwidth: 200px                       +
+                                          |                                          +
+   Strip in NLA mode..                    |   Strip in Tweak mode.                   +
+------------------------------------------+------------------------------------------+


If you try moving the strip, while in edit mode,
you'll notice that the keys will go along with it.  On occasion,
you'll prefer the keys to remain on their original frames, regardless of where the strip is.
To do so, hit the 'unpin' icon, next to the strip.

.. figure:: /images/nla_pinned_01.jpg
   :width: 350px
   :figwidth: 350px

   Nla strip with pinned keys.


.. figure:: /images/nla_pin_02.jpg
   :width: 350px
   :figwidth: 350px

   Strip moved, notice the keys move with it.


.. figure:: /images/nla_pin_03.jpg
   :width: 350px
   :figwidth: 350px

   The unpinned keys return to their original frames.


When your finished editing the strip, simply go to View > Exit Tweak Mode.
Note the default key for this is Tab.


Re-Instancing Strips
====================

The contents' of one Action strip can be instanced multiple times.  To instance another strip,
select
a strip, go to

.. admonition:: Reference
   :class: refbox

   | Menu:     Edit→ Duplicate Strips


Now, when any strip is tweaked, the others will change too.
If a strip other than the original is tweaked,
the original will turn to red.

+------------------------------------------+--------------------------------------------+---------------------------------------------------+
+.. figure:: /images/NLA_original_strip.jpg|.. figure:: /images/NLA_linked_duplicate.jpg|.. figure:: /images/NLA_linked_duplicate_edited.jpg+
+   :width: 200px                          |   :width: 200px                            |   :width: 200px                                   +
+   :figwidth: 200px                       |   :figwidth: 200px                         |   :figwidth: 200px                                +
+                                          |                                            |                                                   +
+   Original strip.                        |   Duplicated strip.                        |   Duplicated strip being edited.                  +
+------------------------------------------+--------------------------------------------+---------------------------------------------------+


Strip Properties
================

Strip properties can be accessed via the NLA header.

.. admonition:: Reference
   :class: refbox

   | Menu:     View→ Properties


Renaming Strips
---------------

All strips can be renamed, in the "Active Track" section in the Strip Properties.


.. figure:: /images/NLA_StripRename.jpg


Active Track
------------

This is which track the strip currently belongs to.


.. figure:: /images/ActiveTrack.jpg


Active Strip
------------

Elements of the strip itself.  An Action Strip can be either an Action Clip,
or a Transition Clip.  Note that the 'Strip Extents' fields determine strictly the strip,
and not the action.
Also, the "Hold" value in the Extrapolation section means hold both beginning, and after.
This can cause
previous clips to not work, if checked.


.. figure:: /images/ActiveStrip.jpg


Active Action
-------------

This represents the 'object data' of the strip.  Much like the transform values of an object.


.. figure:: /images/ActionClip.jpg


Evaluation
----------

This determines the degree of influence the strip has, and over what time.


.. figure:: /images/Evaluation.jpg


If influence isn't animated, the strips will fade linearly, during the overlap.


.. figure:: /images/NLA_influence_strip.jpg


Strip Modifiers
===============

Like its close cousins in mesh and graph editing,
Modifiers can stack different combinations of effects for strips.
Obviously there will be more to come on this.


.. figure:: /images/Modifiers.jpg

