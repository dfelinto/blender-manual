.. _bpy.types.ID:
.. _bpy.types.BlendData:

***********
Data-Blocks
***********

The base unit for any Blender project is the data-block. Examples of data-blocks include:
meshes, objects, materials, textures, node trees, scenes, texts, brushes, and even Workspaces.

.. figure:: /images/files_data-blocks_outliner-blender-file-view.png
   :align: right

   Blender File view of the Outliner.

A data-block is a generic abstraction of very different kinds of data,
which features a common set of basic features, properties and behaviors.

Some common characteristics:

- They are the primary contents of the blend-file.
- They can reference each other, for reuse and instancing.
  (Child/parent, object/object-data, materials/images, in modifiers or constraints too...)
- Their names are unique within a blend-file, for a given type.
- They can be added/removed/edited/duplicated.
- They can be linked between files (only enabled for a limited set of data-blocks).
- They can have their own animation data.
- They can have `Custom Properties`_.

User will typically interact with the higher level data types (objects, meshes, etc.).
When doing more complex projects, managing data-blocks becomes more important,
especially when inter-linking blend-files.
The main editor for that is the :doc:`Outliner </editors/outliner/index>`.

Not all data in Blender is a data-block,
bones, sequence strips or vertex groups e.g. are not,
they belong to armature, scene and mesh types respectively.


.. _data-system-datablock-types:

Data-Block Types
================

.. EDITORS NOTE:
   Mostly we want to avoid long lists of data -- but in this case,
   it is the only comprehensive list of data-blocks, and something which you cannot
   find directly just through looking at the interface.
   ::
   (TODO add) links to related docs for each type.

.. Image source Scene tab --> Active keying set panel --> ID-block (sound replaced).

.. figure:: /images/files_data-blocks_id-types.png
   :align: right

   Data-blocks types with their icon.

For reference, here is a table of data-blocks types stored in blend-files.

Link
   Library Linking, supports being linked into other blend-files.
Pack
   File Packing, supports file contents being packed into the blend-file
   (**not** applicable for most data-blocks which have no file reference).

.. EDITORS NOTE:
   For each data-block, we have 2 lines.
   1) a terse description.
   2) how its used.
   ::
   Keep these short.

.. container:: lead

   .. clear

.. |tick|  unicode:: U+2713
.. |cross| unicode:: U+2717
.. |none|  unicode:: U+2014

.. list-table::
   :header-rows: 1
   :class: valign
   :widths: 20 5 5 70

   * - Type
     - Link
     - Pack
     - Description
   * - :doc:`Action </animation/actions>`
     - |tick|
     - |none|
     - | Stores animation F-curves.
       | Used as data-block animation data,
       | and the Nonlinear Animation editor.
   * - :doc:`Armature </animation/armatures/introduction>`
     - |tick|
     - |none|
     - | Skeleton used to deform meshes.
       | Used as data of armature objects, and by the Armature Modifier.
   * - :doc:`Brush </sculpt_paint/brush/brush>`
     - |tick|
     - |none|
     - | Used by paint tools.
   * - :doc:`Camera </render/cameras>`
     - |tick|
     - |none|
     - | Used as data by camera objects.
   * - :doc:`Cache File </modeling/modifiers/modify/mesh_sequence_cache>`
     - |tick|
     - |none|
     - | Used by Mesh Cache modifiers.
   * - :doc:`Curve </modeling/curves/introduction>`
     - |tick|
     - |none|
     - | Used as data by curve, font & surface objects.
   * - :doc:`Font </modeling/texts/introduction>`
     - |tick|
     - |tick|
     - | References font files.
       | Used by curve object-data of text objects.
   * - :doc:`Grease Pencil </grease_pencil/introduction>`
     - |tick|
     - |none|
     - | 2D/3D sketch data used by Grease Pencil objects.
       | Used as overlay *helper* info, by the
       | 3D Viewport, Image, Sequencer & Movie Clip editors.
   * - :doc:`Collection </scene_layout/collections/introduction>`
     - |tick|
     - |none|
     - | Group and organize objects in scenes.
       | Used to instance objects, and in library linking.
   * - :doc:`Image </editors/image/introduction>`
     - |tick|
     - |tick|
     - | Image files.
       | Used by shader nodes and textures.
   * - :doc:`Keys (Shape Keys) </animation/shape_keys/introduction>`
     - |cross|
     - |none|
     - | Geometry shape storage, which can be animated.
       | Used by mesh, curve, and lattice objects.
   * - :doc:`Light </render/lights/light_object>`
     - |tick|
     - |none|
     - | Used as object data by light objects.
   * - :doc:`Library </files/linked_libraries/index>`
     - |cross|
     - |tick|
     - | References to an external blend-file.
       | Access from the Outliner's *Blender File* view.
   * - :doc:`Line Style </render/freestyle/introduction>`
     - |tick|
     - |none|
     - | Used by the Freestyle renderer.
   * - :doc:`Lattice </animation/lattice>`
     - |tick|
     - |none|
     - | Grid based lattice deformation.
       | Used as data of lattice objects, and by the Lattice Modifier.
   * - :doc:`Mask </movie_clip/masking/introduction>`
     - |tick|
     - |none|
     - | 2D animated mask curves.
       | Used by compositing nodes & sequencer strip.
   * - :doc:`Material </render/materials/introduction>`
     - |tick|
     - |none|
     - | Set shading and texturing render properties.
       | Used by objects, meshes & curves.
   * - :doc:`Metaball </modeling/metas/introduction>`
     - |tick|
     - |none|
     - | An isosurface in 3D space.
       | Used as data of metaball objects.
   * - :doc:`Mesh </modeling/meshes/introduction>`
     - |tick|
     - |none|
     - | Geometry made of vertices/edges/faces.
       | Used as data of mesh objects.
   * - :doc:`Movie Clip </editors/clip/introduction>`
     - |tick|
     - |cross|
     - | Reference to an image sequence or video file.
       | Used in the *Movie Clip* editor.
   * - :doc:`Node Tree </render/shader_nodes/groups>`
     - |tick|
     - |none|
     - | Groups of re-usable nodes.
       | Used in the node editors.
   * - :doc:`Object </scene_layout/object/introduction>`
     - |tick|
     - |none|
     - | An entity in the scene with location,
       | scale, rotation.
       | Used by scenes & collections.
   * - :doc:`Paint Curve </sculpt_paint/brush/stroke>`
     - |tick|
     - |none|
     - | Stores a paint or sculpt stroke.
       | Access from the paint tools.
   * - :doc:`Palette </sculpt_paint/index>`
     - |tick|
     - |none|
     - | Store color presets.
       | Access from the paint tools.
   * - :doc:`Particle </physics/particles/introduction>`
     - |tick|
     - |none|
     - | Particle settings.
       | Used by particle systems.
   * - :doc:`Light Probe </render/eevee/light_probes/introduction>`
     - |tick|
     - |none|
     - | Help achieve complex real-time lighting in Eevee.
   * - :doc:`Scene </scene_layout/scene/introduction>`
     - |tick|
     - |none|
     - | Primary store of all data displayed and animated.
       | Used as top-level storage for objects & animation.
   * - :doc:`Sounds </render/output/audio/speaker>`
     - |tick|
     - |tick|
     - | Reference to sound files.
       | Used as data of speaker objects.
   * - :doc:`Speaker </render/output/audio/speaker>`
     - |tick|
     - |none|
     - | Sound sources for a 3D scene.
       | Used as data of speaker object.
   * - :doc:`Text </editors/text_editor>`
     - |tick|
     - |cross|
     - | Text data.
       | Used by Python scripts and OSL shaders.
   * - :doc:`Texture </render/materials/legacy_textures/introduction>`
     - |tick|
     - |none|
     - | 2D/3D textures.
       | Used by brushes and modifiers.
   * - :doc:`Window Manager </interface/window_system/introduction>`
     - |cross|
     - |none|
     - | The overarching manager for all of Blender's user interface.
       | Includes Workspaces, notification system, operators, and keymaps.
   * - :doc:`World </render/lights/world>`
     - |tick|
     - |none|
     - | Define global render environment settings.
   * - :doc:`Workspace </interface/window_system/workspaces>`
     - |cross|
     - |none|
     - | UI layout.
       | Used by each window, which has its own workspace.


.. _data-system-datablock-life-time:

Life Time
=========

Every data-block has its usage counted (reference count), when there is more than one,
you can see the number of current users of a data-block to the right of its name in the interface.
Blender follows the general rule that unused data is eventually removed.

Since it is common to add and remove a lot of data while working,
this has the advantage of not having to manually manage every single data-block.
This works by skipping zero user data-blocks when writing blend-files.


.. _data-system-datablock-fake-user:

Protected
---------

Since zero user data-blocks are not saved,
there are times when you want to force the data to be kept irrespective of its users.

If you are building a blend-file to serve as a library of assets that you intend to link to and from other files,
you will need to make sure that they do not accidentally get deleted from the library file.

To protect a data-block, use the button with the shield icon next to its name.
The data-block will then never be silently deleted by Blender,
but you can still manually remove it if needed.


Sharing
=======

Data-blocks can be shared among other data-blocks.

Examples where sharing data is common:

- Sharing textures among materials.
- Sharing meshes between objects (instances).
- Sharing animated actions between objects,
  for example to make all the lights dim together.

You can also share data-blocks between files, see
:doc:`linked libraries </files/linked_libraries/index>`.


.. _data-system-datablock-make-single-user:

Making Single User
==================

When a data-block is shared between several users, you can make a copy of it for a given user.
To do so, click on the user count button to the right of its name.
This will duplicate that data-block and assign the newly created copy to that usage only.

.. note::

   Objects have a set of more advanced actions to become single-user,
   see :ref:`their documentation <bpy.ops.object.make_single_user>`.


Removing Data-Blocks
====================

As covered in `Life Time`_, data-blocks are typically removed when they are no longer used.
They can also be manually *unlinked* or *deleted*.

Unlinking a data-block means that its user won't use it anymore.
This can be achieved by clicking on the "X" icon next to a data-block's name.
If you unlink a data-block from all of its users,
it will eventually be deleted by Blender as described above (unless it is a protected one).

Deleting a data-block directly erases it from the blend-file, automatically unlinking it from all of its users.
This can be achieved by :kbd:`Shift-LMB` on the "X" icon next to its name.

.. warning::

   Deleting some data-blocks can lead to deletion of some of its users, which would become invalid without them.
   The main example is that object-data deletion (like mesh, curve, camera...) will also delete all objects using it.

Those two operations are also available in the context menu
when :kbd:`RMB`-clicking on a data-block in the *Outliner*.


.. _files-data_blocks-custom-properties:
.. _bpy.types.bpy_struct:
.. _bpy.ops.wm.properties:

Custom Properties
=================

.. figure:: /images/files_data-blocks_add.png
   :align: right

   Custom Properties panel.

Custom properties are a way to store your own data in Blender's data-blocks. It can be used for rigging
(where bones and objects can have custom properties driving other properties), and Python scripts,
where it's common to define new settings not available in Blender. It is also possible to access
custom properties from materials via the :doc:`Attribute Node </render/shader_nodes/input/attribute>`.

Only certain data supports custom properties:

- All :ref:`data-blocks types <data-system-datablock-types>`.
- Bones and pose bones.
- Sequence strips.

To add a custom property, search for the *Custom Properties* panel,
found at the bottom of most :doc:`Properties </editors/properties_editor>` or Sidebar region, and click *New*.
Properties can be removed from the same location with the delete icon.
Once properties are added they can be configured via the edit icon to work for a particular use case;
see `Editing Properties`_ for more information.


.. _bpy.ops.wm.properties_edit:

Editing Properties
------------------

User Interface
^^^^^^^^^^^^^^

.. figure:: /images/files_data-blocks_edit.png
   :align: right

   Custom Properties edit pop-up.

Custom properties can be edited using the panel available for data types that support it.
Editing the properties allows you to configure things such as default values,
ranges, and even add a custom tooltip.

.. container:: lead

   .. clear

Type
   The data type of the property; different data types have can only have specific data properties.

   :Float: A numeric value with decimals e.g. 3.141, 5.0, or 6.125.
   :Float Array:
      A collection of multiple float data types e.g. ``[3.141, 5.0, 6.125]`` .
      This data type can also be used for data that can be represented as a float array such as colors.
      These special float arrays can be set in the *Subtype* selector.
   :Integer: A numeric value without any decimals e.g. 1, 2, 3, or 4.
   :Integer Array: A collection of multiple integer data types e.g. ``[1, 2, 3, 4]`` .
   :String: A sequence of characters such as "Some Text".
   :Python: Edit a python data type directly, used for unsupported data types.

   .. note::

      Boolean values must be handled as integers and only work
      when using *Min*/*Max* values that are integers and that are no more than 1 apart.

      At this point, the Boolean values will still look like integers but behave like
      a Boolean having one lower, off, value and a higher, on, value.

Array Length
   The number of elements in the array.
   Note that if the array length is greater than 7 you cannot directly edit its elements,
   you must press *Edit Value* to edit the elements of the array.

Property Name
   The text that is displayed to the left of the value.
   This name is also used to access the property via Python.

Default Value
   This sets the default value of the property used by the *Reset to Default Value* operator.

   .. warning::

      Default values are used as the basis of :ref:`NLA blending <bpy.types.AnimData.action_blend_type>`,
      and a nonsensical default (e.g. 0 for a property used for scaling) on a property intended for
      being keyframed is likely to cause issues.

Min, Max
   The minimum/maximum value the custom property can take.

Is Library Overridable
   Allow the property to be :doc:`overridden </files/linked_libraries/library_overrides>`
   when the data-block is linked.

Use Soft Limits
   Enables limits that the *Property Value* slider can be adjusted to
   without having to input the value numerically.

   Soft Min, Max
      The minimum/maximum value for the soft limit.

Step
   A multiplier to control how much the data type is incremented at a time.
   The internal step size for floats is 0.01, so a *Step* value of 5 will
   increment at a rate of 0.05 and a *Step* value of 100 will increment by 1.0.
   For integers the internal step size is 1.

Precision
   The number of digits after the decimal to display in the user interface for float data types.

Subtype
   Specifies the type of data the property contains, which affects how it appears in the user interface.
   In order for this property to appear the *Property Value* must be a vector of floats.
   For either of the color subtypes to work the *Property Value* must be a vector
   with three or four values depending on the availability of an :term:`Alpha Channel`.

   :Plane Data: Data values do not have any special behavior.
   :Linear Color: Color in linear color space.
   :Gamma-Corrected Color: Color in gamma corrected color space.
   :Euler Angles: :term:`Euler Rotation` angles.
   :Quaternion Angles: :term:`Quaternion Rotation` angles.

Description
   Allows you to write a custom :doc:`Tooltip </getting_started/help>` for your property.


Python Access
^^^^^^^^^^^^^

Custom properties can be accessed in a similar way to
`dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`__,
with the constraints that keys can only be strings,
and values can only be strings, numbers, arrays of such, or nested properties.

See the `API documentation <https://docs.blender.org/api/current/info_quickstart.html#custom-properties>`__
for details.
