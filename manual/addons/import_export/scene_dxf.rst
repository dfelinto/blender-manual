
***********
AutoCAD DXF
***********

.. admonition:: Reference
   :class: refbox

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Import/Export --> AutoCAD DXF`


.. _dxf-import:

Import
======

DXF layers are reflected as Blender groups. This importer uses a general purpose DXF library called "dxfgrabber".


DXF Type Mapping
----------------

To be as non-destructive as possible the importer aims to map as many DXF types to
Blender curves as possible.


DXF to Curves
^^^^^^^^^^^^^

- ``LINE`` as ``POLYLINE`` curve (with the option to merge connecting lines).
- ``(LW)POLYLINE``, ``(LW)POLYGON`` as ``POLYLINE`` curve if they have no bulges else as ``BEZIER`` curve.
- ``ARC``\ s, ``CIRCLE``\ s and ``ELLIPSE``\ s as ``BEZIER`` curves.
- ``HELIX``\ es (3D) as ``BEZIER`` curves.


DXF to Meshes
^^^^^^^^^^^^^

- ``MESH`` is mapped to a mesh object with a Subdivision Surface modifier, including the edge crease.
- ``POLYFACE``\ s and ``POLYMESH``\ es are imported to a mesh object.
- ``3DFACE`` \ s, ``SOLID`` \ s, ``POINT`` \ s are imported into one combined mesh object
  per layer called ``layername_3Dfaces``.


Missing DXF Types
^^^^^^^^^^^^^^^^^

- Hatches
- Leader


Properties
----------

Merge Options
^^^^^^^^^^^^^

Blocks As
   DXF Blocks can be imported as linked objects or group instances.
   Linked objects use parenting for DXF sub-blocks (blocks in blocks).

Parent Blocks to Bounding Boxes
   Draw a bounding box around blocks.
Merged Objects
   Since Blender (v2.71) is pretty slow at adding objects the user might want to
   merge similar DXF geometry to one object.

   By Layer
      Produces one object per layer; if there is mesh, curve, lamp, text data on one layer
      one object per layer and per Blender object.
   By Layer and DXF Type
      The second not only differentiates between Blender data types but also DXF types,
      such as ``LWPOLYLINE`` and ``POLYLINE``.
   By Layer and Closed No-bulge Polygons
      Closed polylines with no bulge, that is no curved edges, can be merged to one single mesh.
      This makes sense when the DXF polylines have an extrusion and/or an elevation attribute,
      which basically describes a location/rotation/scale transformation.
      If this merge option is chosen, line thickness settings will be ignored/disabled.
   By Layer and DXF-Type and Blocks
      For DXF files with a block being referenced many times, this option allows to insert the same block many times
      with one instanced-face object instead of with one object for each time the block needs to be inserted.
      Unfortunately this works only for block inserts that are uniformly scaled.
      Non-uniformly scaled block inserts are being imported as defined in *Blocks As*.
Combine ``LINE`` Entities to Polygons
   Separated lines in DXF might be merged to one consecutive Blender poly curve.
   Similar to *Remove Doubles* but for curves.


Line Thickness and Width
^^^^^^^^^^^^^^^^^^^^^^^^

Represent Line Thickness/Width
   DXF line attributes *thickness* and *width* have an effect on line in Z and X/Y direction respectively.
   A straight line might be turned to a cube by its attributes for instance.
   Therefore, in Blender these attributes are represented with curve extrusion, bevel and taper objects.
Merge by Attributes
   If both *Merged Objects* and *Represent Line Thickness/Width* are activated
   the object merging needs to be extended to separate all lines width different thickness and width.
   With *Merge by Attributes* this separation option is also available without
   the actual representation of line thickness and width.


Optional Objects
^^^^^^^^^^^^^^^^

Import ``TEXT``
   (``TEXT``, ``MTEXT``)
Import ``LIGHT``
   Including support for AutoCAD colors.
Export ``ACIS`` Entities
   Export NURBS 3D geometry (``BODY``, ``REGION``, ``PLANESURFACE``, ``SURFACE``, ``3DSOLID``) to ACIS-Sat files,
   since this is the format AutoCAD stores NURBS to DXF.
   You are going to be notified about the amount of stored ``.sat``/``.sab`` files.


View Options
^^^^^^^^^^^^

Display Groups in Outliner(s)
   Switch the Outliner display mode to ``GROUPS`` (DXF layers are mapped to groups).
Import DXF File to a New Scene
   Todo.
Center Geometry to Scene
   Center the imported geometry to the center of the scene;
   the offset information is stored as a custom property to the scene.


Georeferencing
^^^^^^^^^^^^^^

Important: DXF files do not store any information about
the coordinate system / spherical projection of its coordinates.
Best practice is to know the coordinate system for your specific DXF file and
enter this information in the DXF importer interface as follows:

Pyproj
   Installation: Download (`Windows <https://github.com/pyproj4/pyproj>`__,
   `macOS <http://www.ia.arch.ethz.ch/wp-content/uploads/2013/11/pyproj.zip>`__) Pyproj and copy it to your

   .. parsed-literal:: AppData/ApplicationSupport Folder/Blender/|BLENDER_VERSION|/scripts/modules/.

   In case you need to compile your own binary refer to
   `this post <https://blenderartists.org/forum/showthread.php?323358-DXF-Importer&p=2664492&viewfull=1#post2664492>`__
   on Blender Artists.

   Pyproj is a Python wrapper to the PROJ library, a well known C library used to
   convert coordinates between different coordinate systems.
   Open source GIS libraries such as PROJ are used directly or indirectly by many authorities and
   therefore can be considered well maintained.

   If Pyproj is available the DXF importer shows a selection of national coordinate systems
   but lets the user also to enter a custom EPSG / SRID code.
   It also stores the SRID as a custom property to the Blender scene.
   If a scene has already such an SRID property the coordinates are being converted from
   your DXF file to target coordinate system and therefore you **must** specify an SRID for the DXF file.
   If no SRID custom property is available the scene SRID is by default the same as the DXF SRID.
No Pyproj
   In case Pyproj is not available the DXF importer will only use its built-in lat/lon to X/Y converter.
   For conversion the "transverse Mercator" projection is applied that inputs a lat/lon coordinate to be used
   as the center of the projection. The lat/lon coordinate is being added to your scene as a custom property.
   Subsequent imports will convert any lat/lon coordinates to the same georeference.

   Important: So far only lat/lon to X/Y conversion is supported.
   If you have a DXF file with Euclidean coordinates that refer to another lat/lon center
   the conversion is not (yet) supported.

Rules of thumb for choosing an SRID
   if you have your data from OpenStreetMap or some similar GIS service website and
   exported it with QGIS or ArcGIS the coordinates are most likely in lat/lon then use WGS84 as
   your SRID with Pyproj or "spherical" if Pyproj is not available.
   For other DXF vector maps it's very likely that they use local / national coordinate systems.

   Open the DXF with a text editor (it has many thousands of lines) and
   make an educated guess looking at some coordinates.
   DXF works with "group codes", a name Autodesk invented for "key" as in key/value pairs.
   X has group code 10, Y has 20, Z has 30. If you find a pattern like:

   .. code-block:: none

      10, newline, whitespace, whitespace, NUMBER, newline,
      20, newline, whitespace, whitespace, NUMBER, newline,
      30, newline, whitespace, whitespace, NUMBER

   then ``NUMBER`` will be most likely your coordinates.
   You can probably tell from the format and/or the range of the coordinates which coordinate system it should be.


.. _dxf-export:

Export
======

Supported Data
--------------

- Mesh face: ``POLYFACE`` or ``3DFACE``
- Mesh edge: ``LINE``
- Modifier (optionally)


Unsupported Data
----------------

- Mesh vertex: ``POINT``
- Curve: ``LINE``\ s or ``POLYLINE``
- Curve NURBS: ``curved-POLYLINE``
- Text: ``TEXT`` or (wip: ``MTEXT``)
- Camera: ``POINT`` or ``VIEW`` or ``VPORT`` or (wip: ``INSERT(ATTRIB+XDATA)``)
- Light: ``POINT`` or (wip: ``INSERT(ATTRIB+XDATA)``)
- Empty: ``POINT`` or (wip: ``INSERT``)
- Object matrix: extrusion (``210-group``), rotation, elevation
- 3D Viewport: (wip: ``VIEW``, ``VPORT``)
- Instancing vert: auto-instanced or (wip: ``INSERT``)
- Instancing frame: auto-instanced or (wip: ``INSERT``)
- Instancing group: auto-instanced or (wip: ``INSERT``)
- Material: ``LAYER``, ``COLOR`` and ``STYLE`` properties
- Group: ``BLOCK`` and ``INSERT``
- Parenting: ``BLOCK`` and ``INSERT``
- Visibility status: ``LAYER_on``
- Frozen status: ``LAYER_frozen``
- Locked status: ``LAYER_locked``
- Surface
- Meta
- Armature
- Lattice
- :abbr:`IPO (InterPOlated)`/Animation
