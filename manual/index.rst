
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  Blender |BLENDER_VERSION| Reference Manual
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Welcome to the manual for `Blender <https://www.blender.org>`__,
the free and open source 3D creation suite.

.. see T64071 for why we don't use ':download:'

.. only:: builder_html

   This site can be used offline:

   - `Download the manual (HTML) <blender_manual_html.zip>`__
   - `Download the manual (EPUB) <blender_manual_epub.zip>`__


Getting Started
===============

.. only:: builder_html and (not singlehtml)

   .. container:: tocdescr

      .. container:: descr

         :doc:`/getting_started/about/index`

      .. container:: descr

         :doc:`/getting_started/installing/index`

      .. container:: descr

         :doc:`/getting_started/configuration/index`

      .. container:: descr

         :doc:`/getting_started/help`

Sections
========

.. only:: builder_html and (not singlehtml)

   .. container:: tocdescr

      .. container:: descr

         .. figure:: /images/index_interface.jpg
            :target: interface/index.html

         :doc:`/interface/index`
            An introduction to Blender's window system, widgets and tools.

      .. container:: descr

         .. figure:: /images/index_editors.jpg
            :target: editors/index.html

         :doc:`/editors/index`
            Overview of the interface and functionality of all editors.

      .. container:: descr

         .. figure:: /images/index_scene.jpg
            :target: scene_layout/index.html

         :doc:`/scene_layout/index`
            Objects and their organization into scenes, view layers and collections.

      .. container:: descr

         .. figure:: /images/index_modeling.jpg
            :target: modeling/index.html

         :doc:`/modeling/index`
            Meshes, curves, metaballs, text, modeling tools, and modifiers.

      .. container:: descr

         .. figure:: /images/index_painting.jpg
            :target: sculpt_paint/index.html

         :doc:`/sculpt_paint/index`
            Sculpting, texture painting and vertex painting.

      .. container:: descr

         .. figure:: /images/index_grease-pencil.jpg
            :target: grease_pencil/index.html

         :doc:`/grease_pencil/index`
            2D drawing and animation with Grease Pencil.

      .. container:: descr

         .. figure:: /images/index_animation.jpg
            :target: animation/index.html

         :doc:`/animation/index`
            Keyframes, drivers, constraints, armatures and shape keys.

      .. container:: descr

         .. figure:: /images/index_physics.jpg
            :target: physics/index.html

         :doc:`/physics/index`
            Physics simulations, particle systems and dynamic paint.

      .. container:: descr

         .. figure:: /images/index_render.jpg
            :target: render/index.html

         :doc:`/render/index`
            Rendering and shading with Eevee, Cycles and Freestyle.

      .. container:: descr

         .. figure:: /images/index_compositing.jpg
            :target: compositing/index.html

         :doc:`/compositing/index`
            Post-processing with the compositing nodes.

      .. container:: descr

         .. figure:: /images/index_movie-clip.jpg
            :target: movie_clip/index.html

         :doc:`/movie_clip/index`
            Video motion tracking & masking.

      .. container:: descr

         .. figure:: /images/index_sequencer.jpg
            :target: video_editing/index.html

         :doc:`/video_editing/index`
            Video editing with the sequencer.

      .. container:: descr

         :doc:`/files/index`
            Data-block management and the structure of blend-files.

      .. container:: descr

         :doc:`/addons/index`
            Additional functionality available as add-ons.

      .. container:: descr

         :doc:`/advanced/index`
            Python scripting, how to write add-ons and a reference for command-line arguments.

      .. container:: descr

         :doc:`/troubleshooting/index`
            Solving crashes, graphics issues and Python errors, recovering data and reporting bugs.

      .. container:: descr

         :doc:`Glossary </glossary/index>`
            A list of terms and definitions used in Blender and this manual.

      .. container:: descr

         :ref:`Manual Index <genindex>`
            A list of terms linked to the Glossary.


.. only:: latex or epub or singlehtml

   .. toctree::
      :maxdepth: 1

      getting_started/index.rst
      interface/index.rst
      editors/index.rst
      scene_layout/index.rst
      modeling/index.rst
      sculpt_paint/index.rst
      grease_pencil/index.rst
      animation/index.rst
      physics/index.rst
      render/index.rst
      compositing/index.rst
      movie_clip/index.rst
      video_editing/index.rst
      files/index.rst
      addons/index.rst
      advanced/index.rst
      troubleshooting/index.rst
      glossary/index.rst


Get Involved
============

This manual is maintained largely by volunteers.

Please consider to join the effort and :ref:`Contribute to this Manual <about-user-contribute>`.

.. just so this is included in the toc (not user visible).

.. toctree::
   :hidden:

   about/index.rst
