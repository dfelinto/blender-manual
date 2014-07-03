


Shadows
=======


The shadows that appear in a scene are affected by a combination of the layout of objects, the shape of the objects,  the materials of the objects, and the lighting. In Blender, the Display Mode (Single Texture, Multitexture,or GLSL) also affects the appearance of shadows. See :doc:`lighting/shadows` for a more complete description of this subject.


 .. admonition:: Shadows in 3D mode
   :class: nicetip

   To see shadows in 3D (textured) mode, you must have switched to GLSL mode before making any materials.   In MultiTexture mode, shadows only appear in the rendered image: none of these can be seen in the preview image.


.. figure:: /images/Doc_2.6_Materials_Properties_Shadow.jpg

   Fig. 1: Shadow Panel.


The Shadow panel in the Materials Properties window (Fig. 1)
controls the effects that the material can have on the shadows that appear in the scene.
The various properties are described in the sections below.


.. figure:: /images/Doc_2.6_Materials_Properties_Shadow2.jpg

   Fig. 2: Scene- all shadow properties off.


Options
-------


The following properties can be set for each individual material with which objects in the
scene are shaded. The effects are illustrated with rendered images for a simple scene (Fig. 2)
consisting of two "posts", one with a red (totally non-transparent) material; one green
(partially transparent) material, set up on a light blue  plane to receive the shadows.
The illustrations were all taken in Blender Render engine, with Multitexture mode.


Shadow Receiving Object Material
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following options affect the material that receives shadows:


**Receive**
    Allows this material to receive full-intensity shadows (Fig. 3).

**Receive Transparent**
    Allows this material to receive shadows whose intensity is modified by the transparency and color of the shadow-casting object (Fig. 4).


.. figure:: /images/Doc_2.6_Materials_Properties_Shadow3.jpg

   Fig. 3: Plane - Receive.


.. figure:: /images/Doc_2.6_Materials_Properties_Shadow4.jpg

   Fig. 4: Plane - Receive + Receive Transparency.


Shadow Casting Object Material
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The following options affect the material that casts shadows:


**Cast Only**
    Material appears transparent, but it still casts shadows  (Fig. 5).

**Casting Alpha**
    ??

**Shadows Only**
    Material appears transparent except for where it receives shadows from other objects, and  also it retains its own transparency (Fig. 6). Note the faint image of the partly-transparent post.

**Shadow and Distance**
    ???


.. figure:: /images/Doc_2.6_Materials_Properties_Shadow5.jpg

   Fig. 5: Posts - Cast Only.


.. figure:: /images/Doc_2.6_Materials_Properties_Shadow6.jpg

   Fig. 6: Posts - Shadows Only.


Buffered Shadow Options
~~~~~~~~~~~~~~~~~~~~~~~

In addition to the shadow options described above, there are further material properties which control buffered shadow features. See section on :doc:`Spot Buffered Shadows <lighting/lamps/spot/buffered_shadows>` for further discussion of these techniques.

**Cast Buffer Shadow**
    Casts shadows from shadow buffer lamps.

**Buffer Bias**
    Multiplication factor for Buffer shadows (0 = ignore)

**Auto Ray Bias** -
    Prevent raytraced shadow errors on surfaces with smooth shaded normals.

**Ray Bias**
    Bias value to be used.

**Cast Approximate**
    Allow this material to cast shadows when using approximate ambient occlusion.


