
System
======


The :guilabel:`System` tab at the Render context of the Properties Window, let the game
developer specify options about the system performance regarding to frame discards and
restrictions about frame renderings, the key to stop the Blender Game Engine,
and whether to maintain geometry in the internal memory of the Graphic card.


Options
-------


.. figure:: /images/(Doc_26x_Manual_Game_Engine_Performance_System)_(System_Tab_BGE_Render_Context)_(GBAFN).jpg

   System tab at the Render Context


**Use Frame Rate**
   When checked, this will inform Blender whether to run freely without frame rate restrictions or not. The frame rate is specified at the :guilabel:`Display` tab of the :guilabel:`Render` Context of the Properties Window. For more information about frame rates, see the :doc:`Display <game_engine/performance/display>` page.

**Display Lists**
   When checked, this will tell Blender to maintain the lists of the meshes geometry allocated at the GPU memory. This can help to speed up viewport rendering during the game if you have enough GPU memory to allocate geometry and textures.

**Restrict Animation Updates**
   When checked, this will force Blender game engine to discard frames (even at the middle of redrawing, sometimes causing *tearing* artifacts) if the rate of frame rendered by the GPU is greater than the specified at the :doc:`Display <game_engine/performance/display>` Tab.

**Exit Key**
   Clicking at this button will ask the user to type a key to specify a key to stop the game engine from running.