:orphan:

.. _bpy.ops.object.pointcloud:

***********
Point Cloud
***********

:term:`Point clouds <Point Cloud>` can be used to represent 3D scans and
in the future can represent particles. Each point can store data in a set of `Attributes`_.

.. figure:: /images/modeling_point-cloud_example.png

   Example of a monkey object represented as a point cloud.


Properties
==========

Attributes
----------

The *Attributes* panel contains different point cloud characteristics such as the position and size of points.

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

   :Type: Color

Particle ID
   A unique identifier given to each particle.

   :Type: Integer

Velocity
   The speed and direction that the particle is traveling.

   :Type: Vector

Custom Attributes
   Custom attribute can be given to particles to hold a custom characteristic.

   Name
      The name of the attribute.
   Data Type
      The type of data to store in the attribute.

      :Float: Floating-point value
      :Integer: 32-bit integer
      :Vector: 3D vector with floating-point values
      :Color: RGBA color with floating-point precision
      :Byte Color: RGBA color with 8-bit precision
      :String: Text string

   Domain
      The type of element the attribute is stored in.
      Currently, attributes can only be stored per *Point*.


Custom Properties
-----------------

See the :ref:`Custom Properties <files-data_blocks-custom-properties>` page for more information.


Editing
=======

Currently, not much can be done with point clouds; however,
they can be :doc:`converted to/from meshes </scene_layout/object/editing/convert>`.
