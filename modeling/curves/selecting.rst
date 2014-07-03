

..    TODO/Review: {{review|im = add images}} .


Curve Selection
===============

Curve selection in :guilabel:`Edit` mode is much less complex than with meshes! Mainly this is
because you have only one selectable element type, the control points
(no select mode needed here…). These points are a bit more complex than simple vertices,
however, especially for Béziers, as there is the central vertex, and its two handles…

The basic tools are the same as with :doc:`meshes <modeling/meshes/selecting/basics>`\ , so you can select a simple control point with a :kbd:`lmb`\ -click, add to current selection with :kbd:`shift-lmb`\ -clicks, :kbd:`B`\ order-select, and so on.

One word about the Bézier control points: when you select the main central vertex,
the two handles are automatically selected too, so you can grab it as a whole,
without creating an angle in the curve. However, when you select a handle,
only this vertex is selected, allowing you to modify this control vector…

:kbd:`L` (or :kbd:`ctrl-L`\ ) will add to the selection the cursor's nearest control point, and all the linked ones, i.e. all points belonging to the same curve. Note that for Bézier, using :kbd:`L` with a handle selected will select the whole control point and all the linked ones.


Select Menu
-----------

With curves, all "advanced" selection options are regrouped in the :guilabel:`Select` menu of
the 3D views header. Let's detail them.

:guilabel:`Random...`
:guilabel:`Inverse`
:guilabel:`Select/Deselect All`
:guilabel:`Border Select`
   All these options have the same meaning and behavior as in :doc:`Object mode <modeling/objects/selecting>` (and the specifics of :guilabel:`Border Select` in :guilabel:`Edit` mode have already been discussed :doc:`here <modeling/meshes/selecting>`\ ).


Every Nth
---------


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Select --> Every Nth`
   | Hotkey:   None


This only works if you already have at least one control point selected.
Using the current selection, it will add to it every nth control point,
before and after the initial selection. The "selection step" is specified in the :guilabel:`N`
pop-up numeric field shown during the tool start.


Select/Deselect First/Last
--------------------------


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Select --> Select/Deselect First`\ , :menuselection:`Select --> Select/Deselect Last`
   | Hotkey:   None


These commands will toggle the selection of the first or last control point(s) of the curve(s)
in the object. This is useful to quickly find the start of a curve (e.g.
when using it as path…).


Select Next/Previous
--------------------


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Select --> Select Next`\ , :menuselection:`Select --> Select Previous`
   | Hotkey:   None


These commands will select the next or previous control point(s),
based on the current selection (i.e.
the control points following or preceding the selected ones along the curve).


More and Less
-------------


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Select --> More/Less`
   | Hotkey:   :kbd:`ctrl-pad+`\ /\ :kbd:`ctrl-pad-`


These two options are complementary and similar to :doc:`those for meshes <modeling/meshes/selecting/advanced#less_and_more>`\ . Their purpose, based on the currently selected control points, is to reduce or enlarge this selection.

The algorithm is the same as with meshes, but results are more easy to understand:

- :guilabel:`More`\ : for each selected control point, select **all** its linked points (i.e. one or two…).
- :guilabel:`Less`\ : for each selected control point, if **all** points linked to this point are selected, keep this one selected. Otherwise, de-select it.

This implies two points:

- First, when **all** control points of a curve are selected, nothing will happen (as for :guilabel:`Less`\ , all linked points are always selected, and of course, :guilabel:`More` can't add any). Conversely, the same goes when no control points are selected.
- Second, these tools will never "go outside" of a curve (they will never "jump" to another curve in the same object).
