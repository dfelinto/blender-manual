.. _bpy.types.PreferencesEdit:

*******
Editing
*******

These preferences control how several tools will interact with your input.

.. figure:: /images/editors_preferences_section_editing.png


Objects
=======

New Objects
-----------

Link Materials to
   To understand this option properly, you need to understand how Blender works with Objects.
   Almost everything in Blender is organized in a hierarchy of data-blocks.
   A data-block can be thought of as containers for certain pieces of information. For example,
   the Object data-block contains information about the Object's location, rotation, and scale
   while the associated linked Object Data data-block contains information about the mesh.

   .. figure:: /images/editors_preferences_editing_data-blocks-hierarchy.png

      Example for a mesh.

   A material may be linked in two different ways:

   Object Data
      Any created material will be created as part of the Object Data data-block.
   Object
      Any created material will be created as part of the Object data-block.

   .. figure:: /images/editors_preferences_editing_data-blocks-link.png

      A material linked to Object Data (left) and Object (right).

   .. seealso::

      :doc:`Read more about Blender's Data System </files/index>`.

Align to
   World
      New objects align with world coordinates.
   View
      New object align with view coordinates.
   3D Cursor
      New objects align to the 3D cursor's orientation.
Enter Edit Mode
   If selected, Edit Mode is automatically activated when you create a new object.
Instance Empty Size
   The display size for empties when
   a new :doc:`collection instance </scene_layout/object/properties/instancing/collection>` is created.


.. _prefs-editing-duplicate-data:

Duplicate Data
--------------

The *Duplicate Data* checkboxes define what data is copied with a duplicated object and
what data remains linked. Any boxes that are checked will have their data copied along with
the duplication of the object. Any boxes that are not checked will instead have their data linked
from the source object that was duplicated.

For example, if you have *Mesh* checked,
then a full copy of the mesh data is created with the new object,
and each mesh will behave independently of the duplicate.
If you leave the mesh box unchecked then when you change the mesh of one object,
the change will be mirrored in the duplicate object.

The same rules apply to each of the checkboxes in the *Duplicate Data* list.


3D Cursor
=========

Cursor Surface Project
   When placing the cursor by clicking,
   the cursor is projected onto the surface under the cursor.
Cursor Lock Adjust
   When the viewport is locked to the cursor,
   moving the cursor avoids the view *jumping* based on the new offset.


Annotations
===========

Default Color
   The default color for new Annotate layers.
Eraser Radius
   The size of the eraser used with the Annotate Tool.

.. seealso::

   :doc:`Read more about Annotations </interface/annotate_tool>`.


.. _prefs-system-weight:

Custom Weight Paint Range
=========================

*Mesh skin weighting* is used to control how much a bone deforms the mesh of a character.
To visualize and paint these weights, Blender uses a color ramp (from blue to green, and from yellow to red).
Enabling the checkbox will enable an alternate map using a ramp starting with an empty range.
Now you can create your custom map using the common color ramp options.
For detailed information see the :doc:`Color ramps </interface/controls/templates/color_ramp>` page.


Grease Pencil
=============

Distance
   Manhattan
      The minimum number of pixels the mouse should have moved either
      horizontally or vertically before the movement is recorded.
      Decreasing this should work better for curvy lines.
   Euclidean
      The minimum distance that mouse has to travel before movement is recorded.

.. seealso::

   :doc:`Read more about Grease Pencil </grease_pencil/index>`.


Text Editor
===========

Auto Close Character Pairs
   Automatically insert the corresponding character to close an expression
   when typing characters such as quotes, brackets, braces, or parentheses.


Miscellaneous
=============

Sculpt Overlay Color
   Defines a color to be used in the inner part of
   the brushes circle when in Sculpt Mode, and it is placed as an overlay to the brush,
   representing the focal point of the brush influence.
   The overlay color is visible only when the overlay visibility is selected
   (clicking at the *eye* to set its visibility), and the transparency of the overlay is
   controlled by the alpha slider located at the :menuselection:`Tool tab --> Display panel` in the Sidebar.
Node Auto-offset Margin
   Margin to use for :ref:`offsetting nodes <editors-nodes-usage-auto-offset>`.
