
***********
Paper Model
***********

.. reference::

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Export --> Paper Model (.pdf/.svg)`
   :Panel:     :menuselection:`Properties --> Mesh --> Paper Model Islands`
   :Menu:      :menuselection:`Mesh --> Unfold`

This add-on generates a flat net of a given mesh.
It creates either PDF or SVG files suitable for direct printing and paper modeling.
The main goal is a maximal possible automation of the whole process.
Common tasks like baking the model's texture into the output document are also supported.


Usage
=====

To avoid eventual issues, switch to Object Mode.
Then, select the mesh you want to export so that it is the active one.
If you want to get results quickly, just execute this add-on from the :menuselection:`File --> Export` menu.
It will ask for a file name and do everything else automatically.
All relevant settings are in the bottom left corner.
These are described in more detail below.

If you are unhappy with the generated net, you can edit it manually.
For this, you have to execute the *Unfold* tool first (available Mesh tab in the Properties).
Edges that will be cut in order to flatten the mesh must be marked as Edit Mode seams.
You can use *Clear Seam* and *Mark Seam* tools to organize them as you wish,
or use the helper button *Clear All Seams* in Object Mode to start from scratch.
When you export the model, it will use all the given seams and add some more cuts if necessary.

You can also call the *Unfold* tool just for a preview of the net.
It will list all islands of the produced net in the panel and if you enable so in the tool's settings,
it will also create a UV layout showing the islands.
Note that island positions are not calculated in this stage, so that they will all just lay on top of each other.
You can use Blender's *Pack Islands* tool to arrange them.

There are a few kinds of topology that are possible in Blender but not in paper reality:

- N-gon faces (everything except triangles) that are not perfectly flat.
- Zero-length edges (two vertices exactly in the same spot and connected by an edge)
- Zero-area faces (typically their vertices lie all in line)

If any of these cases is detected, the add-on will throw an error message and will not export.
The error message guides you how to fix the issues.


Exporting Textured Meshes
-------------------------

To export your model with a hand-painted texture, you have to unwrap the model, paint an image and
assign it to the model so that it has an effect during render.
You can use any tools you like for these tasks.
What the add-on does is simply that it uses baking in *Textures* mode.

Switch to Object Mode and deselect any objects except the one to be exported.
Then execute *Export Paper Model* and in the File Browser switch the *Textures* selector to *From Materials*.

If you choose to export an SVG file, you get several options how to attach the images.
All the options are explained in more detail `Properties`_.

The resulting texture does not depend on any scene settings except for the given material,
and on the other hand, all settings should be intact after doing the export.


How to Read the Net
-------------------

Most of the document's appearance can be customized during export (see below).
However, the default style is supposed to be familiar to paper modelers:
dashed lines represent folding outwards, dash-dotted lines inwards (i.e., to form concave shapes).
Boundary of each part of the net is rendered in solid lines.
Sticking tabs have a grayish fill color to be distinguishable from other parts of the net.

A label is written on a tab when its target edge might not be clear.
Specifically, the label is omitted if the edge will be sticked to the same place as its both neighbors or
if one of these is the target itself.
The format of labels is ``island_abbreviation: edge_number``.
Island abbreviation is written in square brackets under the corresponding island, before to its full-length name.
Edge number is written as a triangle arrow next to that target edge, outside the net.

If *Create Tabs* is disabled, the same format is used for labels along each of the related edges, inside the net.
This method is designed for modeling from hard and/or thick materials, for which sticking tabs are quite pointless.
If *Create Numbers* is disabled, the labels are omitted; this may be necessary for highly detailed models.


How to Print the Net
--------------------

The PDF file can be directly printed almost anywhere.
However, things become difficult if you need to change the net by hand.

If you select the SVG format, you can edit the exported files in a vector graphics editor such as Inkscape.
One reason why you may want to do is to pack the islands manually and save paper.
Another reason is that the tabs and numbers often make a lot of clutter around the model and
it can be helpful to remove some of them by hand.

If printed document gets cropped around the page borders,
it means you should increase the *Margin* setting during export.


Placing Marks on the Net
------------------------

Edges with a Freestyle Mark (:menuselection:`Edge --> Mark Freestyle Edge`) will be highlighted
in the net with a user-defined color and drawing style.
This is helpful especially when used on flat edges, which would normally not be drawn at all.
If you draw a shape with the *Knife* tool and then mark some of the edges as Freestyle ones,
you can make a simple line drawing on the model.

When used on folding edges, the highlight will be drawn below the folding line.
So you will probably have to change the *Freestyle Lines* drawing style to make it wider and not black,
so that the lines stay distinguishable.


Settings
========

Paper Model Islands
-------------------

The *Paper Model Islands* tab in the Mesh tab offers two buttons for calling
the *Unfold* and *Export Paper Model* tools conveniently.
It also offers buttons for marking and clearing seams, depending on the context,
and the experimental functionality *Limit Island Size*.

Once the *Unfold* tool is called, the model is split into flattened parts and
these are presented in a list called *Islands* below.
The list allows you to change the label of each island.
If *Create Numbers* is enabled during export, abbreviations of these labels will be used to
describe which tab should be sticked to which island.
After running the *Unfold* tool, these island labels are recalculated so
that as many faces as possible remain under the same label.

If you select an island and enable the *Highlight Selected Island* button
(and the mesh you unfolded is the active one), the island will be highlighted in orange in the 3D Viewport.
Using the slider below, you can change the opacity of the highlight.


Unfold
^^^^^^

The first option from top is *Create UV map*.
If enabled, a new UV map will be generated to show all the islands.
However, their positions are not calculated yet at this time of the export process,
so they are all just placed in the bottom left corner.
This option is useful when editing the cutting lines by hand.
You can use the *Unwrap* tool and get a similar result.

The tool has three sliders, which all adjust edge cutting priority
(namely: *Face Angle Convex*, *Face Angle Concave*, *Edge Length*).
A high value gives an edge with the corresponding property a higher chance to be cut.
Because of that, it is usually better to set Edge Length to a negative value, letting long edges stay connected.
Randomly modifying these values may often help to reduce the count of islands in the net.
For information about the meaning of these values, read the Unfold section in the `Technical Details`_.


Properties
----------

When the export is initiated, the add-on silently unfolds the mesh (without marking any seams) and
divides all faces into islands, which may take a few seconds for complex meshes.
Then, a File Browser is displayed. With SVG format, the file name you choose will get a ``_page<number>.svg`` suffix,
even if only one page was needed.

Settings of this exporter are presented in the bottom left corner of the File Browser.

Preset
   The *Preset* menu allows to quickly save and recall all the settings below it,
   including model scale and color style.
Model Scale
   Model Scale can be used to scale the whole net.
   If you want to have a model in 1:72 scale, just set this to 72.
   This is an important option also because the add-on often produces islands bigger than the page.

   By default, this value is set so that even the biggest island fits onto the page.
   If set to one, the real model will have the same dimensions as the virtual one.
Create UV Map
   Has a similar effect as the similar named option of the *Unfold* tool, but not the same.
   It will create a new UV map that exactly reflects the placement of all the model's islands.
   Unfortunately, islands from all pages are placed on top of each other,
   and it is quite impossible to tell them apart.


Document Settings
^^^^^^^^^^^^^^^^^

Settings closely related to the format of the output document are in the Document Settings subpanel.

Format
   First selector switches between PDF and SVG document formats.
Page Size
   Another selector below allows you to choose one of the most common paper sizes quickly.
   If you need something else, choose *User Defined* and set the dimensions manually.
Page Margin
   Makes it easier to export models in exact scale (if you set the *Model Scale* slider to 1).

   You can set it to the width of the non-printable border of your printer,
   in order for the resulting SVG document to be printable without further scaling. However,
   exporting in-scale models is still difficult, as the add-on does not automatically split oversize islands.
DPI
   The next value is *DPI*, which defines the overall resolution of the net.
   That is, not only resolution of baked images (if any), but also line thickness.

Create Tabs
   Controls if the sticking tabs are created at all.
   For example, uncheck this if you want to stick the model using tape.
Create Numbers
   Adds numbers to some edge pairs that are supposed to be sticked together.
   These numbers are excluded if the correct destination is easy to guess from the neighboring edges.
   In more complex models, they may overlap a lot with each other and with the net itself.
   Disabling this option may help solve such issues.
   If *Create Tabs* is disabled, the numbers will be rendered inside of the net.
Tabs and Text Size
   Sets the maximal width of the sticking tabs around islands.
   The actual size of each tab is adjusted to be at most half the length of the corresponding edge.
   In some special cases, tabs are made not to overlap with real faces, but it does not work reliably yet.
   If *Create Tabs* is disabled, this slider controls the size of numbers on edges.
Hidden Edge Angle
   Edges with folding angle below Hidden Edge Angle will not be drawn at all.
   Increasing this value may produce nicer results when exporting smooth surfaces, such as cylinders:
   it will spare a lot of unnecessary lines.
   Decreasing it could possibly help in some special cases.
Textures
   The *Textures* select menu lists options for exporting textured meshes.

   No Texture
      Just creates the net on a white background (this used to be called "Pure Net").
      The remaining options invoke texture baking and therefore are noticeable slower.
   From Materials
      Exports the image that is assigned to each of the model's faces in their active material.
   Full Render, Selected to Active
      Correspond to the respective *Bake Type* options.
      They both render all the materials and illumination: *Full Render* renders the model only,
      while *Selected to Active* projects other nearby selected objects onto the model.
      It may be helpful for creating patterns such as fur or leaves procedurally.
Images
   The *Images* select menu allows you to choose how to include the baked images in the SVG file.
   If you want to edit the layout of the net in an SVG editor, choose either *Linked* or *Embedded*.

   Embedded
      Creates standalone SVG files, making them bigger but portable.
   Single Linked
      Remains mostly for compatibility reasons.


Colors and Style
^^^^^^^^^^^^^^^^

Options related to the drawing style are packed in the *Colors and Style* subpanel.
They should be quite self-explanatory.


Technical Details
=================

Unfold
------

Firstly, the algorithm assigns every edge a "priority", depending on its angle and length.
Edges with higher priority will more probably be cut apart in the final net.
Shorter edges have higher priority (they are easier to glue on) and sharper angles too
(that makes the net easier to visually understand).

Faces form a concave angle if their normals are pointing against each other.
Such angles have even a bit higher priority which is supposed to help for typical models.
If some face normals are flipped, the algorithm always assumes the angle between them be convex.

If more than two faces are connected by an edge, two of them are designated as the main ones and
all others will have to be glued. The main faces are chosen so that they form the smallest angle possible.

The actual priority effect of angle versus length may change the resulting net very much.
The default values were chosen by trial and error for some basic models, but may be a bad choice for others.
If you want to tweak them, the *Unfold* tool allows you to: they are the tool's three only settings.

The cutting algorithm begins with all faces separated and tries to connect them to form bigger islands,
ordered by the connecting edge's priority. If some of the faces of the resulting island would overlap,
the operation is canceled and the algorithm continues with another edge.
If some vertices or edges end up close enough to each other, they are merged.
During this process, each edge is visited exactly once.

The overlap check is basically the Bentley-Ottmann algorithm for line segment intersection,
applied to the boundary of the resulting island. To handle some special cases,
the algorithm automatically switches between a slightly quicker and a more robust version of itself.
Another check is applied to detect if the boundary crosses itself in just a vertex of the resulting island --
such cases have to be tested explicitly as they need not cause any intersecting line segments.


Positioning the Nets on Pages
-----------------------------

Because the nets are not consisting only of the real faces, but also of the gluing tabs around,
they cannot be positioned by the internal Blender tool (*Pack Islands*).
Therefore, a standalone algorithm had to be written.

For a great simplification of the process, all nets are packed into (smallest possible) bounding rectangles.
These are then ordered by size (largest first) and in this order the algorithm tries to position them on a page.
The positions tested for the lower left corner are given by an n × n grid resulting from
all the corners of islands already positioned. A position is accepted or rejected by checking overlaps
with each of the islands' bounding rectangles.

When there are any islands left that could not be placed onto the page, a new free page is created.

This algorithm should work reliably and quite fast.
However, it is clearly inefficient if the bounding rectangles contain much free space.
Also, the packing depends heavily on the order in which the islands are processed, which is in no way optimal.
