

..    TODO/Review: {{review
   |text=
   wrong version
   : Data Select Browser not applicable/available in 2.5
   Overview
   : http://wiki.blender.org/index.php/Doc:2.5/Manual/Data_System/Data_System#Overview
   }} .


Overview
========

Each .blend file contains a database. This database contains all scenes, objects, meshes,
textures, etc. that are in the file.
A file can contain multiple scenes and each scene can contain multiple objects.
Objects can contain multiple materials which can contain many textures.
It is also possible to create links between different objects.


 .. admonition:: Reference
   :class: refbox

   | Mode:     All Modes, Any Window
   | Hotkey:   :kbd:`shift-F4` - Data Select Browser


To access the database, press :kbd:`shift-F4` and the window will change to a
:guilabel:`Data Select Browser` window, which lists the Objects in your .blend file.
To go up a level, click the breadcrumbs (\ ``..``\ )
and then you will see the overall structure of a file: :guilabel:`Action`\ ,
:guilabel:`Armature`\ , :guilabel:`Brush`\ , :guilabel:`Camera`\ , :guilabel:`Curve`\ ,
:guilabel:`Group`\ , and so on (including :guilabel:`Object`\ s).

:kbd:`lmb` selecting any datablock type, :guilabel:`Mesh`\ , for example, will give you a listing of the meshes used in the file, along with how many users there are for each one. For example, if you had a car mesh, and used that car mesh for six cars in a parking lot scene, the :guilabel:`Mesh` listing would show the Car and then the number 6.


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Data Select Browser`
   | Hotkey:   :kbd:`F` - Fake User


:kbd:`rmb` selecting certain kinds of datablocks (\ :guilabel:`Material`\ s, :guilabel:`Image`\ s, :guilabel:`Texture`\ s…) and pressing :kbd:`F` will assign a "fake user" to those datablocks. With a fake user in place, Blender will keep those datablocks in the file, even if they have no "real user". Datablocks without a user, real or fake, are not saved in the .blend file. Pressing :kbd:`F` again toggles the fake user assignment. Performing this action is the same as clicking the :guilabel:`F` button next to material/image/… names.


Outliner and OOPS Schematic
===========================

You can easily inspect the contents of your file by using the :guilabel:`Outliner` window. This window displays the Blender data system (\ :doc:`fully documented here <data_system/the_outliner>`\ ). This window offers two views of the database. The :guilabel:`Outliner` view allows you to do simple operations on the objects. These operations include selecting, renaming, deleting and linking. The :guilabel:`OOPS Schematic` (Object-Oriented Programming System) view allows you to easily see how datablocks are linked. You can filter the view by using buttons found in the header.


Users (Sharing)
===============

Many datablocks can be shared among other datablocks - re-use is encouraged. For example,
suppose you have a material for one object, named "\ ``Glossy``\ ".
You can select a second object, for example, one that does not have a material yet.
Instead of clicking :guilabel:`ADD NEW` for the material,
click the little up-down arrow next to the :guilabel:`ADD NEW`\ ,
which brings up a list of existing materials. Select "\ ``Glossy``\ ". Now,
these two objects share the same material.
You will notice a "2" next to the name of the material, indicating that there are two users
(the two objects) for this material. Other common examples include:

- Sharing textures among materials.
- Sharing meshes between objects ("clones").
- Sharing Ipo curves between objects, for example to make all the lights dim together.


Fake User
---------

Remember that Blender does not save datablocks that are not linked to anything in the
*current* file.  If you're building a ".blend" file to serve as a library of things that you
intend to link-to from *other* files,
you'll need to make sure that they don't accidentally get deleted from the current
(the library) file.  Do this by giving the datablocks a "fake user,
" by hitting the :guilabel:`F` button next to the name of the datablock.
This prevents the user count from ever becoming zero:  therefore,
the datablock will not be deleted.
(Blender does not keep track of how many other files link to this one.)


Copying and Linking Objects Between Scenes
==========================================

Sometimes you may want to link or copy objects between scenes. This is possible by first selecting objects you want to link or copy and then using the :guilabel:`Make Links` and :guilabel:`Make Single User` items found in :guilabel:`Object` menu in the 3D viewport header. Use :guilabel:`Make Links` to make links between scenes. To make a plain copy, you first make a link and then use :guilabel:`Make Single User` to make a stand-alone copy of the object in your current scene. Further information on working with scenes can be found :doc:`here <data_system/scene_creation>`\ .


Appending or Linking Across Files
=================================

The content of one .blend file is easily accessed and put into your current file by using the :guilabel:`File` → :guilabel:`Append` function (accessed at any time by :kbd:`shift-F1`\ ). To find out more about how to copy or link objects across .blend files, :doc:`click here <data_system/linked_libraries>`\ .


Proxy Objects
-------------

:doc:`Proxy objects <data_system/linked_libraries>` allow you to make (parts of) linked data local. For example, this allows an animator to make a local "copy" of the handler bones of a character, without having the actual rig duplicated. This is especially useful for character animation setups, where you want the entire character to be loaded from an external library, but still permit the animator to work with poses and actions. Another example: you can have a modeler working on the shape (mesh) of a car and another painter working on the materials for that car. The painter cannot alter the shape of the car, but can start working with color schemes for the car. Updates made to the shape of the car are applied automatically to the painter's proxy.


Pack and Unpack Data
====================

Blender has the ability to encapsulate (incorporate)
various kinds of data within the .blend file that is normally saved outside of the .
blend file. For example, an image texture that is an external ``.jpg`` file can be
put "inside" the .blend file via :guilabel:`File` → :guilabel:`External Data` →
:guilabel:`Pack into .blend file`\ . When the .blend file is saved,
a copy of that ``.jpg`` file is put inside the .blend file.
The .blend file can then be copied or emailed anywhere, and the image texture moves with it.

You know that an image texture is packed because you will see a little "Christmas present gift
box" displayed in the header.


Unpack Data
-----------

When you have received a packed file,
you can :guilabel:`File` → :guilabel:`External Data` → :guilabel:`Unpack into Files...`
. You will be presented with the option to create the original directory structure or put
the file in the ``//`` (directory where the .blend file is). Use "original locations"
if you will be modifying the textures and re-packing and exchanging .blend files,
so that when you send it back and the originator unpacks,
his copies of the textures will be updated.


