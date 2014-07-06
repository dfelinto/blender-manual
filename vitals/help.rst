
..    TODO/Review: {{review}} .

Help system
***********

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Menu:     :menuselection:`Help`
   | Hotkey:   Undefined - You can add one for your :doc:`Keymap » <preferences/input>`


Blender has a range of built-in and web-based Help options.

The built in help options include:

- A Menu with all of the Help Options including the Web based ones. Some of them are also present in the :guilabel:`Splash Screen`.

Other new features like:


- The Blender Search (new feature).
- Tooltips showing also the internal Python Operators (new feature), when the user hovers the Mouse over a Button, a Menu, Numeric Field or any Blender function that has a named Python Operator.


General Web-based Help Options
==============================

.. admonition:: Browser and Internet Connection
   :class: nicetip

   Some forms of Help start up your web browser and access the Blender Foundation's web servers. In order to do this, you must have configured a default web browser for your Operating System, and have a connection to the Internet.


.. figure:: /images/Manual-Vitals-Help_Menu_2.61.jpg

   Help menu


- :doc:`Manual <>` - This is a link for the Official Blender Manual, in *Wiki* format, which you are now reading.
- `Release Log <http://www.blender.org/development/release-logs/>`__ - The release notes on the Web for the current Blender version.
- `Blender Website <http://www.blender.org/>`__ - The :guilabel:`blender.org` home page.
- `Blender e-Shop <http://www.blender3d.org/e-shop/>`__ - The Blender e-Store, where you can buy Training DVD's, books, t-shirts and other products.
- `Developer Community <http://www.blender.org/community/get-involved/>`__ - The :guilabel:`blender.org` "Get Involved" page. This is the launch page for Blender software development, bug tracking, patches and scripts, education and training, documentation development and functionality research.
- `User Community <http://www.blender.org/community/user-community/>`__ - Lists of many different support venues here.
- `Report a Bug <http://projects.blender.org/tracker/?atid=498&group_id=9&func=browse>`__ - The Blender Bug Tracker page.

**Important:** in order to Report a Bug, you must register at the website.


Programming Options
===================

- `Python 2.6X API Reference <http://www.blender.org/documentation/blender_python_api_2_61_3/>`__ - Python application programming interface (API) that Blender and :doc:`Python <introduction/installing_blender/python>` use to communicate with each other. Useful for the Blender Game Engine, Customizing, and other scripting.


.. figure:: /images/Manual-Vitals-Help-Search-Operator.jpg

   Operator Cheat Sheet


- :guilabel:`Operator Cheat Sheet` - Creates the ``OperatorList.txt`` file, which you can access in the :guilabel:`Text Editor`. You can also use Blender Search to generate the file. The text will list the available Python operators. At the time we were writing this part of the Manual (Blender 2.61), Blender had 1245 Operators.

While Blender is generating this list, the :guilabel:`Info Window` will change,
showing a message for the operation (See Fig: Info Window - Operator Cheat Sheet ).
To read the Text, switch to the Blender :guilabel:`Text Editor` Window, using the :doc:`Window type Selector <interface/window_types>`, and then, clicking on the button *Browse Text to be Linked* of the Text Editor, your text block will be shown in the Editor. The file will be in your list of Text files, named as *OperatorsList.txt*, if the file is  already generated, Blender will add a numeric suffix for the subsequent ones.


.. figure:: /images/Manual-Vitals-Help-Info-Operator-Cheat-Sheet.jpg

   Info Window - Operator Cheat Sheet


Diagnostics Options
===================

.. figure:: /images/Manual-Vitals-Help-Search-Info.jpg

   Blender Search - System Info


- :guilabel:`System Info` - Creates a ``system-info`` file, which you can access  in the Blender :guilabel:`Text Editor`. The text lists various key properties of your system and Blender, which can be useful in diagnosing problems. When you click on this Option, Blender will verify your installation, will change the :guilabel:`Info Window` for a while when generating the file ( See: Info Window - Info.txt ). You can also use Blender Search to generate the file.

To read the Text, switch to the Blender :guilabel:`Text Editor` Window, using the :doc:`Window type Selector <interface/window_types>`, and then, clicking on the button *Browse Text to be Linked* of the Text Editor, your text block will be shown in the Editor. The file will be in your list of Text files, named as *system-info.txt*, if the file is  already generated, Blender will add a numeric suffix for the subsequent ones.


- The text file is created with **4** different sections: Blender, Python, Directories and OpenGL, which we will explain below:
  - **Blender:** This section of the info.txt shows you the Blender version, flags used when Blender was compiled, day and time when Blender was compiled, build system, and the path in which Blender is running.
  - **Python:** The Python version you are using, showing the paths of the Python programming language paths.
  - **Directories:** The Blender directories setup for ``scripts``, ``user scripts``, ``datafiles``, ``config``, ``scripts (internal)``, ``autosave`` directory and ``temp dir``. Those directories are configured using the  :doc:`User Preferences <preferences/file>` Editor Window.
  - **OpenGL:** This section will show you the version of OpenGL that you are using for Blender, the name of the manufacturer, version, vendor and a list with your card capabilities or OpenGL software capabilities.


.. figure:: /images/Manual-Vitals-Help-Info-Window-System.Info.jpg

   Info Window - Info.txt


- :guilabel:`Toggle System Console` - Reveals the command window that contains Blender's :guilabel:`stdout` messages. Can be very useful for figuring out how the UI works, or what is going wrong if you encounter a problem. Even more information is available here, if you invoke Blender as :guilabel:`blender -d`. This menu item only shows up on Windows.
  - In all Operating Systems, to see this information, simply run :guilabel:`blender` from the command-line.
  - On Linux, if you ran Blender from the GUI, you can see the output in :guilabel:`~/.xsession-errors`
  - On Mac OS X, you can open Console.app (in the Utilities folder in Applications) and check the Log there.


- :guilabel:`Info Window Log` - This is not exactly a Help menu, but it is related. If you mouseover the line between the Info window and the 3D then click and drag the Info window down a bit, you can see the stream of Python calls that the UI is making when you work. This can be useful in creating scripts.


.. figure:: /images/Manual-Vitals-Help_Info_Log.jpg

   The Info Window Log after adding a Cube


Legacy Version Support
======================

- :guilabel:`FCurve/Driver fix` - Sometimes, when you load .blend's made from older versions of Blender (2.56 and previous), the Function Curves and Shapekey Drivers will not function correctly due to updates in the animation system. Selecting this option updates the FCurve/Driver data paths.


- :guilabel:`TexFace to Material Convert` - Convert old Texface settings into material. It may create new materials if needed.


Splash Screen
=============

.. figure:: /images/Manual-Vitals-Help-Search-Splash.jpg

   Splash Screen Search


:guilabel:`Splash Screen` - This displays the image where you can identify package and version. At the top-right corner, you can see the Version and SVN (Subversion) revision (See Fig: Blender Splash Screen). For example, in our Splash Screen, you can see the version **2.66.0** and the revision number **r54697**. This can be useful to give to support personnel when diagnosing a problem. You can also use Blender Search to Show the Splash Screen or click in the Small Blender Logo present in the :guilabel:`Info Window`

There are some Internet Based Help options that are also present in the Blender
:guilabel:`Splash Screen`.
They are presented as the same links you will find at the :guilabel:`Help` Menu.


.. figure:: /images/(Doc_26x_Manual_Vitals_Help)_(Splash_Screen_2.66)_(GBV266FN).jpg

   Blender Splash Screen, Blender Version 2.66


Other Help Options
******************

Here we explain the two new features added for Blender,
:guilabel:`Blender Search` and the recoded :guilabel:`Tooltips`.


Blender Search
==============

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Hotkey:   :kbd:`space`


.. figure:: /images/Manual-Vitals-Help-Search-Keyword-Render.jpg

   Blender Search - Render


The Blender Search feature, called :guilabel:`Blender Search`,
is a new functionality added by the Blender recode
(from 2.4x series to 2.5x series and so on).
The Internal name of the feature is *Operator Search*.
When you hit :kbd:`space` from your keyboard,
Blender will present you with a small Pop Up Window,
no matter which Blender Window your Mouse pointer is located
(except the :guilabel:`Text Editor` Window and :guilabel:`Python console`),
and a field for you to type in.
Just type what you need and Blender will present you a list of available options.
You can click on the appropriate function for you, or search through them using your keyboard,
type :kbd:`enter` to accept, or :kbd:`esc` to leave.
Clicking outside of the Blender Search Window or taking the Mouse pointer away,
will also leave Blender Search.

The Image at the right shows Blender Search when we type the word *Render* inside the field.
If you continue typing,
your search keywords will refine your search and if no named operator can be found,
the small Pop Up Window for the Blender Search will stay blank.


- How it works:
  - Every Blender Internal Operator can use a defined name, some of them are predefined names for the user. For example, the :guilabel:`Render` command is a named Python call, the appropriate Operator is  ``Python: bpy.ops.render.render()`` , but for the user, it is called Render. All of those *user* names that were previously attributed for Python operators can searched for using :guilabel:`Blender Search`.


Tooltips
========

.. figure:: /images/Manual-Vitals-Help-Tooltip-Render-Engine.jpg

   The Mouse pointer was  Stopped for a while over the Render Engines List in the Info Window. The normal Tooltip  is in white and the Python operator is displayed in grey


The :guilabel:`Tooltips` in Blender were completely recoded,
and every time you hover your Mouse over a Button, a Command,
Numeric Fields or things that are related to Operators, staying for a while,
it will show you not only the normal Tooltip, but also the specific related operator.
Those operators are useful for lots of tasks, from Python Scripts to Keymaps.
In the example Image at the right, we pointed our Mouse over the Info Window,
specifically over the list of the Render engines available, waited for a while,
and the Tooltip with the appropriate operator was shown. In our example,
it shows the Tooltip *Engine to Use for Rendering* in white, and  ``Python:
RenderSettings.engine``  in grey, which is the Operator associated with the function.


