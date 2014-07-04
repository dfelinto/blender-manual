
Filter 2D Actuator
==================

:guilabel:`2D Filter` s are image filtering actuators, that apply on final render of objects.


**Filter 2D Type**
Select the type of 2D Filter required.


.. figure:: /images/BGE_Actuator_Filter_2D.jpg
   :width: 271px
   :figwidth: 271px

   Edit Object actuator


   :guilabel:`Custom Filter`
   :guilabel:`Invert`
   :guilabel:`Sepia`
   :guilabel:`Gray Scale`
   :guilabel:`Prewitt`
   :guilabel:`Sobel`
   :guilabel:`Laplacian`
   :guilabel:`Erosion`
   :guilabel:`Dilation`
   :guilabel:`Sharpen`
   :guilabel:`Blur`
   :guilabel:`Motion Blur`
   :guilabel:`Remove Filter`
   :guilabel:`Disable Filter`
   :guilabel:`Enable Filter`

Only one parameter is required for all filters:

**Pass Number**
   The pass number for which this filter is to be used.
Details of the filters are given in the descriptive text below.


Motion Blur
-----------

:guilabel:`Motion Blur` is a :guilabel:`2D Filter` that needs previous rendering information to produce motion effect on objects. Below you can see :guilabel:`Motion Blur` filter in Blender window, along with its logic bricks:


.. figure:: /images/Motionblur_render-full.jpg

   2D Filters: Motion Blur.


.. figure:: /images/Motion_Blur_logic_2.5.jpg

   2D Filters: Game Logic.


To enable this filter:

- Add appropriate Sensor(s) and Controller(s).
- Add a :guilabel:`2D Filter` Actuator.
- Select :guilabel:`Motion Blur` in the drop-down list.
- Set Motion Blur :guilabel:`Value` (Factor).

And for disabling this filter:

- Add appropriate Sensor(s) and Controller(s).
- Add a :guilabel:`2D Filter` Actuator.
- Select :guilabel:`Motion Blur`.
- Toggle :guilabel:`Enable` button to go to disabled mode.

You can enable Motion Blur filter using a :guilabel:`Python` controller:
from bge import render
render.enableMotionBlur(0.85)

And disable it:
from bge import render
render.disableMotionBlur()


.. admonition:: Note
   :class: note

   Your graphic hardware and OpenGL driver must support accumulation buffer (``glAccum`` function).


Built-In 2D Filters
-------------------

All 2D filters you can see in :guilabel:`2D Filter` actuator have the same architecture,
all built-in filters use fragment shader to produce final render view,
so your hardware must support shaders.


.. figure:: /images/Motionblur_render-full.jpg
   :width: 200px
   :figwidth: 200px

   2D Filters: Motion Blur.


.. figure:: /images/Sepia_render-full.jpg
   :width: 200px
   :figwidth: 200px

   2D Filters: Sepia.


.. figure:: /images/Sobel_render-full.jpg
   :width: 200px
   :figwidth: 200px

   2D Filters: Sobel.


:guilabel:`Blur`, :guilabel:`Sharpen`, :guilabel:`Dilation`, :guilabel:`Erosion`, :guilabel:`Laplacian`, :guilabel:`Sobel`, :guilabel:`Prewitt`, :guilabel:`Gray Scale`, :guilabel:`Sepia` and :guilabel:`Invert` are built-in filters. These filters can be set to be available in some passes.

To use a filter you should:

- Create appropriate sensor(s) and controller(s).
- Create a :guilabel:`2D Filter` actuator.
- Select your filter, for example :guilabel:`Blur`.
- Set the pass number that the filter will be applied.

To remove a filter on a specific pass:

- Create appropriate sensor(s) and controller(s).
- Create a :guilabel:`2D Filter` actuator.
- Select :guilabel:`Remove Filter`.
- Set the pass number you want to remove the filter from it.

To disable a filter on a specific pass:

- Create appropriate sensor(s) and controller(s).
- Create a :guilabel:`2D Filter` actuator.
- Select :guilabel:`Disable Filter`.
- Set the pass number you want to disable the filter on it.

To enable a filter on a specific pass:

- Create appropriate sensor(s) and controller(s)
- Create a :guilabel:`2D Filter` actuator.
- Select :guilabel:`Enable Filter`.
- Set the pass number you want to enable the filter on it.


Custom Filters
--------------

.. figure:: /images/Custom_2D_filter.jpg

   2D Filters: Custom Filter.


Custom filters give you the ability to define your own 2D filter using GLSL.
Its usage is the same as built-in filters,
but you must select :guilabel:`Custom Filter` in :guilabel:`2D Filter` actuator,
then write shader program into the Text Editor, and then place shader script name on actuator.

Blue Sepia Example:
uniform sampler2D bgl_RenderedTexture;
void main(void)
{
vec4 texcolor = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);
float gray = dot(texcolor.rgb, vec3(0.299, 0.587, 0.114));
gl_FragColor = vec4(gray * vec3(0.8, 1.0, 1.2), texcolor.a);
}


