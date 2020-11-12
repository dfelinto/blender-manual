
************
Introduction
************

Bones are the base elements of armatures.
The visualization of bones can be set in the Armatures :doc:`/animation/armatures/properties/display`.

.. (wip) are rigid.


.. (todo move)? to bone > properties > deform, extend control: fk

Classification
==============

Bones in an Armature can be generally classified into two different types:

#. Deforming Bones
#. Control Bones


Deforming Bones
---------------

Are bones which when transformed will result in vertices associated with
them also transforming in a similar way. Deforming Bones are directly involved in altering
the positions of vertices associated with their bones.


Control Bones
-------------

Are Bones which act in a similar way to switches,
in that, they control how other bones or objects react when they are transformed.
A Control Bone could for example act as a sliding switch control when the bone is in one
position to the left, it could indicate to other bones that they react in a particular way when
transformed, and when the Control Bone is positioned to the right,
transforming other bones or objects could do something completely different.
Control Bones are not directly used to alter the positions of vertices;
in fact, Control Bones often have no vertices directly associated with themselves.
