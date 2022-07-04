
******
Tissue
******


.. figure:: /images/addons_mesh_tissue_cover.jpg

Tissue is a collection of tools that facilitate the use of computational-design techniques inside Blender.
It consists of different tools, visible in the right panel.
According to the active mode, different tools are displayed:

- :ref:`Tissue Tools <tissue tools>` (visible in Edit Mode and Object Mode)
- :ref:`Tissue Weight Tools <tissue weight tools>`  (visible in Weight Paint Mode)
- :ref:`Tissue Color Tools <tissue color tools>`  (visible in Vertex Weight Mode)


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Mesh then Tissue to enable the script.

.. _tissue tools:

Tissue Tools
============

.. figure:: /images/addons_mesh_tissue_tissue-tools.jpg

Generators
----------

*Generators* are non-destructive functions that generate new objects starting
from input objects. They include **Tessellate**, **Dual Mesh** (a special
Tessellate) and **Convert to Curve**. For all of them, a **Refresh** operator can be used in order to reload the
changes from the input objects.

Tessellate
----------

The *Tessellate* tool allows the user to copy a selected object (Component) on the faces of
the active object (Base), adapting its bounding box to the shape of quad faces.
It is possible to use as input objects *Mesh*, *Curve*, *Surface* and *Text* and *Meta* objects.
When using Tessellate, two objects must be selected.
Once the *Tessellate* button was pressed, then more options will appear in the tool parameters.

.. figure:: /images/addons_mesh_tissue_tessellate-operator.jpg

Later it will be possible to change them,
together with more advanced settings from the *Object Data Panel* of the generated object.

.. figure:: /images/addons_mesh_tissue_tessellate-panel.jpg

Use Modifiers
   This option is available for both *Base* and *Component* objects and allows the use
   the respective modifiers. If this option is disabled, then only the original object's
   data will be used.

Fill Mode
  Tessellation strategy used to map the Component's coordinates on the Base's faces.

  .. figure:: /images/addons_mesh_tissue_tessellate-fill-modes.jpg

  Tri
    This options will automatically triangulate the Base object and will map the component
    to the triangular faces. The input domain will be considered rectangular, but the
    target domain will have two vertices coincident.
  Quad (default)
    This is the default method and will map the Component domain to each quad face of the Base object.
    If an face has more than 4 vertices, then it will be automatically separated in quad or triangular faces.

    .. figure:: /images/addons_mesh_tissue_tessellate-quad-mode.jpg

  Fan
    This option will split every face of the Base object in triangles connecting each side of the face
    to its center.

    .. figure:: /images/addons_mesh_tissue_tessellate-fan-mode.jpg

  Patch
    This option require the use of a Subdivision Surface modifier on the Base object.
    It is similar to the *Quad* method, but it will allow to use curved domains, based on the Subdivided patches.
    If more subdivision surfaces (or Multiresolution modifiers) are used, then only the last one will be used for
    defining the target patches.

    .. figure:: /images/addons_mesh_tissue_tessellate-patch-mode.jpg

  Frame
    Similarly to an Inset Face operator, this option will allow to apply the components along
    offset faces of a given Thickness.

    .. figure:: /images/addons_mesh_tissue_tessellate-frame-mode.jpg


Merge
  Automatically merge together all the generated components.

Smooth Shading
  Automatically sets the shading of the generated geometry as Smooth. If the Component
  object is already set as Smooth, then this option is not necessary.

Components
  Three different method can be used to assign the components.

  Object
    Repeat the same object on all the target faces.

  Collection
    Assign the objects contained in a given Collection.
    The components can be assigned either randomly or according to a Vertex Group.

  Materials
    Assign the components according to the name of the materials assigned to each face.
    If for a given material, there is no an object with the same name, then the face is not used.

    Watch the `Tutorial <https://youtu.be/2Wcu9E0EGEM>`__ (it is based on an old version of Tissue,
    the procedure is slightly different now)

Thickness
  Scale Mode
    Constant
      Generate components with a fixed and uniform thickness in the normal direction.
    Relative
      Generate components with a thickness proportional to the target face dimension.
      This will produce components with an aspect ration similar to the original Component
      object.
    Scale
      control the scaling factor of the components' Thickness
    Offset
      Allows to control the alignment of the components in relation to the Base object surface.

Components Coordinates
  Strategy used to determine the component's domain for mapping it on the target faces.

  .. figure:: /images/addons_mesh_tissue_tessellate-component-coordinates.jpg

  Bounds (Default)
    Automatically defines the domain according the *Bounding Box* of the component object.

  Local
    Defines the domain according to the local coordinates of the component object.
    The face domain is considered from 0 to 1 in both Local X and Local Y directions.
    This method allows a customization of the mapping strategies, maintaining the result independent
    from Location/Rotation/Scale of the component object.

  Global
    Similar to Local, but based on the Global coordinates of the component. This allows to easily
    produce animations changing the Location/Rotation/Scale of the component.

    Watch the `Tutorial <https://youtu.be/PRIcB1Q-gK4>`__

  Extend (Local and Global coordinates)
    Extend the domain of the components with a domain bigger than 0-1.

  Clip (Local and Global coordinates)
    Truncate the component according to the domain 0-1.

  Cyclic (Local and Global coordinates)
    Cut and move to the other side the parts of the component that exceed the domain 0-1.

    .. figure:: /images/addons_mesh_tissue_tessellate-bounds-cyclic.jpg


Weight and Morphing
  Combine the Vertex Groups of the base object with the Shape Keys from the component,
  in order to generate morphing components.

  .. figure:: /images/addons_mesh_tissue_tessellate-weight-and-morphing.jpg

  Map Vertex Groups
    Remap each Vertex Group from the base mesh to the generated geometry

  Use Shape Keys
    Transfer the Shape Keys from the component object to the generated object.
    If the name of the base's vertex groups and the Shape Keys match, then they
    will be automatically assigned in order to control their morphing behavior.

    Watch the `Tutorial <https://youtu.be/2Wcu9E0EGEM>`__

Iterations
  Automatically repeat the tessellation using as base the result of the previous iteration.

  .. figure:: /images/addons_mesh_tissue_tessellate-iterations.jpg

  Repeat
    Number of iterations.

  Combine iterations
    Combine the resulting tessellation with part or all of the previous iteration:

      Last
        Ignore the previous iterations.

      Unused
        Combine the tessellation with the faces of the previous iteration that are not generating components.

      All
        Combine the tessellation with all the faces from the previous iteration.


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

Generate a Curve object from the *Loops*, *Edges* or *Particles* of the active object.
This is a non-destructive operation, meaning that in any moment it will be possible to reload
the changes from the base object and change the parameters of the conversion.
It will be possible to convert specific edges/loops according to different criteria, together
with the addition of a pattern effect.

.. figure:: /images/addons_mesh_tissue_convert-to-curve-example.jpg

(To Do)


Refresh
-------

Update the active object according to the changes in the base geometries.
This operator works on the objects generated through *Tessellate* and *Convert to Curve*.


Rotate Faces
------------

Rotate the indexes of the selected faces (in Edit-Mode). This allows to control the rotation of the components
of Tessellated objects, when using *Default* rotation.
Once the operator is executed, then the interested Tessellated objects are automatically refreshed.


Convert to Dual Mesh
--------------------

Destructive version of the Dual-Mesh operator. This directly convert the active object to its Dual-Mesh.


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

Assign random materials to the face's of the active mesh object.


Weight to Materials
-------------------

Distribute existing materials according to the weight of the active vertex group.
It is also possible to automatically create new materials.


Tissue Render Animation
-----------------------

(To Do)


.. _tissue weight tools:

Tissue Weight Tools
===================

.. figure:: /images/addons_mesh_tissue_weight-tools.jpg


Area
----

Weight from Faces area (Automatic Bounds, Manual Bounds)

.. figure:: /images/addons_mesh_tissue_weight-area.jpg


Curvature
---------

Weight from Curvature (Based on Dirty Color Attributes)

.. figure:: /images/addons_mesh_tissue_weight-curvature.jpg


Weight Distance
---------------

Generate a vertex group according to the distance from the selected vertices.
Different methods can be used: *Geodesic*, *Euclidean* or *Topology* distance.

.. figure:: /images/addons_mesh_tissue_weight-distance.jpg


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
(Deformation Modifiers and Simulations)

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

Tissue implements the Gray-Scott model for the
`Reaction-Diffusion <https://en.wikipedia.org/wiki/Reaction%E2%80%93diffusion_system>`__ simulation.
This allows to simulate through the vertex groups the distribution of the two substances
that generate the various patterns of many living organisms.

.. figure:: /images/addons_mesh_tissue_weight-reaction-diffusion.jpg

See `this video <https://youtu.be/J-0NzU1TmIY>`__ for an example of the Reaction-Diffusion simulation with Tissue.


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


.. _tissue color tools:

Tissue Color Tools
==================

.. figure:: /images/addons_mesh_tissue_color-tools.jpg


Convert to Weight
-----------------

Red Channel
   Add a vertex group derived to red channel of the active Color Attribute.
Green Channel
   Add a vertex group derived to green channel of the active Color Attribute.
Blue Channel
   Add a vertex group derived to blue channel of the active Color Attribute.
Value Channel
   Add a vertex group derived to value channel of the active Color Attribute.
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
