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

The Menu Search pop-up searches Blender's interface for a desired
:doc:`/interface/operators` and allows you to execute that operator.
It displays a list of matches and shows which menu the operator was found in.
Start typing the name of the operator you want to refine the list.
When the list is sufficiently narrowed, :kbd:`LMB` on the desired operator or
navigate with :kbd:`Down` and :kbd:`Up`, run the selected operator by pressing :kbd:`Return`.

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

When :ref:`Developer Extras <prefs-interface-dev-extras>` are activated
the Operator Search can be accessed from the Edit menu in the Topbar.
This search menu search all :doc:`/interface/operators`
within Blender even if they are not exposed in a menu.
This is useful for Python developers for testing purposes.
Blender might also include a few advanced operators that are not
exposed in a menu and can only be accessed via this search menu.
