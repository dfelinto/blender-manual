.. _render-cycles-settings-object-subdivision:
.. _bpy.types.CyclesObjectSettings.use_adaptive_subdivision:
.. _bpy.types.CyclesObjectSettings.dicing_rate:

********************
Adaptive Subdivision
********************

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Modifier --> Subdivision Surface`

.. note::

   Implementation not finished yet, marked as an :ref:`Experimental Feature Set <cycles-experimental-features>`.

When using the *Experimental Feature Set*
the :doc:`Subdivision Surface Modifier </modeling/modifiers/generate/subdivision_surface>`
gets changed to control the subdivision of a mesh at the time of rendering.
For this, all the other settings are the same except the *View* and *Render* settings.
These before mentioned settings get removed/renamed and the following settings are added:


.. rubric:: Viewport

Levels
   The levels of subdivision to see in the 3D Viewport,
   this works the same as the *View* setting on the original *Subdivision Modifier*.


.. rubric:: Render

Adaptive
   Use OpenSubdiv to give different subdivision levels to near and far objects automatically.
   This allows nearer objects to get more subdivisions and far objects to get less.

   Dicing Rate
      When using *Adaptive* the *Render Levels* property gets changed to *Dicing Rate*,
      this property is used to multiply the :ref:`scene dicing rate <cycles-subdivision-rate>`.

      .. figure:: /images/render_cycles_object-settings_adaptive-subdiv_displacement-dicing.png

         Subdivision Off/On, Dicing Rate: 1.0 - 0.3 - 0.05 (monkeys look identical in viewport, no modifiers).

Levels
   The levels of subdivision to see in the final render,
   this works the same as the *Render* setting on the original *Subdivision Modifier*.


Known Limitations
=================

- Multi-user object data are currently made single users, leading to increased memory usage.
  For those it is better to use non-adaptive subdivision still.
- Multi-view renders can have some inconsistencies between views.

.. warning::

   Instances are not tessellated individually.
   Instead, the original object is tessellated and then duplicated on all instances.
   To take advantage of both adaptive subdivision and instancing you should place
   the original object at the position of the instance that is closest from the camera.
