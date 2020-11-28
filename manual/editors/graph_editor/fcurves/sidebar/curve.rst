
*******
F-Curve
*******

Active F-Curve
==============

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar region --> F-Curve --> Active F-Curve`

.. figure:: /images/editors_graph-editor_fcurves_properties_active-fcurve-panel.png

   Active F-Curve panel.

This panel displays properties for the active F-curve.

Channel Name
   ID Type + Channel name (X Location).
RNA Path
   RNA Path to property.
RNA Array Index
   Index to the specific property affected by the F-curve if applicable.
Display Color
   The method used to determine the color of the F-curve shown in the Graph editor.

   Auto Rainbow
      Increment the hue of the F-curve color based on the channel index.
   Auto XYZ to RGB
      For property sets like location XYZ, automatically set the set of colors to red, green, blue.
   User Defined
      Define a custom color for the active F-curve.

.. _graph_editor-auto-handle-smoothing:

Handle Smoothing
   Selects the method used to compute :ref:`automatic Bézier handles <editors-graph-fcurves-settings-handles>`
   (*Automatic*, *Auto Clamped*, *Vector*).

   .. figure:: /images/editors_graph-editor_fcurves_properties_auto-smoothing.png
      :align: center

      Handle smoothing mode comparison. Yellow: *None*, Cyan: *Continuous Acceleration*.

      From left to right, four *Auto Clamped* keys, one *Vector*, and the rest are *Automatic*.

   None
      Only directly adjacent key values are considered when computing the handles.
      Vector handles are pointed directly at the adjacent keyframes.

      This older method is very simple and predictable, but it can only produce
      truly smooth curves in the most trivial cases. Note the kinks in the yellow curve
      around the keys located between the extremes, and near the Vector handles.

   Continuous Acceleration
      A system of equations is solved in order to avoid or minimize jumps in acceleration
      at every keyframe. Vector handles are integrated into the curves as smooth transitions
      to imaginary straight lines beyond the keyframe.

      This produces much smoother curves out of the box, but necessarily means that
      any changes in the key values may affect interpolation over a significant stretch
      of the curve; although the amount of change decays exponentially with distance.
      This change propagation is stopped by any key with *Free*, *Aligned*, or *Vector*
      handles, as well as by extremes with *Auto Clamped* handles.

      This mode also tends to overshoot and oscillate more with fully *Automatic* handles
      in some cases (see the right end of the image above), so it is recommended to use
      *Auto Clamped* by default, and only switch to *Automatic* handles in places where this
      is desired behavior. This effect can also be reduced by adding in-between keys.

      .. tip::

         Considering the upsides and downsides of each mode, *Continuous Acceleration* should be
         better suited for limited animation, which uses a small number of interpolated keys with
         minimal manual polish. In case of highly polished high key rate animation, the benefits of
         smoothing may not outweigh the workflow disruption from more extensive change propagation.


Active Keyframe
===============

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar region --> F-Curve --> Active Keyframe`

.. figure:: /images/editors_graph-editor_fcurves_properties_active-keyframe-panel.png

   Active Keyframe panel.

Interpolation
   Set the forward :ref:`editors-graph-fcurves-settings-interpolation` for the active keyframe.
Key Value
   Set the value for the active keyframe.
Frame
   Set the frame for the active keyframe.
Left/Right Handle Frame/Value
   Set the position of the left/right interpolation handle for the active keyframe.

   Type
      See :ref:`editors-graph-fcurves-settings-handles`.
