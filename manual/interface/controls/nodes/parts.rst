.. _bpy.types.NodeSocket:
.. _bpy.types.NodeTree:

**********
Node Parts
**********

All nodes in Blender are based on a similar construction.
This applies to :ref:`any type of node <tab-node-tree-types>`.
These parts include the Title, Sockets, Preview and more.

.. figure:: /images/interface_controls_nodes_parts_overview.png


Title
=====

The title shows the name/type of the node;
it can be overridden by changing the node's :ref:`Label <bpy.types.Node.label>`.
On the left side of the title is the *collapse* toggle
which can be used to collapse the node. This can also be done with :kbd:`H`.

.. figure:: /images/interface_controls_nodes_parts_collapsed.png

   How a node appears when collapsed.


.. _bpy.types.NodeLink:

Sockets
=======

.. figure:: /images/interface_controls_nodes_parts_sockets.png
   :align: right

Sockets are input and output values for the node.
They appear as little colored circles on either side of the node.
Unused sockets can be hidden with :kbd:`Ctrl-H`.

Each socket is color-coded depending on what type of data it handles.

Float (gray)
   Indicates that the socket accepts/produces floating-point numbers.
   It can either be a single value or a so-called "value map".
   (You can think of a value map as a grayscale image where the brightness of a pixel represents its value.)
   If a single value is used as an input for a "value map" socket, all points of the map are set to this same value.
Integer (lime green)
   Used to pass an integer value (a number without a fractional component).
Boolean (pink)
   Used to pass a true or false value.
String (light blue)
   Used to pass a text value.
Vector (dark blue)
   Indicates vector, coordinate and normal information.
Color (yellow)
   Indicates that the socket accepts/produces color information.
   The colors may or may not have an alpha component depending on the node tree type.
Shader (bright green)
   Used for shaders in :doc:`Cycles </render/cycles/index>` and :doc:`Eevee </render/eevee/index>`.
Geometry (turquoise)
   Used in :doc:`Geometry Nodes </modeling/geometry_nodes/index>`.
Object (orange)
   Used to pass an object data-block.
Collection (white)
   Used to pass a collection data-block.
Image (apricot)
   Used to pass an image data-block.


Inputs
------

The inputs are located on the bottom left side of the node,
and provide the data the node needs to perform its function.
Each input socket, except for the green shader input, when disconnected,
has a default value which can be edited via a color, numeric, or vector interface input.
In the screenshot of the node above, the second color option is set by a color interface input.

Some nodes have special sockets that can accept multiple inputs.
These sockets will have an ellipsis shape rather than a circle to indicate their special behavior.


Outputs
-------

The outputs are located on the top right side of the node,
and can be connected to the input of nodes further down the node tree.


Conversion
----------

Some socket types can be converted to others either implicitly or explicitly.
Implicit conversion happens automatically without the need of a conversion node.
For example, Float sockets and Color sockets can be linked to each other.

Once a socket conversion is made, data may be lost and cannot be retrieved later down the node tree.
Implicit socket conversion can sometimes change the data units as well.
When plugging a *Value* input node into an angle socket, it'll default to use radians
regardless of the scene's :ref:`bpy.types.UnitSettings`.
This happens because the Value node has no unit while the angle input does.

Valid conversions:

- Between color and vector -- mapping between color channels and vector components.
- Between color and float -- the color data is converted to its grayscale equivalent.
- Color/float/vector to Shader -- implicitly converts to color and gives the result of using an Emission node.

Explicit conversion requires the use of a conversion node such as
the :doc:`/render/shader_nodes/converter/shader_to_rgb` node
or the :doc:`/render/shader_nodes/converter/rgb_to_bw` node.
The :doc:`/render/shader_nodes/converter/math` node also contains
some functions to convert between degrees and radians.


.. _bpy.types.NodeSetting:

Properties
==========

Many nodes have settings which can affect the way they interact with inputs and outputs.
Node settings are located below the outputs and above any inputs.

.. figure:: /images/interface_controls_nodes_parts_controls.png

   An example of the controls on the Chroma Key node.


Preview
-------

Some nodes can show an image that previews their result.
The preview can be toggled using the icon on the very top right-hand corner of the node, next to the title.

.. figure:: /images/interface_controls_nodes_parts_previewless.png

   How a node appears without the preview.
