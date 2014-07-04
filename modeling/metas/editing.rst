
Editing Metas
=============

When in :guilabel:`Edit` mode, the :guilabel:`Active Element` panel appears.
These settings apply only to the selected meta element.


+----------------------------------------------+
+.. figure:: /images/MetaPropertiesEditMode.jpg+
+   :width: 300px                              +
+   :figwidth: 300px                           +
+                                              +
+   the active element panel.                  +
+----------------------------------------------+


Meta Shape
----------

The :guilabel:`Type` menu lets you change the shape of the meta object, as explained above.


Stiffness
---------

Together with :guilabel:`Threshold`, :guilabel:`Stiffness` controls the influencing range. While the threshold is common to all metas in the same object (or even the same
FIXME(TODO: Internal Link;
[[#Object Family|object family]]
)), the stiffness is specific to each meta.

Scaling the inner green circle changes the :guilabel:`Stiffness` value.
Stiffness defines how much the meta object is filled.
This essentially defines how sensitive a meta is to being affected by other metas.
With a low stiffness, the meta will begin to deform from further away.
A higher value means the meta needs to be close to another one to begin merging.

When a :guilabel:`Meta` object comes within "range" of another meta,
the two will begin to interact with each other. They don't necessarily need to intersect,
and depending on the :guilabel:`Threshold` and :guilabel:`Stiffness` settings,
they most likely won't need to.
:guilabel:`Stiffness` is materialized by the
*FIXME(Tag Unsupported:span;
<span style="color:
lightgreen;">green ring</span>
)*.


The range is from **0.0** to **10.0**. But to be visible,
the :guilabel:`Stiffness` must be slightly larger than the :guilabel:`Threshold` value. You
can also visually adjust the :guilabel:`Stiffness` ring by using the :kbd:`rmb` to
select it and activate :guilabel:`Scale` mode with :kbd:`S`.


.. figure:: /images/MetaStiffness.jpg
   :width: 630px
   :figwidth: 630px

   Stiffness.


In (*Stiffness*), the meta ball labeled "\ ``A`` ",
has a smaller :guilabel:`Stiffness` value than the one labeled "\ ``B`` ".
As you can see, the
*FIXME(Tag Unsupported:span;
<span style="color:
lightgreen;">green ring</span>
)* radius is different for each of them.


Negative Influence
------------------

.. figure:: /images/2.5_Manual-Part-II-MetaObject-Metaball-Negative-Ex.jpg
   :width: 630px
   :figwidth: 630px

   Negative.


The opposite effect of a *positive* influence would be a *negative* influence:
the objects repel each other. (*Negative*)
shows a meta ball and a meta plane where the first is negative and the second, positive.
Notice how the negative meta is not visible: only the surrounding circles appear.
This is how Blender indicates that the object is negative.

Moving the sphere to the plane causes the plane's mesh to "cave in" or collapse inward.
If you move the plane away from the sphere, the plane's mesh will restore itself.

To make a meta *negative*, just select the meta in edit mode,
and check *negative* in the *active element* panel.


Hiding Elements
---------------

As in :guilabel:`Object` mode, you can hide the selected meta(s),
and then reveal what was hidden. This is very handy for cleaning your views up a bit… Note
that the two red and green rings always remain visible in :guilabel:`Edit` mode,
as well as the select circle (in :guilabel:`Object` mode…).

To hide the current selection, use :kbd:`H`,
the :guilabel:`Hide` toggle button in the :guilabel:`MetaBall tools`,
or the :menuselection:`Metaball --> Hide MetaElems --> Hide Selected` menu option.

To hide everything but the current selection,
hit :kbd:`shift-H` or use :menuselection:`Metaball --> Hide MetaElems --> Hide Deselected`.

To reveal what was hidden, use :kbd:`alt-H`,
or the relevant option in the same :menuselection:`Metaball --> Hide MetaElems` menu.
You can also un-toggle the :guilabel:`Hide` button in the (:guilabel:`MetaBall tools` panel).


Deleting Elements
-----------------

There is no :guilabel:`Erase` menu for metas,
just a confirmation pop-up asking you if you want to delete the selected metas.
Clear and simple!


Conversion
----------

.. figure:: /images/MetaConvertToMesh.jpg
   :width: 300px
   :figwidth: 300px

   the convert menu


You can only convert metas to meshes,
but here you have the option to keep the original :guilabel:`Meta` object (i.e.
create a new :guilabel:`Mesh` one, instead of a "real" conversion…).
Note that the resolution used for the new mesh is the :guilabel:`Wiresize` one,
not the :guilabel:`Rendersize` one.

To convert the meta, press :kbd:`alt-C` in :guilabel:`Object` mode, and select *mesh*


Object Families
===============

:guilabel:`Meta` objects have different behavior in :guilabel:`Object` mode than other object types - they can be "regrouped" into so-called "families".

A "family" is a way to regroup several meta objects,
producing something very similar to having several metas inside the same object.

A family is defined by the left part of an object's name (the one before the dot). Remember,
an object's name is the one in the "\ :guilabel:`OB` " field, in most panels,
**not** the "\ :guilabel:`MB` " field, which is the meta datablock's name… For example,
the *family* part of "\ ``MetaPlane.001`` " is "\ ``MetaPlane`` ".
Each meta object in the same "family" is associated with one another as discussed below.


.. figure:: /images/2.5_Manual-Part-II-MetaObject-Base-Ex.jpg
   :width: 300px
   :figwidth: 300px

   Meta ball base.


Families of metas are controlled by a *base* :guilabel:`Meta` object which is identified by
an :guilabel:`Object` name **without** a right part. For example,
if we have five metas called "\ ``MetaThing`` ", "\ ``MetaThing.001`` ",
"\ ``MetaThing.002`` ", "\ ``MetaThing.003`` " and "\ ``MetaThing.004`` ",
the *base* :guilabel:`Meta` object would be "\ ``MetaThing`` ".

The *base* :guilabel:`Meta` object determines the basis, the resolution, the threshold,
*and* the transformations. It also has the material and texture area.
The *base* meta is effectively the parent of
(or perhaps a better word to use is "the owner of") the other metas in the group (i.e.
it is as if the other metas were "included" or joined into the base one).


Examples
--------

(*Meta ball base*) shows the *base* meta labeled "\ ``B`` ". The other two :guilabel:`Meta` objects are *children*. Children's selection rings are always black, while the group's mesh is orange. Because the metas are grouped, they form a unified mesh which can always be selected by selecting the mesh of any meta in the group. For example, in the example (*Meta ball base*), only the lower sphere (the parent) has been selected, and you see that both the parent's mesh *and* all of the children's meshes are now highlighted.


.. figure:: /images/2.5_Manual-Part-II-MetaObject-Base-Scale-Ex.jpg
   :width: 300px
   :figwidth: 300px

   Scaling the "base".


The *base* :guilabel:`Meta` object controls the **polygonalization** (mesh structure)
for the group, and as such, also controls the polygonalization for the children (*non-base*)
metas. If we transform the *base* meta, the children's polygonalization changes. However,
if we transform the children, the polygonalization remains unchanged.


Hints
-----

This discussion of "polygonization" *doesn't* mean that the various meshes don't deform
towards or away from each other (meta objects always influence one another in the usual way,
whether or not they are members of the same family). Rather,
it means that the underlying mesh structure changes only when the *base* object transforms.
For example, if you scale the *base*, the children's mesh structure changes. In
(*Scaling the "base"*), the *base* has been scaled down,
which has the effect of scaling the mesh structure of each of the children. As you can see,
the children's mesh resolution has increased, while the *base* decreased.
*The children did not change size!*


