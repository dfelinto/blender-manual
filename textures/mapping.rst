
..    TODO/Review: {{review|text=missing dupli part}} .


Texture Mapping
===============


Textures need mapping coordinates, to determine how they are applied to the object.
The mapping specifies how the texture will ultimately wrap itself to the object.

For example,
a 2D image texture could be configured to wrap itself around a cylindrical shaped object.


Coordinates
-----------


.. figure:: /images/25-Manual-Textures-Mapping-Coord.jpg
   :width: 207px
   :figwidth: 207px

   Mapping Coordinate menu


:guilabel:`Coordinates` Mapping works by using a set of coordinates to guide the mapping process. These coordinates can come from anywhere, usually the object to which the texture is being applied to.
:guilabel:`Global`
    The scene's global 3D coordinates. This is also useful for animations; if you move the object, the texture moves across it. It can be useful for letting objects appear or disappear at a certain position in space.

:guilabel:`Object`
    Uses an object as source for coordinates.  Often used with an :guilabel:`Empty`\ , this is an easy way to place a small image at a given point on the object (see the
FIXME(TODO: Internal Link;
[[#Position a Decal on a Mesh|example below]]
)). This object can also be animated, to move a texture around or through a surface.
   :guilabel:`Object`
      Select the name of an object.

:guilabel:`Generated`
    The original undeformed coordinates of the object.  This is the default option for mapping textures.

:guilabel:`UV`
    UV mapping is a very precise way of mapping a 2D texture to a 3D surface. Each vertex of a mesh has its own UV co-ordinates which can be unwrapped and laid flat like a skin. You can almost think of UV coordinates as a mapping that works on a 2D plane with its own local coordinate system to the plane on which it is operating on. This mapping is especially useful when using 2D images as textures, as seen in :doc:`UV Mapping <textures/mapping/uv>`\ . You can use multiple textures with one set of UV coordinates.
   :guilabel:`Layer`
      Select your UV layer to use it for mapping.

:guilabel:`Strand/Particle`
    Uses normalized 1D strand texture coordinate or particle age(X) and trail position (Y). Use when texture is applied to hair strands or particles.

:guilabel:`Sticky`
    Uses a mesh's sticky coordinates, which are a form of per-vertex UV co-ordinates. If you have made sticky coordinates first (in (usually) :guilabel:`Camera View` → :kbd:`Space` → type :guilabel:`Sticky` → choose :guilabel:`Add Sticky`\ /\ :guilabel:`Remove Sticky`\ ), the texture can be rendered in camera view (so called "\ :doc:`Camera Mapping <ls/textures/uv/camera_mapping>`\ ").

:guilabel:`Window`
    The rendered image window coordinates. This is well suited to blending two objects.

:guilabel:`Normal`
    Uses the direction of the surface's normal vector as coordinates. This is very useful when creating certain special effects that depend on viewing angle.

:guilabel:`Reflection`
    Uses the direction of the reflection vector as coordinates. This is useful for adding reflection maps — you will need this input when Environment Mapping.

:guilabel:`Stress`
    Uses the difference of edge length compared to original coordinates of the mesh.  This is useful, for example, when a mesh is deformed by modifiers.

:guilabel:`Tangent`
    Uses the optional tangent vector as texture coordinates.


Projection
----------


.. figure:: /images/25-Manual-Textures-Mapping-Proj.jpg
   :width: 210px
   :figwidth: 210px

   Projection menu


:guilabel:`Flat`
    Flat mapping gives the best results on single planar faces. It does produce interesting effects on the sphere, but compared to a sphere-mapped sphere the result looks flat. On faces that are not in the mapping plane the last pixel of the texture is extended, which produces stripes on the cube and cylinder.

:guilabel:`Cube`
    Cube mapping often gives the most useful results when the objects are not too curvy and organic (notice the seams on the sphere).

:guilabel:`Tube`
    Tube mapping maps the texture around an object like a label on a bottle. The texture is therefore more stretched on the cylinder. This mapping is of course very good for making the label on a bottle or assigning stickers to rounded objects. However, this is not a cylindrical mapping so the ends of the cylinder are undefined.

:guilabel:`Sphere`
    Sphere mapping is the best type for mapping a sphere, and it is perfect for making planets and similar objects. It is often very useful for creating organic objects. It also produces interesting effects on a cylinder.


Inheriting coordinates from the parent object
---------------------------------------------


:guilabel:`From Dupli`

    Duplis instanced from vertices, faces, or particles, inherit texture coordinates from their parent.

**Todo: explaination**


Coordinate Offset, Scaling and Transformation
---------------------------------------------


.. figure:: /images/25-Manual-Textures-Mapping-Offset.jpg

   Offset panel


:guilabel:`Offset`
    The texture co-ordinates can be translated by an offset. Enlarging of the Ofs moves the texture towards the top left.


.. figure:: /images/25-Manual-Textures-Mapping-Size.jpg

   Size panel


:guilabel:`Size`
    These buttons allow you to change the mapping of axes between the texture's own coordinate system, and the mapping system you choose (Generated, UV, etcetera.)  More precisely, to each axis of the texture corresponds one of four choices, that allow you to select to which axis in the mapping system it maps! This implies several points:

- For 2D textures (such as images), only the first two rows are relevant, as they have no Z data.
- You can rotate a 2D picture a quarter turn by setting the first row (i.e. X texture axis) to Y, and the second row (Y texture axis) to X.
- When you map no texture axis (i.e. the three "void" buttons are set), you'll get a solid uniform texture, as you use zero dimension (i.e. a dot, or pixel) of it (and then Blender extends or repeats this point's color along all axes.)
- When you only map one texture axis (i.e. two "void" buttons are enabled), you'll get a "striped" texture, as you only use one dimension (i.e. a line of pixel) of it, and then Blender stretches this line along the two other axes.
- The same goes, for 3D textures (i.e. procedural ones), when one axis is mapped to nothing, Blender extends the plan ("slice") along the relevant third axis.

So, all this is a bit hard to understand and master. Fortunately,
you do not have to change these settings often, except for some special effects… Anyway,
the only way to get used to them is to practice!


