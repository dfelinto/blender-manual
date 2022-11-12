
********************
Copy Render Settings
********************

This is a simple tool that adds in the Render properties a new panel with a big *Copy Render Settings* button,
and some options to control what to copy, and to which scenes...

I wrote it as I often have tens of scenes all edited/gathered in a single "main" scene sequence.
When I want to make preview renders of that main scene,
I had to manually set all other scenes' preview scale -- long and boring.
And even worse, I often forgot to put them back to full resolution before final rendering!

So, with this add-on, I just have to set the preview scale in the main scene,
enable or disable :term:`Anti-Aliasing`, and hit *Copy Render Settings*!


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Render then Copy Render Settings to enable the script.


Description
===========

Render Settings
   This lists all render settings. The checkbox to the right controls whether that setting will be copied or not.
   So if you want to copy a specific setting, hover your mouse over its control,
   note its Python name (e.g. ``resolution_x`` for the X resolution, etc.),
   and enable the corresponding item in this list.

   .. important::

      This will only work if you have a Blender patched with ``ui_template_list diff``,
      see `UI Template List Enhancement
      <https://archive.blender.org/wiki/index.php/User:Mont29/UI_Template_List_Enhancement/>`__.

Presets
   The column of buttons to the right of the list are a set of presets
   which set or clear one or more settings at once.
   *This will work even without the UI template list patch.*

   Set Scale/Clear Scale
      Copy the render scale setting (below resolution controls, in *Dimensions* panel).
      Highly useful to do preview renders!

   Set Resolution/Clear Resolution
      Copy the render resolution and aspect ratio settings.
      Beware of side effects if you modify the aspect of your render (e.g. switching from: 4/3 to 16/9...).

   Set OSA/Clear OSA
      Copy the global :abbr:`OSA (Oversampling)` usage, and OSA level settings.
      Together with *Render Scale*, this is most useful for preview renders.

   Set Threads/Clear Threads
      Copy the settings (auto/fixed, and number) of threads used during rendering.
      Might be useful when e.g. you render your blend-files on various computers
      (even though the *Auto* option should work good in general...).

   Set Fields/Clear Fields
      Copy all fields settings.
      Allows you to easily switch from progressive to interlaced...

   Set Stamp/Clear Stamp
      Copy whether to render stamps or not (i.e. the global stamp switch setting).

Affected Scenes:
   Filter Scene
      You can type in this text field a regex (using Python syntax), and only scene
      which name matches this regex will be available. Quite useful when you have tens of scenes in a file...

      E.g. if you only want to copy some of your current render settings to scenes
      having "rabbit" in their name, type ``.*rabbit.*`` in this field.

   Columns of buttons
      These toggle buttons represent all scenes of the blend-file
      (optionally filtered through the *Filter Scene* regex),
      except the current one. Only enabled scenes will receive the copied settings!


.. reference::

   :Category: Render
   :Description: Allows to copy a selection of render settings from current scene to others.
   :Location: :menuselection:`Properties --> Render tab`
   :File: render_copy_settings folder
   :Author: Bastien Montagne
   :License: GPL
   :Note: This add-on is bundled with Blender.
