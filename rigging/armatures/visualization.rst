


Armature visualization
======================

We have 4 basic bone visualization: Octahedral, Stick, B-Bone, Envelope and Wire:


.. figure:: /images/Man2.5RiggingBonePrincipalsBoneDisplayOctahedral.jpg
   :width: 300px
   :figwidth: 300px

   Octahedral bone display.


.. figure:: /images/Man2.5RiggingBonePrincipalsBoneDisplayStick.jpg
   :width: 300px
   :figwidth: 300px

   Stick bone display.


.. figure:: /images/Man2.5RiggingBonePrincipalsBoneDisplayBBone.jpg
   :width: 300px
   :figwidth: 300px

   B-Bone bone display.


.. figure:: /images/Man2.5RiggingBonePrincipalsBoneDisplayEnvelope.jpg
   :width: 300px
   :figwidth: 300px

   Envelope bone display.


Display Panel
=============


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object`\ , :guilabel:`Edit` and :guilabel:`Pose` modes
   | Panel:    :guilabel:`Display` :guilabel:`Object Data` context


But let's first see some general visualization properties of armatures,
found in the :guilabel:`Display` panel of the :guilabel:`Object data` context.


.. figure:: /images/Man2.5RiggingEditingObjectDataPropertyCxtDisplayPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Display panel.


Bone types
----------


.. figure:: /images/ManRiggingOctahedronEx3DViewEditMode.jpg
   :width: 250px
   :figwidth: 250px

   A basic armature in Octahedron visualization, Edit mode.

   Note the 40- rolled Bone.001 bone.


Octahedral bone
~~~~~~~~~~~~~~~


This is the default visualization, well suited for most of editing tasks. It materializes:

- The bone root ("big" end) and tip ("small" end).
- The bone "size" (its thickness is proportional to its length).
- The bone roll (as it has a square section).


.. figure:: /images/ManRiggingStickEx3DViewPoseMode.jpg
   :width: 250px
   :figwidth: 250px

   The same armature in Stick visualization, Pose mode.
   Note that Bone.001 roll angle is not visible (except by its XZ axes).


Stick bone
~~~~~~~~~~


This is the simplest and most non-intrusive visualization.
It just materializes bones by sticks of constant (and small) thickness,
so it gives you no information about root and tip, nor bone size or roll angle.


.. figure:: /images/ManRiggingBBoneEx3DViewEditMode.jpg
   :width: 250px
   :figwidth: 250px

   The same armature in B-Bone visualization, Edit mode.


B-Bone bone
~~~~~~~~~~~


This visualization shows the curves of "smooth" multi-segmented bones; see the :doc:`bone page <rigging/armatures/bones#bones_rigidity>` for details.


.. figure:: /images/ManRiggingEnvelopeEx3DViewPoseMode.jpg
   :width: 250px
   :figwidth: 250px

   The Bone Groups panel.


Envelope bone
~~~~~~~~~~~~~


This visualization materializes the bone deformation influence. More on this in the :doc:`bone page <rigging/armatures/bones#bones_influence>`\ .


Attributes
----------

:guilabel:`Names`
   When enabled, the name of each bone is drawn.

:guilabel:`Colors`
   This is only relevant for :guilabel:`Pose` mode, and is described in detail :doc:`there <rigging/posing/visualization>`\ .


:guilabel:`Axes`
   When enabled, the (local) axes of each bone are drawn (only relevant for :guilabel:`Edit` and :guilabel:`Pose` modes).

:guilabel:`X-Ray`
   When enabled, the bones of the armature will always be drawn on top of the solid objects (meshes, surfaces, …) - i.e. they will always be visible and selectable (this is the same option as the one found in the :guilabel:`Display` panel of the :guilabel:`Object data` context. Very useful when not in :guilabel:`Wireframe` mode.

:guilabel:`Shapes`
   When enabled, the default standard bone shape is replaced, in :guilabel:`Object` and :guilabel:`Pose` modes, by the shape of a chosen object (see
FIXME(TODO: Internal Link;
[[#Shaped Bones|below]]
) for details).

:guilabel:`Delay Refresh`
   When enabled, the bone doesn't deform its children when manipulating the bone in pose mode.


Shaped Bones
------------


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` and :guilabel:`Pose` modes
   | Panel:    :guilabel:`Display` panel from :guilabel:`Bone` context.


Blender allows you to give to each bone of an armature a specific shape
(in :guilabel:`Object` and :guilabel:`Pose` modes), using another object as "template".
First of all, you have to enable the :guilabel:`Shapes` button (\ :guilabel:`Armature` panel).


.. figure:: /images/Man2.5RiggingEditingBoneCxtDisplayPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Display panel.


Attributes
~~~~~~~~~~

:guilabel:`Wireframe`
   When enabled, bone is displayed in wireframe mode regardles of the viewport drawing mode. Useful for non-obstructive custom bone chains.

:guilabel:`Hide`
   Bone is not visible when not in :guilabel:`Edit mode`\ .

:guilabel:`Custom Shape`
   Object that defines the custom shape of the selected bone.

:guilabel:`Custom At`
   Bone that defines the display transform of this shape bone


To assign a custom shape to a bone, you have to:

- Switch to :guilabel:`Pose` mode (\ :kbd:`ctrl-Tab`\ ).
- Select the relevant bone (\ :kbd:`rmb` click on it).
- Go to the :guilabel:`Display` panel :guilabel:`Custom Shape` field and select the 3D object previously created in the scene; in this example we are using a cube and a cone. Tou can optionally set the :guilabel:`At` field to another bone.


.. figure:: /images/Man2.5RiggingEditingBoneCxtDisplayPanel2.jpg
   :width: 250px
   :figwidth: 250px

   The Display panel.


.. figure:: /images/ManRiggingBoneShapeEx3DViewObjectMode.jpg
   :width: 300px
   :figwidth: 300px

   The armature with shapes assigned to two bones, in Object mode.
   Note the centers of the Cone and Cube objects.


.. figure:: /images/ManRiggingBoneShapeEx3DViewPoseMode.jpg
   :width: 300px
   :figwidth: 300px

   The same armature in Pose mode…


Note that:

- These shapes will never be rendered - like any bone, they are only visible in 3D views.
- Even if any type of object seems to be accepted by the :guilabel:`OB` field (meshes, curves, even metas…), only meshes really work - all other types just make the bone invisible; nothing is drawn…
- The center of the shape object will be at the *root of the bone* (see the :doc:`bone page <rigging/armatures/bones>` for root/tip).
- The object properties of the shape are ignored (i.e. if you make a parallelepiped out of a cube by modifying its dimensions in :guilabel:`Object` mode, you'll still have a cube shaped bone…).
- The "along bone" axis is the Y one, and the shape object is always scaled so that one Blender Unit stretches along the whole bone length.
- If you need to remove the custom shape of the bone, just right click in the :guilabel:`Custom Shape` field and select :guilabel:`Reset to default value` in the popup menu.

So to summarize all this, you should use meshes as shape objects,
with their center at their lower-Y end, and an overall Y length of **1.0** BU.


Armature Layers
===============


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object`\ , :guilabel:`Edit` and :guilabel:`Pose` modes
   | Panel:    :guilabel:`Skeleton` panel, :guilabel:`Object data` context


.. figure:: /images/Man2.5RiggingEditingObjectDataPropertyCxtSkeletonPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Skeleton panel.


Each armature has 32 "Armature layers" which allow you to organize your armature by
"regrouping" sets of bones into layers; this works similar to scene layers
(those containing your objects). You can then "move" a bone to a given layer,
hide or show one or several layers, etc.


Showing/hiding bone layers
--------------------------


Only bones in active layers will be visible/editable - but they will always be effective
(i.e move objects or deform geometry), whether in an active layer or not. To
(de)activate a layer, you have several options, depending in which mode you are in:

- In all modes, use the row of small buttons at the top of the :guilabel:`Display Options` group, :guilabel:`Armature` panel. If you want to enable/disable several layers at once, as usual, hold :kbd:`shift` while clicking…
- In :guilabel:`Edit` and :guilabel:`Pose` modes, you can also do this from the :guilabel:`3D View`\ s, either by using the menu (\ :menuselection:`Armature --> Switch Armature Layers` or :menuselection:`Pose --> Switch Armature Layers`\ ), or the :kbd:`shift-M` shortcut, to display a small pop-up dialog containing the same buttons as described above (here again, you can use :kbd:`shift-lmb` clicks to (de)select several layers at once).


Protected Layers
----------------

You can lock a given bone layer for all :doc:`proxies <data_system/linked_libraries#proxy_objects>` of your armature, i.e. all bones in this layer won't be editable. To do so, in the :guilabel:`Skeleton` panel, :kbd:`ctrl-lmb` click on the relevant button, the layer lock will be enabled.

Protected layers in proxy are restored to proxy settings on file reload and undo.


Bone Layers
===========


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object`\ , :guilabel:`Edit` and :guilabel:`Pose` modes
   | Panel:    :guilabel:`Relations` panel :guilabel:`Bone` context


.. figure:: /images/Man2.5RiggingEditingBoneCxtRelationsPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Relations panel.


Moving bones between layers
---------------------------


Obviously, you have to be in :guilabel:`Edit` or :guilabel:`Pose` modes to move bones between
layers - note that as with objects, bones can lay in several layers at once,
just use the usual :kbd:`shift-lmb` clicks… First of all,
you have to select the chosen bone(s)!

- In the :guilabel:`Button` window, use the "layer buttons" of each selected bone "sub-panel" (\ :guilabel:`Armature Bones` panel) to control in which layer(s) it lays.
- In the :guilabel:`3D View` window, use the menu (\ :menuselection:`Armature --> Move Bone To Layer` or :menuselection:`Pose --> Move Bone To Layer`\ ) or hit :kbd:`M` to show the usual pop-up layers dialog. Note that this way, *you assign the same layers to all selected bones*\ .


Hiding Bones
============


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` and :guilabel:`Pose` modes
   | Panel:    :guilabel:`Display` panel, :guilabel:`Bone` context


.. figure:: /images/Man2.5RiggingEditingBoneCxtDisplayPanel.jpg
   :width: 250px
   :figwidth: 250px

   The Display panel.


You do not have to use bone layers to show/hide some bones. As with objects,
vertices or control points, you can use the :kbd:`H` key:

- :kbd:`H` will hide the selected bone(s).
- :kbd:`shift-H` will hide all bones *but the selected one(s)*\ .
- :kbd:`alt-H` will show all hidden bones.

You can also use the :guilabel:`Hide` check button of the :guilabel:`Display` panel,
:guilabel:`Bone` context).

Note that hidden bones are specific to a mode - i.e.
you can hide some bones in :guilabel:`Edit` mode,
they will still be visible in :guilabel:`Pose` mode, and vice-versa.
Hidden bone in :guilabel:`Pose` mode are also invisible in :guilabel:`Object` mode.
And in :guilabel:`Edit` mode, the bone to hide must be fully selected,
not just his root or tip…


