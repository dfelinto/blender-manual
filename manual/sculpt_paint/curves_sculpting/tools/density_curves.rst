
*************
Density Brush
*************

Create (or remove) curves based on a target distance.
It generates a high number of points and then rejects the
ones that are too close to existing points.


Brush Settings
==============

Density Mode
   :Auto:
    Either add or remove curves depending on the minimum distance of the curves under the cursor.
   :Add:
      Add new curves between existing curves, taking the minimum distance into account.
   :Remove:
      Remove curves whose root points are too close.

Distance Min
   Goal distance between the curve roots.

Count Max
   The maximum amount of points that it tries to sample in the surface.
