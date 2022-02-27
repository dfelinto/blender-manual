****************
Before You Begin
****************

There are a number of principles to be aware of before you begin working with PDT:

Be sure to check Page (https://github.com/Clockmender/Precision-Drawing-Tools/wiki/98-PDT-Latest-Release-Menus) to see current layouts.

1) PDT is split into several sections and this list will grow as the add-on develops.
2) PDT has a concept of a ``Working Plane`` that applies in all Operations, i.e. those defined in the Design section and some in the Pivot Point section.
3) PDT has been designed to work as far as possible in Edit and Object modes with many commands equally applicable to both.
4) Certain Operations relating to ``Cursor Placement`` and ``Pivot Point Placement`` have been set to work in either Selected, or Relative Modes, these will be explained later.
5) PDT can be driven from its own Command Line input for **most** operations.

The first thing to establish is the ``Working Plane``, here a number of choices are available:

1) ``Front(X-Z)`` - Uses Global X and Z axes, if you want to work from the Back view, the working plane is also this as the axes remain the same.
2) ``Top(X-Y)`` - Uses Global X and Y axes, if you want to work from the Bottom view, the working plane is also this as the axes remain the same.
3) ``Right(Y-Z)`` - Uses Global Y and Z axes, if you want to work from the Left view, the working plane is also this as the axes remain the same.
4) ``View`` - This uses axes relative to your screen, no matter how the 3D View is rotated, X is always view-horizontal, Y is always view-vertical and Z is always view-depth.

.. figure:: /images/addons_pdt_setup_1.png
   :align: left
   :width: 300px

.. container:: lead

   .. clear
Setting the Working Plane.
=========================

Whatever your ``View`` is set to other than **View**, it does not matter how the view is oriented, inputs are always along global axes.

The second thing is whether you want Cursor, or Pivot Point locations to be based upon ``Selected``, or ``Current`` values. Set ``Selected`` if you want the Cursor to be placed relative to selected geometry, or ``Current`` if you want it to be placed relative to its current location. For example, moving the cursor in ``Current`` mode by a ``Delta`` input of 1,3,2 will move the cursor relative to itself, so it moves this amount every time you activate the command.

.. figure:: /images/addons_pdt_setup_2.png
   :align: left
   :width: 300px

.. container:: lead

   .. clear
Setting the Cursor/Pivot Point Movement Mode.
============================================

Then you can set the type of Operation you want to undertake, these will be discussed on another page. There are a number of Operations, shown below:

1) Cursor.
2) Pivot Point.
3) Move.
4) New Vertex.
5) Extrude Vertices.
6) Split Edges.
7) Duplicate Geometry.
8) Extrude Geometry.

.. figure:: /images/addons_pdt_setup_3.png
   :align: left
   :width: 300px

.. container:: lead

   .. clear
Setting the Operation Mode.
===========================

Setting the `Operation` mode determines what the buttons below this command actually do, so for example to **move** the ``Cursor`` to ``Absolute`` location, you would select ``Cursor`` operation, set the input values for **X, Y & Z** then click the ``Absolute`` button.

Below is a table showing which options are available in which Modes, including Edit, or Object Modes in Blender:

.. figure:: /images/addons_pdt_setup_4.png
   :align: left
   :width: 720px

.. container:: lead

   .. clear
Note! Only Edit and Object Modes are supported by PDT at present, Further, only Mesh Objects are supported, not Curves for now.

Note! From Version 1.1.8, Menu widths will affect how the menus are arranged, with less items per row as the width decreases below a threshold set in the PDT Add-on's Preferences. Here are two sample Images:

.. figure:: /images/addons_pdt_op_1.png
   :align: left
   :width: 250px

.. container:: lead

   .. clear
   .. figure:: /images/addons_pdt_op_2.png
      :align: left
      :width: 300px

   .. container:: lead

      .. clear
Note! PDT Add-on Preferences now also sets the Parts Library location and Debug mode.

.. figure:: /images/addons_pdt_op_3.png
   :align: left
   :width: 420px

.. container:: lead

   .. clear
