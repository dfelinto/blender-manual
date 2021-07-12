.. _bpy.ops.anim.keying_set:

***********
Keying Sets
***********

.. figure:: /images/editors_timeline_keying-sets.png
   :align: right

   The Active Keying Sets data ID in the Timeline.

Keying sets are a collection of animated properties that are used to animate
and keyframe multiple properties at the same time.
For example, using keying sets you can press :kbd:`I` in the 3D Viewport,
Blender will add keyframes for all the properties in the active keying set.
There are some built-in keying sets and,
also custom keying sets called *Absolute Keying Sets*.
To select and use a keying set, set the *Active Keying Set*
in the :ref:`Keying popover <timeline-keying>` in the Timeline header,
or the Keying Set panel, or press :kbd:`Shift-Ctrl-Alt-I` in the 3D Viewport.


Keying Set Panel
================

.. reference::

   :Editor:    Properties
   :Panel:     :menuselection:`Scene --> Keying Set`

This panel is used to add, select, manage *Absolute Keying Sets*.

.. figure:: /images/animation_keyframes_keying-sets_scene-keying-set-panel.png

   The Keying Set panel.

Active Keying Set
   The :ref:`List View <ui-list-view>` of keying sets in the active scene.

   Add ``+``
      Adds an empty keying set.

Description
   A short description of the keying set.

Export to File
   Export keying set to a Python script ``File.py``.
   To re-add the keying set from the ``File.py``, open then run the ``File.py`` from the Text Editor.


Keyframing Settings
-------------------

General Override
   These options control all properties in the keying set.
   Note that the same settings in *Preferences* override these settings if enabled.

Active Set Override
   These options control individual properties in the keying set.

Common Settings
   Only Needed
      Only insert keyframes where they are needed in the relevant F-curves.
   Visual Keying
      Insert keyframes based on the visual transformation.
   XYZ to RGB
      For new F-curves, set the colors to RGB for the property set, Location XYZ for example.


Active Keying Set Panel
=======================

.. reference::

   :Editor:    Properties
   :Panel:     :menuselection:`Scene --> Active Keying Set`

This panel is used to add properties to the active keying set.

.. figure:: /images/animation_keyframes_keying-sets_scene-active-keying-set-panel.png

   The Active Keying Set panel.

Paths
   A collection of paths in a :ref:`List View <ui-list-view>` each with a *Data Path* to a property
   to add to the active keying set.

   Add ``+``
      Adds an empty path.

Target ID-Block
   Set the ID Type and the *Object IDs* data path for the property.

Data Path
   Set the rest of the Data Path for the property.

Array All Items
   Use *All Items* from the Data Path or select the array index for a specific property.

F-Curve Grouping
   This controls what group to add the channels to.

   Keying Set Name, None, Named Group


Adding Properties
=================

.. reference::

   :Menu:      :menuselection:`Context menu --> Add All/Single to Keying Set`
   :Shortcut:  :kbd:`K`

Some ways to add properties to keying sets.

:kbd:`RMB` the property in the *User Interface*, then select *Add Single to Keying Set* or *Add All to Keying Set*.
This will add the properties to the active keying set, or to a new keying set if none exist.

Hover the mouse over the properties, then press :kbd:`K`, to add *Add All to Keying Set*.


.. _whole-character-keying-set:

Whole Character Keying Set
==========================

The built-in *Whole Character* keying set is made to keyframe all properties
that are likely to get animated in a character rig. It is also implicitly used by
the :doc:`Pose Library system </animation/armatures/properties/pose_library>`.

In order to determine which bones to add keys for, and which bones to skip,
the keying set uses the bone names. The following bone name prefixes will be skipped:

"COR", "DEF", "GEO", "MCH", "ORG", "VIS"
