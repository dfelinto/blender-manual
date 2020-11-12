
***********
Switch Node
***********

.. figure:: /images/compositing_node-types_CompositorNodeSwitch.png
   :align: right

   Switch Node.

Switch between two images using a checkbox.


Inputs
======

Image
   First image input.
Image
   Second image input.


Properties
==========

Switch
   - When it is unchecked, the first input labeled "Off" is passed to the output.
   - When checked, the second input labeled "On" is passed to the output.


Outputs
=======

Image
   Standard image output.

.. tip::

   Switch state may be animated by adding a :doc:`keyframe </animation/keyframes/introduction>`.
   This makes the Switch node useful for bypassing nodes which are not wanted during part of a sequence.
