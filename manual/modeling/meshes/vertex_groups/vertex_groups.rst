Vertex Groups
*************

.. figure:: /images/modeling_meshes_vgroups_01.jpg
   :figwidth: image
   :align: right

   The Vertex Group Panel

Vertex Groups are mainly used to tag the vertices belonging 
to parts of a Mesh Object or :term:`Lattice`. Think of the legs of a chair or 
the hinges of a door, or hands, arms, limbs, head, feet, etc. of a character. 
In addition you can assign different :guilabel:`weight values` 
(in the range [ 0.0, 1.0 ] ) to the vertices within a Vertex Group.
Hence Vertex Groups are sometimes also named :guilabel:`Weight Groups`.

Vertex Groups are most commonly used for Armatures
(See also :doc:`Skinning Mesh Objects </rigging/skinning/obdata>`).
But they are also used in many other areas of Blender, like for example:

- Shape keys
- Modifiers
- Particle Generators
- Physics Simulations

Many more usage scenarios are possible.
Actually you can use Vertex Groups for whatever makes sense to you.
In some contexts Vertex Groups can also be automatically generated
(i.e. for rigged objects). However in this section we will focus 
on manually created (user-defined) Vertex Groups.

.. admonition:: Vertex groups only apply to Mesh and Lattice Objects
   :class: note

   Any other Object type has no vertices, hence it can not have Vertex Groups.


Typical usage scenarios for Vertex groups
=========================================

**Skinning an armature**
   If you want to animate your mesh and make it move, you will 
   define an armature which consists of a bunch of bones.
   Vertex Groups are used to associate parts of the Mesh 
   to Bones of the Armature, where you can specify an influence
   :guilabel:`weight` in the range [0.0 ... 1.0] for each vertex
   in the Vertex Group.

**Working with Modifiers**
   Many modifiers contain the ability to control the modifier
   influence on each vertex separately.
   This is also done via Vertex Groups and the weight values 
   associated to the vertices.

**Quickly select/edit/hide parts of a mesh**
   By defining mesh regions with Vertex Groups you can easily 
   select entire parts of your mesh with 3 clicks and work
   on them in isolation without having to create separate objects. 
   With the hide function you can even remove a vertex
   group from the view (for later unhide).

**Cull out and duplicate parts of a mesh**
   Consider modeling a Lego block. The most simple brick consists
   of a base and a stud (the bump to connect the bricks together).
   To create a four-stud block, you would want to be able to 
   easily select the stud vertices, and, still in
   :guilabel:`Edit mode`, duplicate them and position them 
   where you want them.


Creating Vertex Groups
======================

.. figure:: /images/26-Manual-Modeling-Meshes-vertex-group-panel-empty.jpg
   :figwidth: image
   :align: right

   Empty Vertex Group Panel


Vertex Groups are maintained within the :guilabel:`Object Data Properties` window (1),
and there in the :guilabel:`Vertex Groups` panel.
As long as no Vertex groups are defined (the default for new Mesh Objects),
the Panel is empty (2).

You create a vertex group by :kbd:`lmb` :guilabel:`+` on the right Panel
border (3). Initially the group is named *Group*
(or *Group.nnn* when the name already exists) and gets displayed in the Panel (2)
(see next image).

Vertex Groups Panel Controls
----------------------------

.. figure:: /images/26-Manual-Modeling-Meshes-vertex-group-panel-one.jpg
   :figwidth: image
   :align: right

   One Vertex Group

Once a new Vertex Group has been added, the new Group appears in the
vertex Groups panel. There you find 3 clickable elements:

Group Name
~~~~~~~~~~

The Groupname can be changed by :kbd:`lmb-x2` on the name itself.
Then you can edit the name as you like.

Plus Icon
~~~~~~~~~

When the little icon in the left lower corner can be clicked, a new
row opens up where you can enter a search term. This becomes handy when
the number of vertex groups gets big.

Drag Handle
~~~~~~~~~~~

If you have a large number of vertex groups and you want to see more 
then a few Groups, you can  :kbd:`lmb` on the small drag handle to tear
the vertex groups list larger or smaller.

Active Group
~~~~~~~~~~~~

When a Vertex Group is created,
then it is also automatically marked as the :guilabel:`Active Group`.
This is indicated by setting the background of the panel entry 
to a light blue color. If you have two or more groups in the list, 
then you can change the active group by :kbd:`lmb` on the 
corresponding entry in the Vertex Group panel.


Deleting vertex Groups
======================

.. figure:: /images/26-Manual-Modeling-Meshes-vertex-group-panel-dg.jpg
   :figwidth: image
   :align: right

   Delete a Vertex Group

You delete a Vertex Group by first making it the active group
(select it in the panel) and then :kbd:`lmb` 
the :guilabel:`-` button at the right Panel border.

Deleting a Vertex Group only deletes the vertex assignments to the Group.
The vertices themselves are not deleted.


Locking Vertex Groups
=====================

.. figure:: /images/26-Manual-Modeling-Meshes-vertex-group-panel-lg.jpg
   :figwidth: image
   :align: right

   Lock a Vertex Group


Right after creation of a Vertex Group,
an open lock icon shows up on the right side of the Vertex Group List entry.
This icon indicates that the Vertex Group can be edited.
You can add vertex assignments to the group or remove assignments from the group.
And you can change it with the weight paint brushes, etc.

When you click on the icon,
it changes to a closed lock icon and all vertex group modifications get disabled.
You  can only rename or delete the group, and unlock it again.
No other operations are allowed on locked Vertex Groups,
thus all corresponding function buttons become disabled for locked Vertex Groups.


Working with Content of Vertex Groups
=====================================

.. figure:: /images/26-Manual-Modeling-Meshes-vertex-group-panel-one.jpg
   :figwidth: image
   :align: right

   Vertex Group Panel in Edit Mode


When you switch either to :guilabel:`Edit-Mode` 
or to :guilabel:`Weight-Paint` Vertex
Selection Mode, then the Vertex Group panel expands and displays 2 more rows:

The first row contains 4 buttons for maintaining the Assign- and 
Select- status of vertices of the active Vertex Group:


- **Assign** : To assign the Selected vertices to the Group with the weight as defined in the "Weight:" input field (see below)
- **Remove** : To Remove the selected vertices from the Group (and thus also delete their weight values)
- **Select** : To Select all vertices contained in the Group
- **Deselect** : To deselect all verts contained in the group

Below this row of buttons you see a numeric "Weight:" input field where you specify the weight
value that gets assigned to the selected verts when you press the Assign Button.


Assigning verts to a Group
--------------------------

.. figure:: /images/26-Manual-Modeling-Meshes-vertex-group-panel-assign.jpg
   :figwidth: image
   :align: right

   Assign weights to active group


You add vertices to a group as follows:

- Select the group from the group list, thus make it the Active Group (1).
- From the 3D Viewport select :kbd:`shift-rmb` all vertices that you want to add to the group.
- Set the weight value that shall be assigned to all selected verts (2).
- :kbd:`lmb` the :guilabel:`Assign` button to assign the selected verts to the active group using the given weight (3).

Note that weight Assignment is not available for locked Vertex Groups.
The Assign button is grayed out in that case.


.. note:: Assign is additive

   The :guilabel:`Assign` button only adds the currently 
   selected vertices to the active group. Vertices already 
   assigned to the group are not removed from the group.

   Also keep in mind that a vertex can be assigned to multiple groups.


Checking assignments
--------------------

To be sure the selected verts really have been added to the Vertex Group,
you can try the deselect button. If the verts do not get deselected,
then you probably forgot to hit the :guilabel:`Assign` button. 
But you can do that safely now.
But remind:
All selected verts get the weight assigned as displayed in the "Weight:" input field!


Removing assignments from a Group
---------------------------------

You remove vertices from a group as follows:

- Select the group from the group list (make it the active group).
- :kbd:`shift-rmb` all vertices that you want to remove from the group.
- :kbd:`lmb` click the :guilabel:`Remove` button.

Note that Removing weight Assignments is not available for locked Vertex Groups.
The Remove button is grayed out in that case.


Using groups for Selecting/Deselecting
--------------------------------------

You can quickly select all assigned vertices of a group:

- (optionally) press :kbd:`A` once or twice to unselect all vertices.
- Select the group from the group list (make it the active group).
- When you now :kbd:`lmb` click the :guilabel:`Select` button, then the vertices assigned to the active group will be selected and highlighted in the 3D Viewport.
- When you :kbd:`lmb` click the :guilabel:`Deselect` button instead, then the vertices assigned to the active group will be deselected in the 3D Viewport.


.. note:: Selecting/Deselecting is additive

   If you already have verts selected in the 3D View,
   then selecting the verts of a group will add the verts 
   but also keep the already-selected verts selected. 
   Vice versa, deselecting the verts of a vertex group 
   will only deselect the verts assigned to the group 
   and keep all other verts selected.


Finding ungrouped verts
-----------------------

You can find ungrouped vertices as follows:

- Press :kbd:`A` once or twice to unselect all vertices.
- In the footer of the 3D Viewport: Navigate to Select → Ungrouped verts


Keyboard Shortcuts
------------------

.. figure:: /images/26-Manual-Modeling-Meshes-vertex-group-popup.jpg
   :figwidth: image
   :align: right

   Vertex Groups popup menu


In Edit Mode you can type :menuselection:`[ctrl][G]` to a shortcut Menu for adding/removing
verts to/from groups.
The popup menu provides the following functions with obvious functionality:


- Assign to New Group
- Assign to Active Group
- Remove from Active Group
- Remove from All

The following functions should not be located here and might be removed in a future version of
Blender:


- Set Active Group
- Set Remove Acive Group
- Set Remove All Groups


Vertex Group Management
=======================

.. figure:: /images/26-Manual-Modeling-Meshes-vertex-group-pulldown.jpg
   :figwidth: image
   :align: right

   Vertex groups panel's dropdown menu


Vertex Groups provide a more complex set of functions 
inside a Pull down menu. This menu is accessible 
from the Vertex Group Panel by clicking on the 
dark gray :guilabel:`arrow down` icon on the right panel border.

The following functions of the Pulldown Menu operate on the assigned vertices:

:guilabel:`Sort Vertex Groups`:
   Sorts Vertex Groups Alphabetically
:guilabel:`Copy Vertex Group`:
   Add a Copy of the active Vertex Group as a new Group.
   The new group will be named like the original group with "_copy" appended at the end of its name.
   And it will contain associations to exactly the same verts with the exact same weights as in the source vertex group.
:guilabel:`Copy Vertex Groups to Linked`:
   Copy Vertex Groups of this Mesh to all linked Objects which use the same mesh data (all users of the data).
:guilabel:`Copy Vertex Group to Selected`:
   Copy all Vertex Groups to other Selected Objects provided they have matching indices
   (typically this is true for copies of the mesh which are only deformed and not otherwise edited).
:guilabel:`Mirror Vertex Group`:
   Mirror all Vertex Groups, flip weights and/or names, editing only selected vertices,
   flipping when both sides are selected; otherwise copy from unselected.
   Note this function will be reworked (and fully documented) in a future release.
:guilabel:`Remove from All Groups`:
   (not available for locked groups) Unassign the selected Vertices from all groups.
   After this operation has been performed, the verts will no longer be contained in any vertex group.
:guilabel:`Clear Active group` (not available for locked groups):
   Remove all assigned vertices from the active Group. The group is made empty.
   Note that the vertices may still be assigned to other Vertex Groups of the Object.
:guilabel:`Delete All Groups`:
   Remove all Vertex Groups from the Object.

The following functions operate only on the lock state settings:

:guilabel:`Lock All`
   Lock all groups
:guilabel:`Unlock All`
   Unlock all groups
:guilabel:`Lock_Invert All`
   Invert Group Locks


Hints
=====

- Multiple objects sharing the same mesh data have the 
  peculiar property that the group names are stored on the object,
  but the weights in the mesh. This allows you to name groups 
  differently on each object, but take care because removing a 
  vertex group will remove the group from all objects sharing this mesh.
