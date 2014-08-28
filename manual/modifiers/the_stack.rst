
Modifier
********

A modifier is defined as the application of a "process" or "algorithm" upon objects. They can
be applied interactively and non-destructively in just about any order the users chooses. This
kind of functionality is often referred to as a "modifier stack" and is found in several other
3D applications.

Modifiers are added from the :guilabel:`Modifiers` menu.  Some tools and scripts, for example :guilabel:`Decimate` and :guilabel:`Solidify`, have been migrated from its previous location and changed into a modifier.  In a modifier stack the order in which modifiers are applied has an effect on the result. Fortunately modifiers can be rearranged easily by clicking the convenient up and down arrow icons. For example, (*Stack ordering*) shows :doc:`SubSurf </modifiers/generate/subsurf>` and :doc:`Mirror </modifiers/generate/mirror>` modifiers that have switched places.


+---------------------------------------------------------------+---------------------------------------------------------------+
+.. figure:: /images/25-Manual-Modifiers-stackorder-example2.jpg|.. figure:: /images/25-Manual-Modifiers-stackorder-examp1e1.jpg+
+   :width: 300px                                               |   :width: 300px                                               +
+   :figwidth: 300px                                            |   :figwidth: 300px                                            +
+---------------------------------------------------------------+---------------------------------------------------------------+
+Stack ordering                                                                                                                 +
+---------------------------------------------------------------+---------------------------------------------------------------+


In the first example, the :guilabel:`Mirror` modifier is the last item in the stack.
The result looks like two surfaces.  In the other example the mirror modifier is the first
item in the stack and the result is a single merged surface.

You can see that the results look different from the previous.
This means that the stack order is very important in defining the end results.


Interface
*********

.. figure:: /images/25-Manual-Modifiers-Subsurf.jpg

   Panel Layout (Subsurf as an example)


Each modifier has been brought in from a different part of Blender,
so each has its own unique settings and special considerations. However,
each modifier's interface has the same basic components, see (*Panel Layout
(* :guilabel:`Subsurf` *as an example)*).

At the top is the :guilabel:`panel header`.
The icons each represent different settings for the modifier (left to right):

- Arrow — Collapse modifier to show only the header.
- Modifier icon and a box for the name of this modifier — default being the name of the modifier itself. It is unique amongst other modifiers of the same type.
- Camera — Display modifier effect during render time.
- Eye — Display modifier effect in the 3D view.
- Box — Shows modifier effect in :guilabel:`Edit mode`. This button may not be available depending on the type of modifier.
- Triangle — Applies modifier to editing cage in :guilabel:`Edit mode`.  This icon materializes the :guilabel:`Cage` mode.
- Up arrow — Moves modifier up in the stack.
- Down arrow — Moves modifier down in the stack.
- Cross — Removes the modifier from the stack.

Below the header are two buttons:

- :guilabel:`Apply` - Makes the modifier real.
- :guilabel:`Copy` - Creates a copy of the modifier at the base of the stack.

And below these buttons is a sub panel with settings for individual modifiers.


Stack
*****

.. figure:: /images/25-Manual-Modifiers-stackorder-example3.jpg

   In this example a simple subdivided cube has been transformed into a rather complex object using a stack of modifiers. (`.blend <http://wiki.blender.org/index.php/:File:25-Manual-Modifiers-example.blend>`__)


To add a modifier you add it to the *stack*. Once added (always at the bottom of the stack),
they can be rearranged to your liking.

Some modifiers can only be applied to certain object types. This is indicated by the panel
filtering the :guilabel:`Add Modifier` button on the :guilabel:`Modifiers` panel.
Only modifiers that can be applied are shown in this listbox button.
:guilabel:`Mesh` objects can have all available modifiers added, while, for example,
:guilabel:`Lattice` objects type objects can only have a few.


