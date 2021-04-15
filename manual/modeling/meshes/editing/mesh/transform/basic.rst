
*******************
Move, Rotate, Scale
*******************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Move, Rotate, Scale`
   :Menu:      :menuselection:`Mesh --> Transform --> Move, Rotate, Scale`
   :Shortcut:  :kbd:`G`, :kbd:`R`, :kbd:`S`

Once you have a selection of one or more elements, you can move :kbd:`G`,
rotate :kbd:`R` or scale :kbd:`S` them, like many other things in Blender,
as described in the :doc:`Manipulation in 3D Space </scene_layout/object/editing/transform/introduction>` section.
To move, rotate and scale selected components, either use the *Move*, *Rotate*, and *Scale* buttons,
the :doc:`transform gizmos </editors/3dview/display/gizmo>`,
or the shortcuts: :kbd:`G`, :kbd:`R`, and :kbd:`S` respectively.

After moving a selection, the options in the :ref:`ui-undo-redo-adjust-last-operation` panel allow you to
fine-tune your changes, limit the effect to certain axes, turn Proportional Editing on and off, etc.
Of course, when you move an element of a given type (e.g. an edge),
you also modify the implicitly related elements of other kinds (e.g. vertices and faces).

Pressing :kbd:`G` twice enters either *Edge Slide* or *Vertex Slide* tool depending on the selection.
You also have in *Edit Mode* an extra option when using these basic manipulations:
the :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`.


.. _modeling-mesh-transform-panel:

Transform Panel
===============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Panel:     :menuselection:`Sidebar region --> Transform`

When nothing is selected, the panel is empty.
When more than one vertex is selected, the median values is edited
and "Median" is added in front of the labels.

Vertex
   The first controls (X, Y, Z) show the coordinates of the selected vertex or the median point.
Space
   The Space radio buttons let you choose if those coordinates are relative to the object origin (local) or
   the global origin (global).

   Global, Local


Vertex Data
-----------

Bevel Weight
   This vertex property, a value between (0.0 to 1.0),
   is used by the :doc:`Bevel Modifier </modeling/modifiers/generate/bevel>`
   to control the bevel intensity of the vertices,
   when the Only Vertices option is active.


Edge Data
---------

When an edge is selected, the following options are available. More buttons appear:

Bevel Weight
   See :ref:`Edge bevel weight <modeling-edges-bevel-weight>`.
Crease
   The :ref:`crease <modeling-edges-crease-subdivision>` value of the edge.
