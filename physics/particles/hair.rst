
Hair
====

When set to hair mode, particle system creates only static particles,
which may be used for hair, fur, grass and the like.


Growing
-------

The first step is to create the hair, specifying the amount of hair strands and their lengths.

The complete path of the particles is calculated in advance.
So everything a particle does a hair may do also.
A hair is as long as the particle path would be for a particle with a lifetime of 100 frames.
Instead of rendering every frame of the particle animation point by point there are calculated
control points with an interpolation, the segments.


Styling
-------

The next step is to style the hair. You can change the look of base hairs by changing the :doc:`Physics Settings <physics/particles/physics>`\ .

A more advanced way of changing the hair appearance is to use :doc:`Children <physics/particles/children>`\ . This adds child hairs to the original ones, and has settings for giving them different types of shapes.

You can also interactively style hairs in :doc:`Particle Mode <physics/particles/mode>`\ . In this mode, the particle settings become disabled, and you can comb, trim, lengthen, etc. the hair curves.


Animating
---------

Hair can now be made dynamic using the cloth solver. This is covered in the :doc:`Hair Dynamics <physics/particles/hair/dynamics>` page.


Rendering
---------

Blender can render hairs in several different ways. Materials have a Strand section, which is covered in the materials section in the :doc:`Strands Page <materials/properties/strands>`\ .

Hair can also be used as a basis for the :doc:`Particle Instance modifier <modifiers/simulate/particle_instance>`\ , which allows you to have a mesh be deformed along the curves, which is useful for thicker strands, or things like grass, or feathers, which may have a more specific look.


Options
=======

.. figure:: /images/Blender3D_ParticleSystem_HairSettings-2.5.jpg

   Image 4a: Settings for a Hair particle system.


:guilabel:`Regrow`
   Regrow Hair for each frame.
:guilabel:`Advanced`
   Enables advanced settings which reflect the same ones as working in Emitter mode.


Emission
--------

:guilabel:`Amount`
   Set the amount of hair strands. Use as little particles as possible, especially if you plan to use softbody animation later. But you need enough particles to have good control. For a "normal" haircut I found some thousand (very roughly 2000) particles to give enough control. You may need a lot more particles if you plan to cover a body with fur. Volume will be produced later with :guilabel:`Children`\ .


Hair Dynamics
-------------

Settings for adding movement to hair see :doc:`Hair Dynamics <physics/particles/hair/dynamics>`\ .


Display
-------

:guilabel:`Rendered`
   Draw hair as curves.
:guilabel:`Path`
   Draw just the end points if the hairs.

:guilabel:`Steps`
    The number of segments (control points minus 1) of the hair strand. In between the control points the segments are interpolated. The number of control points is important:

- for the softbody animation, because the control points are animated like vertices, so more control points mean longer calculation times.
- for the interactive editing, because you can only move the control points (but you may recalculate the number of control points in :guilabel:`Particle` Mode).

   10 Segments should be sufficient even for very long hair, 5 Segments are enough for shorter hair, and 2 or 3 segments should be enough for short fur.


Children
--------

See :doc:`Children <physics/particles/children>`\ .


Render
------

Hair can be rendered as a Path, Object, or Group. See :doc:`Particle Visualization <physics/particles/visualization>` for descriptions.


Usage
=====

.. figure:: /images/Blender3D_FurWithParticles-Finished-2.48a.jpg
   :width: 400px
   :figwidth: 400px

   Image 4b: Particle systems may get hairy…


- `Fur Tutorial <http://en.wikibooks.org/wiki/Blender_3D:_Noob_to_Pro/Furry>`__\ , which produced (\ *Image 4b*\ ). It deals especially with short hair.


- `Blender Hair Basics <http://www.youtube.com/watch?v=kpLaxqemFU0>`__\ , a thorough overview of all of the hair particle settings.


