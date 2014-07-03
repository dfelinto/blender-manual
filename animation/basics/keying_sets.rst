


Keying Sets
===========


.. figure:: /images/Doc_kia_Cube02.jpg

   Timeline Keying Sets.


Keying Sets are a collection of properties.
They are used to keyframe multiple properties at the same time,
usually by pressing :kbd:`I` in the 3D View.

There are some built in Keying Sets,
and also custom Keying Sets called *Absolute Keying Sets*\ .

To select and use a Keying Set, set the *Active Keying Set* in the :doc:`Timeline Header <animation/editors/timeline#v_keyframe_control>`\ , or the *Keying Set Panel*\ , or press :kbd:`Ctrl-Alt-Shift-I` in the 3D View.


Keying Set Panel
----------------


This panel is used to add, select, manage *Absolute Keying Sets*\ .


.. figure:: /images/Doc_Keying_Set_Panel.jpg

   Properties > Scene > Keying Set Panel.


*Keying Set Name*
    The active Keying Set is highlighted in blue, :kbd:`lmb-x2` to rename.

**+**
    Add new (Empty) keying set to the active Scene.

**-**
    Remove the active Keying Set.

*Active Keying Set properties*

   *Description*
       A short description of the keying set.

   *Export to File*
       Export Keying Set to a python script *File.py*\ .
       To re add the keying set from the *File.py*\ , open then run the *File.py* from the Text Editor.

    *Keyframing Settings*
       These options control all properties in the Keying Set.
       Note, the same settings in *User Preferences* override these settings if enabled.

       *Only Needed*
          Only insert keyframes where they're needed in the relevant F-Curves.

       *Visual Keying*
          Insert keyframes based on the visual transformation.

       *XYZ=RGB Colors*
          For new F-Curves, set the colors to RGB for the property set, Location XYZ for example.


Active Keying Set Panel
-----------------------


This panel is used to add properties to the active Keying Set.


.. figure:: /images/Doc_Keying_Set_Active_Panel.jpg

   Properties > Scene > Active Keying Set Panel.


.. figure:: /images/Doc_Keying_Set_Group.jpg

   Properties > Graph Editor > Channels, Named Group.


*Paths*
    A collection of *Paths* each with a *Data Path* to a property to add to the active Keying Set.
    The active *Path* is highlighted in blue.

**+**
    Add new empty path to active Keying Set.

**-**
    Remove active path from the active Keying Set.

*Active Path properties*

   *ID-Block*
       Set the *ID-Type* + *Object ID* *Data Path* for the property.

   *Data Path*
       Set the rest of the *Data Path* for the property.

   *Array Target*
       Use *All Items* from the *Data Path* or select the array index for a specific property.

   *F-Curve Grouping*
       This controls what *Group* to add the *Channels* to.
       *Keying Set Name*\ , *None*\ , *Named Group*\ .

    *Keyframing Settings*
       These options control individual properties in the Keying Set.

       *Only Needed*
          Only insert keyframes where they're needed in the relevant F-Curves.

       *Visual Keying*
          Insert keyframes based on the visual transformation.

       *XYZ=RGB Colors*
          For new F-Curves, set the colors to RGB for the property set, Location XYZ for example.


Adding Properties
-----------------


Some ways to add properties to keying sets.

:kbd:`rmb` the property in the *User Interface*\ , then select *Add Single to Keying Set* or *Add All to Keying Set*\ . This will add the properties to the active keying set, or to a new keying set if none exist.

Hover the mouse over the properties, then press :kbd:`K`\ ,
to add *Add All to Keying Set*\ .


See Also
--------


- :doc:`Timeline Header - V Keyframe Control <animation/editors/timeline#v_keyframe_control>`


