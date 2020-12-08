:orphan:

Shader AOV
----------

Shader AOVs (Arbitrary Output Variables) provide custom render passes for any shader node components.
As an artist this can be a good way to fix or tweak fine details of a scene in post-processing.
To use Shader AOVs create the pass in the *Shader AOV* panel then reference this pass with
the :doc:`AOV Output </render/shader_nodes/output/aov>` shading node.
Shader AOVs can be added or removed in the *Shader AOV* panel.
In this panel is a list of all AOV passes; each AOV in the list consists of a *Name* and *Data Type*.

Name
   The name of the render pass; this is the *Name* that is referenced in the *AOV Output* node.
   Any names can be used for these passes,
   as long as they do not conflict with built-in passes that are enabled.

Data Type
   Shader AOVs can either express a *Color* or a *Value* output.
   The *Color* type as the name suggest can be used for a color but also for normals.
   A *Value* type can be used for any single numerical value.
