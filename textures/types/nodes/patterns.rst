
..    TODO/Review: {{review|}} .


Pattern Nodes
=============


Checker
-------


.. figure:: /images/Doc26-textureNodes_checker.jpg
   :width: 200px
   :figwidth: 200px

   Checker node


The checker node creates a checkerboard pattern

:guilabel:`color 1/color 2`
   Sets the color of the squares
:guilabel:`Size`
   The scale of the checker pattern


Bricks
------


.. figure:: /images/Doc26-textureNodes_bricks.jpg
   :width: 200px
   :figwidth: 200px

   Bricks node


The Bricks node creates a brick like pattern

:guilabel:`Offset`
   The relative offset of the next row of bricks

:guilabel:`Frequency`
   Offset every N rows. The brick pattern offset repeats every N rows.

:guilabel:`Squash`
   Scales the bricks in every N rows by this amount.

:guilabel:`Frequency`
   Squash every N rows.

:guilabel:`Bricks 1, Bricks 2`
   Sets the color range of the bricks. Brick colors are chosen randomly between these two colors.

:guilabel:`Mortar`
   Sets the mortar color, in between the bricks.

:guilabel:`Thickness`
   Sets the thickness of the mortar

:guilabel:`Bias`
   The bias of randomly chosen colors, between -1 and 1. -1 Makes all bricks Color 1, and a value of 1 makes them all Color 2.

:guilabel:`Brick Width`
   Sets the horizontal size of all the bricks.

:guilabel:`Row Height`
   Sets the verticalsize of all the bricks.