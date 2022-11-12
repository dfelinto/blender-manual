
****************
Sapling Tree Gen
****************

This add-on creates trees. There are many preset tree types to choose from or create your own.
The method is presented by Jason Weber & Joseph Penn in their paper "Creation and Rendering of Realistic Trees".


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Add Curve then Sapling Tree Gen to enable the script.


Interface
=========

.. figure:: /images/addons_add-curve_sapling_example.jpg
   :align: center
   :width: 640px

Located in the :menuselection:`3D Viewport --> Add --> Curve` menu.


Instructions
============

Once the tree is created there are eight settings to build your tree.
When creating your tree it's often best to use the settings in order until your familiar with them.


Geometry
--------

Bevel
   This determines whether the curve should be shown with its full thickness or only the underlying curve.
   Disabled by default to permit rapid feedback on parameter changes.
Bevel Resolution
   Determines how smooth the outline of the bevelled curve is.
   The lower this value, the smaller the number of vertices but
   the resulting geometry will be coarser.
Curve Resolution
   Changes the smoothness of the curve along its length. This is only relevant if *Handle Type* is set to Auto.

Handle Type
   Determines the method of interpolation of the curve between Bézier points.
   Vector type results in fewer vertices but straight segments.
   Auto type smooths the segments but requires more expensive geometry.
Shape
   Governs the distribution of branches in order to effect the overall shape of the tree.

   Custom Shape
      Customize the branch shape along the branch length.

Secondary Splits
   Change the style of secondary branches.
Branch Distribution
   Adjust branch distribution towards the top or bottom of the tree.
Branch Rings
   Grow the Branches in Rings.
Random Seed
   Sets the basis on which all random values for the tree are generated.
   This can be changed to allow different trees with the same basic parameters to be generated.

Tree Scale:
   Scale
      The underlying size of the tree in Blender units.
   Scale Variation
      The maximum amount that the scale of the tree can vary (up or down) from the value of *Scale*.
   Radius Scale
      The scale of the radius at the base of the tree.
   Radius Variation
      The maximum amount that the radius scale of the tree can vary (up or down) from the value of *Radius Scale*.

Preset:
   Preset Name
      The name of the preset to be exported. This will export all current properties of the tree to
      the Sapling preset folder as a py-file.
   Export Preset
      Export all current properties.
   Load Preset
      Any presets found in the Sapling preset directory may be imported when selected here.
   Limit Import
      This can be used to restrict what geometry is created when a preset is imported.
      If selected, only two levels of branches and no leaves will be generated.


Branch Radius
-------------

This sub menu contains the settings for the branch radius.
You can adjust the bevel and taper of the branches here.


Branch Splitting
----------------

This sub menu contains the settings for branch splitting.
You can adjust how the branches form and split here.
Settings include levels, height and angle of the split.


Branch Growth
-------------

This sub menu contains the settings for branch growth.
You can adjust how the branches grow here.
Settings include length, angle and curvature.


Pruning
-------

This sub menu contains the settings for pruning the branches.

#. Press the *Prune* checkbox and you will see the prune object next to the tree.
#. Change the settings to adjust the prune objects shape to form your tree.


Leaves
------

This sub menu contains the settings for leaves.

#. Press the *Show Leaves* checkbox and you will see leaves on the tree.
#. Press the *Make mesh* checkbox if you want to convert the curve to a mesh.

Settings include shape, object type, rotations and scale.


Armature
--------

This sub menu contains the settings to add an armature to your tree.
It's not recommended to use this function on highly complex trees as it may take time to compute.

#. Turn off leaves and prune if you have them on.
#. Press the *Use Armature* checkbox to add the armature to the tree.
#. Adjust the armature levels and bone length to your liking.
#. Do not pose the bones until you have finished the tree.
#. you are now ready to use the next sub menu *Animation*.


Animation
---------

This sub menu contains the settings to animate your tree.
It's recommended to finalize all your settings now.

#. You will need to have an armature already created above.
#. Press the *Armature Animation* checkbox to add the animation to the tree.
#. Press the *Leaf Animation* checkbox to add the animation to the leaves if you have them.
#. Press the *Fast Preview* checkbox to hide the leaves and bevel for fast animation playback in the viewport.

Settings include speed, wind strength and leaf animation.


.. reference::

   :Category: Add Curve
   :Description: Adds a parametric tree.
   :Location: :menuselection:`3D Viewport --> Add --> Curve --> Sapling Tree Gen`
   :File: add_curve_sapling folder
   :Author: Andrew Hale (TrumanBlending), Aaron Butcher, CansecoGPC
   :Maintainer: To Do
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
