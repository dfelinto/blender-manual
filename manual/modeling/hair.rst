:orphan:

****
Hair
****

Hair type particle system can be used for strand-like objects,
such as hair, fur, grass, quills, etc.

.. figure:: /images/physics_particles_hair_introduction_example.jpg

   Particle hair systems example. Used for the grass and fur.


Properties
==========

Attributes
----------

The *Attributes* panel contains different hair characteristics such as the position and color of hair strands.

Use the :ref:`List View <ui-list-view>` to manage attributes.


Attribute Types
^^^^^^^^^^^^^^^

Position
   The position of the point in 3D space.

   :Type: Vector

Radius
   The radius of each point.

   :Type: Float

Color
   The color of each point.

   :Type: Float Color

Custom Attributes
   Custom attribute can be given to particles to hold a custom characteristic.

   Name
      The name of the attribute.
   Data Type
      The type of data to store in the attribute.

      :Float: Floating point value
      :Integer: 32-bit integer
      :Vector: 3D vector with floating point values
      :Float Color: RGBA color with floating point precision
      :Byte Color: RGBA color with 8-bit precision
      :String: Text string

   Domain
      The type of element the attribute is stored in.

      :Point: The attribute is stored per hair point.
      :Curve: The attribute is stored per hair curve.


Custom Properties
-----------------

See the :ref:`Custom Properties <files-data_blocks-custom-properties>` page for more information.
