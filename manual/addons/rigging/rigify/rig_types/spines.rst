
******
Spines
******

These rigs are used to generate spine structures, including the head and tail.


``spines.super_spine``
======================

Will create a complete bendy and stretchy b-bones spine system based on bone numbers of
your bone chain and user defined options.

Requirement: A chain of at least three connected bones (base system).

Pivot Position (integer)
   Defines the pivot position for torso and hips.
Head (Boolean)
   When checked neck and head systems will be added to your spine rig.

   Neck Position (integer)
      Defines the bone where the neck system starts. The last bone will always be the head system.
      If neck position is the last bone of the chain, then only the head system will be created ignoring the neck.
Tail (Boolean)
   When checked tail system will be added to your spine rig.

   Tail Position (integer)
      Defines the bone where the tail system starts. The next bone will always be the hips system.
