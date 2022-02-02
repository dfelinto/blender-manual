
************
Feature Sets
************

Rigify allows third party developers to implement sub-add-ons, called *Feature Sets*,
which can provide new :doc:`Meta-Rigs </addons/rigging/rigify/metarigs>` and
:doc:`Rig Types </addons/rigging/rigify/rig_types/index>`. Similar to regular add-ons,
they can be installed from zip-files through Rigify settings.

These are some examples of *Feature Sets* currently provided by past and current Rigify developers:

`Cessen's Rigify Extensions <https://github.com/cessen/cessen_rigify_ext>`__
   This feature set provides the original Rigify rigs by Nathan Vegdahl, minimally ported
   and repackaged to work without switching Rigify to legacy mode. Note that their names
   were changed, so meta-rigs designed for legacy mode aren't directly compatible.

`Experimental Rigs by Alexander Gavrilov <https://github.com/angavrilov/angavrilov-rigs>`__
   Rig experiments, some of which might be included in Rigify in the future. Examples include
   limbs with an extra IK system based at knee/elbow, a spline based tentacle, and more.

`Cloud Rig <https://gitlab.com/blender/CloudRig>`__
   This major conversion feature set by Demeter Dzadik implements the rig used by
   the Blender Animation Studio using the Rigify framework.

You can install these packages by clicking :menuselection:`Clone --> Download ZIP`,
and then install the downloaded file through Rigify settings.

Developer documentation is available on the `Blender Wiki <https://wiki.blender.org/wiki/Process/Addons/Rigify>`__.
