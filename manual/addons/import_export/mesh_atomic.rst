
************************
Atomic Blender (PDB/XYZ)
************************

The Atomic Blender (PDB/XYZ) add-on imports atomic structures
(molecules, crystals, clusters, particles, surfaces, etc.), which are described in
PDB (``.pdb``) and XYZ files (``.xyz``) (`Import PDB/XYZ`_). The add-on reads the coordinates of
all atoms in the PDB/XYZ file and represents the atoms as balls in the Blender world.
Also the sticks, which are described in PDB files only, can be shown if the sticks are listed in the PDB file.
For the import, many options can be chosen, which allow representing the atoms and sticks in different ways.
With help of several tools in the `Atomic Blender Utilities panel`_, the atomic structures can be modified
after the import. Note that the coordinates of selected atomic structures in the Blender 3D world
can also be exported into PDB/XYZ files.

Atomic Blender (PDB/XYZ) is interesting for scientists, who want to
visualize their atomic structures described in PDB or XYZ files with Blender.
Thanks to Blender, fancy graphics of molecules, crystal structures, surfaces,
nanoparticles, clusters and complex atomic arrangements can be obtained.
Such graphics meet the standards of top-level journals, which have a high impact factor.
See `Examples`_ at the end of this page.

.. seealso:: Info about PDB and XYZ

   - Description of the PDB file format:
     `Wikipedia <https://en.wikipedia.org/wiki/Protein_Data_Bank_(file_format)>`__ and
     `RCSB <https://www.rcsb.org/pdb/static.do?p=file_formats/pdb/index.html>`__.
   - Description of the XYZ file format:
     `Wikipedia <https://en.wikipedia.org/wiki/XYZ_file_format>`__ and
     `Open Babel <https://openbabel.org/docs/dev/FileFormats/XYZ_cartesian_coordinates_format.html>`__.
   - Some notes about PDB and XYZ files can also be found on one of
     the `developer's site <https://development.root-1.de/Atomic_Blender_PDB_XYZ.php>`__ and
     `remarks <https://development.root-1.de/Atomic_Blender_PDB_XYZ_Remarks.php>`__.
   - Many molecules can be downloaded from the `RCSB site <https://www.rcsb.org/>`__ (go to 'Download').
   - A list of software that deals with PDB in different ways can be found on
     the `RCSB site <https://www.rcsb.org/pages/thirdparty/molecular_graphics>`__. There also is
     `Vesta <https://jp-minerals.org/vesta/en/>`__, `ASE <https://wiki.fysik.dtu.dk/ase/>`__ and all the
     `quantum chemical calculators <https://en.wikipedia.org/wiki/List_of_quantum_chemistry_and_solid-state_physics_software>`__
     used in research, which can create or even calculate atomic structures and store them in PDB/XYZ files.

.. seealso:: Forum

   - Please, use the `Blender Artists forum <https://blenderartists.org/t/1197801>`__ for comments and questions.
   - There also is the possibility to ask questions on
     `Stack Exchange <https://blender.stackexchange.com/>`__. However,
     note that some of the developers (like Blendphys) don't have enough credits,
     which are needed to give answers on Stack Exchange.

.. hint:: Defects in an Atomic Structure

   If you want to show defects like vacancies in an atomic structure, use an 'X' for
   the element name in the PDB or XYZ file. A defect is shown in the form of a cube.


Import PDB/XYZ
==============

.. figure:: /images/addons_import-export_mesh-atomic_import-PDB.png
   :align: right
   :width: 239px

   The panel with the options for PDB import.


Camera & Lamp
-------------

A camera and/or a light source are placed into the 3D world.
Both are placed such that the entire atomic structure can be well seen by
the camera with enough light from the light source.


Object to Origin (PDB)
----------------------

The atomic structure is placed into the origin (0.0, 0.0, 0.0) of the 3D world.


Object to Origin (XYZ)
----------------------

Either in only *the first* or in *all frames*, the atomic structure is put into
the origin (0.0, 0.0, 0.0) of the 3D world.


Balls/Atoms
-----------

Type Of
   Choose either *NURBS*, *Mesh* or *Metaballs* for the atoms.
   For option *Mesh* the *Azimuth* and *Zenith* values can be chosen.
   Metaballs can lead to some fancy effects: for instance,
   if enough large, their shapes melt together showing some kind of surface effect.

.. figure:: /images/addons_import-export_mesh-atomic_import-XYZ.png
   :align: right
   :width: 238px

   The panel with the options for XYZ import.

Scaling Factors
   The atom radii as well as the distances between the atoms can be scaled by a simple factor.

Type
   The type of atom radius (atomic, van der Waals or as specified in the custom data file [predefined]) can be chosen.


Sticks/Bonds (only PDB)
-----------------------

Use Sticks
   Use sticks or not.

Type
   In general, the options *Sector* and *Radius* determine the precision and dimension of the sticks, respectively.
   Option *Smooth* always means that a Smooth operator is applied on the sticks.
   Option *Color* means that the stick is divided into two parts,
   showing the colors of the respective two atoms which it connects.

   Instancing Vertices
      The sticks of one element are put into one instancing vertices structure and the sticks appear as cylinders.
      The instancing vertices structure makes the displaying and loading of many sticks relatively fast
      (`Separate Atoms`_ for more info). Options *Unit* is the length of a unit (a small cylinder):
      several of such units are put together forming actually the stick (cylinder).
      The longer the unit length is the less is the number of such units and
      thus the faster is the displaying. However, if the unit length is too long the stick becomes
      eventually longer than the bond length, which the stick will actually represent.
      This then creates some overlapping effects. Option *Bonds*
      displays apart from single also double, triple, etc. bonds whereas
      option *Distance* is the corresponding bond distance measured in stick diameter.
   Skin
      The skin and subdivision modifiers are used to build the sticks.
      This gives a nice network of sticks, which can be used to show,
      e.g. only the bonds of the structure (delete the atoms before!).
      Options *SubDivV* and *SubDivR* are parameters of the subdivision operator.
      If option *Smooth* is activated, the initial squarish profile of the sticks changes to a more circular one.
      Note that if this option is chosen, there is only one object representing all sticks.
   Normal
      Normal cylinders are used. For each bond, one individual cylinder is used.
      If option *One Object* is activated, about *No* sticks are joined into one mesh object.
      This makes displaying the sticks very fast. However, individual sticks do not exist anymore.


Frames (only XYZ)
-----------------

Load All Frames
   Load only the first or all frames.

Skip Frames
   Skip and load only each n-th frame. This is quite useful for large data
   where it might be sufficient to show only each 4th frame.

Frames/Key
   Show a specific number of frames per key. Many frames in a key lead to a more fluid presentation.

.. important::

   The number of atoms in a frame has to be the **same** for all frames!


Atomic Blender Utilities Panel
==============================

The *Atomic Blender Utilities* panel makes your life easier during manipulating
atoms of imported structures.

.. figure:: /images/addons_import-export_mesh-atomic_utilities-panel.png
   :align: right
   :width: 211px

   The *Atomic Blender Utilities* panel.


Custom Data File
----------------

A separate custom data file containing all types of radii and colors of the atoms can be loaded.
Such an option is useful when it is desired to use predefined values for radii and colors.
An example can be downloaded from here:
`Custom data file <https://development.root-1.de/X-Download/atom_info.dat>`__.

The custom data file is an ASCII file, which can be duplicated and modified by the user.
The radius and/or color of the atoms can be permanently changed as follows:
Open the ASCII file with a standard text editor, search the name of the atom
and change the radius (``Radius used``). Do the same with the RGB values for the color.
The value RGBA(1.0, 1.0, 1.0, 1.0) corresponds to white and RGBA(0.0, 0.0, 0.0, 1.0) is black.
Note that the last value of a color tuple is the alpha value of the color.

Inside Blender, the data file needs to be loaded first. The colors and radii
are changed after executing *Apply*. Note that only selected atoms are changed.


Measure Distances
-----------------

This is to measure the distance of two objects in Object Mode but also in Edit Mode.
The unit is Ångström.


Change Atom Size
----------------

Type of Radii
   Type
      With this selector the type of radii can be chosen.
      Either one uses *Predefined*, *Atomic* or *Van der Waals* radii.
      The default values for Predefined radii are the *Atomic* radii.
   Charge
      For option *Ionic radii*, the charge state can be chosen and the radii of selected objects
      are instantaneously changed. Select one type of atom (e.g. only all hydrogen ones)
      and then apply the charge state. Changes only apply if a charge state of an atom is available.

Radii in pm
   All radii of a specific type of atom can be manipulated.
   Type in the name of the atom (e.g. 'Hydrogen') and choose the radius in picometer.

Radii by Scale
   This modifies the radii of all atoms with one scaling factor.
   Type in the scaling factor and increase or decrease the size of the radii by
   using the *Bigger* or *Smaller* button, respectively.


Change Stick Size
-----------------

The diameter of the sticks are changed. The buttons *Bigger* and *Smaller*
allow increasing or decreasing the diameter, respectively.
The scale factor determines, how strong the change of diameter will be.
By using the Outliner, one can apply these operators on only a selection of sticks
(e.g. only the sticks of the hydrogen atoms). Note that changes only apply
if the sticks are individual objects, e.g. single cylinders or if the sticks are described
in instancing vertices structures.


Change Atom Shape
-----------------

It is possible to change the shape (sphere, cube, icosphere, etc.) and
material of the atoms. First, select your atoms in the 3D Viewport or the Outliner.

Shape
   Choose the shape in the first selector.
Material
   Choose one of the materials in the second selector. The materials are only examples,
   further refinements can be done in the Materials tab of the Properties.
Special
   Here, you can choose an object with a special shape, material, etc.
   Such objects are quite nice to represent defects in atomic structures.
   When choosing such a special object, you cannot anymore separately choose
   the shape and material from above. In the Objects and Materials tabs of the Properties
   further changes can be done.

Replace
   After all, push the *Replace* button. The shape and/or material of all
   selected atoms are then changed. This option works for objects and
   instancing vertices object structures.

Default
   If you want to have the default values (NURBS spheres and specific element
   colors and sizes) of selected atoms push the *Default* button.


Separate Atoms
--------------

When structures are imported via the PDB or XYZ importer, the atoms are put
into a so-called instancing vertices structure, somewhat into 'groups' of elements
(e.g. all hydrogen atoms form one instancing vertices structure). In the Edit Mode of Blender,
single atoms can be deleted or displaced by modifying the position of the vertices.
However, they are always a part of the structure and are not independent objects.
Sometimes one would like to mark a single atom or replace an atom by something different:
for instance, imagine you have a NaCl cube where you would like to replace an atom by
an atomic defect in form of a ball with a different color.

To separate single atoms, one needs to select the atom (vertices) first in the Edit Mode.
In the *Atomic Blender Utilities* panel, the *Object* selector and the *Separate* button appear at the bottom.
If the selector remains on *Unchanged* the type of object (NURBS, mesh, meta) and
its properties will not be changed upon separation. If desired also an other type of object can be chosen,
which then replaces the standard type of object.

After having chosen the type of object, use button *Separate Atoms* to separate the selected atoms:
the atoms are then single, new objects, which can be manipulated in any way.
They appear in the Outliner and carry the suffix ``_sep``.

.. hint:: Converting All Atoms of an Instancing Vertices Structure to Real Independent Objects

   Do the following: Select the whole atomic structure
   with the mouse then use :ref:`bpy.ops.object.duplicates_make_real`.
   With this you produce real independent objects!
   In the Outliner delete the remaining instancing vertices structures,
   named like "Carbon", "Hydrogen", etc.


Examples
========

.. list-table::

   * - .. figure:: /images/addons_import-export_mesh-atomic_molecule-representations.jpeg

          Different presentations of one and the same molecule.

     - .. figure:: /images/addons_import-export_mesh-atomic_DNA.jpeg

          Part of a DNA molecule.

   * - .. figure:: /images/addons_import-export_mesh-atomic_JPCC-2014.jpg

          Functionalized [5]helicene molecules on the NaCl(001) surface
          (Clemens Barth et al. -- `Link to publication <https://doi.org/10.1021/jp501738c>`__).

     - .. figure:: /images/addons_import-export_mesh-atomic_ESE-2017.jpeg

          Solar cell structure to underline the properties of silicon nanocrystals deposited by pulsed spray system
          (Mickael Lozac'h et al. -- `Link to publication <https://doi.org/10.1002/ese3.174>`__).

The following movie was created by Sébastien Coget (responsible researcher: Frank Palmino)
at the `Femto-ST institute <https://www.femto-st.fr/en>`__ in Besançon (France).
The movie demonstrates that with Blender, professional movies can be done for research.
It was rendered with Cycles.

.. youtube:: 8WmCn5xGebs
   :width: 600
