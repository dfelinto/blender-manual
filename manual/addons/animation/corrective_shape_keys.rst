
*********************
Corrective Shape Keys
*********************

From the Author(s):

I merged and converted two old scripts, to let you make corrective shape keys.
The first `script <http://www.apexbow.com/randd.html>`__ was created by Tal Trachtman in 2007 and
the second one I believe was done by Brecht. That one works with any combination of modifiers,
but it is very slow (like three minutes for a mesh with 4,000 points).
The other one works only with objects that have no more than one armature.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Animation then Corrective Shape Keys to enable the script.


Interface
=========

Located in the :menuselection:`Properties --> Object Data --> Shape Keys Specials`.


Usage
=====

#. Select a posed character object and click on *Create duplicate for editing* in the shape keys panel.
   This will create a copy of the mesh that you can edit/sculpt.
#. Select your sculpted copy and then the character object.
   Click on the little black arrow in the shape keys panel and choose one of the options shown in the image.
   If your object has only Armature modifiers, choose the faster method.
   If other (more complex?) modifiers are involved, or you want to incorporate dual quaternion skinning
   (now called *Preserve Volume* in the UI) you will have to use the slower method.

If all went right, your character or object should have the new shape key for your pose.
If not, double check that your mesh and armature object have no translation or rotation and try again.


Known Limitations
=================

- Target mesh may not have any transformation at object level, it will be set to zero.
- Fast/Armature method does not work with Bone envelopes or dual quaternions,
  both settings will be disabled in the modifier.


.. admonition:: Reference
   :class: refbox

   :Category:  Animation
   :Description: Creates a corrective shape key for the current pose.
   :Location: :menuselection:`Properties --> Object Data --> Shape Keys Specials`
   :File: animation_corrective_shape_key.py
   :Author: Ivo Grigull (loolarge), Tal Trachtman, Tokikake
   :Maintainer: to do
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
