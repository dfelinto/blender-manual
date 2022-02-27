
*****************
PDT Parts Library
*****************

The Menu For Parts library

.. figure:: /images/addons_pdt_library_1.png
   :align: left
   :width: 300px

.. container:: lead

   .. clear

This module is in its infancy for releases up to and including 1.1.5 and is an attempt to organise a collection of parts, as objects, in a central repository. This library will consist of Objects, Collections and Materials. For now, these are placed in a holding blend file in Blender’s:

"...../Scripts/Addons/clockworxpdt" folder (the location of the PDT Add-on).


Principles:
===========

The concept is to store parts as either individual objects, or in the case of more complex parts, like an engine assembly for example, as collections. The way Blender handles materials for append, or linked, objects is that if you load an object using Append, it will bring the materials of the object with it. If you append the part many times, you get many copies of the same material – not a situation that is efficient. So the recommendation for this trial system is to leave the materials off the objects and store them either against a “holder” object, or set a *f*ake user** so the material is always held in the library blend file. Then you can append, or link the material once and assign it to many copies of the appended, or linked object.

The plan is to expand the system so users can send objects, or collections, or material from their current open blend file to the Library blend file. This will be a further development in a later release, if this is possible. Parts Libraries have been in existence in CAD systems since the 1980’s where they were called “Cells” and had one, or many “Cell Libraries” to store them in, each cell had a user defined origin point that was used to place the part. The process was to put the cursor where you wanted the part, then call it by name and it would be placed with its origin at the cursor location.

PDT Parts Library uses the same method to store, recall and place parts at the cursor location:

.. figure:: /images/addons_pdt_library_2.png
   :align: left
   :width: 450px

.. container:: lead

   .. clear

This shows the Parts Library Menu and some sample parts brought in by either ``Appending``, or ``Linking``.


Parts Library File:
===================

The Parts Libraries can be located wherever you want them on your system. The location of your file, a normal Blender blend file, is set in the PDT Add-on Preference (User Preferences => Add-ons Tab):

.. figure:: /images/addons_pdt_library_4.png
   :align: left
   :width: 450px

.. container:: lead

   .. clear

You can either type in the location and name of the file, or click the ``Folder`` icon and use Blender file select tools to navigate to your file. The Selectors in PDT are then automatically updated with your file's objects, collections and materials, subject to any search criteria. this can be changed at any time in your session to access data from another library file.


The Options are:
================

``Append`` – this will append the chosen Object, Collection, or Material from the library into your current blend file.

``Link`` – this will link the chosen Object, Collection, or Material from the library into your current blend file.

Whether you are going to work with objects, collections, or materials depends on the setting of the **Selector** next to the Link button.

The next three **Selectors** will show the ``Objects``, ``Collections`` and ``Materials`` in the Library blend file, either all of them, or filtered by the Search input next to each Selector.

The ``Search`` strings consist of any characters that appear anywhere in the Object’s , Collection’s, or Material’s Name. So searching with ``gear`` in the search box will find, for example, objects named ``25T 20mm gear``, or ``gears – 20mm 25teeth``, etc.

The principle of operation is therefore:

* Place the 3D cursor where you want the objects to be located.
* Enter any required search criteria, to narrow the list shown in the selector.
* Select the type to work with; Objects, Collections, or Materials.
* Select the required object, collection, or material.
* Click either ``Append``, or ``Link``.

At the moment, if you bring in a collection, ALL objects in that collection are placed at the cursor location. The purpose of this is to bring in complex models and assume that they will be placed “as one” at the cursor location, this also assumes that they were built as a number of objects with a shared origin in the library.

The suggestion at this stage that materials can be imported and used on each object to which they are appropriate, it may be that many parts share a common material, in which case, using this approach does not result in many duplicate materials in the blend file.

The ``Show Library File`` button will show the user in a popup the location of the parts library file, this is also printed to the console, if you are running Blender from a Terminal. This purpose of this is to make it easier to locate the parts library for editing.

The library file can be opened in Blender and edited like any blend file to add your own objects, collections and materials.

Here is an example of a series of engines that are used in many different bikes, trikes and three-wheelers, these have been Appended from the library file to a working blend file, then the materials assigned:

.. figure:: /images/addons_pdt_library_3.png
   :align: left
   :width: 450px

.. container:: lead

   .. clear

Each engine is modelled as a set of individual objects, organised as collections in the library blend file. All individual objects in each collection share a common origin point so they can be placed in the correct relative location.

An alternative under consideration at this stage would be to store in the parts library, only the unique components of these engines, they share cylinder barrels for example, then append, or link these into a project file and build whichever engine is required.

The system has been left deliberately fluid at this stage in development, so ideas can be explored and the system refined. it may be obviated by developments in Blender towards better and more capable Asset Management Systems.
