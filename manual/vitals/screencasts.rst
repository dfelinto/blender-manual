
..    TODO/Review: {{Review}} .


Blender Screencasts
*******************

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Hotkey:   :kbd:`alt-F3`


The shortcut :kbd:`alt-F3` starts the screencast function. Screencasts will record your actions over time either as a video or sequence of image files. The type and location of the output is determined by the settings in the :doc:`Output panel </render/output>` of the :doc:`Render context </interface/contexts>` window.
The default settings will generate a screencast consisting of a series of PNG images captured
every 50 ms and stored in the :guilabel:`/tmp` folder. If you want to record a video, set the
:guilabel:`Output` to one of the :guilabel:`Movie File Formats` supported by your system
listed in the :guilabel:`Output panel` format menu.
If you are unsure what video codecs your system supports, select :guilabel:`AVI JPEG`.


.. figure:: /images/Manual-Vitals-Screencast-Small-User-Preferences-System.jpg

   Options in the User Preferences Editor


The FPS for video Screencasts and time between each Screenshot for an image series Screencast can be set from the :doc:`System panel </preferences/system>` of the :doc:`User Preferences </preferences>` window.

(See Fig: Options in the User Preferences Editor)


.. note:: Audio support

   Blender Screencast doesn't support audio recordings, so you will have to do it manually using other software, e.g. `Audacity <http://audacity.sourceforge.net/>`__, in conjunction with Blender.


When you start Blender Screencasts, the header of the :guilabel:`Info Window` will change,
and it will show you a button for stopping your capture.

Below, we show the normal header of the :guilabel:`Info Window`,
when in normal Blender operation (See Fig: Info Window - Header - Normal Operation),
and with the Stop button for the Screencast, when in Screencast Mode. (See Fig:
Info Window - Header - Capture Stop Button).


.. figure:: /images/Manual-Vitals-Screencast-Small-Header-Info-Window-Normal.jpg

   Info Window - Header - Normal Operation


.. figure:: /images/Manual-Vitals-Screencast-Small-Header-Info-Window-Stop.jpg

   Info Window - Header - Capture Stop Button


(Note: The header Image was taken using Blender 2.61)


.. note:: The only way to stop the Screencast

   Pressing the Stop button in the header of the Info Window is the only way to stop the Screencast capture. If you press :kbd:`esc`, the shortcut will only work for operations performed in the Blender :guilabel:`User Interface`, (it will stop animations, playbacks and so on...), but will not work to stop :guilabel:`Screencasts`.


.. figure:: /images/Manual-Vitals-Screencast-Frame-Range-Sufix.jpg

   Dimensions Panel - Frame Range


The frames are stored using a suffix added to their file name, where the suffix is composed of the numbers present in the fields for *start* and *end frames*, defined in the Frame Range of the Dimensions panel, :doc:`Render context </interface/contexts>`. (See Fig: Dimensions Panel - Frame Range - highlighted in yellow)

.. note::

   The configuration of the End frame, present in the Frame Range of the Dimensions Panel,
   **will not** stop your capture automatically.
   You will always have to stop the Screencast manually, using the Stop button.


The Videos are generated internally in the same manner as the :guilabel:`Screenshots`,
using the width and height of the Window you are working in.
If you choose to capture to a Video file,
Blender will have to pass those frames to a Video codec.

**Warning:** Some codecs limit the output width/height or the video quality.


- When you save your :guilabel:`Screencast` in an Image format, the Images will be saved using the entire Blender Window, with full width and height, and the quality of the Image will be defined by its type (i.e. JPG, PNG, and so on) and configuration (i.e. Slider *quality* of the .JPG format).


- When you save your :guilabel:`Screencast` in a Video format, it will be sent to a codec. Depending on the codec limitations, the resulting output Video could be scaled down. Furthermore, some combinations of Window width and height cannot be processed by certain codecs. In these cases, the :guilabel:`Screencast` will try to start, but will immediately stop. In order to solve this, choose another Window format and/or another codec.


Blender Window Dimension
------------------------

There is a way to match the Blender Window dimensions with the Output Video File,
achieving standard dimensions for the output of the Blender Screencast. (I.e. NTSC, HD,
Full HD, etc).
You can control the width and height of your Blender Window, starting Blender from a Command Line. To learn more about starting Blender from a command line, see the page about :doc:`Blender Console Window </interface/window_system/console_window>`.


Addon: {{Literal|3D View:Screencast Keys}}
------------------------------------------

The community based Addon :guilabel:`3D View:Screencast Keys` will show you the keys,
combination of keys pressed and mouse clicks on the left bottom corner of your 3D screen every
time you press a key or mouse button when capturing :guilabel:`Screencasts`.
The community Addon comes with the default installation of Blender.
The Image below shows the community Addon with its Tab Open. (See Fig: 3D View:
Screencast Keys - Addon). To enable the Addon,
open the :guilabel:`User Preferences` Editor Window :kbd:`ctrl-alt-u`,
go to the :guilabel:`Addons` Tab, and go to the *3D View* Addons. Just click on the checkbox
(Highlighted in yellow) to enable the Addon.


.. figure:: /images/Manual-Vital-Screencast-Small-Addon-Screencast-Keys.jpg

   3D View: Screencast Keys - Addon


.. admonition:: Reference
   :class: refbox

   | Mode:     All modes →  Addon Enabled
   | Menu:     :menuselection:`View --> Properties` →  :guilabel:`Screencast Keys Tab`
   | Hotkey:   Use :kbd:`N` to show the :guilabel:`Properties Panel` →  :guilabel:`Screencast Keys Tab`


.. figure:: /images/Manual-Vital-Screencast-Small-Addon-Screencast-Keys-Function.jpg

   Screencast Keys Addon Tab - Properties Panel


Once the Addon is enabled you will see the Screencast Keys section at the end of the list,
on the Properties panel.

**Description:**


- **Start display button:** When you press this button, Blender will display any Key or combination of Keys you are pressing on the bottom left corner of the 3D window as floating text. If you press several times the same Key or combination of Keys, Blender will add an " xn" tag at the end of the Keys or combination of Keys, indicating how many times you pressed the Key or combination of Keys.
- **Stop display button:** will stop Blender from displaying ScreenCast Keys.
- **PosX:** postion of the Screencast text on **X** axis.
- **PosY:** position if the Screencast text on **Y** axis.
- **Font:** Screencast text font size.
- **Mouse:** Screencast mouse icon size.
- **Mouse display:** In this drop down menu you can select how the Screencast text will be displayed
- **Text:** Will display the Keys pressed and Mouse buttons pressed as text.
- **Icon:** Will display the Mouse as an icon and Keys pressed as text.
- **None:** Will display info about Keys pressed only, without mouse button info.
- **Group Mouse & Text Check box:** When this is checked, Blender will display a box around the Screencast Text to make reading easy.
- **Color:** Lets you choose the color of the Screencast text.


.. tip:: New Community Addon

   There is also currently an Addon for Blender 2.5/2.6 which will take a screenshot of any area you like at the click of a button, and proceed to upload it directly to `Pasteall <http://www.pasteall.org/pic/.>`__. The Addon currently has no development page, but it will be linked to here when it's finished.


