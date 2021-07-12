
*****************
Multiplane Scrape
*****************

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Multiplane Scrape`

Scrapes the mesh with two angled planes at the same time, producing a sharp edge between them.
This is useful for creating edges when sculpting hard surface objects.


Brush Settings
==============

.. _bpy.types.Brush.multiplane_scrape_angle:

Plane Angle
   The angle between the two planes of the brush, pressing :kbd:`Ctrl` inverts the angle.

.. _bpy.types.Brush.use_multiplane_scrape_dynamic:

Dynamic Mode
   When enabled, the base angle is sampled from the mesh surface.
   The *Plane Angle* controls how much the angle will increase when applying pen pressure.
   When pressing :kbd:`Ctrl`, it locks the plane angle to 0 degrees.

.. _bpy.types.Brush.show_multiplane_scrape_planes_preview:

Show Cursor Preview
   Displays a preview of the two scrape planes
   and the angle they form instead of the cursor while performing the stroke.
