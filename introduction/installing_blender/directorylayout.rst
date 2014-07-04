
Configuration & Data Paths
==========================

Blender can be installed system wide or run from an extracted bundled with all necessary files
contained.

There are 3 different directories blender may use,
their exact locations are operating system dependent.

- **LOCAL:** location of configuration and runtime data (for self contained bundle)


- **USER:** location of configuration files (normally in the user's home directory).


- **SYSTEM:** location of runtime data for system wide installation (may be read-only).

For system installations both **SYSTEM** & **USER** directories are needed.

For locally extracted blender distributions the user configuration and data runtime data are
kept in the same sub-directory, allowing multiple blender versions to run without conflict,
ignoring the **USER** and **SYSTEM** files.

Here are the default locations for each system:


OSX
~~~

FIXME(Tag Unsupported:div;
<div class="tableNormal">
'''LOCAL:''' <code>./{{Blender/Version/Current}}/</code><br />
'''USER:''' <code>/Users/{user}/Library/Application Support/Blender/{{Blender/Version/Current}}/</code><br />
'''SYSTEM:''' <code>/Library/Application Support/Blender/{{Blender/Version/Current}}/</code>

''note, OSX stores blender binary in ./blender.app/Contents/MacOS/blender, so the local path to data & config is ./blender.app/Contents/MacOS/{{Blender/Version/Current}}''
</div>
)


Windows
~~~~~~~

FIXME(Tag Unsupported:div;
<div class="tableNormal">
'''LOCAL:''' <code>.\{{Blender/Version/Current}}\</code><br />
'''USER:''' <code>C:\Documents and Settings\{username}\AppData\Roaming\Blender Foundation\Blender\{{Blender/Version/Current}}\</code><br />
'''SYSTEM:''' <code>C:\Documents and Settings\All Users\AppData\Roaming\Blender Foundation\Blender\{{Blender/Version/Current}}\</code><br />
</div>
)


Unix (Linux/BSD/Solaris)
~~~~~~~~~~~~~~~~~~~~~~~~

FIXME(Tag Unsupported:div;
<div class="tableNormal">
'''LOCAL:''' <code>./{{Blender/Version/Current}}/</code><br />
'''USER:''' <code>$HOME/.config/blender/{{Blender/Version/Current}}/</code><br />
'''SYSTEM:''' <code>/usr/share/blender/{{Blender/Version/Current}}/</code>
</div>
)

*note that ./
FIXME(Template Unsupported: Blender/Version/Current;
{{Blender/Version/Current}}
)/ is relative to the blender executable & used for self contained bundles distributed by official blender.org builds.*

*note the USER path will use XDG_CONFIG_HOME if its set:* ``$XDG_CONFIG_HOME/blender/
FIXME(Template Unsupported: Blender/Version/Current;
{{Blender/Version/Current}}
)/``


Path Layout
===========

This is the path layout which is used within the directories described above.

Where ./config/\ **startup.blend** could be ~/.blender/2.66/config/startup.blend for example.


- ``./autosave/ ...``

autosave blend file location. *Windows only, temp directory used for other systems.*
search order: **LOCAL, USER**


- ``./config/ ...``

defaults & session info
search order: **LOCAL, USER**

- ``./config/`` **startup.blend**

default file to load on startup.

- ``./config/`` **userpref.blend**

default preferences to load on startup.

- ``./config/`` **bookmarks.txt**

file selector bookmarks.

- ``./config/`` **recent-files.txt**

recent file menu list.


- ``./datafiles/ ...``

runtime files
search order: **LOCAL, USER, SYSTEM**

- ``./datafiles/locale/{language}/``

Static precompiled language files for UI translation.

- ``./datafiles/icons/*.png``

icon themes for blenders user interface. *not currently selectable in the theme preferences.*

- ``./datafiles/brushicons/*.png``

images for each brush.


- ``./scripts/ ...``

python scripts for the user interface and tools
search order: **LOCAL, USER, SYSTEM**

- ``./scripts/addons/*.py``

python addons which may be enabled in the user preferences, includes import/export format support, render engine integration and many handy utilities.

- ``./scripts/addons/modules/*.py``

modules for addons to use (added to pythons sys.path)

- ``./scripts/addons_contrib/*.py``

another addons directory which is used for community maintained addons (must be manually created).

- ``./scripts/addons_contrib/modules/*.py``

modules for addons_contrib to use (added to pythons sys.path)

- ``./scripts/modules/*.py``

python modules containing our core API and utility functions for other scripts to import (added to pythons sys.path)

- ``./scripts/startup/*.py``

scripts which are automatically imported on startup.

- ``./scripts/presets/{preset}/*.py``

presets used for storing user defined settings for cloth, render formats etc.

- ``./scripts/templates/*.py``

example scripts which can be accessed from: Text Space's Header → Text → Script Templates


- ``./python/ ...``

bundled python distribution only necessary when the systems python is absent or incompatible
search order: **LOCAL, SYSTEM**


Notes
=====

User Scripts Path
-----------------

The user preferences script path provides a way to set your own directory which is used for
scripts as well as the user scripts path. Be sure to create subfolders within this directory
which match the structure of blenders scripts directory, startup/, addons/, modules/ etc.
because copying scripts directly into this folder will not load them on startup or as addons.


Environment Variables
---------------------

Environment variables can be used to override default path locations, eg:
$BLENDER_USER_CONFIG, $BLENDER_SYSTEM_PYTHON.

This is not normally something which needs setting but can be useful for custom configurations.

For details see the 'Environment Variables' section in 'blender --help'


Scripts Path & Missing Buttons
------------------------------

If blender starts with no interface this is probably because the scripts are not loading
correctly and can be caused by...

- script path not found.
- an error in one of the scripts.
- a version mis-match between blender and the scripts.

It's best to load blender from a terminal to see any error messages to see what's wrong.


