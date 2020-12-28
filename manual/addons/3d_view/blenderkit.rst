
**********
BlenderKit
**********

`BlenderKit <https://www.blenderkit.com/>`__ is an online database of materials, brushes and 3D models
which you can search, download, upload and rate directly from the add-on.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click 3D View then BlenderKit Asset Library to enable the script.


Account and Login
-----------------

Click on the sign-up button to create a new account and activate it by pressing *Log in*
directly in BlenderKit settings. It will direct you to log in through our website.


Basic Usage
===========

#. Type a search term into the search field.
#. The result are shown in the Assetbar.
#. Drag-and-drop the material or model into your scene.

.. figure:: /images/addons_3d-view_blenderkit_search-sidebar.jpg
   :align: center
   :width: 300px

.. figure:: /images/addons_3d-view_blenderkit_assetbar.jpg
   :align: center
   :width: 300px

.. figure:: /images/addons_3d-view_blenderkit_drag-drop.jpg
   :align: center
   :width: 300px


Interface
=========

.. _bpy.ops.scene.blenderkit_download:
.. _bpy.ops.view3d.blenderkit_asset_bar:

Assetbar
--------

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Assetbar`

.. figure:: /images/addons_3d-view_blenderkit_assetbar.jpg
   :align: center
   :width: 600px

Assetbar shows search results and allows users to interact with them.
The Assetbar pops up when the search results are retrieved from the server.
It can be shown or hidden by clicking the toggle with the eye icon next to the search field.

Actions that can be performed in the Assetbar:

- Drag and dropping an object or material directly into the scene.
- Click a result to link/append it to the scene.
- Open the context menu of a result for further interaction:

  Open Authors Website
     Opens a web browser and goes to the web presentation that the author specified.
  Show Assets by Author
     Shows all assets uploaded by the author of the selected 3D model.
  Replace Active Models
     You need to select several assets to use this option from the Selected Model panel.
     All those selected will be replaced with the last asset selected (active).
     If you use this option from the context menu, the target asset is downloaded and replaces selected assets.

- Use the :kbd:`Wheel` to scroll the results.
- Click arrows on the side of the Assetbar for a jump to the next or previous page.


BlenderKit Profile Panel
------------------------

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar --> BlenderKit --> BlenderKit Profile`

.. figure:: /images/addons_3d-view_blenderkit_sidebar-search_bkprofile.jpg
   :align: right
   :width: 300px

This panel shows the user's login information and information about the user's public and private remaining storage.

See My Uploads
   Open the BlenderKit website and show a list of the author's assets.


BlenderKit Login Panel
----------------------

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar --> BlenderKit --> BlenderKit Login`

.. figure:: /images/addons_3d-view_blenderkit_sidebar-search_login.jpg
   :align: right
   :width: 300px

.. _bpy.ops.wm.blenderkit_login:

Log In
   Log in online on BlenderKit webpage.

.. _bpy.ops.wm.blenderkit_logout:

Log Out
   Log out from BlenderKit immediately.


Find and Upload Assets Panel
----------------------------

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar --> BlenderKit --> Find and Upload`

.. figure:: /images/addons_3d-view_blenderkit_search-sidebar.jpg
   :align: right
   :width: 300px

The main panel enables you to Search or Upload all supported asset types.

Search/Upload
   Switch the main panel between Search and Upload functionality.


Search and Download
-------------------

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar --> BlenderKit --> Find and Upload --> Search`

.. figure:: /images/addons_3d-view_blenderkit_sidebar-search-common.jpg
   :align: right
   :width: 300px


Models/Materials/Brushes
^^^^^^^^^^^^^^^^^^^^^^^^

Switch between asset types available in BlenderKit.

These fields are common for all asset types:

.. _bpy.ops.view3d.blenderkit_search:

Search
   Search assets by name.
Show (eye icon) :kbd:`;`
   Show/hide Assetbar interface.
Style
   Search filter limiting the results (realistic, painted, polygonal, and other).


Options Visible for Models Search
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar --> BlenderKit --> Find and Upload --> Search --> Models`

.. _bpy.data.scenes.blenderkit_models.own_only:

My Assets
   Search only for your 3D models.

.. _bpy.data.scenes.blenderkit_models.free_only:

Free Only
   Show only free models. This option is available only for models, since all Materials and all Brushes are free.

Search filters subpanel:

.. _bpy.data.scenes.blenderkit_models.search_condition:

Condition
   Condition of the object.

   New, Used, Old, Desolate

.. _bpy.data.scenes.blenderkit_models.search_design_year:

Designed In (min - max)
   When the object was approximately designed in terms of *year*.
   Can be used for parallel worlds or future :abbr:`sci-fi (Science Fiction)` dates
   (search for sci-fi assets by entering 2100 as minimum year).

.. _bpy.data.scenes.blenderkit_models.search_polycount:

Poly Count In (min - max)
   Use the poly count of 3D object for filtering.

.. _bpy.data.scenes.blenderkit_models.search_texture_resolution:

Texture Resolution (min - max)
   Limit search to the texture resolutions in a range.

.. _bpy.data.scenes.blenderkit_models.search_file_size:

File Size (min - max)
   Limit search file size. This uses the basic file size of the original file.


Categories
^^^^^^^^^^

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar --> BlenderKit --> Find and Upload --> Search --> Models --> Categories`

Category panel enables direct browsing of BlenderKit categories.

.. _bpy.ops.view3d.blenderkit_set_category:

Set Category ``>>``
   Visit subcategory.
Return ``↲``
   Return to parent category.


Import Method
^^^^^^^^^^^^^

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar --> BlenderKit --> Find and Upload --> Search --> Models --> Import settings`

.. figure:: /images/addons_3d-view_blenderkit_sidebar-search-models-importsettings-only.jpg
   :align: right
   :width: 300px

.. _bpy.data.scenes.blenderkit_models.link_method:

Link
   Link 3D model into Blender scene. Linked models are saved in original files.
   To edit them, you need to open the model in the subdirectory of your project: -- assets/models.
   Linking helps to keep file size low.

.. _bpy.data.scenes.blenderkit_models.append_method:

Append
   Append 3D model into Blender scene. Appended objects are included and editable in your scene.

.. _bpy.data.scenes.blenderkit_models.randomize_rotation:

Randomize Rotation
   Randomize the rotation of the model around the Z axis during placement in the Blender scene.

.. _bpy.data.scenes.blenderkit_models.perpendicular_snap:

Perpendicular Snap
   Limit snapping if the angle is close to perpendicular angles to become exactly perpendicular.
   Useful for placing lamps on curved ceilings, or placing trees on slopes and similar cases.

.. _bpy.data.scenes.blenderkit_models.perpendicular_snap_treshold:

Threshold
   Limit perpendicular snap.


Options Visible for Materials Search:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar --> BlenderKit --> Find and Upload --> Search --> Materials`

Search filters:

.. _bpy.data.scenes.blenderkit_mat.search_procedural:

Procedural/Texture Based/Both
   Limit search to only procedural or texture based materials.

.. _bpy.data.scenes.blenderkit_mat.search_texture_resolution:

Texture Resolution
   Limit search with resolution of the texture.

.. _bpy.data.scenes.blenderkit_mat.search_file_size:

File Size
   Limit search with file size.


Categories
^^^^^^^^^^

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar --> BlenderKit --> Find and Upload --> Search --> Materials --> Categories`

Same as the model search.

Set Category ``>>``
   Visit subcategory.
Return ``↲``
   Return to parent category.


Import Settings
^^^^^^^^^^^^^^^

.. _bpy.data.scenes.blenderkit_mat.automap:

Auto-Map
   Add cube mapping UV to the object after drag drop.
   This allows most materials to be applied instantly to any mesh.
   BlenderKit generates a new UV map called 'automap', and doesn't replace your previous UV maps.
   The action also resets texture space of the target object to (1.0, 1.0, 1.0).
   This enables most procedural materials to have correct scaling.


Upload
------

Models/Materials/Brushes
   Switch between asset types which are available to upload in BlenderKit.


Common Options for All Assets Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: /images/addons_3d-view_blenderkit_sidebar-upload-model-public-design.jpg
   :align: right
   :width: 300px

Hide Asset Preview
   Show/Hide asset preview, which shows how approximately will the asset look for people searching the database.

.. _bpy.ops.wm.url_open:

Read Upload Instructions
   Open the `Upload manual <https://www.blenderkit.com/docs/upload-tutorials/>`__ on the BlenderKit website.
   Read the manuals for `models <https://www.blenderkit.com/docs/upload/>`__,
   `materials <https://www.blenderkit.com/docs/uploading-material/>`__,
   and `brushes <https://www.blenderkit.com/docs/uploading-brush/>`__ on the website.

Upload
   Upload or re-upload the 3D model.
   In the operator you can choose if you want to update the files.
   If both file and thumbnail are off, only metadata gets updated.
Category
   Main category to place the model into.
Subcategory
   Subcategory to place the model into.

.. _bpy.data.materials.blenderkit.is_private:

Private/Public
   Set the assets privacy. Assets marked as Public go into
   the `Validation <https://www.blenderkit.com/docs/validation-status>`__
   process automatically. Private assets will be hidden to the public.
   Private assets are limited by a quota.

.. _bpy.data.materials.blenderkit.license:

License
   BlenderKit offers two `licenses <https://www.blenderkit.com/docs/licenses>`__ for the assets.
   Both licenses allow for non-commercial and commercial use.

   :Royalty free: Royalty-free commercial license
   :Creative Commons Zero: Creative Commons Zero

.. figure:: /images/addons_3d-view_blenderkit_thumbnail-generator.jpg
   :align: right
   :width: 300px

.. _bpy.data.materials.blenderkit.name:

Name
   Name of your asset.

.. _bpy.data.materials.blenderkit.thumbnail:

Thumbnail
   Thumbnail. Path to the thumbnail a square image (at least 512×512 JPG image).

Generate Thumbnail
   Automatically generate a thumbnail for the 3D model assets.

.. _bpy.data.materials.blenderkit.description:

Description
   Describe the properties of the object in detail. Do not include obvious technical specifications.

.. _bpy.data.materials.blenderkit.tags:

Tags
   List of tags, separated by commas. Include at least three tags.


Options Specific for Models
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _bpy.objects.blenderkit.style:

Style
   Define the visual style of the asset.

   :Realistic: Photo-realistic model
   :Painterly: Hand-painted with visible strokes
   :Mostly: For games
   :Low-poly art: Do not mix up with poly count!
   :Anime: Anime style
   :2D Vector: 2D vector graphics
   :3D graphics: 3D graphics
   :Other: Other style
   :Any: Any style

.. _bpy.objects.blenderkit.production_level:

Production Level
   Production state of the asset. Also template should be actually finished,
   just the nature of it can be a template, like a thumbnail scene,
   finished mesh topology as start for modeling or similar:

   :Finished:
      For public database, the asset should always be ready for rendering.
      Assets without materials aren't accepted into the public database.
   :Template:
      Templates are models that have general usability, and have clear description of
      how the asset is supposed to work. An example can be a beverage can with a prepared texture slot.

.. _bpy.objects.blenderkit.condition:

Condition
   Condition of the object.

   New, Used, Old, Desolate

.. _bpy.objects.blenderkit.is_free:

Free for Everyone
   You consent you want to release this asset as free for everyone,
   under the license specified in the license field.

.. _bpy.objects.blenderkit.pbr:

PBR Compatible
   Is compatible with `PBR standard <https://www.blenderkit.com/docs/pure-pbr-assetes>`__.

Design properties:

   .. _bpy.objects.blenderkit.manufacturer:

   Manufacturer
      Company making the design piece or product.

   .. _bpy.objects.blenderkit.designer:

   Designer
      Author of the original design piece depicted.
      Usually not you -- fill in your name and personal statement in your profile on BlenderKit webpage.

   .. _bpy.objects.blenderkit.designer_collection:

   Design Collection
      Fill if this piece is part of a real-world design collection.

   .. _bpy.objects.blenderkit.design_variant:

   Variant
      Color or material variant of the product.

   .. _bpy.objects.blenderkit.use_design_year:

   Design Year
      Time when the item was designed.
      It can also be used for living creatures and other objects,
      for example, for a dinosaur you can set it to something like 240 million years.

   .. _bpy.objects.blenderkit.work_hours:

   Work Hours
      How long it takes to finish the asset? This value isn't used in BlenderKit score mechanism,
      but serves as comparison for administrators on how `rating system performs <https://www.blenderkit.com/docs/rating>`__

   .. _bpy.objects.blenderkit.adult:

   Adult Content
      Mark adult content.


Options Specific for Materials Only
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: /images/addons_3d-view_blenderkit_sidebar-upload-material.jpg
   :align: right
   :width: 300px

.. _bpy.data.materials.blenderkit.pbr:

Pure PBR Compatible
   Is compatible with `PBR standard <https://www.blenderkit.com/docs/pure-pbr-assetes>`__.
   This means only image textures are used with no procedural textures and no color correction, only PBR shader is used.

.. _bpy.data.materials.blenderkit.uv:

Needs UV
   Requires an UV set.

.. _bpy.data.materials.blenderkit.animated:

Animated
   The material is animated.

.. _bpy.data.materials.blenderkit.texture_size_meters:

Texture Size in Meters
   If the material uses Textures, this value sets the length of one side of the texture.
   This value is very important so that the materials apply with correct scale.

Thumbnail
   Path to the thumbnail (512×512 jpg-file image).
   Needs always to be the image generated with the BlenderKit thumbnail generator, or with the same look.
   Only exceptions are special effects like fire.

.. _bpy.ops.object.blenderkit_material_thumbnail:

Render Thumbnail with Cycles
   Generate a thumbnail in the background. Use only this tool for thumbnails.


Selected Model/Name Panel
-------------------------

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar --> BlenderKit --> Selected model`

This panel shows up if you select a 3D model downloaded from BlenderKit.
Name of the model appears below.

Bring to Scene
   Bring linked object hierarchy to scene and make it editable.
   This is similar as if you would originally append the asset.
Ratings
   You can rate the assets by giving them stars with a maximum of 10.
Work Hours
   Estimate how many hour you saved thanks to this asset.
   Rating helps BlenderKit distribute rewards to authors,
   and thus it is very important to rate assets and do it in a fair way.

Asset tools:

Open Authors Website
   Opens a web browser and goes to the web presentation that the author specified.

Show Assets by Author
   Shows all assets uploaded by the author of the selected 3D model.

Replace Active Models
   You need to select several assets to use this option from the *Selected Model* panel --
   all will be replaced with the last asset selected (active). If you use this option from
   the context menu, the target asset is downloaded and replaces selected assets.

The same options are available when you right click in the Assetbar.

Management Tools:
   Delete
      Change asset status.

Downloads:
   This panel is visible when there are running downloads.
   You can cancel downloading of assets by pressing the ``X`` button.
   This cancels the download immediately and deletes the file on your computer.


Preferences
===========

.. figure:: /images/addons_3d-view_blenderkit_preference-open.jpg
   :align: center
   :width: 600px

Show Assetbar when Starting Blender
   Shows Assetbar after Blender startup.
Log out
   Log out from BlenderKit immediately.
Your API Key
   The BlenderKit API Key stores your API key that is retrieved automatically
   when you Login to the service, and is used to connect to BlenderKit server.
   Don't change this value manually.
Global Files Directory
   Global storage for your asset files. Set this up on a hard drive where you have enough space to store the assets.
Project Assets Subdirectory
   Naming of the subdirectory where your assets will be stored.
   For each blend-file where you use BlenderKit assets, a subdirectory will be created in the same folder.
   This enables you to compress the whole directory and transfer it to a render farm or another workstation.

Use Directories:
   Which directories will be used for storing download data.

   :Global and Subdirectory:
      Use both previously mentioned methods.
   :Global:
      Store downloaded files only in global directory. This saves drive space -- assets are only stored in one place.
      You have to pack your project carefully when transferring it to another computer,
      since the assets won't be in the subfolder of the current project.
   :Local:
      store downloaded files only in local directory.
      This option can use more bandwidth when you reuse assets in different projects,
      since the add-on won't find assets that are already in different folders.
      However, it enables you to pack your projects easily.

Use GPU for Thumbnails Rendering
   By default the CPU is used so that the user can continue their work while the thumbnail renders in the background.
Asset Thumbnail Size
   Size of the asset thumbnails in the Assetbar UI element.
Max Assetbar Rows
   Number of rows for the Assetbar UI element.
Show Tips when Starting Blender
   Show tips when starting Blender.
Show BlenderKit Search in 3D Header
   Show extra keyword search field in the header of the 3D viewport.
   This enables fast access to search with a hidden Sidebar.


Tutorials
=========

.. youtube:: pSay3yaBWV0
   :width: 500px

.. admonition:: Reference
   :class: refbox

   :Category:  Add Mesh
   :Description: Online Blenderkit Library, materials, models, brushes and more.
   :Location: :menuselection:`3D Viewport --> Sidebar --> Blenderkit`
   :File: blenderkit folder
   :Author: Vilem Duha, Petr Dlouhy
   :Maintainer: Vilem Duha
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
