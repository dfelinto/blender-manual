.. _bpy.types.ObjectLineArt:

********
Line Art
********

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Panel:     :menuselection:`Properties --> Object Properties --> Line Art`

The *Line Art* panel is used to enable extra display options for customizing
line art rendering for a specific object.

.. figure:: /images/scene-layout_object_properties_line-art_panel.png

   Line Art panel.

.. _bpy.types.ObjectLineArt.usage:

Usage
   How the object is loaded into line art.
   This property overrides the parent collection's :ref:`scene_layout-collections-line-art` usage.

   :Inherit:
      No special loading strategy for line art.
      Loading of the object is controlled by parent collection's line art settings.
   :Include:
      Force include the object into line art calculation
      even if its parent collection specifies otherwise.
   :Intersection Only:
      The object will only produce intersection lines in the scene and its own geometry stays invisible.
   :Occlusion Only:
      The object will only cause occlusion to existing feature lines and its geometry stays invisible.
   :Exclude:
      The object will not be loaded into line art at all.
   :No Intersection:
      The object will not generate intersection lines on itself or with other objects in scene.

.. _bpy.types.ObjectLineArt.use_crease_override:

Override Crease
   Allows the object to have a different crease value than the global one set in the line art modifier.

   .. _bpy.types.ObjectLineArt.crease_threshold:

   Crease
      Override crease value for the object.
