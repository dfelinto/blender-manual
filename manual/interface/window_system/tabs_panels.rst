
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
The content of only one Tab is visible at a time.
Tabs are listed in a *Tab header*, which can be horizontal or vertical.


Switching/Cycling
-----------------

Vertical tabs can be switched with :kbd:`Ctrl-Wheel` from anywhere in the tab.
You can also cycle through tabs with :kbd:`Ctrl-Tab` and
:kbd:`Shift-Ctrl-Tab`, or press down :kbd:`LMB` and move the mouse over the tab header icons.
(This does not apply to Workspace tabs; see :ref:`Workspace controls <workspaces-controls>`.)

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
The panel header shows the title of the panel. It is always visible.
Some panels also include subpanels.


Collapsing and Expanding
------------------------

A panel can either be expanded to show its contents, or collapsed to hide its contents.
An expanded panel is indicated by a down-arrow (▼) in the panel header,
while a collapsed panel is shown with a right-arrow (►).

- Clicking :kbd:`LMB` on the panel header expands or collapses it.
- Pressing :kbd:`A` expands/collapses the panel under the mouse pointer.
- Clicking :kbd:`Ctrl-LMB` on the header of a collapsed panel will expand it and collapse all others.
- Clicking :kbd:`Ctrl-LMB` on the header of an expanded panel will expand/collapse all its subpanels.
- Dragging with :kbd:`LMB` over the headers will expand or collapse many at once.


Position
--------

You can change the position of a panel within its region by clicking
and dragging the grip widget (\:\:\:\:) on the right side of its header.


Pinning
-------

Sometimes it is desirable to view panels from different tabs at the same time.
Like, for instance, having access to a camera's properties, while other objects are selected.
This has been solved by making panels pinnable.

A pinned panel remains visible regardless of which tab has been selected.
You can pin a panel by clicking on the pin icon in its header.
Panels that do not have a pin icon can be pinned by :kbd:`RMB` on the panel header
and selecting *Pin*, or by pressing :kbd:`Shift-LMB`.

.. note::

   Pinning is not available for all panels. For example, it's available in the Sidebar
   but not in the Properties editor.


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
   New presets can be added based on the currently applied set of properties, which will be saved for later reuse.
   A pop-up opens where you can set a name, after which you can select it from the list and
   in some cases additional settings.
Remove ``-``
   Deletes the selected preset.

.. saving preset: data-system?
