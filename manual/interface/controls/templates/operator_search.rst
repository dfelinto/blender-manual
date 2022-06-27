.. _bpy.ops.wm.search:

******
Search
******

.. _bpy.ops.wm.search_menu:

Menu Search
===========

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Edit --> Menu Search`
   :Shortcut:  :kbd:`F3`

The Menu Search pop-up lets you search Blender's interface for a certain
:doc:`operator </interface/operators>` and execute it.
First narrow down the list by typing (part of) the operator's name,
then either click the operator with :kbd:`LMB`, or navigate to it with
:kbd:`Down` and :kbd:`Up` and activate it with :kbd:`Return`.

Apart from the operator names, the pop-up also shows the menus
where they're located.

.. figure:: /images/interface_controls_templates_operator-search_pop-up.png
   :align: center

   The Menu Search pop-up.

.. seealso::

   The :ref:`Spacebar Action <keymap-blender_default-spacebar_action>`
   option in the Preferences.


.. _bpy.ops.wm.search_operator:

Operator Search
===============

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Edit --> Operator Search`

When :ref:`Developer Extras <prefs-interface-dev-extras>` are activated,
the Operator Search can be accessed from the Edit menu in the Topbar.
This menu searches all :doc:`/interface/operators`
within Blender, even if they are not exposed in a menu.
This is useful for Python developers for testing purposes.
Blender might also include a few advanced operators that are not
exposed in a menu and can only be accessed via this search menu.
