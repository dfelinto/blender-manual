
******
Scrape
******

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Scrape`

The *Scrape* brush works like the *Flatten* brush, but only brings vertices above the plane downwards.


Brush Settings
==============

Area Radius
   Ratio between the brush radius and the radius that is going to be used to sample the area center.

   Use Pressure (pressure sensitivity icon)
      Uses stylus pressure to control how strong the effect is.
      The gradient of the pressure can be customized using
      the :doc:`curve widget </interface/controls/templates/curve>`.

Invert to Fill
   When enabled, holding :kbd:`Ctrl` while sculpting
   changes the brush behavior to be the same as the *Fill* brush.
   When disabled, holding :kbd:`Ctrl` while sculpting,
   will push vertices above the cursor up away from the cursor.
