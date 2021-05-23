
******************
Collection Manager
******************

This add-on adds new functionality for the management of collections via a pop-up
and a QCD (Quick Content Display) system in the 3D Viewport. It also offers simple display
and modification of the relationship of objects with collections.

.. list-table::

   * - .. figure:: /images/addons_interface_collection-manager_popup.png

     - .. figure:: /images/addons_interface_collection-manager_qcd.png


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Interface then Collection Manager to enable the script.


Description
===========

Pop-up
------

Use :kbd:`M` to call up the main Collection Manager pop-up in the 3D Viewport when in Object Mode.
It can also be found in the :menuselection:`Object --> Collection` menu.

View Layer
   Render
      Enable/disable rendering of this view layer with this checkbox.
   View Layer
      :ref:`ui-data-block` of the current view layer.

Expand All Items
   Toggle all collections expanded or collapsed. Only enabled when you have subcollections.

Renumber QCD Slots
   Shown only if QCD is enabled in the preferences.

   - :kbd:`LMB` -- Renumber the QCD slots from the root slot (the slot designated 1)
     down to the bottom, for each depth level
     (`breadth first search <https://en.wikipedia.org/wiki/Breadth-first_search>`__).
   - :kbd:`Alt-LMB` -- Renumber from the first top-level collection in
     a `breadth first search <https://en.wikipedia.org/wiki/Breadth-first_search>`__ pattern.
   - :kbd:`Ctrl-LMB` -- Switch the renumber pattern to linear.
     This pattern will renumber straight down the list regardless of hierarchy.
   - :kbd:`Shift-LMB` -- Constrain renumbering to the branch under the root slot.

   .. hint::

      All options can be combined with each other.

Undo
   Undoes the previous action.

   .. note::

      Clears any in progress copy/swap actions.

Redo
   Redoes the previously undone action.

Specials
   Remove Empty Collections
      Remove all collections that have no subcollections or objects.

   Purge All Collections Without Objects
      Remove all collections that have no objects regardless of whether they have subcollections.

Display Options (funnel icon)
   Choose which restriction toggles are shown in the interface
   and whether the restriction toggles are aligned to the right in
   the tree view.

Scene Collection
   Set Active Collection
      Sets the active collection to the Scene Collection.

   Name
      This is static and can't be edited.

   Select All Objects in the Collection (multiple icons)
      - :kbd:`LMB` -- Select all of the objects in the collection (deselects all other objects).
      - :kbd:`Shift-LMB` -- Add/Remove all of the objects in the collection to/from the selection.
      - :kbd:`Ctrl-LMB` -- Select all of the objects in the collection and all of its subcollections (deselects all other objects).
      - :kbd:`Ctrl-Shift-LMB` -- Add/Remove all of the objects in the collection and all of its subcollections to/from the selection.

      Icons and button highlights are used to show the selection state:
         - ``no icon`` -- No objects are present in this collection to be selected.
         - ``no highlight`` -- No objects are selected in this collection.
         - ``Diamond outline`` -- Objects are present in the collection.
         - ``highlight`` -- One or more objects are selected in this collection.
         - ``Filled diamond`` -- All objects are selected in this collection.
         - ``small dot and greyed out`` -- No objects can be selected in this collection (the collection is hidden or marked as not selectable or all objects are marked as not selectable, etc.)  *Note: The button isn't disabled to allow selecting subcollections; however, if you left click on it it will deselect all objects.*

         .. hint::

            If you try to select all the objects in the collection but the diamond doesn't fill, that means you have one or more unselectable objects in the collection.

   Set Object (multiple icons)
      - :kbd:`LMB` -- Move selected object(s) to collection.
      - :kbd:`Shift-LMB` -- Add/Remove selected object(s) to/from collection.

      Icons are used to show the object/selection state:
         - ``Grid`` -- No objects are present in this collection.
         - ``Box outline`` -- Objects are present, but none are selected in this collection.
         - ``3 boxes with dashed outline`` -- The collection contains objects that are selected, but does not contain the active object in the selection.
         - ``Filled box`` -- The collection contains the active object in the selection.

         .. note::

            The active object must also be selected to be indicated/moved.

            If no objects are selected the button is disabled.


   Global Restrictions (checkbox, cursor, eye, screen, camera, holdout, indirect only icons)
      See the Outliner page for information about
      :ref:`Restrictions <editors-outliner-interface-restriction_columns>`.

      - :kbd:`LMB` -- Enable the restriction for all collections. Click again to restore the previous state.
      - :kbd:`Shift-LMB` -- Invert the restriction state on all collections.
      - :kbd:`Shift-Ctrl-LMB` -- Isolate collections with selected objects.
      - :kbd:`Shift-Alt-LMB` -- Disable collections with selected objects.
      - :kbd:`Ctrl-LMB` -- Copy/paste the restriction state on all collections.  Click on an RTO to copy the restriction state, then click on another RTO to paste it.
      - :kbd:`Ctrl-Alt-LMB` -- Swap the restriction state on all collections with that of another restriction.  Click on an RTO to copy the restriction state, then click on another RTO to swap the two.
      - :kbd:`Alt-LMB` -- Discard the previous state, and anything that has been stored for Copy/Paste or Swap.

Tree View
   Shows the collections within the current selected scene.

   Disclosure (small triangle icon)
      - :kbd:`LMB` -- Expand/collapse subcollections.
      - :kbd:`Shift-LMB` -- Isolate the tree. Collapses everything but the current item,
        and it's parents/descendants. Click again to restore the previous state.
      - :kbd:`Ctrl-LMB` -- Expand/collapse subcollections and their descendants.

   Set Active Collection
      Click to set the active collection to this collection.

   QCD Slot
      Set which QCD slot the collection corresponds to.
      (Shown only if QCD is enabled in the preferences.)

   Name
      Double :kbd:`LMB`-click to rename the collection.

   Select All Objects in the Collection (multiple icons)
      - :kbd:`LMB` -- Select all of the objects in the collection (deselects all other objects).
      - :kbd:`Shift-LMB` -- Add/Remove all of the objects in the collection to/from the selection.
      - :kbd:`Ctrl-LMB` -- Select all of the objects in the collection and all of its subcollections (deselects all other objects).
      - :kbd:`Ctrl-Shift-LMB` -- Add/Remove all of the objects in the collection and all of its subcollections to/from the selection.

      .. note::

         See the section in the Scene Collection for more details.


   Set Object (multiple icons)
      - :kbd:`LMB` -- Move selected object(s) to collection.
      - :kbd:`Shift-LMB` -- Add/Remove selected object(s) to/from collection.

      .. note::

         See the section in the Scene Collection for more details.

   Local Restrictions (checkbox, cursor, eye, screen, camera, holdout, indirect only icons)
      - :kbd:`LMB` -- Toggle the collection's restriction on/off.
      - :kbd:`Shift-LMB` -- Isolate the collection's restriction, preserving parents if need be.
        Click again to restore the previous state.
      - :kbd:`Shift-Ctrl-LMB` -- Isolate the collection and
        it's descendants' restrictions, preserving parents if need be.
        Click again to restore the previous state.
      - :kbd:`Ctrl-LMB` -- Toggle the restrictions of the collection and it's descendants on/off.
      - :kbd:`Alt-LMB` -- Discard the previous state.

   Remove ``X``
      Remove the collection.

   Filtering
      By Name
         A text field to filter collections by name.

      Invert (magnifying glass icon)
         Invert filtering (inverts the collections shown in the tree view so that what is
         shown is hidden and what was hidden is shown).

      By Selected (box icon)
         Filter collections by selected objects (show only collections that contain
         the selected objects).

      By QCD Slots (Q key icon)
         Filter collections by those designated as QCD slots (show only collections that
         correspond to a QCD slot). Shown only if QCD is enabled in the preferences.

      .. hint::

         All options can be combined with each other.

Add Collection, Add Subcollection
   Self-explanatory.

   .. note::

      If the tree view is filtered when adding collections,
      new collections that do not fit the filter rules will be displayed
      until the filtering changes.

Phantom Mode
   All visibility changes made in this mode will be discarded when it's disabled.

   Enabling Phantom Mode saves the current state of the restrictions and
   allows you to edit them without fear of losing their current state.
   When finished, disabling Phantom Mode will restore the saved state.

   Note: You will be unable to edit anything other than the restrictions while in Phantom Mode.

Apply Phantom Mode (check mark icon)
   Applies all changes made to RTOs while in Phantom Mode and exits the mode.


QCD
---

The Quick Content Display system provides a way to rapidly interact with
collections by allowing you to designate up to 20 collections as QCD slots.
You can then interact with these slots by using hotkeys or the widget
to view or move objects to them.


3D Viewport Header Widget
^^^^^^^^^^^^^^^^^^^^^^^^^

The header widget is composed of the Quick View Toggles button and 20 QCD slots.

Quick View Toggles (eye icon)
   - Enable All QCD Slots.
   - Enable All QCD Slots Isolated. (Enables all QCD slots and disables any non QCD slots)
   - Isolate Selected Objects Collections.
   - Disable Selected Objects Collections.
   - Disable All Non QCD Slots.
   - Disable All Collections.
   - Select All QCD Objects. (Select all objects that belong to enabled QCD slots)
   - Discard QCD History. (Discards previous QCD slot states)


   .. rubric:: Hotkeys

   - :kbd:`LMB` -- Enable All QCD Slots.
   - :kbd:`Alt-LMB` -- Select All QCD Objects.
   - :kbd:`LMB` hold down -- Opens a menu with all Quick View Toggles.

QCD Slots
   20 buttons in two rows in groups of five
   where the first row starts with slot 1 and the second with slot 11.

   The state of each slot is shown with a combination of the following indicators:

   - ``x`` -- Unassigned slot.
   - ``non-highlighted`` -- non-visible slot.
   - ``highlighted`` -- visible slot.
   - ``no icon`` -- no objects in the slot.
   - ``horizontal line icon`` -- objects are present in this slot.
   - ``circle icon`` -- one or more objects in this slot are selected.
   - ``dot icon`` -- the active object is in this slot.


   .. rubric:: Hotkeys

   - :kbd:`LMB` -- View single slot excluding all others.
   - :kbd:`Shift-LMB` -- Add/remove slot to/from view.
   - :kbd:`Ctrl-LMB` -- Move selected objects to slot.
   - :kbd:`Shift-Ctrl-LMB` -- Add/remove selected objects to/from slot.
   - :kbd:`Alt-LMB` -- Replace selection with objects in this slot.
   - :kbd:`Shift-Alt-LMB` -- Add/remove slot objects to/from the selection.


Move Widget
^^^^^^^^^^^

Use :kbd:`V` to call up the Move widget in the 3D Viewport when in Object Mode.
It can also be found in the :menuselection:`Object -> Collection` menu.

The Move Widget shares its layout and indicators with the 3D Viewport header widget.


.. rubric:: Hotkeys

- :kbd:`LMB` -- Move selected objects to slot.
- :kbd:`Shift-LMB` -- Add/remove selected objects to/from slot.
- :kbd:`0` - :kbd:`9` -- Move selected objects to slot 1-10 (0 is slot 10).
- :kbd:`Alt-0` - :kbd:`Alt-9` -- Move selected objects to slot 11-20 (0 is slot 20).
- :kbd:`Shift-0` - :kbd:`Shift-9` -- Add/remove selected objects to/from slot 1-10 (0 is slot 10).
- :kbd:`Shift-Alt-0` - :kbd:`Shift-Alt-9` -- Add/remove selected objects to/from slot 11-20 (0 is slot 20).


3D Viewport Hotkeys
-------------------

.. rubric:: Object Mode

QCD
   - :kbd:`0` - :kbd:`9` -- View slot 1-10 (0 is slot 10). Excludes all others.
   - :kbd:`Alt-0` - :kbd:`Alt-9` -- View slot 11-20 (0 is slot 20). Excludes all others.
   - :kbd:`Shift-0` - :kbd:`Shift-9` -- Add/remove slot 1-10 (0 is slot 10) to/from view.
   - :kbd:`Shift-Alt-0` - :kbd:`Shift-Alt-9` -- Add/remove slot 11-20 (0 is slot 20) to/from view.
   - :kbd:`Shift-=` -- Enable All QCD Slots.
   - :kbd:`=` -- Isolate Selected Objects Collections.
   - :kbd:`Minus` -- Disable Selected Objects Collections.
   - :kbd:`Shift-Alt-=` -- Disable All Non QCD Slots.
   - :kbd:`Ctrl-Alt-=` -- Disable All Collections.
   - :kbd:`Shift-Ctrl-=` -- Select All QCD Objects.
   - :kbd:`Alt-=` -- Discard QCD History.

Disable Objects (only available if enabled in the preferences.)
   - :kbd:`H` -- Disable Selected.
   - :kbd:`Shift-H` -- Disable Unselected.
   - :kbd:`Alt-H` -- Restore Disabled Objects.


.. rubric:: Edit Mode

All Object Mode hotkeys except for Select All QCD Objects and the Disable Objects hotkeys.
(Only available if enabled in the preferences.)

- :kbd:`AccentGrave` -- Mesh Select Mode menu.

.. note::

   Slots with objects not in Object Mode can not be excluded.


Preferences
===========

Disable objects instead of hiding
   Replaces the object hiding hotkeys with hotkeys to disable objects instead and adds these options to
   the :menuselection:`Object --> Show/Hide` menu.

   Disabling objects prevents them from being shown again
   when a collection's exclude checkbox is toggled off and on,
   and so will preserve the object's visibility when switching QCD slots.

QCD
   Enable the QCD system.
QCD Hotkeys
   Enable 3D Viewport hotkeys in Object Mode.
QCD Edit Mode Hotkeys
   Enable 3D Viewport hotkeys in Edit Mode.

QCD Move Widget:
   Tool Theme Overrides
      Enable overrides in this section to change the color of individual elements
      in the QCD Move Widget (colors default to the current theme).

      Icon Alpha
         Opacity of the icons for selected (but not active) objects and unselected objects.

         .. note::

            The values for icon alpha are not overrides and always affect the QCD Move Widget.


Known Issues
============

- Linked collections are not supported.
- Two QCD slots can swap collections if the collections are under the same parent and
  you rename one collection with the name of the other, then undo the rename and redo the rename.


Glossary
========

General
   :Chaining: Dependent on parents for whether an RTO can be active.
   :QCD: Quick Content Display.
   :QVT: Quick View Toggles.
   :RTO: Restriction Toggle Option.

RTO Short Forms
   :EC: Exclude Checkbox. (Excludes the collection from the current view layer --
        affects both 3D Viewport and render -- non-chaining.)
   :SS: Selectability. (Disables selection for the collection in all view layers --
        affects 3D Viewport -- chaining.)
   :VV: Visibility. (Hides the collection from the current view layer -- affects 3D Viewport -- chaining.)
   :DV: Disable Viewports. (Disables the collection in all view layers -- affects 3D Viewport -- chaining.)
   :RR: Renderability. (Disables the collection from being rendered in all view layers --
        affects render -- chaining.)
   :HH: Holdout. (Masks out the collection from the view layer -- affects render -- non-chaining.)
   :IO: Indirect Only. (Makes the collection only contribute indirectly (shadows/reflections) to the render
        for the current view layer -- affects render -- non-chaining -- *Cycles only*.)

.. admonition:: Reference
   :class: refbox

   :Category:  Interface
   :Description: Collection management system.
   :Location: 3D Viewport
   :File: object_collection_manager folder
   :Author: Imaginer (Ryan Inch)
   :Maintainer: Imaginer
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
