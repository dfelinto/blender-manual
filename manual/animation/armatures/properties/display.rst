
**********************
Viewport Display Panel
**********************

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Panel:     :menuselection:`Armature --> Viewport Display`

.. TODO2.8
   .. figure:: /images/animation_armatures_properties_display_panel.png

      The Display panel.

Display As
   This controls the way the bones appear in the 3D Viewport; you have four different visualizations you can select.

   .. list-table::

      * - .. figure:: /images/animation_armatures_properties_display_octahedral.png
             :width: 320px

             Octahedral bone display.

        - .. figure:: /images/animation_armatures_properties_display_stick.png
             :width: 320px

             Stick bone display.

      * - .. figure:: /images/animation_armatures_properties_display_b-bone.png
             :width: 320px

             B-Bone bone display.

        - .. figure:: /images/animation_armatures_properties_display_envelope.png
             :width: 320px

             Envelope bone display.

   Octahedral
      This is the default visualization, well suited for most of editing tasks. It materializes:

      - The bone root ("big" joint) and tip ("small" joint).
      - The bone "size" (its thickness is proportional to its length).
      - The bone roll (as it has a square section).

      .. figure:: /images/animation_armatures_properties_display_type-octahedral.png
         :width: 300px

         Note the 40° rolled Bone.001 bone.

   Stick
      This is the simplest and most non-intrusive visualization.
      It just materializes bones by sticks of constant (and small) thickness,
      so it gives you no information about root and tip, nor bone size or roll angle.

      .. figure:: /images/animation_armatures_properties_display_type-stick.png
         :width: 300px

         Note that Bone.001 roll angle is not visible (except by its XZ axes).

   B-Bone
      This visualization shows the curves of "smooth" multi-segmented bones;
      see the :doc:`/animation/armatures/bones/properties/bendy_bones` for details.

      .. list-table::

         * - .. figure:: /images/animation_armatures_bones_properties_bendy-bones_b-bones-1.png
                :width: 320px

                An armature of B-Bones, in Edit Mode.

           - .. figure:: /images/animation_armatures_bones_properties_bendy-bones_b-bones-3.png
                :width: 320px

                The same armature in Object Mode.

   Envelope
      This visualization materializes the bone deformation influence.
      More on this in the :ref:`bone page <armature-bone-influence>`.

      .. figure:: /images/animation_armatures_bones_structure_envelope-pose-mode.png
         :width: 300px

   Wire
      This simplest visualization shows the curves of "smooth" multi-segmented bones.

      .. list-table::

         * - .. figure:: /images/animation_armatures_properties_display_type-wire-pose-mode.png
                :width: 320px

                An armature of Wire, in Pose Mode.

           - .. figure:: /images/animation_armatures_properties_display_type-wire-edit-mode.png
                :width: 320px

                The same armature in Edit Mode.

Show
   Names
      Displays the name of each bone.
   Shapes
      When enabled, the default standard bone shape is replaced,
      in *Object Mode* and *Pose Mode*, by the shape of a chosen object
      (see :doc:`Shaped Bones </animation/armatures/bones/properties/display>` for details).
   Group Colors
      Use the Bone Group colors to color the bone.
      For more details see :doc:`Bone Groups </animation/armatures/properties/bone_groups>`.
   In Front
      When enabled, the bones of the armature will always be shown on top of
      the solid objects (meshes, surfaces, ...). I.e. they will always be visible and selectable
      (this is the same option as the one found in the *Display* panel of the *Object data* tab).
      Very useful when not in *Wireframe* mode.

.. _bpy.types.Armature.show_axes:

Axis
   When enabled, the (local) axes of each bone are displayed (only relevant for *Edit Mode* and *Pose Mode*).

   Position
      The position for the axes display on the bone.
      Increasing the value moves it closer to the tip; decreasing moves it closer to the root.
