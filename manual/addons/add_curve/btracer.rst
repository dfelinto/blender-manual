
*******
BTracer
*******

The purpose of this script is to add tools that are similar to C4D Tracer.
Btrace provides several ways to trace objects and particles and animate the resulting curve.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Add Curve then BTracer to enable the script.


Interface
=========

Located in the :menuselection:`3D Viewport --> Sidebar --> Edit tab`.

The default setting in the interface is Choose Tool, here you pick what trace methods and functions.

.. figure:: /images/addons_add-curve_btracer_ui.jpg
   :align: right
   :width: 220px


Information
===========

The five main tools (Object Trace, Object Connect, Mesh Follow, Particle Trace, Particle Connect)
all share common settings for the most part. Each tool creates a curve as the end result.
The settings for the curve created can be setup under the *Curves Settings* button.

The tools have access to a few other features. All of them have access to
the grow curve animation tool which animates the curve radius.
As well as the Color Blender tool.

Object Trace
   Creates a curve by joining points of a mesh in a continuous manner or by all edges.
   Options to modulate the curves radius or add distortion to mesh before converting.

Objects Connect
   Join selected objects with a curve and add hooks to each node.

Particle Trace
   Creates a curve from each particle of a system. Keeping particle amount under 250 will make this run faster.

Particle Connect
   Connects each particle of a system with a continuous curve.

Mesh Follow
   Creates curve from animated mesh object. Following the path of
   either the vertices, edges or faces, and also the option to follow the object's origin.

Grow Curve Animation
   Animate the radius of a curve over time. Can be run alone on a curve object, or run with the tools above.

F-Curve Noise
   Quick link to add an F-curve modifier to an object.

Color Blender
   Assign colors, create color palettes and randomize colors.

Each script has a number of different options which can be used to create some very interesting effects.


.. admonition:: Reference
   :class: refbox

   :Category:  Add Curve
   :Description: Tools for converting/animating objects/particles into curves.
   :Location: :menuselection:`Sidebar --> Create tab`
   :File: btrace folder
   :Author: liero, crazycourier
   :Contributors: Atom, MacKracken, meta-androcto
   :Maintainer: Brendon Murphy (meta-androcto)
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
