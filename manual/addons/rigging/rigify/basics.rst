
***********
Basic Usage
***********

.. _bpy.ops.pose.rigify_generate:

Basic Rig Generation
====================

#. Add a meta-rig structure from the :menuselection:`Add --> Armature` menu.
#. Edit the bone positions to match the character geometry.
#. In the armature properties click on the *Generate* button to generate the rig.


Add a Predefined Meta-Rig
-------------------------

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Add --> Armature`
   :Shortcut:  :kbd:`Shift-A`

Rigify stores all the information required to generate complex rig controls and mechanism in
more simple armatures called "meta-rigs".

The precompiled meta-rigs can be found in the *Add* menu.
Currently available meta-rig types are:

- Basic Human
- Basic Quadruped
- Human
- Cat
- Wolf
- Horse
- Shark


Edit Bone Positions
-------------------

To correctly match your character, meta-rig bones must be moved to correct positions.
This can be achieved in two different ways: Pose Mode or Edit Mode.

.. note::

   Rigify assumes that 1 unit corresponds to 1 meter. So a human is about 2 units tall.
   If your character is in a different scale and you are more familiar with modeling rather than rigging,
   it is suggested to scale it to Rigify dimensions before positioning the meta-rig bones.
   f you want to scale the character's geometry, we suggest you to first scale up the character in Object Mode,
   then apply the geometry scale with the *Apply Scale* tool.


Rigify Human Alignment Tips
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Limbs: Keep the legs as straight as possible in the front view (Rigify human works better in predictable cases).
  Give the knee and the elbow a slight bend angle (Rigify needs to know where your knee/elbow is pointing).
- Torso: Keep the spine as straight as possible in the front view (Rigify human works better in predictable cases).
  The last bone of the spine is the head. By default the next two bones (top to bottom)
  are considered the neck bones. It is suggested to keep the neck bones as aligned as possible while editing.
- Face: Positioning face bones can be tricky if you are not an expert in bone editing and
  they are almost useless if you plan to make facial animation through shape keys.
  Consider removing face features from your character if they aren't really needed.
  If you don't need the face all the face bones can be deleted.
  All the face bones are on the first armature layer by default.
  You can select them by displaying only bone layer 1, selecting all of its content and
  then deleting the bones in Edit Mode to correctly remove the face.

  If you want to scale all the face bones at once, consider scaling the face master bone
  in Pose Mode (see Pose Mode matching method).
  The face master bone is placed in the same position of the head bone.
  To select it easily, hide all other bone layers.

  For more tips, see the :doc:`Positioning Guide </addons/rigging/rigify/bone_positioning>`.


Pose Mode Matching (Basic)
--------------------------

Enter the meta-rig Pose Mode. Rotate, scale, and translate the bones in the correct position.
When bones are in correct positions (always staying in Pose Mode)
use :menuselection:`Apply --> Apply Pose As Rest Pose`.

.. note::

   Connected bones cannot be translated in Pose Mode.
   You can scale the parent bones to match the general length and then refine child bones scale.
   For more detailed information on armature modes please refer to
   the :doc:`armatures section </animation/armatures/bones/editing/introduction>`.


Edit Mode Matching (Advanced)
-----------------------------

Some basic armature display setup is suggested before entering bone Edit Mode.

With the meta-rig selected, go in the Properties and click on the Object tab.
Scroll down to the display panel and enable X-ray and under *Maximum Draw Type* selector select *Wire*.
This way the bones will always be drawn in wireframe on top of your geometry.

Then, always in the Properties click on the Armatures tab and under display check the *Axis* checkbox.
This way you the bones rotation axes will be displayed during the edit process.

For more detailed information on armature display modes please refer to
the :doc:`Display panel page </animation/armatures/properties/display>`.


Generating the Rig
------------------

With the bones in the correct positions, jump back in Object Mode, go to the Armature tab,
scroll down to the bottom and click on the *Generate* button to finalize the rig creation.
The generation process will take from few seconds to one minute depending on
rig complexity and hardware specifications of your machine.
If the generated rig needs tweaking, you can modify the meta-rig accordingly and
then click again on the generate button. If the rig already exists,
Rigify will simply overwrite it retaining all your modifiers and constraints and -- where possible --
all the previously generated features.

If you need to generate more than one rig in the scene or update a specific one
(when there are more than one in the same file), follow the instructions in the `Advanced Rig Generation`_ section.

.. tip:: Rig Updating

   To make the rig overwriting work as expected, you need to have **both** the rig and
   the meta-rig visible before generating again.

.. warning::

   As with all Python add-ons, Blender interface cannot be updated until the Python script execution is over.
   Wait until the rig appears to see the results.


Binding the Geometry to the Rig
-------------------------------

To bind the geometry to the rig you can use your preferred tools. Just few things you have to know:

- All the deforming bones are on the armature layer 30.
- Eyes and Teeth bones are not deforming. You are supposed to bind the eyes and teeth geometry
  through Child Of constraints.
- Usually armature deform with automatic weights do a really good job out of the box
  if you correctly place your bones (and there is enough topology to work with!).

For more detailed information on armature layers, Armature modifier and weight painting refer to the Blender manual.


.. _bpy.types.Armature.rigify:

Advanced Rig Generation
=======================

Advanced Options Features
-------------------------

When Advanced Options are enabled, user will be able to:

- Generate more than one rig per scene.
- Generate a rig with a specific name.
- Update/Overwrite a specific rig.


Advanced Options Activation
---------------------------

Advanced Rig Generation Options are locked by default. Click on the *Advanced Options* button to enable.
With Advanced Options enabled the panel will be updated displaying two main modes:

- Overwrite
- New

By default overwrite is selected. At this stage if you don't touch anything in the UI the generate function
will be invoked as is, meaning in fact that generating the rig now will create a new rig from the meta-rig
if none is present in the scene, or overwrite the default one if you have already generated a rig from a meta-rig.
For further information about the Rigify generate function look at basic usage section.


New Rig Mode
^^^^^^^^^^^^

The *New* rig mode will let the user generate a new rig from the meta-rig regardless of
an already generated rig is present in the scene.
A specific name for the rig can be set by the user through the specific *Rig Name* text field.
If no name is set, Rigify will generate an armature object named "rig" and a Python script named ``rig_ui.py``.

.. note::

   Keep in mind that along with the rig, Rigify generates also a ``rig_ui`` Python script
   which controls the UI in the 3D Viewport. This Python script will be named accordingly with
   the specified rig name.


Overwrite Rig Mode
^^^^^^^^^^^^^^^^^^

The *Overwrite* rig mode will let the user specify a target rig to be overwritten.
If none is set Rigify will search and eventually overwrite an armature object named "rig" and
a Python script named ``rig_ui.py``.


Library Linking
===============

When linking a rig into another file, you generally want to create a collection that includes
the generated rig and the character mesh, with another nested and hidden collection for the "WGT-" objects.
You do not need to include the meta-rig. You then link in the collection, and either run *Make Proxy*
and select the rig object, or run *Make Library Override*.

The ``rig_ui.py`` text data-block responsible for the rig UI will be automatically linked along with
the rig, you don't need to link it separately. However, the script will not run until you run it
manually from the Text editor or save and restart Blender.
