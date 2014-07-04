
.. figure:: /images/Blender25features.jpg
   :width: 650px
   :figwidth: 650px


Introduction
============

With version 2.5, Blender has seen phenomenal improvements in virtually all areas: software,
interface, modeling, animation flow, tools, the python API, etc.
This is the result of a careful study of use cases,
years of additions and community collaboration,
and a complete reorganization and rewrite of the software source code. As a result,
this is one of the largest projects undertaken on the Blender code base to date.

This page explains the most striking differences between Blender 2.4 and Blender 2.5.
This is not an exhaustive list of new functionality (that would be too long!) but is rather a
concise introduction to the evolution of 2.5 and its major improvements over previous
versions.


FIXME(Tag Unsupported:youtube;
<youtube>WamG6HIZ1rw</youtube>
)


Interface
=========

New User Interface
------------------

.. figure:: /images/Change-interface.jpg
   :width: 300px
   :figwidth: 300px


The Blender User Interface is based on 3 principles:


- **Non Overlapping** : The UI permits you to view all relevant options and tools at a glance without pushing or dragging windows around.
- **Non Blocking** : Tools and interface options do not block the user from any other parts of Blender. Blender doesn't pop up requesters that require the user to fill in data before things execute.
- **Non Modal** : User input should remain as consistent and predictable as possible without changing commonly used methods (mouse, keyboard) on the fly.

The User Interface has been reorganized. Old *Buttons Windows* are now **Properties**.
Properties present data to users. Everything you see in the Properties can be animated,
driven, and freely changed by the user. This means there are no tools here.
These go to the new **Toolbar** of the different editors (like 3D view).


.. figure:: /images/Change-from-global-to-specific.jpg


Starting at the top level, the Properties editor contains a list of tabs.
The list of tabs themselves are organized so that the most general controls appear on the left
(Render Properties), while more fine-grained controls (Object>Mesh>Material>Texture)
appear on the right, following reading direction. Furthermore,
available tabs depend on the selection (i.e. Mesh options are different from Camera options).


FIXME(Link Type Unsupported: dev;
[[Dev:2.5/Source/Development/WinterCamp/UIRules|Read more about new UI design rules »]]
)


FIXME(Link Type Unsupported: dev;
[[Dev:2.5/Source/UI/UIParadigms|Read more about 2.5 UI Paradigms »]]
)


FIXME(Link Type Unsupported: dev;
[[Dev:2.5/Source/Development/WinterCamp/Properties|Read more about new properties panel »]]
)


Multi-screen
------------

With its new Window Manager, Blender allows configuration of multiple windows/screens which is
useful for multi-screen setups. As with the main window,
each new window can be subdivided into areas.


Customizable
------------

.. figure:: /images/Change-ui-python-api.jpg
   :width: 300px
   :figwidth: 300px


The UI is more flexible than it was in 2.4x. Thanks to the new python API,
it is possible to customize the interface and change the place of panels or buttons. Most of
the interface uses python scripts available in the /.blender/scripts/ui/ folder so you can
edit them easily and make your own Blender interface.

Thanks to this new python API,
it is easier for the developer to integrate scripts in the Blender interface
(like render engine, tools, import/export scripts...).

`Read more about new python API » <http://www.blender.org/documentation/blender_python_api_2_58_1/>`__


.. figure:: /images/Change-keymap-edit.jpg
   :width: 300px
   :figwidth: 300px


Furthermore, Blender 2.5 includes a new **Keymap Editor**.
Hotkey/mouse definitions are grouped together in 'key maps'.
For each editor in Blender as well as for all modes or modal tools like transform,
there are multiple key maps.  Customizing the keys is done by making a local copy of the
default map and then editing all the options you'd like to have.
The default key maps will always be unaltered and available to use.


Animation system
================

Everything is animatable!
-------------------------

In Blender 2.5 every property can be animated,
from the output image size to the modifiers options. Now you can set keys in every editor:
3D view, video sequence editor, Node editor (material, texture, composite)...
This new system is called *Animato*.


FIXME(Link Type Unsupported: dev;
[[Dev:2.5/Source/Animation/Animato|Read more about Animato »]]
)


Dope sheet and graph editor
---------------------------

.. figure:: /images/Change-new-animation.jpg
   :width: 300px
   :figwidth: 300px


The IPO Curves Editor, Action Editor,
and NLA Editor have been rebuilt into the **Dope Sheet** and **Graph Editor**
(generic name used also in Maya).

The "Action Editor" has been extended to become a full Dope Sheet,
allowing control over multiple actions at once, grouping per type,
and with better access to shape keys.

Blender's new animation system also allows the addition of a Function Curve to any property.
The new Graph Editor (formerly Ipo Curve Editor) enables viewing,
browsing and editing of any collection of function curves,
including all the curves of an entire scene!

`Watch this character animation » <http://www.youtube.com/watch?v=8Wj3Hm_Pt18>`__


New functions
=============

Search tool
-----------

.. figure:: /images/Change-search-tool.jpg


Blender 2.5 integrates a search tool which permits you to find a function by entering its name
(or a part of it).
Just hit :kbd:`space` where you want to search and the menu will appear.
It is also available at the top of the Blender screen.


File browser improvements
-------------------------

The old file browser and Image browser have been linked into a single powerful browser.
Files can be displayed as lists or thumbnails,
and a new filter permits selection of which file types you want to show in the browser.

A side bar has also been added where you can see your disks, the most recent folder used,
and a new function lets you create bookmarks !


.. figure:: /images/Change-file-browser.jpg
   :width: 650px
   :figwidth: 650px


Python API
==========

Now based on Python 3.2


Watch this page on video!
=========================

This page has been made into a video. You can watch it on YouTube!


FIXME(Tag Unsupported:youtube;
<youtube>WamG6HIZ1rw</youtube>
)

