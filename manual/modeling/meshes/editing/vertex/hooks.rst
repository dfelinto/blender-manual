.. _bpy.ops.object.hook:
.. _bpy.ops.object.hook_add_selob:

*****
Hooks
*****

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Hooks`
   :Hotkey:    :kbd:`Ctrl-H`

Adds a :doc:`Hook Modifier </modeling/modifiers/deform/hooks>`
(using either a new empty, or the current selected object) linked to the selection.
Note that even if it appears in the history menu,
this action cannot be undone in *Edit Mode* -- because it involves other objects...

When the current object has no hooks associated, only the first two options will appear on the menu.

Hook to New Object
   Creates a new Hook Modifier for the active object and assigns it to the selected vertices;
   it also creates an empty at the center of those vertices, which are hooked to it.
Hook to Selected Object
   Does the same as *Hook to New Object*, but instead of hooking the vertices to a new empty,
   it hooks them to the selected object (if it exists).
   There should be only one selected object (besides the mesh being edited).
Hook to Selected Object Bone
   Does the same as *Hook to New Object*,
   but it sets the last selected bone in the also selected armature as a target.
Assign to Hook
   The selected vertices are assigned to the chosen hook. For that to happen,
   a list of the hooks associated to the object is displayed.
   All the unselected vertices are removed from it (if they were assigned to that particular hook).
   One vertex can be assigned to more than one hook.
Remove Hook
   Removes the chosen hook (from the displayed list) from the object.
   Which means that the specific Hook Modifier is removed from its modifier stack.
Select Hook
   Selects all vertices assigned to the chosen hook (from the hook list).
Reset Hook
   It's equivalent to the *Reset* button of the specific Hook Modifier (chosen from the hook list).
Recenter Hook
   It's equivalent to the *Recenter* button of the specific Hook Modifier (chosen from the hook list).
