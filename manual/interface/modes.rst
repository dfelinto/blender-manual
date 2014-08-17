
Modes
*****

*Modes* are a Blender-level object-oriented feature, which means that *the whole Blender application* is always in *one and only one mode*, and that the available modes vary depending on the selected active object's type - most of them only enable the default :guilabel:`Object` mode (like cameras, lamps, etc.). Each mode is designed to edit an aspect of the selected object. See the *Blender's Modes* table below for details.


.. figure:: /images/2.6_ModeSelect.jpg

   Mode selection example (mesh object).


You set the current mode in the :guilabel:`Mode` drop-down list of :guilabel:`3D View` header
(see *Mode selection example (mesh object)*).


 .. warning::

   FIXME - warning body below

You can only select objects in :guilabel:`Object` mode. In all others, the current object selection is "locked" (except, to some extent, with an armature's :guilabel:`Pose` mode).

Modes might affect many things in Blender:

- They can modify the panels and/or controls available in some :guilabel:`Buttons` windows' contexts.
- They can modify the behavior of whole windows, like e.g. the :guilabel:`UV/Image Editor` window (and obviously, :guilabel:`3D View` s!).
- They can modify the available header tools (menus and/or menu entries, as well as other controls...). For example, in the :guilabel:`3D View` window, the :guilabel:`Object` menu in :guilabel:`Object` mode changes to a :guilabel:`Mesh` menu in :guilabel:`Edit` mode (with an active mesh object!), and a :guilabel:`Paint` menu in :guilabel:`Vertex Paint` mode...


+--------------------------------------------+------------------------------+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+**Blender's Modes**                                                                                                                                                                                                                                                                                               +
+--------------------------------------------+------------------------------+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+Icon                                        |Name                          |Shortcut                 |Remarks                                                                                                                                                                                                     +
+--------------------------------------------+------------------------------+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+.. figure:: /images/2.6_IconObjectMode.jpg  |:guilabel:`Object` mode       |*None* :sup:`1`          |The default mode, available for all object types, as it is dedicated to :guilabel:`Object` datablock editing (i.e. position/rotation/size).                                                                 +
+--------------------------------------------+------------------------------+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+.. figure:: /images/2.6_IconEditMode.jpg    |:guilabel:`Edit` mode         |:kbd:`tab`:sup:`1`       |A mode available for all renderable object types, as it is dedicated to their "shape" :guilabel:`ObData` datablock editing (i.e. vertices/edges/faces for meshes, control points for curves/surfaces, etc.).+
+--------------------------------------------+------------------------------+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+.. figure:: /images/2.6_IconSculptMode.jpg  |:guilabel:`Sculpt` mode       |*None* :sup:`1`          |A mesh-only mode, that enables Blender's mesh 3D-sculpting tool.                                                                                                                                            +
+--------------------------------------------+------------------------------+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+.. figure:: /images/2.6_IconVertexPaint.jpg |:guilabel:`Vertex Paint` mode |*None* :sup:`1`          |A mesh-only mode, that allows you to set your mesh's vertices colors (i.e. to "paint" them).                                                                                                                +
+--------------------------------------------+------------------------------+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+.. figure:: /images/2.6_IconTexturePaint.jpg|:guilabel:`Texture Paint` mode|*None* :sup:`1`          |A mesh-only mode, that allows you to paint your mesh's texture directly on the model, in the 3D views.                                                                                                      +
+--------------------------------------------+------------------------------+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+.. figure:: /images/2.6_IconWeightPaint.jpg |:guilabel:`Weight Paint` mode |:kbd:`ctrl-tab`:sup:`2`  |A mesh-only mode, dedicated to vertex group weighting.                                                                                                                                                      +
+--------------------------------------------+------------------------------+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+.. figure:: /images/2.6_IconParticleMode.jpg|:guilabel:`Particle` mode     |*None* :sup:`1`          |A mesh-only mode, dedicated to particle systems, useful with editable systems (hair).                                                                                                                       +
+--------------------------------------------+------------------------------+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+.. figure:: /images/2.6_IconPoseMode.jpg    |:guilabel:`Pose` mode         |:kbd:`ctrl-tab`:sup:`2`  |An armature-only mode, dedicated to armature posing.                                                                                                                                                        +
+--------------------------------------------+------------------------------+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Notes about modes shortcuts:

- :kbd:`tab` toggles :guilabel:`Edit` mode.
- :kbd:`ctrl-tab` switches between the :guilabel:`Weight Paint` (meshes)/\ :guilabel:`Pose` (armatures) modes, and the other current one (by default, the :guilabel:`Object` mode). However, the same shortcut has other, internal meanings in some modes (e.g. in :guilabel:`Sculpt` mode, it is used to select the current brush)...

As you can see, using shortcuts to switch between modes can become quite tricky,
especially with meshes...

We won't detail further more modes' usages here. Most of them are tackled in the :doc:`modeling chapter <modeling>`, as they are mainly related to this topic. The :guilabel:`Particle` mode is discussed in the :doc:`particle section <physics/particles/mode>`, and the :guilabel:`Pose` and :guilabel:`Edit` modes for armatures, in the :doc:`rigging one <rigging>`.


.. admonition:: Note
   :class: note

   If you are reading this manual and some button or menu option is referenced that does not appear on your screen, it may be that you are not in the proper mode for that option to be valid.


