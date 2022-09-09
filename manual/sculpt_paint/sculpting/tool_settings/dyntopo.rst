.. _bpy.ops.sculpt.dynamic_topology_toggle:

*******
Dyntopo
*******

.. reference::

   :Mode:      Sculpt Mode
   :Panel:     :menuselection:`Sidebar --> Tool --> Dyntopo`
   :Shortcut:  :kbd:`Ctrl-D`

Dynamic topology (aka dyntopo) is a dynamic tessellation sculpting method,
adds and removes details on-the-fly, whereas regular sculpting only affects the shape of a mesh.
This makes it possible to sculpt complex shapes out of a simple mesh,
rather than just adding details onto a modeled base mesh.

Dyntopo can be toggled with the checkbox in the header or with :kbd:`Ctrl-D`.
With dynamic topology active, most brushes will subdivide the mesh during the stroke.

.. _bpy.types.Sculpt.detail_size:
.. _bpy.types.Sculpt.constant_detail_resolution:
.. _bpy.types.Sculpt.detail_percent:
.. _bpy.ops.sculpt.dyntopo_detail_size_edit:

Detail Size/Percentage, Resolution :kbd:`Shift-D`
   Each Detail Type's detail is set here. Depending on the Detail Type being used
   this property will rather show as a pixel count (px), or percentage.

   Sample Detail Size (pipette icon)
      When using *Constant Detail*, it is possible to sample the detail value of a certain mesh area
      by clicking the pipette icon next to the detail setting and then clicking on the area.

.. _bpy.types.Sculpt.detail_refine_method:

Refine Method
   Setting the option will determine which of the methods will be used when altering the topology.

   Subdivide Edges
      Just like the Subdivide tool, this method will only subdivide topology
      to match the detail given.
   Collapse Edges
      When topology is too dense, and is smaller than the detail given, edges will
      be collapsed to fit the detail size appropriately.
   Subdivide Collapse
      This method combines the two methods, subdividing edges smaller than
      the detail size, and collapsing topology.

.. _bpy.types.Sculpt.detail_type_method:

Detailing
   Dyntopo uses three different detail methods to create dynamic detail to an object.

   Relative Detail
      This method uses a detail size based on the number of pixels, and in turn
      will create topology in that size. Zoom out big details, zoom in small fine details.
   Constant Detail
      To keep detail uniform across the entire object, Constant Detail can be used.
      The Detail is based on the percentage of a single unit.
   Brush Detail
      Giving more control over the topology, with this method you can create topology
      based on the brush size. You can increase and lower topology by resizing the brush itself.
      The detail size is based the size of the brush itself,
      where full detail will create topology the size of the brush radius itself.

.. _bpy.ops.sculpt.detail_flood_fill:

Detail Flood Fill
   When using *Constant* or *Manual* *Detailing*, this option is made available,
   allowing you to fill the entire object with a uniform detail, based on the detail size.

.. _bpy.types.Sculpt.use_smooth_shading:

Smooth Shading
   Toggles whether mesh faces are smooth or flat-shaded.
   In dynamic-topology mode all faces have the same type of shading.


.. _bpy.types.Brush.topology_rake_factor:

.. rubric:: Topology Rake

.. reference::

   :Mode:      Sculpt Mode
   :Panel:     :menuselection:`Tool Settings --> Brush --> Topology Rake`

*Topology Rake* automatically aligns mesh edges to the brush direction
to generate cleaner topology and define sharp features.
*Topology Rake* can have a severe performance impact so it works best on low-poly meshes.

.. figure:: /images/sculpt-paint_sculpting_tool-settings_dyntopo_topology-rake.jpg
