
*************
Edit Face Set
*************

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Edit Face Set`
   :Operator:  :ref:`bpy.ops.sculpt.face_set_edit`

Edits the :doc:`Face Set </sculpt_paint/sculpting/editing/face_sets>` under the cursor.


Tool Settings
=============

Mode
   The operation to apply to the face set.

   Grow Face Set
      Grows the face sets boundary by one face based on mesh topology.
   Shrink Face Set
      Shrinks the face sets boundary by one face based on mesh topology.
   Delete Geometry
      Deletes the faces that are assigned to the face set.
   Fair Positions
      Creates a smooth as possible geometry patch from the face set minimizing changes in vertex positions.
   Fair Tangency
      Creates a smooth as possible geometry patch from the face set
      minimizing changes in vertex :term:`tangents <Tangent>`.

Modify Hidden
   Apply the edit operation to hidden face sets.
