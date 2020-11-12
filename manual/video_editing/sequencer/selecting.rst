
*********
Selecting
*********

The active sequence strip is displayed with a light outline.
The *entire* strip could be selected by clicking :kbd:`LMB` in the middle of the strip.


Select Menu
===========

The Select Menu helps you select strips in different ways.

All :kbd:`A`
   Selects all the strips in the timeline.
None :kbd:`Alt-A`
   Deselects all the strips in the timeline.
Invert :kbd:`Ctrl-I`
   Inverts the current selection.
Box Select :kbd:`B`
   Click and drag a rectangular lasso around a region of strips in your Sequence workspace.
   Selects strips all intersecting this rectangle.
Box Select (Include Handles) :kbd:`Ctrl-B`
   Works the same as *Box Select* but it selects only the strip's handles,
   if just one handle is selected moving the strip after selecting will change the strip's length.
   If both handles are selected the strip will move and behave the exact same as *Box Select*.
Side of Frame
   Left/Right :kbd:`[`/:kbd:`]`
      Select strips laying left or right to the current frame.
Handle
   Select left, right or both handles of selected strips.

   .. note::

      Select with this method when you want to change the timing of a cut.

Channel
   Select strips in the same channel laying left or right to active strip.
Linked
   All :kbd:`Ctrl-L` / Less :kbd:`Ctrl-NumpadMinus` / More :kbd:`Ctrl-NumpadPlus`
      Selects strips, that are placed next to each other without any gaps.
Grouped :kbd:`Shift-G`
   Selects strips according to their relation with other strips.

   Type
      Selects any strips of the same type within a category for example,
      if you have a cross strip selected this will select all other effect strips.
   Global Type
      Selects any strips of the same type, e.g. Effect, Image, Movie, etc.
   Effect Type
      Selects all effect strips.
   Data
      Selects strips that share the same data, for example, two image strips sharing the same image file.
   Effect
      Selects the strip that shares an effect strip.
   Effect/Linked
      Selects the effect strips, if any, linked to the currently selected strip.
   Overlap
      Selects any strips that occur on the same frame as the current.
