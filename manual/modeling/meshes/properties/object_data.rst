
***********
Object Data
***********

Meshes
   The mesh :ref:`Data-Block Menu <ui-data-block>` can be used to link the data between objects.


Vertex Groups
=============

Vertex groups can be used to assign a group or weighted group to some operator.
An object can have several weight groups and can be assigned in
:doc:`Weight Paint </modeling/meshes/properties/vertex_groups/vertex_groups>` mode,
or in :doc:`Edit Mode </modeling/meshes/properties/vertex_groups/assigning_vertex_group>` via this panel.

See :doc:`Vertex Groups </modeling/meshes/properties/vertex_groups/index>` for more information.


Shape Keys
==========

Shape Keys can be used to transform one shape into another.
See :doc:`/animation/shape_keys/shape_keys_panel` for more information.


UV Maps
=======

UV Maps are used to map a 3D object onto a 2D plane that determines where a texture appears on the 3D object.
Different UV Maps can be used for different textures. For more information see :ref:`uv-maps-panel`.


.. _bpy.ops.geometry.color_attribute_remove:
.. _bpy.ops.geometry.color_attribute_render_set:
.. _modeling-meshes-properties-object_data-color-attributes:

Color Attributes
================

Color data can be applied directly to an object's vertices rather than using a texture or a material.
There are two modes to paint color attributes in.
Use :doc:`Vertex Paint </sculpt_paint/vertex_paint/index>` mode to paint per face corner
by enabling the paint mask in the header.
This is useful to achieve sharp edges in the color attribute on low-poly assets.
Alternatively use Sculpt mode to paint on a much higher vertex count.


.. _bpy.ops.geometry.color_attribute_add:

Creating a New Color Attribute
------------------------------

To create a new Color Attribute select the plus icon next to the list of attributes.
This action will open a pop-up with the following information.

Name
   The name of the Color Attribute which can be referenced elsewhere in Blender.
Domain
   The associated part of the geometry that stores the attribute.
   See :ref:`attribute-domains` for more information.

   :Vertex: Color Attributes are stored per each vertex.
   :Face Corner: Color Attributes are stored per each corner of a face.
Data Type
   The data type to represent colors internally.

   :Color: RGBA color with floating-point precision.
   :Byte Color: RGBA color with 8-bit precision.
Color
   The default color to fill for every element in the domain.


.. _bpy.types.FaceMaps:
.. _bpy.ops.object.face_map:

Face Maps
=========

Face Maps create custom gizmos to deform meshes by assigning faces to *Face Maps*.
They can be used to rig quickly within Object Mode and without making complicated rigging setups.
Face Maps are currently not fully implemented in Blender and require add-ons to take full advantage of this feature.

.. seealso::

   `Auto Face Map Widgets add-on <https://developer.blender.org/diffusion/BAC/browse/master/object_facemap_auto/>`__


Attributes
==========

An attribute is data stored per mesh element. Every attribute has a data type, domain and name.
This panel only lists custom attributes which excludes all the built-in attributes like ``position`` and
other attributes like vertex groups.

See :doc:`Attributes Reference </modeling/geometry_nodes/attributes_reference>` for more information.


Normals
=======

In geometry, a normal is a direction or line that is perpendicular to something,
typically a triangle or surface but can also be relative to a line, a tangent line for a point on a curve,
or a tangent plane for a point on a surface. Normals help to determine the shading of the mesh among other things.

See :ref:`Normal Properties <modeling_meshes_editing_normals_properties>` for more information.


Texture Space
=============

Each object can have an automatically generated UV map, these maps can be adjusted here.

See :ref:`Generated UV Properties <properties-texture-space>` for more information.


Remesh
======

Mesh objects, in particular meshes that have been modeled to represent organic objects,
often have geometry that is not particularly uniform.
This can cause problems if the object needs to be :ref:`rigged <animation-rigging>`
or just needs simpler geometry for workflows such as 3D printing.
Remeshing is a technique that rebuilds the geometry with a more uniform topology.
Remeshing can either add or remove the amount of topology depending on the defined resolution.
Remeshing is especially useful for :doc:`sculpting </sculpt_paint/sculpting/index>`,
to generate better topology after blocking out the initial shape.

See :doc:`Mesh Retopology </modeling/meshes/retopology>` for more information.


Geometry Data
=============

Mesh objects can have different types of custom data attached to them.
This data is mostly used internally and can be exported by some :doc:`exporters </files/import_export>`.
See :doc:`/modeling/meshes/properties/custom_data` for more information.
