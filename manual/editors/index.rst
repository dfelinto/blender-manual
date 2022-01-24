.. _bpy.types.Space:

###########
  Editors
###########

Blender provides a number of different editors for displaying and modifying different aspects of data.
An Editor is contained inside an :doc:`Area </interface/window_system/areas>`
which determines the size and placement of the editor with in the Blender window.
Every area in Blender may contain any type of editor.

The *Editor Type* selector, the first button at the left side of a header,
allows you to change the Editor in that area,
it is also possible to open the same Editor type in different areas at the same time.

See :doc:`User Interface </interface/index>` for documentation on the general interface.

.. figure:: /images/editors_index_menu.png
   :align: center

   The Editor Type selector.


.. rubric:: General

.. toctree::
   :maxdepth: 1

   3dview/index.rst
   image/index.rst
   uv/index.rst
   shader_editor.rst
   compositor.rst
   geometry_node.rst
   texture_node/index.rst
   video_sequencer/index.rst
   clip/index.rst


.. rubric:: Animation

.. toctree::
   :maxdepth: 1

   dope_sheet/index.rst
   timeline.rst
   graph_editor/index.rst
   drivers_editor.rst
   nla/index.rst


.. rubric:: Scripting

.. toctree::
   :maxdepth: 1

   text_editor.rst
   python_console.rst
   info_editor.rst


.. rubric:: Data

.. toctree::
   :maxdepth: 1

   outliner/index.rst
   properties_editor.rst
   file_browser.rst
   asset_browser.rst
   preferences/index.rst
   spreadsheet.rst
