
**********
Properties
**********

Active F-Curve
==============

.. reference::

   :Panel:     :menuselection:`Sidebar region --> F-Curve --> Active F-Curve`

.. figure:: /images/editors_graph-editor_fcurves_sidebar_curve_active-fcurve-panel.png

   Active F-Curve panel.

This panel displays properties for the active F-curve.

Channel Name
   ID Type + Channel name (X Location).

.. _bpy.types.FCurve.data_path:

Data Path
   RNA Path to property.

.. _bpy.types.FCurve.array_index:

RNA Array Index
   Index to the specific property affected by the F-curve if applicable.

.. _bpy.types.FCurve.color_mode:

Display Color
   The method used to determine the color of the F-curve shown in the Graph editor.

   :Auto Rainbow:
      Increment the hue of the F-curve color based on the channel index.
   :Auto XYZ to RGB:
      For property sets like location XYZ, automatically set the set of colors to red, green, blue.
   :User Defined:
      Define a custom color for the active F-curve.

.. _bpy.types.FCurve.auto_smoothing:

Handle Smoothing
   Selects the method used to compute :ref:`automatic Bézier handles <editors-graph-fcurves-settings-handles>`
   (*Automatic*, *Auto Clamped*, *Vector*).

   .. figure:: /images/editors_graph-editor_fcurves_sidebar_curve_auto-smoothing.png
      :align: center

      Handle smoothing mode comparison.

      Yellow: *None*, Cyan: *Continuous Acceleration*.
      From left to right, four *Auto Clamped* keys, one *Vector*, and the rest are *Automatic*.

   :None:
      Only directly adjacent key values are considered when computing the handles.
      Vector handles are pointed directly at the adjacent keyframes.

      This older method is very simple and predictable, but it can only produce
      truly smooth curves in the most trivial cases. Note the kinks in the yellow curve
      around the keys located between the extremes, and near the Vector handles.

   :Continuous Acceleration:
      A system of equations is solved in order to avoid or minimize jumps in acceleration
      at every keyframe. Vector handles are integrated into the curves as smooth transitions
      to imaginary straight lines beyond the keyframe.

      It produces much smoother curves out of the box, but necessarily means that
      any changes in the key values may affect interpolation over a significant stretch
      of the curve; although the amount of change decays exponentially with distance.
      This change propagation is stopped by any key with *Free*, *Aligned*, or *Vector*
      handles, as well as by extremes with *Auto Clamped* handles.

      The mode also tends to overshoot and oscillate more with fully *Automatic* handles
      in some cases (see the right end of the image above). So it is recommended to use
      *Auto Clamped* by default, and only switch to *Automatic* handles in places
      where this is desired behavior. That effect can also be reduced by adding in-between keys.

      .. tip::

         Considering the upsides and downsides of each mode, *Continuous Acceleration* should be
         better suited for limited animation, which uses a small number of interpolated keys with
         minimal manual polish. In case of highly polished high key rate animation, the benefits of
         smoothing may not outweigh the workflow disruption from more extensive change propagation.


Active Keyframe
===============

.. reference::

   :Panel:     :menuselection:`Sidebar region --> F-Curve --> Active Keyframe`

.. figure:: /images/editors_graph-editor_fcurves_sidebar_curve_active-keyframe-panel.png

   Active Keyframe panel.

.. _bpy.types.Keyframe.interpolation:
.. _editors-graph-fcurves-settings-interpolation:

Interpolation
   Mode for the :term:`Interpolation` between the current and next keyframe.


   .. rubric:: Interpolation

   :Constant:
      .. figure:: /images/editors_graph-editor_fcurves_introduction_constant.png
         :align: right
         :width: 300px

         Constant.

      There is no interpolation at all. The curve holds the value of its last keyframe,
      giving a discrete (stairway) "curve".
      Usually only used during the initial "blocking" stage in pose-to-pose animation workflows.

   :Linear:
      .. figure:: /images/editors_graph-editor_fcurves_introduction_linear.png
         :align: right
         :width: 300px

         Linear.

      This simple interpolation creates a straight segment, giving a non-continuous line.
      It can be useful when using only two keyframes and the *Extrapolation* extend mode,
      to easily get an infinite straight line (i.e. a linear curve).

   :Bézier:
      .. figure:: /images/editors_graph-editor_fcurves_editing_clean1.png
         :align: right
         :width: 300px

         Bézier.

      The more powerful and useful interpolation, and the default one.
      It gives nicely smoothed curves, i.e. smooth animations!

   .. note::

      Remember that some F-curves can only take discrete values,
      in which case they are always shown as if constant interpolated, whatever option you chose.


   .. rubric:: Easing (by strength)

   Different methods of easing interpolations for F-curve segment.
   The "Robert Penner easing equations" (basically, equations which define some preset ways that
   one keyframe transitions to another) which reduce the amount of manual work (inserting and tweaking keyframes)
   to achieve certain common effects. For example, snappy movements.

   - Linear
   - Sinusoidal
   - Quadratic
   - Cubic
   - Quartic
   - Quintic
   - Exponential
   - Circular

   .. seealso::

      For more info and a few live demos, see https://easings.net and
      http://robertpenner.com/easing/


   .. rubric:: Dynamic Effects

   These additional easing types imitate (fake) physics-based effects like bouncing/springing effects.
   The corresponding settings can be found in the :menuselection:`Sidebar region --> Active Keyframe panel`.

   :Back:
      Cubic easing with overshoot and settle.
      Use this one when you want a bit of an overshoot coming into the next keyframe,
      or perhaps for some wind-up anticipation.

      Back
         The back property controls the size and direction (i.e. above/below the curve) of the overshoot.

   :Bounce:
      Exponentially decaying parabolic bounce, like when objects collide.
      e.g. for Bouncing balls, etc.

   :Elastic:
      Exponentially decaying sine wave, like an elastic band.
      This is like bending a stiff pole stuck to some surface,
      and watching it rebound and settle back to its original state.

      Amplitude
         The amplitude property controls how strongly the oscillation diverges from the basic curve.
         At 0.0, there is no oscillation (i.e. it just snaps to the B-value like an extreme exponential transition),
         and at 1.0 a profile similar to the one shown in the icon occurs.
      Period
         The period property controls the frequency with which oscillations occur.
         Higher values result in denser oscillations.

.. _editors-graph-fcurves-settings-easing:

Easing
   The Easing Type controls which end of the segment between the two keyframes that the easing effects apply to.
   It has no effect if the :ref:`Interpolation Mode <editors-graph-fcurves-settings-interpolation>`
   is set to either *Constant*, *Linear*, or *Bézier*.

   :Automatic Easing:
      The most commonly expected of the below behaviors is used.
      For the transitional effects, this is basically *ease in*, while for the physics effects it is *ease out*.
   :Ease In:
      Effect builds up to the second keyframe.
   :Ease Out:
      Effect fades out from the first keyframe.
   :Ease In Out:
      Effect occurs on both ends of the segment.

.. _bpy.types.Keyframe.co_ui:

Key Frame
   Set the frame for the active keyframe.
Value
   Set the value for the active keyframe.

.. _bpy.types.Keyframe.handle_left_type:
.. _bpy.types.Keyframe.handle_right_type:
.. _editors-graph-fcurves-settings-handles:

Left/Right Handle Type
   When using Bézier-interpolated curves it is possible to control the slope of the curve at the control points.
   This is done via the curve point *handles*; you can set the type of handle to use
   for the curve points by pressing :kbd:`V` or choosing Key, Handle Type in the Graph editor menu.
   Each curve point can have a different handle type, even within the same curve.

   There are three automatic modes, *Automatic*, *Auto Clamped*, and *Vector*,
   where Blender automatically determines the curve's slope at each control point.
   The neighboring control points have the most influence of the slope,
   and points further away have a smaller influence. This can be controlled per F-curve with
   the :ref:`Auto Handle Smoothing <bpy.types.FCurve.auto_smoothing>` properties.

   By using the other, non-automatic modes, you have full manual control over the slope.

   :Automatic:
      .. figure:: /images/editors_graph-editor_fcurves_introduction_auto.png
         :align: right
         :width: 300px

         Auto handles.

      Handle positions are automatically chosen to produce smooth curves.

   :Auto Clamped:
      .. figure:: /images/editors_graph-editor_fcurves_introduction_autoclamped.png
         :align: right
         :width: 300px

         Auto clamped handles.

      Automatic handles clamped to prevent overshoots and
      changes in the curve direction between keyframes (S-shapes).

   :Vector:
      .. figure:: /images/editors_graph-editor_fcurves_introduction_vector.png
         :align: right
         :width: 300px

         Vector handles.

      Creates automatic linear interpolation between keyframes. The segments remain linear when
      keyframe centers are moved. However, when the handles are moved, the handle type switches to *Free*.

   :Aligned:
      .. figure:: /images/editors_graph-editor_fcurves_introduction_aligned.png
         :align: right
         :width: 300px

         Aligned handles.

      The two handles of the curve point are locked together to always point in exactly opposite directions.
      This results in a curve that is always smooth at the control point.

   :Free:
      .. figure:: /images/editors_graph-editor_fcurves_introduction_free.png
         :align: right
         :width: 300px

         Free handles.

      The handles can be moved completely independently, and thus can result in a sharp change of direction.


   .. _bpy.types.Keyframe.handle_left:
   .. _bpy.types.Keyframe.handle_right:

   Frame, Value
      Set the frame and value for the left/right interpolation handle for the active keyframe.
