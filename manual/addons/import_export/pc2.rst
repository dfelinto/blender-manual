
****************
Pointcache (pc2)
****************

.. admonition:: Reference
   :class: refbox

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Export --> Pointcache (.pc2)`

This exporter produces pointcache files. These can be used to transfer animated meshes to external applications.
Only the vertex positions at the samples are saved.

The exporter can export meshes, surfaced curves, surfaces and font objects. They are all treated as meshes.
The base object has to be converted into a mesh before exporting it also.


Properties
==========

Convert to Y-Up
   Rotates the mesh data -90 degrees around X.
Export into World Space
   Transform the mesh data into world space.
Apply Modifiers
   Whether to apply modifiers before exporting.
Start Frame
   First frame to export.
End Frame
   Export up to this frame.
Sampling
   The sample rate. 1 means one sample per frame. 0.1 means 10 samples per frame,
   and 10 means one sample every 10 frames.


Importing
=========

The use of these files depends on the importing application.
In general the object has to be first exported normally (OBJ export or the like) and
then the pointcache data can be attached to the object.

- In 3ds Max there is a modifier which can directly read pc2 files.
- In Maya the pc2 cache has to be converted into Maya's geometry cache format first.
  The MEL command for that is this:

  .. code-block:: sh

     cacheFile -pc2 1 -pcf "<insert filepath of source>" -f "<insert target filename w/o extension>" -dir "<insert directory path for target>" -format "OneFile";
