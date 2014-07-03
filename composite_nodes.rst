

..    TODO/Review: {{review|copy=X}} .


Composite Nodes
===============

Compositing Nodes allow you to assemble and enhance an image (or movie).
Using composition nodes,
you can glue two pieces of footage together and colorize the whole sequence all at once. You
can enhance the colors of a single image or an entire movie clip in a static manner or in a
dynamic way that changes over time (as the clip progresses). In this way,
you use composition nodes to both assemble video clips together, and enhance them.


.. admonition:: Term: Image
   :class: note

   We use the term *Image* to refer to a single picture, a picture in a numbered sequence of images, or a frame of a movie clip. A node layout processes one image at a time, no matter what kind of input you provide.


.. figure:: /images/Manual-Compositing-SimpleNoodle.jpg

   Default Composition Noodle


To process your image, you use nodes to import the image into Blender, change it,
optionally merge it with other images, and finally save it.

The example to the right shows the simplest noodle;
an input node threads the camera view to an output node so it can be saved.


FIXME(Template Unsupported: Doc:2.6/Reference/Nodes/Concepts;
{{Doc:2.6/Reference/Nodes/Concepts}}
)


Accessing and Activating Nodes
------------------------------


Access the :doc:`Node Editor <materials/nodes/editor>` and enable :guilabel:`Composite Nodes` by clicking on the *Image* icon.


.. figure:: /images/Manual-Compositing-Node_Header.jpg

   Node Editor Header with Composite Nodes enabled


.. figure:: /images/Manual-Part-VI-Using_Nodes-WindowsType.jpg

   Select the Node Editor window


To activate nodes for compositing, click the :guilabel:`Use Nodes` checkbox.
Blender creates a default starting noodle, consisting of two nodes threaded together.


.. figure:: /images/Manual-Compositing-Do.jpg

   Use Composition Nodes


To use this mini-map,
you must now tell Blender to use the Compositing Node map that has been created,
and to composite the image using composition nodes. To do so, switch to the :guilabel:`Render`
button area and activate the :guilabel:`Compositing` button located below the
:guilabel:`Post Processing` tab.
This tells Blender to composite the final image by running it through the composition node map.


You now have your first noodle, a RenderLayer input node threaded to a Composite output node. From here, you can add and connect many :doc:`types of compositing nodes <composite_nodes/types>`\ , in a sort of map layout, to your heart's content (or physical memory constraints, whichever comes first).


Examples
--------


You can do just about anything with images using nodes.

Raw footage from a foreground actor in front of a blue screen,
or a rendered object doing something, can be layered on top of a background.
Composite both together, and you have composited footage.

You can change the mood of an image:

- To make an image 'feel' colder, a blue tinge is added.
- To convey a flashback or memory, the image may be softened.
- To convey hatred and frustration, add a red tinge or enhance the red. The film 'Sin City' is the most extreme example of this I have ever seen.
- A startling event may be sharpened and contrast-enhanced.
- A happy feeling - you guessed it - add yellow (equal parts red and green, no blue) for bright and sunny.
- Dust and airborne dirt is often added as a cloud texture over the image to give a little more realism.


