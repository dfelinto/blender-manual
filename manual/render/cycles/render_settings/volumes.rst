
*******
Volumes
*******

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Render --> Volumes`

Volume *Step* size is the distance between volume shader samples.
Cycles automatically estimates this distance based on voxel size in
volume objects and smoke simulations.

Render time can be reduced by increasing the step size, at the cost of
potentially losing some volume detail. For procedural volume shaders
that add detail, step size can be increased per object, material or world.

Render Step Rate
   Global multiplier on the step size for all volumes in renders.
   Increase to reduce render time, at the cost of losing detail.
Viewport Step Rate
   Global multiplier on the step size for all volumes in the viewport.
   Increase for more responsive viewport rendering.
Max Steps
   Maximum number of steps through the volume before giving up,
   to protect from extremely long render times with big objects or small step sizes.
