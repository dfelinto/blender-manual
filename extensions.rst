
..    TODO/Review: {{review}} .


Extending Blender
=================

Unlike many programs you may be familiar with, Blender is not monolithic and static. You can extend its functionality with :doc:`Python scripting <extensions/python>` without having to modify the source and recompile.


Addons
------

Addons are scripts you can enable to gain extra functionality within Blender,
they can be enabled from the user preferences.

Outside of the Blender executable,
there are literally hundreds of addons written by many people:


- Officially supported addons are bundled with Blender.
- Other **Testing** addons are included in development builds but not official releases, many of them work reliably and are very useful but are not ensured to be stable for release.

An Overview of all addons is available in this wiki in the `Scripts Catalog <http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts>`__ and in the `Extensions tracker <https://projects.blender.org/projects/bf-extensions/>`__.


Scripts
-------

Apart from addons there are also scripts you can use to extend Blenders functionality:

- Modules: Utility libraries for import into other scripts.
- Presets: Settings for Blender's tools and key configurations.
- Startup: These files are imported when starting Blender. They define most of Blender's UI, as well as some additional core operators.
- Custom scripts: In contrast to addons they are typically intended for one-time execution via the :doc:`text editor <extensions/python/text_editor>`


Saving your own scripts
-----------------------

File location
~~~~~~~~~~~~~

All scripts are loaded from the ``scripts`` folder of the :doc:`local, system and user paths <introduction/installing_blender/directorylayout>`.

You can setup an addittional search path for scripts in :doc:`User preferences <preferences/file#file_paths>` (:guilabel:`User Preferences` → :guilabel:`File Paths`).


Installation
~~~~~~~~~~~~

Addons are conveniently installed through Blender in the :guilabel:`User Preferences` →
:guilabel:`Addons` window. Click the :guilabel:`Install from File...` button and select the
``.py`` or ``.zip`` file.

To manually install scripts or addons place them in the ``addons``,
``modules``,
``presets`` or ``startup`` directory according to their type.
See the description above.

You can also run scripts by loading them in the :doc:`text editor <extensions/python/text_editor>` window.


