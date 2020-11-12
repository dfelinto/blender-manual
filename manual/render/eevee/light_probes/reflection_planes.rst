
*****************
Reflection Planes
*****************

These special types of Probe object are suited to smooth planar surfaces.
They basically capture the whole scene with a flipped camera.

Using reflection planes is really heavy on the render time
because the scene needs to be rendered as many times as there is Reflection Planes in the view.

Unless Screen Space Reflection is enabled,
Reflection Planes only work on specular surfaces that have their roughness around 0.

If Screen Space Reflection is enabled, Reflection Planes will serve as support buffers.
This accelerates the tracing process and completes the missing data from the view space.
This also make reflection more correct for the affected surfaces that have medium roughness and
disturbed normals (i.e. normal maps).

.. note::

   Subsurface Scattering, Screen Space Reflections and
   Volumetrics are not supported inside Reflection Plane's reflection.


Placement
=========

If Backface Culling is not enabled, snapping the Reflection Plane to the planar surface
will effectively capture the underside of the surface.

You can manually move the Reflection Plane above the surface enough for it to not appear in the capture.
Alternatively you can put a floor object inside a collection and
use this collection as a Visibility Collection (inverted) inside the Reflection Plane's probe settings.

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Object Data --> Probe`

Distance
   A probe object only influences the lighting of nearby surfaces.
   This influence zone is defined by the Distance parameter and object scaling.
   The influence distance varies is a bit, depending on the probe type.

   For Reflection Planes the influence distance is the distance from the plane.
   Only surfaces whose normals are aligned with the Reflection Plane will receive the captured reflection.

Falloff
   Percentage of the influence distance during which the influence of a probe fades linearly.
   Also defines how much shading normals needs to be aligned with the plane to receive reflections.

Clipping Offset
   Define how much below the plane the near clip is when capturing the scene.
   Increasing this can fix reflection contact problems.

Visibility Collection
   In some cases, it is useful to limit which objects appear in the light probe's captured lighting.
   For instance, an object that is too close to a capture point might be better excluded.
   This is what the visibility collection does.
   Only objects that are in this collection will be visible when this probe will capture the scene.

   There is also an option to invert this behavior and effectively hide the objects inside this collection.

   .. note::

      This is only a filtering option.
      That means that if an object is not visible at render time it won't be visible during the probe render.

   .. note::

      Due to a limitation, dupli-objects cannot be hidden by using this option.


Viewport Display
================

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Object Data --> Viewport Display`

Influence
   Show the influence bounds in the 3D Viewport.

Arrow Size
   Size of the arrow showing the reflection plane normal.

Show Preview Plane
   Show the captured reflected image onto a fully reflective plane in the 3D Viewport.
