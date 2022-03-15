
****
Hair
****

.. reference::

   :Panel:     :menuselection:`Render --> Hair`

.. _bpy.types.RenderSettings.hair_type:

.. Editors Note: This part of this page gets copied into:
.. - :doc:`</render/cycles/render_settings/hair>`

.. --- copy below this line ---

Shape
   :Strand:
      Render hair as a thin strand roughly a pixel wide. 
      Hair diameter parameters are ignored with this setting.

   :Strip:
      Render hair as a flat ribbon with rounded normals.

.. _bpy.types.RenderSettings.hair_subdiv:

Additional Subdivisions
   Additional subdivisions to be applied on top of the hair resolution set in the
   hair system settings. Increasing this value will smooth out the curves of the
   hair strands.
