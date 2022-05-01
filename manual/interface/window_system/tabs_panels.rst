
*************
Tabs & Panels
*************

Tabs
====

.. figure:: /images/interface_window-system_tabs-panels_tabs.png
   :align: right
   :figwidth: 300px

   Top: Horizontal Tab header in the Topbar.
   Bottom: Vertical Tab header shows tab icons in the Properties.

Tabs are used to control overlapping sections in the user interface.
Contents of only one Tab is visible at a time.
Tabs are listed in *Tab header*, which can be vertical or horizontal.


Switching/Cycling
-----------------

Vertical tabs can be switched with :kbd:`Ctrl-Wheel` from anywhere in the tab.
You can also cycle through tabs with :kbd:`Ctrl-Tab` and
:kbd:`Shift-Ctrl-Tab`, or press down :kbd:`LMB` and move mouse over tab header icons.
(Workspace tabs do not use this keymap. See :ref:`Workspace controls <workspaces-controls>`.)

.. container:: lead

   .. clear


.. _ui-panels:
.. _bpy.types.Panel:

Panels
======

.. figure:: /images/interface_window-system_tabs-panels_panels.png
   :align: right
   :figwidth: 200px

   Panels in Properties.

   A panel is highlighted in yellow and a subpanel in red.

The smallest organizational unit in the user interface is a panel.
The panel header show the title of the panel. It is always visible.
Some panels also include subpanels.


Collapsing and Expanding
------------------------

A panel can either be expanded to show its contents, or collapsed to hide its contents.
An expanded panel is indicated by a down-arrow (▼) in the panel header,
while a collapsed panel is shown with a right-arrow (►).

- A click with the :kbd:`LMB` on the panel header expands or collapses it.
- Pressing :kbd:`A` expands/collapses the panel under the mouse pointer.
- A :kbd:`Ctrl-LMB` click on the header of a specific panel will collapse
  all other panels and make this the only expanded one.
- A :kbd:`Ctrl-LMB` click on the header of a specific panel that contains subpanels
  will expand / collapse all subpanels.
- Dragging with :kbd:`LMB` over the headers will expand or collapse many at once.


Position
--------

You can change the position of a panel within its region by clicking
and dragging it with the :kbd:`LMB` on the grip widget (\:\:\:\:)
located in on the right side of the panel header.


Pinning
-------

Sometimes it is desirable to view panels from different tabs at the same time. 
Like, for instance, having access to a camera's properties, while other objects are selected.
This has been solved by making panels pinnable.

A pinned panel remains visible regardless of which tab has been selected.
You can pin a panel by clicking on the pin icon in its header.
Panels that do not have a pin icon can also be pinned by :kbd:`RMB` and selecting *Pin*,
or you use :kbd:`Shift-LMB` on the panel.


Zoom
----

The zoom factor of a whole region with panels can be changed by
:kbd:`Ctrl-MMB` clicking and moving the mouse anywhere within that region
or use the :kbd:`NumpadPlus` and :kbd:`NumpadMinus` to zoom in and out the contents.
Pressing :kbd:`Home` (Show All) will reset the zooming at the screen/panel focused by the mouse pointer.


.. _bpy.ops.script.execute_preset:
.. _ui-presets:

Presets
-------

.. figure:: /images/interface_controls_templates_list-presets_preset.png
   :align: right

   Example Presets menu.

.. Share between properties. i.e. different nodes color presets.

Selector
   A list of available presets. A selection will override the included properties.
Add ``+``
   New presets can be added based on currently applied set of properties, which will be saved for later reuse.
   A pop-up opens where you can set a name, after which you can select it from the list and
   in some cases additional settings.
Remove ``-``
   Deletes the selected preset.

.. saving preset: data-system?
