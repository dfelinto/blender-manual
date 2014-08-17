
Scenes
******

Scenes are a very useful tool for managing your projects. The Cube model in empty space you
see when you open Blender for the first time is the default Scene.
You can imagine Scenes to be similar to tabs in your web browser. For example,
your web browser can have many tabs open at once. The tabs could be empty,
showing identical views of the same web page,
showing different views of the same page or show entirely different pages altogether.
Blender's Scenes work in much the same way. You can have an empty Scene, a complete
independent copy of your Scene or a new copy that links to your original Scene in a number of
ways.

You can select and create scenes with the :guilabel:`Scene selector` in the Info window header
(the bar at the top of most Blender layouts, see *Screen and Scene selectors*).


.. figure:: /images/Manual-Part-I-ConceptScreens25.jpg

   Screen and Scene selectors


Scene configuration
*******************

Adding a new Scene
==================

.. figure:: /images/Manual-Part-I-Interface-Scene-AddButton-Dialog25.jpg

   Add Scene menu


You can add a new scene by clicking

.. figure:: /images/Manual-Part-I-Interface-Screens-AddView-Button25.jpg


 in the Scene selector option. When you create a new scene, you can choose between five options to control its contents (*Add Scene menu*).

To choose between these options,
you need to clearly understand the difference between "Objects" and "Object Data".
Each Blender graphic element (Mesh, Lamp, Curve, *etc.*) is composed from two parts:
an Object and Object Data (also known as ObData).
The Object holds information about the position, rotation and size of a particular element.
The ObData holds information about meshes, material lists and so on.
ObData is common to every instance of that particular type of element.
Each Object has a link to its associated ObData,
and a single ObData may be shared by many Objects.

The five choices, therefore, determine just how much of this information will be *copied
from* the currently selected Scene to the new one, and how much will be *shared*
("linked"):

:guilabel:`New`
   Creates an empty Scene. In the new Scene, the Render Settings are set to the default values.

:guilabel:`Copy Settings`
   Creates an empty Scene like the previous option but also copies the Render Settings from the original Scene into the new one.

:guilabel:`Link Objects`
   Is the shallowest form of copying available.
   This option creates the new Scene with the same contents as the currently selected Scene.
   However, instead of copying the Objects,
   the new Scene contains *links to* the Objects in the old Scene at the Object level. Therefore, changes in the
   *new* Scene will result in the same changes to the *original* Scene because the Objects used are *literally* the
   same Objects. The reverse is also true
   (changes in the *old* Scene will cause the same changes in the *new* Scene).

:guilabel:`Link Object Data`
   Creates new, duplicate copies of all of the Objects in the currently selected Scene,
   but each one of those duplicate Objects will have *links to* the ObData (meshes, materials and so on)
   of the corresponding Objects in the original Scene. This means that you can change the position,
   orientation and size of the Objects in the new Scene without affecting other Scenes,
   but any modifications to the ObData (meshes, materials *etc*) will also affect other Scenes. This is because a
   *single instance of* the "ObData" is now being shared by all of the Objects in all of the Scenes that link to it.
   If you want to make changes to an Object in the new Scene independently of the Objects in the other Scenes, you
   will have to manually make the object in the new Scene a "single-user" copy by :kbd:`LMB` the number in the
   :guilabel:`Object Data` panel of the Properties Window.
   More information at the :doc:`Window Type <interface/window_types>` page.
   This has the effect of making a new independent copy of the ObData.


.. figure:: /images/Manual-Interface-Scenes-mk_singleuser.jpg


:guilabel:`Full Copy`
   Is the deepest form of copying available.  Nothing is shared.  This option creates a fully independent Scene with copies of the currently selected Scene's contents.  Every Object in the original Scene is duplicated, and a duplicate, private copy of its ObData is made as well.

To better understand the way Blender works with data, read through :doc:`Blender's Library and Data System. <data_system>`


A brief example
===============

Consider a bar Scene in a film. You initially create the bar as a clean version,
with everything unbroken and in its proper place.
You then decide to create the action in a separate Scene.
The action in your Scene will indicate which type of linking (if any)
would suit your Scene best.

:guilabel:`Link Objects`
   Every object will be linked to the original Scene. If you correct the placement of a wall, it will move in every Scene that uses the bar as a setting.

:guilabel:`Link Object Data`
   Will be useful when the positions of Objects need to change, but their shape and material settings will remain constant. For example, chairs might stand on the floor in the "crowded bar" scene and up on the tables in the "we are closing" scene. Since the chairs don't change form, there is no need to waste memory on exact mesh-copies.

:guilabel:`Full Copy`
   A glass shattering on the floor will need its own copy because the mesh will change shape.

It is not possible to do all of the above in the same Scene,
but it might help in understanding why to link different Objects in different ways.


Deleting a Scene
================

You can delete a scene by using the :guilabel:`Delete datablock` button (

.. figure:: /images/Manual-Part-I-Interface-Screens-DeleteView-Button25.jpg


) from the Scene selector option (see *Screen and Scene selectors*).

