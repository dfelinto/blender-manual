
*****
Proxy
*****

Proxy Settings
==============

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar region --> Proxy & Timecode --> Proxy Settings`

Storage
   Defines whether the proxies are for individual strips or the entire sequence.

   Per Strip
      Proxies are stored in the directory of the input.
   Project
      All proxies are stored in one directory.

      Proxy Directory
         The location to store the proxies for the project.

Set Selected Strip Proxies
   Set proxy size and overwrite flag for all selected strips.

Rebuild Proxy and Timecode Indices
   Generates Proxies and Timecodes for all selected strips,
   same as doing :menuselection:`Strip --> Rebuild Proxy and Timecode indices`.


.. _bpy.types.SequenceProxy:

Strip Proxy & Timecode
======================

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar region --> Proxy & Timecode --> Strip Proxy & Timecode`

.. figure:: /images/video-editing_sequencer_sidebar_proxy_panel.png
   :align: right

Once you have chosen the :term:`Proxy`/:term:`Timecode` parameters,
you need to select all strips for which you want proxies to be built.
Then use :menuselection:`Strip --> Rebuild Proxy and Timecode indices`, or button in `Proxy Settings`_ panel.
Once all proxies are built, they will be ready to use.

In order to use proxies, you have to select matching :ref:`Proxy Render Size <bpy.types.SpaceSequenceEditor.proxy_render_size>`
in Sequencer preview Sidebar panel.

Custom Proxy
   Directory
      By default, all generated proxy images are storing to
      the ``<path of original footage>/BL_proxy/<clip name>`` folder,
      but this location can be set by hand using this option.
   File
      Allows you to use pre-existing proxies.

Resolutions
   Buttons to control how big the proxies are.
   The available options are 25%, 50%, 75%, 100 percent of original strip size.

Overwrite
   Saves over any existing proxies in the proxy storage directory.

Build JPEG Quality
   Defines the quality of the JPEG images used for proxies.

Timecode Index
   When you are working with footage directly copied from a camera without pre-processing it,
   there might be bunch of artifacts, mostly due to seeking a given frame in sequence.
   This happens because such footage usually does not have correct frame rate values in their headers.
   This issue can still arise when the source clip has the same frame rate as the scene settings.
   In order for Blender to correctly calculate frames and frame rate there are two possible solutions:

   #. Preprocess your video with e.g. MEncoder to repair the file header and insert the correct keyframes.
   #. Use Proxy/Timecode option in Blender.

   The following timecodes are supported:

   - No TC in use -- do not use any timecode
   - Record Run
   - Free Run
   - Free Run (rec date)
   - Record Run No Gaps

   .. note::

      Record Run is the timecode which usually is best to use, but if the clip's file is totally damaged,
      *Record Run No Gaps* will be the only chance of getting acceptable result.
