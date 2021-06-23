.. _ui-data-block:

***************
Data-Block Menu
***************

A set of menu buttons used to link :doc:`/files/data_blocks` to
each other. If data-blocks are linked the data will be updated across
all of the :term:`data users <Data User>` when edited.

.. figure:: /images/interface_controls_templates_data-block_menu.png
   :align: right

   A data-block menu with a search field.

Type
   Shows an icon indicating the data-block type. It opens up the following pop-up menu.
   The data-block can be dragged from here e.g. to drag a material onto an object in the 3D Viewport or
   into a :ref:`ui-data-id` field.

   List
      A list of data-blocks available in the current blend-file, or a link to select an item from.
      The menu may show a preview besides the items and
      a search field to search the items in the list by name.
Name
   Displays the internal name of the linked Data-Block, which can be edited as a regular text field.
   If a name is already assigned, Blender will add a digit to the name like ".001".
User Count
   Displays the number of :term:`data users <Data User>` of the data.
   Clicking on user count button will make it a single-user copy,
   with it linked only to the active object/object's data.
Fake User (shield icon)
   Keeps the data-block saved in the blend-file, even if it has no :term:`Real User`.
   When activated an "F" will be shown before the name in the list.
Make Local (chain icon)
   Todo <2.79.
New/Add (files icon)
   Creates a new data-block or duplicates the current data-block and applies it.
Open File (folder icon)
   Opens the :doc:`File Browser </editors/file_browser>`.
Unpack File (bin icon)
   :ref:`Unpack <pack-unpack-data>` the file packed into the current blend-file to external ones.
Unlink Data-block ``X``
   Clears the link. :kbd:`Shift-LMB` to set the users to zero
   allowing the data to be fully deleted from the blend-file.

Sometimes there is a :ref:`list <ui-list-view>` of applied data-blocks
(such as a list of materials used on the object).

.. seealso::

   Data-blocks are discussed further in the :doc:`Data System chapter </files/data_blocks>`.


Preview
=======

.. figure:: /images/interface_controls_templates_data-block_preview.png
   :align: right

   The Data-Block menu with preview.

In the Tool Settings is a version of the data-block menu with a bigger preview.

.. container:: lead

   .. clear


.. rename to selector?

.. _ui-data-id:

Data ID
=======

.. figure:: /images/interface_controls_templates_data-block_data-id.png
   :align: right

   A Data ID field.

A Data ID is a text field with an icon on the left, which opens a pop-up.
Data ID is a unique name for an object. Data ID is used to refer to
objects, and therefore Blender does not allow any two objects of same
type to have same ID (same name). If Data ID is already in use,
Blender will automatically append a number to the end to prevent ID collision
(for example "Cube.001").

Menus showing Data IDs can show the following elements:

Type
   The icon on the left specifies the accepted data-block type.
Name
   The text field functions as a search field by matching elements in the list.
   Press :kbd:`Tab` to auto-complete names up to the level a match is found.
   If more than one match exists, you have to continue typing.
   If you type an invalid name, the value will remain unchanged.
List
   Lets you select the data-block directly.
Eyedropper
   In some Data IDs there is an :ref:`ui-eyedropper`
   available through the pipette icon on the right side.
Remove ``X``
   Click the ``X`` button on the right to remove the reference.


Sub IDs
-------

Related types of IDs may become available to select a property or child object,
depending on the object type.

.. figure:: /images/interface_controls_templates_data-block_subids.png

   Sub ID Example.

Vertex Group
   If the selected object in the *Name* field is a mesh or a lattice,
   an additional field is displayed where a vertex group can be selected.
Bone
   If the selected object in the *Name* field is an armature,
   a new field is displayed offering the choice to specify
   an individual bone by entering its name in the *Bone* data ID.

   Head/Tail
      If a Bone is set, a new field is displayed offering
      the choice of whether the head or tail of a Bone will be pointed at.
      The slider defines where along this bone the point lies interpolating along the bone axis in a straight line.
      A value of zero will point at the Head/Root of a Bone,
      while a value of one will point at the Tail/Tip of a Bone.

      Use B-Bone Shape
         When the bone is a :doc:`bendy bone </animation/armatures/bones/properties/bendy_bones>`,
         click on this button to make the point follow the curvature of the B-spline between head and tail.
