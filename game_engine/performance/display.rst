
Display
=======

The :guilabel:`Display` tab at the :guilabel:`Render` context of the :guilabel:`Properties`
Window, let the game developer specify the maximum frame rate of the animations shown during
the game execution, whether to see informations like framerate and profile, debug properties,
physics geometry visualization, warnings,
if the mouse cursor is shown during the game execution, and options to specify the framing
style of the game to fit the window with the specified resolution.


Options
-------

.. figure:: /images/(Doc_26x_Manual_Game_Engine_Performance_Display)_(Display_Tab_BGE_Render_Context)_(GBAFN).jpg

   Fig. 1 - Display Tab at the Render Context


**Animation Frame Rate**
   This numeric field/slider specify the maximum frame rate at which the game will run.
Minimum is **1**, maximum is **120**.

**Debug Properties**
   When checked, if a property was previously checked to be debugged during the game, the values of this property will be shown with the :doc:`Framerate and Profile <game_engine/performance/display/framerate_and_profile>` contents.

**Framerate and Profile**
   When checked, this will show values for each of the calculations Blender is doing while the game is running, plus the properties marked to be debugged. Each of the values are explained at the :doc:`Framerate and Profile <game_engine/performance/display/framerate_and_profile>` page.

**Physics visualization**
   Shows a visualization of phisycs bounds and interactions (like hulls and collision shapes), and their interaction.

**Deprecation Warnings**
   Every time when the game developer uses a deprecated functionality (which in some cases are outdated or crippled OpenGL Graphic cards functions), the system will emit warnings about the deprecated function.

**Mouse Cursor**
   Wether to show or not the mouse cursor when the game is running.

**Framing**
There are three types of framing available for the Blender Game Engine, *Letterbox*,
*Extend* and *Scale* :

*Letterbox* :
   Show the entire viewport of the game in display window, using horizontal and/or vertical bars when needed.

*Extend* :
   Show the entire viewport of the game in display window, viewing more horizontally or vertically.

*Scale* :
   Stretch or Squeeze the viewport to fill the display window.

**Color Bar**
   This will let the game developer choose the bar colors when using the **Letterbox** Framing mode.