
Noise
=====

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :kbd:`Mesh Tools` panel (:guilabel:`Editing` context)


.. admonition:: Note
   :class: note

   :guilabel:`Noise` is an old feature. The :doc:`Displace Modifier <modifiers/deform/displace>` is a non-destructive alternative to the Noise tool and is a more flexible way to realize these sort of effects. The key advantages of the modifier are that it can be canceled at any moment, you can precisely control how much and in which direction the displacement is applied, and much more….
   See also the ANT Landscape :doc:`add-on <extensions/python/add-ons>`.


The :guilabel:`Noise` function allows you to displace vertices in a mesh based on the grey
values of the first texture slot of the material applied to the mesh.

The mesh must have a material and a texture assigned to it for this tool to work.
To avoid having the texture affect the material's properties,
it can be disabled in the texture menu.

The :guilabel:`Noise` function displaces vertices along the object's ±Z-Axis only.

:guilabel:`Noise` permanently modifies your mesh according to the material texture. Each click adds onto the current mesh. For a temporary effect, map the texture to Displacement for a render-time effect. In :guilabel:`Object` / :guilabel:`Edit` mode, your object will appear normal, but will render deformed.

The deformation can be controlled by modifying the :guilabel:`Mapping` panel and/or the
texture's own panel (e.g. :guilabel:`Clouds`, :guilabel:`Marble`, etc.).


.. figure:: /images/Noise1.jpg
   :width: 300px
   :figwidth: 300px

   mesh before noise is added


.. figure:: /images/Noise2.jpg
   :width: 300px
   :figwidth: 300px

   mesh after noise is added, using basic cloud texture


