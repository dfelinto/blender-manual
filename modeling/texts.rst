
..    TODO/Review: {{review|text=fix headings. Add reference}} .


Text Objects
============

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode (\ :guilabel:`Text`\ )
   | Panel:    :guilabel:`Curve and Surface`\ , :guilabel:`Font` and :guilabel:`Char` (\ :guilabel:`Editing` context, :kbd:`F9`\ )
   | Menu:     :menuselection:`Add --> Text`
   | Hotkey:   :kbd:`F9`


.. figure:: /images/Manual-Part-II-TextSamples.jpg
   :width: 400px
   :figwidth: 400px

   Text Examples.


:guilabel:`Text` objects are exactly what they sound like: they contain some text. They share the same object type as curves and surfaces, as modern fonts (OpenType, TrueType, etc.) are vectorial, made of curves (generally Béziers).

Blender uses a "Font System" to manage mapping "letter codes → objects representing them in 3D
views". This implies that not only does the font system have its own *built-in* font,
but it can use external fonts too, including *PostScript Type 1*\ ,
*OpenType* and *TrueType* fonts. And last but not least,
it can use any objects existing in the current .blend file as letters…

Texts in Bender allow you to create/render 2D or 3D text, shaded as you want,
with various advanced layout options (like justifying and frames), as we will see below.
By default, letters are just flat filled surfaces, exactly like any closed 2D curve.
But you can of course extrude them… And texts can follow other curves.

Of course, once you are happy with the shape of your text, you can convert it
(with :kbd:`alt-C`\ , in :guilabel:`Object` mode), either to a curve,
or directly to a mesh,
allowing you to use all the powerful features of these types of objects on it…

(\ *Text Examples*\ ) shows some examples of various fonts in action, including the "blue" font that has been applied to a curve path.


Notes
-----

A maximum of **50000** characters is allowed per text object; however,
be forewarned that the more characters a single text object has,
the slower the object will respond interactively.

As you can see when you switch between :guilabel:`Object` and :guilabel:`Edit` modes,
the :guilabel:`Font` panel remains the same. This means that its settings can be applied
equally in both modes … and this implies that you cannot apply them to just a part of the
mesh. So font, size, and so on, are common to all letters in a :guilabel:`Text` object.
There is just one exception:
the :guilabel:`Bold`\ /\ :guilabel:`Italic`  buttons control properties specific to each letter
(this is a way to use up to four different fonts in a text).

For optimum resource usage, only characters that are being used consume memory
(rather than the entire character set).


Editing Text
============

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Hotkey:   see below


.. figure:: /images/2.5_Manual-Part-II-Modelling-Text-Create-Ex.jpg
   :width: 300px
   :figwidth: 300px

   Text in Edit mode.


Editing text is quite different from other object types in Blender, and happens mainly in two areas. First, the 3D view, of course, where you type your text, and have a few shortcuts, e.g. for applying
FIXME(TODO: Internal Link;
[[#Bold, Italics and Underline|styles]]
) - note however that most Blender hotkeys you know in :guilabel:`Edit` mode do not exist for texts! The second place is the :guilabel:`Button` window (\ :guilabel:`Editing` context, :kbd:`F9`\ ), especially the :guilabel:`Font` panel.

The menu of the 3D view header has nearly no use,
and there is no :guilabel:`Specials` menu… You have no transform nor mirror tools, and so on.
However, you can apply to texts the same modifiers as for curves.

Editing :guilabel:`Text` is similar to using a standard text editor but is not as
full-featured and has some differences:
Exit :guilabel:`Edit` mode
   :kbd:`Tab` doesn't insert a tab character in the text, but rather enters and exits :guilabel:`Edit` mode, as with other object types.
Copy
   To copy text to the buffer, use :kbd:`ctrl-C` or the :kbd:`Copy` button in the tool shelf.
Cut and Copy
   To cut and copy text to the buffer, use :kbd:`ctrl-X` or the :kbd:`Cut` button in the tool shelf.
Paste
   To paste text from the buffer, use :kbd:`ctrl-V` or the :kbd:`Paste` button in the tool shelf.
Delete all text
   To completely erase or delete all text, use :kbd:`ctrl-Backspace`\ .
Home/End
   :kbd:`Home` and :kbd:`End` move the cursor to the beginning and end of a line respectively.
Next/Previous word
   To move the cursor on a word's boundary, use :kbd:`ctrl-←` or :kbd:`ctrl-→`\ .

The text buffer does not communicate with the desktop. It only works within Blender. To insert text from outside Blender, see
FIXME(TODO: Internal Link;
[[#Inserting Text|Inserting text]]
) below.


Inserting Text
--------------

You can insert text in three different ways: from the internal text buffer (
FIXME(TODO: Internal Link;
[[#Editing Text|Editing Text]]
)), or from a text file.

To load text from a text file, use the :menuselection:`Text --> Paste File` tool.
This will bring up a :guilabel:`File Browser` window for navigating to a valid UTF-8 file.
As usual, be careful that the file doesn't have too many characters,
as interactive response will slow down.


Special Characters
~~~~~~~~~~~~~~~~~~

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Text --> Special Characters`


There are a few special characters that are available using the :kbd:`alt` key or the
:guilabel:`Text` menu in the 3D window header.

Here is a summary of these characters:

+---------------+------------------------------+---------------+-------------------------------+
+:kbd:`alt-C`\ :|Copyright (©)                 |:kbd:`alt-R`\ :|Registered trademark (®)       +
+---------------+------------------------------+---------------+-------------------------------+
+:kbd:`alt-G`\ :|Degrees (- )                  |:kbd:`alt-X`\ :|Multiply symbol (×)            +
+---------------+------------------------------+---------------+-------------------------------+
+:kbd:`alt-S`\ :|German "ss" (ß)               |:kbd:`alt-F`\ :|Currency sign (¤)              +
+---------------+------------------------------+---------------+-------------------------------+
+:kbd:`alt-L`\ :|British Pound (£)             |:kbd:`alt-Y`\ :|Japanese Yen (¥)               +
+---------------+------------------------------+---------------+-------------------------------+
+:kbd:`alt-1`\ :|Superscript 1 (¹)             |:kbd:`alt-2`\ :|Superscript 2 (²)              +
+---------------+------------------------------+---------------+-------------------------------+
+:kbd:`alt-3`\ :|Superscript 3 (³)             |:kbd:`alt-.`\ :|Circle                         +
+---------------+------------------------------+---------------+-------------------------------+
+:kbd:`alt-?`\ :|Spanish question mark (¿)     |:kbd:`alt-!`\ :|Spanish exclamation mark (¡)   +
+---------------+------------------------------+---------------+-------------------------------+
+:kbd:`alt-<`\ :|Left double quotation mark («)|:kbd:`alt->`\ :|Right double quotation mark (»)+
+---------------+------------------------------+---------------+-------------------------------+


All the characters on your keyboard should work, including stressed vowels and so on.
If you need special characters (such as accented chars, which are not there on a US keyboard)
you can produce many of them using a combination of two other characters. To do so,
type the main char, press :kbd:`alt-backspace`\ ,
and then press the desired "modifier" to produce the special character.
Some examples are given below:


+-----------------------------------------------+-+-----------------------------------------------+-+------------------------------------------------+-+
+:kbd:`A`\ , :kbd:`alt-Backspace`\ , :kbd:`~`\ :|ã|:kbd:`A`\ , :kbd:`alt-Backspace`\ , :kbd:`'`\ :|á|:kbd:`A`\ , :kbd:`alt-Backspace`\ , :kbd:`\``\ :|à+
+-----------------------------------------------+-+-----------------------------------------------+-+------------------------------------------------+-+
+:kbd:`A`\ , :kbd:`alt-Backspace`\ , :kbd:`O`\ :|å|:kbd:`E`\ , :kbd:`alt-Backspace`\ , :kbd:`"`\ :|ë|:kbd:`O`\ , :kbd:`alt-Backspace`\ , :kbd:`/`\ : |ø+
+-----------------------------------------------+-+-----------------------------------------------+-+------------------------------------------------+-+


Convert text to text object
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/ConvertTextToTextObject.jpg
   :width: 250px
   :figwidth: 250px


An easy way to get text into Blender is to type it in :doc:`The Text Editor <extensions/python/text_editor>`\ . It is suggested to do this with a :doc:`split window <interface/window_system/arranging_frames#splitting_a_window>` as you will be able to see the 3D view port and text editor at the same time. In the :guilabel:`Text Editor` select *Text > Create Text Block*\ . Then begin typing. When finished, select *Edit >> Text to 3D Object >> One Object* or *One Object per Line* depending on your needs. It is also possible to load a text file via *Text >> Open Text Block* which can be useful for importing large amounts of text at once.


3D Mesh
~~~~~~~

It is possible to convert a Text Object to a 3D Mesh object. This can be useful so that you may edit the vertices in
FIXME(TODO: Internal Link;
[[Edit Mode]]
), but you will lose the ability to edit the text itself. To do this, go to
FIXME(TODO: Internal Link;
[[Object Mode]]
) and select your Text Object. Press :kbd:`Alt-C` and select *Mesh From Curve/Meta/Surf/Text*\ . Now you can return to
FIXME(TODO: Internal Link;
[[Edit Mode]]
) and manually edit the vertices. They are usually a bit messy, so it may be useful to use a *Limited Dissolve* deletion or *Remesh* Object :doc:`Modifier <modifiers>` at a low threshold to clean up your mesh.


.. figure:: /images/TextObjectFromText.jpg
   :width: 500px
   :figwidth: 500px

   left normal text, right the made text object.


Text Selection
--------------

.. figure:: /images/2.5_Manual-Part-II-Modelling-Text-Create-Ex.jpg
   :width: 200px
   :figwidth: 200px

   Text in Edit mode.


In :guilabel:`Edit` mode, your text has a white cursor, and as in any text editor,
it determines where new chars will be inserted! You move this cursor with the arrow keys
(\ :kbd:`→`\ /\ :kbd:`↓`\ /\ :kbd:`←`\ /\ :kbd:`↑`\ )
or :kbd:`Page Up`\ /\ :kbd:`Page Down` and :kbd:`Home`\ /\ :kbd:`End` keys.

Hold :kbd:`shift` while using the arrow keys to select a part of the text.
You can use it to specify different materials, the normal/bold/italic state,
and not much more…


Formatting Text
===============

Fonts
-----

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Font` (\ :guilabel:`Editing` context, :kbd:`F9`\ )


The :guilabel:`Font` panel has several options for changing the look of characters.


Loading and Changing Fonts
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/2.5_Manual-Part-II-Text-Load-Ex.jpg

   Loading a Type 1 font file.


Blender comes with a *built-in* font by default and is displayed in each of the four font
style choosers.
The *built-in* font is always present and shows in this list as "\ ``Bfont``\ ".
The first icon contains a drop-down list displaying currently loaded fonts.
Select one for each font style.

To load a different :guilabel:`Font`\ , click one of the :kbd:`Load` buttons in the
:guilabel:`Font` panel and navigate to a *valid* font.
The :guilabel:`File Browser` window will give all valid fonts a capital F icon,
as seen in *Loading a Type 1 font file.*


.. admonition:: Unix note
   :class: note

   Fonts are typically located under ``/usr/lib/fonts``\ , or some variant like ``/usr/lib/X11/fonts``\ , but not always. They may be in other locations as well, such as ``/usr/share/local`` or ``/usr/local/share``\ , and possibly related sub-trees.


If you select a font that Blender can't understand,
you will get the error "\ ``Not a valid font``\ ".

Remember the same font will be applied to all chars with same style in a text,
but that a separate font is required for each style. For example,
you will need to load an *Italics* font in order to make characters or words italic. Once
the font is loaded you can apply that font "Style" to the selected characters or the whole
object. In all,
you would need to load a minimum of four different types of fonts to represent each style
(\ **Normal**\ , **Italics**\ , **Bold**\ , **Bold-Italics**\ ).

It is important to understand that Blender does not care what font you load for "normal",
"bold", etc., styles. This is how you can have up to four different fonts in use in the same
text - but you have to choose between different styles of a same font, or different fonts.
Blender has a number of typographic controls for changing the style and layout of text,
found in the :guilabel:`Font` panel.


Size and Shear
~~~~~~~~~~~~~~

:guilabel:`Size`
   Controls the size of the whole text (no way to control each char size independently). Note however that chars with different fonts (different styles, see below) might have different visible sizes.


.. figure:: /images/TextShear.jpg
   :width: 300px
   :figwidth: 300px

   shear: 'blender' has a shear value of 1,
   '2.59' a shear value of 0


:guilabel:`Shear`
   Controls the inclination of the whole text. Even if this seems similar to italics style, *this is not the same thing*\ !


Objects as Fonts
~~~~~~~~~~~~~~~~

You can also "create" your own "font" inside Blender! This is quite a complex process,
so let's detail it:

- First, you must create your chars. Each char is an object *of any type* (mesh, curve, meta…). They all must have a name following the schema: ``common prefix`` followed by the ``char name`` (e.g. "\ ``ft.a``\ ", "\ ``ft.b``\ ", etc.).
- Then, for the :guilabel:`Text` object, you must enable the :guilabel:`Dupli Verts` button (\ :guilabel:`Object` context - :kbd:`F7` -, :guilabel:`Anim Settings` panel).
- Back in :guilabel:`Editing` context (\ :kbd:`F9`\ ), in the :guilabel:`Font` panel, fill the :guilabel:`Ob Family` field with the *common prefix* of your "font" objects.

Now, each time a char in your text matches the *suffix part* of a "font" object's name,
this object is duplicated on this char. *The original chars remain visible*\ . The objects are
duplicated so that their center is positioned at the *lower right corner* of the
corresponding chars.


Text on Curve
~~~~~~~~~~~~~

With the :doc:`curve modifier <modifiers/deform/curve>` you can let text follow a curve.


.. figure:: /images/2.5_Manual-Part-II-Text-Curved-LowRes-Ex.jpg
   :width: 200px
   :figwidth: 200px

   Text on curve.


In (\ *Text on curve*\ ) you can see a text deformed by a curve (a 2D Bézier circle).

To apply the curve modifier, the text object first has to be converted to a mesh,
using :kbd:`ALT-C` and click mesh.


+----------------------------------------------+
+.. admonition:: Note                          +
+   :class: note                               +
+                                              +
+   There is also a Text on Curve feature,     +
+   but the curve modifier offers more options.+
+----------------------------------------------+


Underline
~~~~~~~~~

:guilabel:`Underline`
   Toggled with the :guilabel:`Underline` button before typing. Text can also be set to Underlined by selecting it then using the :kbd:`Bold` button in the Tool Shelf.
   :guilabel:`Position`
      This allows you to shift vertically the position of the underline.
   :guilabel:`Thickness`
      This controls the thickness of the underline.


.. figure:: /images/TextFontSettings.jpg
   :width: 300px
   :figwidth: 300px

   check a character option to, for example, type bold text


Character
~~~~~~~~~

.. figure:: /images/2.5_Manual-Part-II-Text-Bold-Ex.jpg
   :width: 300px
   :figwidth: 300px

   Bold text.


:guilabel:`Bold`
   Toggled with the :guilabel:`Bold` button before typing. Text can also be set to Bold by selecting it then using the :kbd:`Bold` button in the Tool Shelf.
:guilabel:`Italics`
   Toggled with the :guilabel:`Italic` button before typing. Text can also be set to Italic by selecting it then using the :kbd:`Italic` button in the Tool Shelf.
:guilabel:`Underline`
   Enables underlining, as controlled by the Underline settings above.
:guilabel:`Small Caps`
   type small capital text.


Blender's :guilabel:`Bold` and :guilabel:`Italic` buttons don't work the same way as other applications, as they also serve as placeholders for you to load up other fonts manually, which get applied when you define the corresponding style; see
FIXME(TODO: Internal Link;
[[#Fonts|above]]
).

To apply the Bold/Italics/Underline attribute to a set of characters, you either turn on
:guilabel:`Bold`\ /\ :guilabel:`Italics`\ /\ :guilabel:`Underline` prior to typing characters,
or highlight (select) first and then toggle Bold/Italics/Underline.


Setting Case
~~~~~~~~~~~~

You can change the text case by selecting it then clicking the :kbd:`To Upper` or
:kbd:`To Lower` in the tool shelf.

Enable the :guilabel:`Small Caps` option to type characters as small caps.

The size of the :guilabel:`Small Caps` can be changed with the :guilabel:`Small Caps Scale`
setting. Note that the :guilabel:`Small Caps Scale` is applied the same to all :guilabel:`Small
Caps` formatted characters.


Paragraph
---------

The :guilabel:`Paragraph` Panel has settings for the alignment and spacing of text.


.. figure:: /images/TextParagraphSettings.jpg
   :width: 300px
   :figwidth: 300px

   the paragraph tab


Align
~~~~~

:guilabel:`Left`
   Aligns text to left of frames when using them, else uses the center point of the :guilabel:`Text` object as the starting point of the text (which grows to the right).
:guilabel:`Center`
   Centers text in the frames when using them, else uses the center point of the :guilabel:`Text` object as the mid-point of the text (which grows equally to the left and right).
:guilabel:`Right`
   Aligns text to right of frames when using them, else uses the center point of the :guilabel:`Text` object as the ending point of the text (which grows to the left).
:guilabel:`Justify`
   Only flushes a line when it is **terminated** by a wordwrap (\ **not** by :kbd:`Enter`\ ), it uses *whitespace* instead of *character spacing* (kerning) to fill lines.
:guilabel:`Flush`
   **Always** flushes the line, even when it's still being entered; it uses character spacing (kerning) to fill lines.

Both :guilabel:`Justify` and :guilabel:`Flush` only work within frames.

Spacing
~~~~~~~

:guilabel:`Character`
   A factor by which space between each character is scaled in width
:guilabel:`Word`
   A factor by which whitespace between words is scaled in width. You can also control it by pressing :kbd:`alt-←` or :kbd:`alt-→` to decrease/increase spacing by steps of **0.1**\ .
:guilabel:`Line`
   A factor by which the vertical space between lines is scaled.


Offset
~~~~~~

:guilabel:`X offset` and :guilabel:`Y offset`
   Well, these settings control the X and Y offset of the text, regarding its "normal" positioning. Note that with
FIXME(TODO: Internal Link;
[[#Text Boxes|frames]]
), it applies to all frames' content…


Shape
=====

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` or :guilabel:`Edit` modes
   | Panel:    :guilabel:`Curve and Surface` (\ :guilabel:`Editing` context, :kbd:`f9`\ )


As you can see in the :guilabel:`Curve and Surface` panel,
texts have most of the same options as curves.


Resolution
----------

:guilabel:`Preview`
   the :doc:`resolution <modeling/curves#curve_resolution>` in the viewport.
:guilabel:`Render`
   the :doc:`resolution <modeling/curves#curve_resolution>` on the render.


.. figure:: /images/TextShapeSettings.jpg
   :width: 300px
   :figwidth: 300px

   the shape settings


:guilabel:`Fast Editing`
   disables curve filling while in edit mode.


Fill

----


The fill options control how the text curves are filled in when text is :guilabel:`Extruded`
or :guilabel:`Beveled` in the :guilabel:`Geometry` Panel.

:guilabel:`Front`
   Fills in the front side of the surface.
:guilabel:`Back`
   Fills in the back side of the surface.
:guilabel:`Fill Deformed`
   Fills the curves after applying shape keys and modifiers.


Textures
--------

.. figure:: /images/TextTextureSettings.jpg

   Texture Settings


:guilabel:`Use UV for Mapping`
   Use UV values as generated texture coordinates.
:guilabel:`Auto Texture Space`
   Adjusts the active object's texture space automatically when transforming object.


Geometry
========

Text objects have all the :doc:`curves extrusion features <modeling/curves/editing/advanced#extrusion>`\ .


