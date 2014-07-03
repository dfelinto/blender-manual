

..    TODO/Review: {{review|void=X}} .


Projection Texture Painting
===========================


Projection texture painting allows an artist to paint on texture mapped on a 3D model.
Unlike painting in the image editor,
projection texture painting is done in the 3D viewport of blender.


Getting Started
---------------

To enter texture paint mode,
you need to select a mesh object and select *Texture Paint* from the mode menu
(the one which toggles between *Object*\ , *Edit* etc. modes).

Painting on a 3D model requires some setup before being possible. Blender needs a way to map an image to the 3D model. This is accomplished by using a UV map (see :doc:`UV Mapping <textures/mapping/uv>` for more details), so if the model hasn't been unwrapped yet, it should be unwrapped prior to entering *Texture Paint* mode. The image assigned to the UV layer is also used for painting. That means that the user should either:

- unwrap the model while the target image is being displayed in the image editor window, or
- unwrap, and while still in edit mode, change the image in the UV editor window to the target image.

If the target image is not square, the first method is preferable,
so that unwrapping accounts for the aspect ratio of the image.


Hints
-----

There are a known limitations in painting...

- Overlapping UVs are not supported (as with texture baking).
- When painting onto a face which is partially behind the view (in perspective mode), the face can't be painted on. To avoid, this zoom out or use an Ortho mode viewport.
- When painting onto a face in perspective mode onto a low poly object with normals pointing away from the view, painting may fail; to workaround disable the **Normal** option in the paint panel.

*Typically this happens when painting onto the side of a cube
FIXME(Template Unsupported: BugReport;
{{BugReport|34665}}
)*