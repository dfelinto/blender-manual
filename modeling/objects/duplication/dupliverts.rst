


DupliVerts
==========


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Panel:    :guilabel:`Object` → :guilabel:`Duplication`


:guilabel:`Duplication Vertices` or :guilabel:`DupliVerts` is the duplication of a base object at the location of the vertices of a mesh. In other words, when using :guilabel:`DupliVerts` on a mesh, an instance of the base object is placed on every vertex of the mesh.

There are actually two approaches to modeling using :guilabel:`DupliVerts`\ .
They can be used as an arranging tool,
allowing us to model geometrical arrangements of objects (e.g. the columns of a Greek temple,
the trees in a garden, an army of robot soldiers, the desks in a classroom).
The object can be of any object type which Blender supports.
The second approach is to use them to model an object starting from a single part of it (e.g.
the spikes in a club, the thorns of a sea-urchin, the tiles in a wall,
the petals in a flower).


 .. admonition:: Download example .blend file
   :class: note

   You can download a file with the examples described on this page.  In `this .blend <http://wiki.blender.org/index.php/:File:Manual-2.5-DupliVerts-Examples.blend>`__\ , the first example, a monkey parented to a circle is on layer 1; while a tentacle parented to an icosphere is on layer 2.  The files was made using Blender 2.55.1 (r33567).


DupliVerts as an Arranging Tool
-------------------------------


Setup
~~~~~


.. figure:: /images/Manual-2.5-Dupliverts-Example01-1start.jpg

   A monkey head and a circle


All you need is a base object (e.g. the *tree* or the *column*\ )
and a pattern mesh with its vertices following the pattern you have in mind.  In this section,
we will use a simple scene for the following part.  We'll be using a monkey head located at
the origin of the coordinate system as our base object and a circle at the same location as
our parent mesh.


.. figure:: /images/Manual-2.5-Dupliverts-Example01-2dupliverted.jpg

   Dupliverted monkeys


First, in :guilabel:`Object mode`\ ,
select the base object and :kbd:`Shift-RMB` to add the circle to the selection
(order is very important here),
and  :kbd:`Ctrl-P` to parent the base object to the circle.  Now,
the circle is the parent of the monkey; if you move the circle, the monkey will follow it.


With only the circle selected, enable :guilabel:`Duplication vertices` in the
:guilabel:`Object` panel→ :guilabel:`Duplication`\ → :guilabel:`Verts`\ .
A monkey head should be placed at every vertex of the circle.

The original monkey head at the center and the parent mesh are still shown in the 3D view but
neither will be rendered.  If the placement and rotation of your monkey head is odd,
you might need to clear its rotation (\ :kbd:`Alt-R`\ ), scale :kbd:`Alt-S`\ ,
location :kbd:`Alt-G`\ , and origin :kbd:`Alt-O`\ .


Rearranging
~~~~~~~~~~~

If you now select the base object and modify it in either object or edit mode,
all changes will also affect the shape of all duplicate objects.
You can also select the parent mesh to modify the arrangement of the duplicates;
adding vertices will also add more base objects.
Note that the base objects will inherit changes made to the parent mesh in object mode, but
not in edit mode — so scaling the circle up in object mode will enlarge the monkey head,
while scaling the circle up in edit mode will only increase the distance between the base
objects.


Orientation
~~~~~~~~~~~


.. figure:: /images/Manual-2.5-Dupliverts-Example01-3Orientation.jpg

   Orientation enabled, orientation +Y


The orientation of the base objects can be controlled by enabling :guilabel:`Rotation` in the
:guilabel:`Duplication` panel.
This will rotate all base objects according to the vertex normals of the parent mesh.


To change the orientation of the duplicated objects, select the base object and in the
:guilabel:`Object`\ → :guilabel:`Relations extras` panel change the :guilabel:`Tracking Axes`\ .

Output of various orientations:


.. figure:: /images/Manual-2.5-Dupliverts-Example01-4negY.jpg

   Negative Y


.. figure:: /images/Manual-2.5-Dupliverts-Example01-5posX.jpg

   Positive X


.. figure:: /images/Manual-2.5-Dupliverts-Example01-6posZ.jpg

   Positive Z, up X


 .. admonition:: Note
   :class: note

   The axes of an object can be made visible in the :guilabel:`Object`\ → :guilabel:`Display` panel.
   To display the vertex normals of the parent mesh, tab into edit mode and enable this function in :guilabel:`Properties` (\ :kbd:`N`\ )→ :guilabel:`Display` panel where you can also resize the displayed normals as necessary.


DupliVerts as a Modeling Tool
-----------------------------

Very interesting models can be made using DupliVerts and a standard primitive.
In this example, a simple tentacle was made by extruding a cube a couple of times.
The tentacle object was then parented to an icosphere.
With dupli :guilabel:`Rotation` enabled for the parent mesh (the icosphere),
the orientation of the base object (the tentacle)
was adapted to the vertex normals of the parent mesh

(in this case the tentacle was rotated -90- about the X axis in edit mode).


.. figure:: /images/Manual-2.5-Dupliverts-Example02-1Tentacle.jpg

   A simple tentacle set to smooth


.. figure:: /images/Manual-2.5-Dupliverts-Example02-2NoRot.jpg

   Tentacle dupliverted onto the parent mesh


.. figure:: /images/Manual-2.5-Dupliverts-Example02-3Rot.jpg

   Rotation enabled to align duplicates


As in the previous example, the shape and proportions of the arrangement can now be tweaked.

To turn all duplicates into real objects, simply select the icosphere and :guilabel:`Object`\ →
:guilabel:`Apply`\ → :guilabel:`Make Duplicates Real` (\ :kbd:`Ctrl-Shift-A`\ ).
To make the icosphere and the tentacle a single object,
make sure they are all selected and go to :guilabel:`Object`\ → :guilabel:`Join`
(\ :kbd:`Ctrl-J`\ ).


See also
--------

Other duplication methods are listed :doc:`here <modeling/objects/duplication>`\ .


