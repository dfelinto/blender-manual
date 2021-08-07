
************
Introduction
************

Blender is a versatile software used for modeling, sculpting, 2D drawing, animation, and video editing.
Most of the work is done in so-called editors:
tools for viewing and modifying your work through a specific part of Blender.

There are a couple of editors that can manage video:
the :doc:`Compositor </editors/compositor>`, the :doc:`Movie Clip Editor </editors/clip/index>`,
the :doc:`Image Editor </editors/image/index>` (only for still images), and the Video Sequencer.

This section describes only the interface of the Video Sequencer,
to read more about usage of the Video Sequencer read the :doc:`Video Editing </video_editing/index>` section.


Editor Layout
=============

The VSE is composed of multiple areas (see figure 1). They are described in more detail in the next sections.
Figure 1 shows the combined view *Sequencer/Preview*. You can select this view with the View Type selector.
This view can contain the following areas:

.. figure:: /images/editors_vse_overview.svg
   
   Figure 1: Sequence Editor shown in the Sequencer & Preview view.
   
   Header (red), Preview (Yellow), Sequencer (blue), Properties (Grey),
   Panels & Tabs (Yellow), Toolbar (Purple)

Header
   This region displays menus and buttons for interacting with the editor.
   The header changes slightly depending on the selected view type (see below).
Preview
   This region shows the output of the sequencer at the time of the playhead.
Sequencer
   This region shows timeline for managing the montage of strips.
Properties
   This region shows the properties of the active strip.
   Is divided into panels and tabs. Toggle on or off with :kbd:`N` key.
Toolbar
   This region shows a list of icons, clicking on a icon will changes the active tool.
   Toggle on or off with :kbd:`T` key.


.. _bpy.types.SpaceSequenceEditor.view_type:

View Types
==========

The Video Sequencer has three view types which can be changed with the View Type menu (see figure 1; top left).

.. figure:: /images/editors_vse_view_types.svg
   
   Figure 2: Three view types for the Video Sequence Editor

Sequencer
   View timeline and strip properties.
Preview
   View preview window and preview properties.
Sequencer & Preview
   Combined view of preview and timeline and properties of both.

.. tip::

   It is possible to create multiple instances of any view type in single workspace.


Performance
===========

Playback performance can be improved through several ways.
The biggest impact on performance is to allow the Video Sequencer to cache the playback.
There are two levels of cache, the first is a RAM cache,
this is enabled by default but can be increased based on the amount of RAM available.
The next level of cache is a disk cache which stores cached strips on disk.
A disk cache can generally cache more than a RAM cache, but it can be slower.
Both of these cache options can be configured in the :ref:`Preferences <prefs-system-sound>`.

Another way to improve performance is by using :ref:`Strip Proxies <bpy.types.SequenceProxy>`.
These are used to cache images or movies in a file that is easier to playback
by reducing the image quality by either decreasing the resolution and/or compressing the image.
