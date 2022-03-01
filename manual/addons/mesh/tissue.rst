
******
Tissue
******

.. figure:: /images/addons_mesh_tissue_cover.jpg

Tissue is a collection of tools that facilitate the use of computational-design techniques inside Blender.
It consists of different tools, visible in the right panel.
According to the active mode, different tools are displayed:

- Tissue Tools (visible in Edit Mode and Object Mode)
- Tissue Weight Tools (visible in Weight Paint Mode)
- Tissue Color Tools (visible in Vertex Weight Mode)


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Mesh then Tissue to enable the script.


Tissue Tools
============

Generators
----------

*Generators* are non-destructive functions that generate new objects starting from input objects.
They include **Tessellate**, **Dual Mesh** (a special Tessellate) and **Convert to Curve**.
For all of them, a **Refresh** operator can be used in order to reload the changes from the input objects.


Tessellate
----------

The *Tessellate* tool allows the user to copy a selected object (Component) on the faces of
the active object (Base), adapting its bounding box to the shape of quad faces.
It is possible to use as input objects *Mesh*, *Curve*, *Surface* and *Text* and *Meta* objects.
When using Tessellate, two objects must be selected.
Once the *Tessellate* button was pressed, then more options will appear in the tool parameters.

.. figure:: /images/addons_mesh_tissue_tessellate-operator.jpg

Later it will be possible to change them, together with more advanced settings
from the *Object Data Panel* of the generated object.

Use Modifiers
   This option is available for both *Base* and *Component* objects and allows the use
   the respective modifiers. If this option is disabled, then only the original object's
   data will be used.

Fill Mode
  Tessellation strategy used to map the Component's coordinates on the Base's faces.

  Tri
    This options will automatically triangulate the Base object and will map the component
    to the triangular faces. The input domain will be considered rectangular, but the
    target domain will have two vertices coincident.
  Quad (default)
    This is the default method and will map the Component domain to each quad face of the Base object.
    If an face has more than 4 vertices, then it will be automatically separated in quad or triangular faces.
  Fan
    This option will split every face of the Base object in triangles connecting each side of the face
    to its center.
  Patch
    This option require the use of a Subdivision Surface modifier on the Base object.
    It is similar to the *Quad* method, but it will allow to use curved domains, based on the Subdivided patches.
    If more subdivision surfaces (or Multiresolution modifiers) are used, then only the last one will be used for
    defining the target patches.
  Frame
    Similarly to an Inset Face operator, this option will allow to apply the components along
    offset faces of a given Thickness.

Merge
  Automatically merge together all the generated components.

Smooth Shading
  Automatically sets the shading of the generated geometry as Smooth. If the Component
  object is already set as Smooth, then this option is not necessary.

Thickness
  Scale Mode
    Constant
      Generate components with a fixed and uniform thickness in the normal direction.
    Relative
      Generate components with a thickness proportional to the target face dimension.
      This will produce components with an aspect ration similar to the original Component object.
    Scale
      Control the scaling factor of the components' Thickness.
    Offset
      Allows to control the alignment of the components in relation to the Base object surface.


Dual Mesh
---------

*Dual Mesh* modifies the selected meshes creating dual meshes.
Dual Mesh output is a polygonal mesh derived from the triangular mesh.
Quadrangular meshes are automatically converted to triangular before.

.. figure:: /images/addons_mesh_tissue_dual-mesh.jpg

Quad Method
   Methods for splitting the quads into triangles. (Inherited from the *Triangulate Faces* tool.)
Polygon Method
   Methods for splitting the polygons into triangles. (Inherited from the *Triangulate Faces* tool.)
Preserve Borders
   Prevent alteration of the open boundaries of the mesh.


Convert to Curve
----------------

(To Do)


Refresh
-------

The options for the *Update* tool are the same of *Tessellate*.
Furthermore, it allows to change Generator object and Component object.


Rotate Faces
------------

(To Do)


Convert to Dual Mesh
--------------------

(To Do)


Polyhedra Wireframe
-------------------

(To Do)


Lattice Along Surface
---------------------

(To Do)


UV to Mesh
----------

Convert the active UV-map to mesh trying to preserve the original 3D model total surface area.

.. figure:: /images/addons_mesh_tissue_uv-to-mesh.jpg


Random Materials
----------------

(To Do)


Weight to Materials
-------------------

(To Do)


Tissue Render Animation
-----------------------

(To Do)


Tissue Weight Tools
===================

Area
----

Weight from Faces area (Automatic Bounds, Manual Bounds)

.. figure:: /images/addons_mesh_tissue_weight-area.jpg


Curvature
---------

Weight from Curvature (Based on Dirty Vertex Colors)

.. figure:: /images/addons_mesh_tissue_weight-curvature.jpg


Weight Distance
---------------

(To Do)


Weight Formula
--------------

Weight based on Vertices parameters. Allows to use vertices coordinates and normals direction.
Integer and Float sliders can be created in order to find the proper parameters more easily.

.. figure:: /images/addons_mesh_tissue_weight-formula.jpg


Weight Laplacian
----------------

(To Do)


Harmonic
--------

Harmonic function based on active Weight

.. figure:: /images/addons_mesh_tissue_weight-harmonic.jpg


Random
------

(To Do)


Edges Deformation
-----------------

Generate a Vertex Group based on Edges Deformation evaluated on the Modifiers result
(Deformation Modifiers and Simulations).

.. figure:: /images/addons_mesh_tissue_weight-edges-deformation.jpg


Edges Bending
-------------

Generate a Vertex Group based on Edges Bending evaluated on the Modifiers result
(Deformation Modifiers and Simulations).

.. figure:: /images/addons_mesh_tissue_weight-edges-bending.jpg


Streamlines Curves
------------------

(To Do)


Contour Curves
--------------

Generates isocurves based on Active Weight.

.. figure:: /images/addons_mesh_tissue_weight-contour-curves.jpg


Contour Displace
----------------

Cut the mesh according to active Weight in a variable number of isocurves and automatically add a Displace Modifier.

.. figure:: /images/addons_mesh_tissue_weight-contour-displace.jpg


Contour Mask
------------

Trim the mesh according to active Weight.

.. figure:: /images/addons_mesh_tissue_weight-contour-mask.jpg


Reaction Diffusion
------------------

(To Do)


Radom Materials
---------------

(To Do)


Weight to Materials
-------------------

(To Do)


Convert to Colors
-----------------

Convert To
   Value Channel, Red Channel, Green Channel, Blue Channel, False Color
Invert
   Invert the values read from vertex weight.


Convert to UV
-------------

(To Do)


Tissue Color Tools
==================

Convert to Weight
-----------------

Red Channel
   Add a vertex group derived to red channel of the active vertex color.
Green Channel
   Add a vertex group derived to green channel of the active vertex color.
Blue Channel
   Add a vertex group derived to blue channel of the active vertex color.
Value Channel
   Add a vertex group derived to value channel of the active vertex color.
Invert
   Invert the values read from vertex weight.


Example
=======

See `this video <https://vimeo.com/132720942>`__ for an example of the Tissue add-on in action.

.. reference::

   :Category:  Mesh
   :Description: Tools for computational design.
   :Location: :menuselection:`Sidebar --> Edit tab`
   :File: mesh_tissue folder
   :Author: Alessandro Zomparelli (Co-de-iT)
   :License: GPL
   :Note: This add-on is bundled with Blender.
