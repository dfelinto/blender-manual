
Texture Nodes
*************

As an alternative to using the :doc:`Texture Stack <textures/options>`, Blender includes a node-based texture generation system which enables you to create textures by combining colors, patterns and other textures in much the same way that you combine :doc:`Material Nodes <materials/nodes>`.

You can use these textures wherever you can use regular textures:
you can place them in texture channels, in material nodes, in particle systems,
and even inside other textures.


FIXME(Template Unsupported: Doc:2.6/Reference/Nodes/Concepts;
{{Doc:2.6/Reference/Nodes/Concepts}}
)


.. admonition:: Note
   :class: note

   Node-based textures do **not** work for realtime display, they will only be visible in rendered images.


Using Texture Nodes
===================

To use texture nodes with the current texture, open a :doc:`Node Editor window <textures/types/nodes/editor>`, set it to :guilabel:`Texture` mode by clicking the "Texture" icon (

.. figure:: /images/26-Manual-Selector-Node-Btn-Texture.jpg

   Texture

) in its header.

To start adding nodes, you first need to select a material.
Now you can either click the :guilabel:`New` button in the Node editor,
or the :guilabel:`New` button in the texture panel. Once you have a texture selected, you can
toggle it to function as a regular texture or a node texture by clicking the :guilabel:`Use
Nodes` option in the Node Editor.

The default node setup will appear: a red-and-white checkerboard node connected to an
:guilabel:`Output` named "\ ``Default`` ". For *texture* nodes,
you can create as many Outputs as you like in your node setup.  (Other types of node networks,
as you may recall, are limited to only one Output node.) See the next section for details.

For instructions on how to add, remove and manipulate the nodes in the tree, see the :doc:`Node Editor manual <materials/nodes/editor>`.


Using Multiple Outputs
======================

Each texture that you define with Texture Nodes can have several outputs,
which you can then use for different things. For example,
you might want your texture to define both a diffuse (color) map and a normal map. To do this,
you would:

- Create two texture slots in the texture list, and set them to the same texture datablock.
- Add two :guilabel:`Output` nodes to the node tree, and type new names into their :guilabel:`Name` text-boxes: *e.g.* "\ ``Diffuse`` " for one and "\ ``Normal`` " for the other.
- Underneath the texture picker in the texture panel, you'll see a dropdown list with the names of your outputs. For each entry in the texture list, select the desired output by changing the menu entry (e.g. set on to "\ ``Diffuse`` " and the other to "\ ``Normal`` ").

You can also use these named outputs if you've decided to define your material using Material
Nodes.  In this case, you probably won't be using Texture Channels.  Instead, you'll insert
:guilabel:`Texture` nodes into your Material Node tree using :guilabel:`Add` →
:guilabel:`Input` → :guilabel:`Texture`. Then,
inside the texture node that you've just added, you can select which output you want to use
*(e.g.* ``Diffuse`` or ``Normal``).


See also
========

-

FIXME(Link Type Unsupported: dev;
[[Dev:2.4/Source/Textures/Nodes - Blender 2.49|Development page]]
)


