
Property Editing
****************

Logic Properties are created and edited using the  panel on the left of the Logic Editor
Panel. The top menu provides a list of the available property types.


.. figure:: /images/BGE_Game_Logic_Properties.jpg

   Property Panel


**Add Property** button
   This button adds a new property to the list, default is a :guilabel:`Float` property named ``prop``, followed
   by a number if there already is one with this name.

**Name** field
   Where you give your property its name, this is how you are going to access it through python or expressions. The
   way to do so in python is by dictionary style lookup (``GameObject["`` *propname* ``"]``). The name is case
   sensitive.

**Type** menu
   This menu determines which type of property it is (
FIXME(TODO: Internal Link;
[[#Property Types|see below]]
)).

**Value** field
   Sets the initial value of the property.


**FIXME(Template Unsupported: Shortcut/Keypress; {{Shortcut/Keypress|I}})** information button
   Display property value in debug information.
   If debugging is turned on, the value of the property is given in the top left-hand corner of the screen while the
   game is run. To turn debugging on, tick :guilabel:`Show Debug Properties` in the :guilabel:`Game` menu. All
   properties with debugging activated will then be presented with their object name, property name and value during
   gameplay. This is useful if you suspect something with your properties is causing problems.

**FIXME(Template Unsupported: Shortcut/Keypress; {{Shortcut/Keypress|X}})** Delete property.


