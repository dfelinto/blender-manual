
##############
  Instancing
##############

There are currently three ways in Blender to procedurally instantiate (or duplicate)
objects directly from other objects.
These options are located in the :menuselection:`Properties --> Object Properties --> Instancing` panel.

.. note::

   There are other ways to indirectly instantiate objects,
   e.g. from a :doc:`particle system </physics/particles/emitter/render>`...

Vertices
   This creates an instance of all children of this object on each vertex
   (for mesh objects only).
Faces
   This creates an instance of all children of this object on each face
   (for mesh objects only).
Collection
   This creates an instance of the collection with the transformation of the object.
   Collection instancers can be animated using actions, or can get a :ref:`Proxy <object-proxy>`.

.. toctree::
   :maxdepth: 2

   verts.rst
   faces.rst
   collection.rst
