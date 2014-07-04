
Pose Library
============

Intro
-----

The *Pose Library* panel is used to save, apply, and manage different armature poses.

*Pose Libraries* are saved to *Actions*. They are not generally used as actions, but can be converted to and from.


Pose Library Panel
------------------

.. figure:: /images/Doc_Pose_Library.jpg

   Properties > Armature > Pose Library.


1. Browse *Action / Pose Library* to be linked.

2. Name of the *Pose Library*.

3. Set Fake User.
   This will make blender save the *Pose Library* for if it has no users.

4. Add new *Pose Library* to the active object.

5. Remove the *Pose Library* from the active object.

6. A list of *Poses* for the active *Pose Library*.

7. Add Pose.

   Add New.
      Add a new *Pose* to the active *Pose Library* with the currect pose of the armature.

   Add New (Current Frame).
      *Add New* and *Replace Existing* automatically allocate a *Pose* to an *Action* frame.
      *Add New (Currect Frame)* will add a *Pose* to the *Pose Library* based on the currect frame of the *Time Cursor*.
      Its not a well supported feature.

   Replace Existing.
      Replace an existing *Pose* in the active *Pose Library* with the currect pose of the armature.

8. Remove the active *Pose* from the *Pose Library*.

9. Apply the active *Pose* to the selected *Pose Bones*.

10. Sanitize Action. Make *Action* suitable for use as a *Pose Library*.
   This is used to convert an *Action* to a *Pose Library*.
   A *Pose* is added to the *Pose Library* for each frame with keyframes.


Editing
-------

3D View, Pose Mode.

   Browse Poses. :kbd:`Ctrl-L`.

   Add Pose. :kbd:`Shift-L`.

   Rename Pose. :kbd:`Shift-Ctrl-L`.

   Remove Pose. :kbd:`Alt-L`.


