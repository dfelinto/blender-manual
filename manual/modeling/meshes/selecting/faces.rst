
Selecting Faces
***************

.. figure:: /images/selection-mode_buttons_face-activated.jpg

   Activated the Face Select Mode

To select parts of a mesh face-wise, you have to switch to Face Select Mode.
Do this by clicking the button shown above, or press :kbd:`Ctrl-Tab` to spawn a menu.
The selection works as usual with :kbd:`rmb` ; to add/remove to an existing selection, additionally press :kbd:`Shift`


Face Loops
==========

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode (Mesh)
   | Hotkey:   :kbd:`alt-rmb` - or :kbd:`shift-alt-rmb` for modifying existing selection


Face Loops are pretty much the same as Edge Rings. If you want to select a Face Loop,
there is no menu entry that works based on a selected face. Using :menuselection:`Select --> Edge Ring`
would select a "cross" with the prior selected face as the middle.
If you want to avoid switching to Edge Select Mode to select a Face Loop,
use the :kbd:`alt-rmb` shortcut.


.. figure:: /images/face-mode_different-loop-selections.jpg
   :width: 600px
   :figwidth: 600px

   Different Loopselect Operations on a grid in Face Select Mode


- Just the selected face.
- Select the face, then :menuselection:`Select --> Edge Ring`.
  See, how Blender selects edges, even if being in Face Select Mode.
  If these edges are desired and you want to work on them, switch in Edge Select Mode.
  Switching to Vertex Select Mode would flood the selection and leave you with the 4th image as result,
  after going back to Face Select Mode.
- Select the face, the :menuselection:`Select --> Edge Loop`.
  As in the example above, Blender pretends to be in Edge Select Mode and takes the four edges of the selected face
  as base for the selection operation.
- This selection was created by :kbd:`alt-rmb` on the left edge of the center face,
  followed by twice :kbd:`shift-alt-rmb` on the top edge of the center face. Two times,
  because the first click will remove the selected face loop (in this case, just the original selected face),
  while the second click will add the whole vertical running loop to the selection, creating the cross.


Ngons in Face Select Mode
=========================

.. figure:: /images/face-mode_ngon_visual-problem.jpg

   Ngon-Face having its center dot inside another face

As already known, faces are marked with a little square dot in the middle of the face.
With ngons that can lead in certain cases to a confusing display.
The example shows the center dot of the U-shaped ngon being inside of the oblong face inside the "U".
It is not easy to say which dot belongs to which face (the orange dot in the image is the object center).
Luckily, you don't need to care much - because to select a face, you don't have to click the center dot,
but the face itself.


.. tip:: Face selection

   *To select a face:*
   Click the face, not the dot!
