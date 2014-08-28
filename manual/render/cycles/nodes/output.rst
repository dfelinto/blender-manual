
Output Nodes
************

Output nodes are the final node in every node tree.
Although you can add more than one, only one will be used (indicated by a colored or darkened header).
Output nodes are always preceded by :doc:`Shaders </render/cycles/nodes/shaders>`
except in the case of the :doc:`Displacement </render/cycles/materials/displacement>` of a Material Output.


[[Doc:2.6/Manual/Render/Cycles/Materials|Material Output]]
==========================================================

:guilabel:`Surface`
   The surface output of the material
:guilabel:`Volume`
   *Currently under independent development, does nothing*
:guilabel:`Displacement`
   Used to create bump mapping or actual subdivided :doc:`Displacement </render/cycles/materials/displacement>`


[[Doc:2.6/Manual/Render/Cycles/Lamps|Lamp Output]]
==================================================

:guilabel:`Surface`
   Not an actual surface, but the final output of a :doc:`Lamp </render/cycles/lamps>` Object


[[Doc:2.6/Manual/Render/Cycles/World|World Output]]
===================================================

:guilabel:`Surface`
   The appearance of the environment, usually preceded by a :doc:`Background Shader </render/cycles/nodes/shaders#background>`
:guilabel:`Volume`
   *Currently under independent development, does nothing*
