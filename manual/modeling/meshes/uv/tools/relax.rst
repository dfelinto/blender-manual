
*****
Relax
*****

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Relax`

The Relax brush can be used to distribute UVs more evenly.
It works by pulling vertices along UV edges to bring the UV unwrap into balance.

The Relax brush can be compared with the :ref:`minimize-stretch` tool which works directly
on faces to reduce texture stretching and shearing.
You may find that sometimes minimize stretch works better, sometimes the unwrap
tool and other times the relax brush.

First using Unwrap, then Minimize Stretch and touching up with the Relax Brush often gives the best results.
Remember, you can use "Undo" at any time to return to an earlier state.


Tool Settings
=============

Brushes
-------

Brushes
   The :ref:`ui-data-block` to select a preset brush type or a custom brush.


Brush Settings
--------------

Radius
   This option controls the radius of the brush, measured in pixels.
   :kbd:`F` allows you to change the brush size interactively by dragging the mouse and then :kbd:`LMB`.
   Typing a number then enter while using :kbd:`F` allows you to enter the size numerically.

   Size Pressure
      Brush size can be affected by enabling the pressure sensitivity icon,
      if you are using a :ref:`Graphics Tablet <hardware-tablet>`.
   Use Unified Radius
      Use the same brush *Radius* across all brushes.

Strength
   Controls how much each application of the brush affects the UVs.
   You can change the brush strength interactively by pressing :kbd:`Shift-F`
   in the 3D Viewport and then moving the brush and then :kbd:`LMB`.
   You can enter the size numerically also while in :kbd:`Shift-F` sizing.

   Use Unified Strength
      Use the same brush *Strength* across all brushes.

.. _bpy.types.ToolSettings.uv_relax_method:

Relaxation Method
   There are three ways to determine the edge weighting:

   :Laplacian:
     The classic discrete laplace operator applied to the UV graph. Each edge has equal weighting,
     resulting in triangles which resemble a honeycomb shape, or quads aligned into square grid.
   :HC:
     Similar to Laplacian, the HC method uses equal weighting while trying to preserve
     a gradient between dense regions of the mesh and regions with fewer edges.e

     Note, this method uses the The "Humphrey's Classes" operator as described in the paper:
     `"Improved Laplacian Smoothing of Noisy Surface Meshes"
     <http://informatikbuero.com/downloads/Improved_Laplacian_Smoothing_of_Noisy_Surface_Meshes.pdf>`
   :Geometry:
     Edges are weighted according to the discrete laplace operator (cotangent formula) applied to the 3D geometry.
     This tries to bring the relative lengths of edges in UV closer to the relative lengths of edges in 3D,
     resulting in a UV unwrap with less distortion across edge boundaries.

.. note::

   All brushes use the :doc:`Airbrush Stroke Method </sculpt_paint/brush/stroke>`;
   they continue to act as long as you keep :kbd:`LMB` pressed.


Falloff
^^^^^^^

The Falloff allows you to control the *Strength* falloff of the brush.
See :doc:`Painting Falloff </sculpt_paint/brush/falloff>` for more information.


Options
-------

.. reference::

   :Mode:      Edit Mode
   :Panel:     :menuselection:`Sidebar --> Tool --> Options`

When UV sculpting is activated, the Sidebar shows the brush tool selection and options.

Lock Borders
   Locks the boundary of UV islands from being affected by the brush.
   This is useful to preserve the shape of UV islands.
Sculpt All Islands
   To edit all islands and not only the island nearest to the brush center
   when the sculpt stroke was started.
Display Cursor
   Hides the sculpt cursor.
