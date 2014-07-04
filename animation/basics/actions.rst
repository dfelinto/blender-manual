
Actions
=======

Actions
-------

When animating objects and properties in blender, Actions record and contain the data.


.. figure:: /images/K_Animation_Actions_Data3.jpg

   Actions.


So when you animate an object by changing its location with keyframes,
the animation is saved to the Action.

Each property has a channel which it is recorded to, for example,
Cube.location.x is recorded to Channel X Location.


.. figure:: /images/K_Animation_Actions_Keyframes.jpg

   Graph Editor. Each Channel has an F-Curve represented by the lines between the keyframes.


:guilabel:`Actions`
   Record and contain animation data.
:guilabel:`Groups`
   Are groups of channels.
:guilabel:`Channels`
   Record properties.
:guilabel:`F-Curves`
   Are used to interpolate the difference between the keyframes.
:guilabel:`Keyframes`
   Are used to set the values of properties.


F-Curve Interpolation
---------------------

.. figure:: /images/Doc_Animation_Driver_FCurve.jpg

   Graph Editor: Channel F-Curve.


The keyframes are set values by the user.

The *F-Curve* is used to interpolate the difference between the keyframes.

The *F-Curve* has different types of interpolation and also :doc:`F-Curve Modifiers <animation/editors/graph/fmodifiers>`.

Most the settings for the :doc:`F-Curve <animation/editors/graph/fcurves>` are found in the :doc:`Graph Editor <animation/editors/graph>`.


Basic Animation
---------------

These are some common ways to animate objects.
These methods can be used on different objects, like armature bones in pose mode.


Insert Keyframes
~~~~~~~~~~~~~~~~

This example shows you how to animate a cubes location, rotation, and scale.


- First, in the *Timeline*, or other animation editors, set the frame to 1.
- With the *Cube* selected in *Object Mode*, press :kbd:`I` in the 3D View.
- From the *Insert Keyframe Menu* select *LocRotScale*.
-    This will record the location, rotation, and scale, for the *Cube* on frame 1.
- Set the frame to 100.
- Use Grab/Move :kbd:`G`, Rotate :kbd:`R`, Scale :kbd:`S`, to transform the cube.
- Press :kbd:`I` in the 3D View. From the *Insert Keyframe Menu* select *LocRotScale*.


.. figure:: /images/Doc_Actions_Insert_Keyframe_00.jpg
   :width: 500px
   :figwidth: 500px

   Insert Keyframes.


To test the animation, press :kbd:`Alt-A` to play.


.. figure:: /images/Doc_Actions_Insert_Keyframe_01.jpg
   :width: 500px
   :figwidth: 500px

   The animation on frames 1, 50, 100.


Auto Keyframe
~~~~~~~~~~~~~

.. figure:: /images/Doc_kia_Cube03.jpg

   Timeline Auto Keyframe.


Auto Keyframe is the red record button in the *Timeline* header. Auto Keyframe adds
keyframes automatically to the set frame if the value for transform type properties changes.

See :doc:`Timeline V Keyframe Control <animation/editors/timeline#v_keyframe_control>` for more info.


Keying Sets
~~~~~~~~~~~

.. figure:: /images/Doc_kia_Cube02.jpg

   Timeline Keying Sets.


Keying Sets are a set of keyframe channels.
They are used to record multiple properties at the same time.
There are some built in keying sets, 'LocRotScale', and also custom keying sets can be made.

To use the keying set, first select a keying set from the *Timeline* header,
or the *Keying Sets Panel*.

Now when you press :kbd:`I` in the 3D view,
blender will add keyframes for all the properties in the active keying set.

See :doc:`Keying Sets <animation/basics/keying_sets>` for more info.


Properties
~~~~~~~~~~

.. figure:: /images/Doc_kia_Cube04.jpg

   Keyframe properties.


Keyframes can be used to animate lots of different properties in blender.
To add keyframes to a property in the UI, :kbd:`RMB` the property,
then select Insert Single Keyframe, or Insert Keyframes.
Insert Keyframes :kbd:`I` will add a keyframes for the set of properties.


.. figure:: /images/K_Doc_Animation_Properties.jpg

   Properties, Drivers, Keyframes.


Properties have different colors and menu items for different states.

Gray - Property is not animated with Keyframes or Drivers.
   Insert Keyframes :kbd:`I`.
   Insert Single Keyframe.
   Add Drivers.
   Add Single Driver.
   Paste Driver.

Purple - Property value is controlled with a Driver.
   Delete Drivers.
   Delete Single Driver.
   Copy Driver.
   Paste Driver.

Green - Property has Channel with Keyframes.
   Insert Keyframes :kbd:`I`.
   Insert Single Keyframe.
   Clear Keyframes :kbd:`Alt-Shift-I`
   Clear Single Keyframes.

Yellow - Property has Keyframes on the current Frame.
   Replace Keyframes :kbd:`I`.
   Replace Single Keyframe.
   Delete Keyframes :kbd:`Alt-I`.
   Delete Single Keyframe.
   Clear Keyframes :kbd:`Alt-Shift-I`
   Clear Single Keyframes.

Each property also has some Keying Set options.
   Add All to Keying Set :kbd:`K`.
   Add Single to Keying Set.
   Remove from Keying Set.


Editing
~~~~~~~

3D View.
   Insert Keyframes on current frame :kbd:`I`
   Delete Keyframes on current frame :kbd:`Alt-I`


Working with Actions
--------------------

.. figure:: /images/K_Animation_Actions_Create.jpg

   Action Browser.


When you first animate an object by adding keyframes,
blender creates an *Action* to record the data.

*Actions* can be managed with the *Action Browser* in the :doc:`DopeSheet <animation/editors/dopesheet>` *Action Editor* header, or the properties region of the :doc:`NLA Editor <animation/editors/nla>`.

If you are making multiple actions for the same object,
press the **F** button for each action,
this will give the actions a *Fake User* and will make blender save the unlinked actions.

Objects can only use one *Action* at a time for editing, the :doc:`NLA Editor <animation/editors/nla>` is used to blend mutiple actions together.
