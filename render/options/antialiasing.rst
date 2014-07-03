
Anti-Aliasing
=============


A computer generated image is made up of pixels;
each pixel can of course only be a single color. In the rendering process the rendering engine
must therefore assign a single color to each pixel on the basis of what object is shown in
that pixel. This often leads to poor results, especially at sharp boundaries,
or where thin lines are present, and it is particularly evident for oblique lines.

To overcome this problem, which is known as *Aliasing*\ ,
it is possible to resort to an Anti-Aliasing technique. Basically,
each pixel is 'oversampled', by rendering it as if it were 5 pixels or more,
and assigning an 'average' color to the rendered pixel.

The buttons to control Anti-Aliasing, or OverSampling (OSA),
are below the rendering button in the :guilabel:`Render` Panel (\ *Render Panel.*\ ).


Options
=======

:guilabel:`Anti-Aliasing` check box
    Enables oversampling

5 / 8 / 11 / 16
    The number of samples to use. The values 5, 8, 11, 16 are preset numbers in specific sample patterns; a higher value produces better edges, but slows down the rendering.

By default, we use in Blender a fixed "Distributed Jitter" table. The samples within a pixel
are distributed and jittered in a way that guarantees two characteristics:

- Each sample has equal distances to its neighbor samples
- The samples cover all sub-pixel positions equally, both horizontally and vertically

    The images below show Blender sample patterns for 5, 8, 11 and 16 samples. To show that the distribution is equalized over multiple pixels, the neighbor pixel patterns were drawn as well. Note that each pixel has an identical pattern.


+-----------------------------------------------------+-----------------------------------------------------+------------------------------------------------------+------------------------------------------------------+
+.. figure:: /images/Manual-oversampling-pattern-5.jpg|.. figure:: /images/Manual-oversampling-pattern-8.jpg|.. figure:: /images/Manual-oversampling-pattern-11.jpg|.. figure:: /images/Manual-oversampling-pattern-16.jpg+
+                                                     |                                                     |                                                      |                                                      +
+   5 samples                                         |   8 samples                                         |   11 samples                                         |   16 samples                                         +
+-----------------------------------------------------+-----------------------------------------------------+------------------------------------------------------+------------------------------------------------------+


:guilabel:`Full Sample`
      For every anti-aliasing sample, save the entire Render Layer results. This solves anti-aliasing issues with compositing.


Filtering
---------

When the samples have been rendered,
we've got color and alpha information available per sample.
It then is important to define how much each sample contributes to a pixel.

The simplest method is to average all samples and make that the pixel color.
This is called using a "Box Filter". The disadvantage of this method is that it doesn't take
into account that some samples are very close to the edge of a pixel,
and therefore could influence the color of the neighbor pixel(s) as well.

Filter menu: Set The filter type to use to 'average' the samples:
|\ :guilabel:`Box`
|The original filter used in Blender, relatively low quality. For the Box Filter, you can see that only the samples within the pixel itself are added to the pixel's color. For the other filters, the formula ensures that a certain amount of the sample color gets distributed over the other pixels as well.

+------------------------------+----------------------------------------------------------------------------+
+:guilabel:`Box`               |A low-quality box-shaped curve (see above)                                  +
+------------------------------+----------------------------------------------------------------------------+
+:guilabel:`Tent`              |A simplistic filter that gives sharp results                                +
+------------------------------+----------------------------------------------------------------------------+
+:guilabel:`Quadratic`         |A Quadratic curve                                                           +
+------------------------------+----------------------------------------------------------------------------+
+:guilabel:`Cubic`             |A Cubic curve                                                               +
+------------------------------+----------------------------------------------------------------------------+
+:guilabel:`Gauss`             |Gaussian distribution, the most blurry                                      +
+------------------------------+----------------------------------------------------------------------------+
+:guilabel:`Catmull-Rom`       |Catmull-Rom filter, gives the most sharpening                               +
+------------------------------+----------------------------------------------------------------------------+
+:guilabel:`Mitchell-Netravali`|Mitchell-Netravali, a good all-around filter that gives reasonable sharpness+
+------------------------------+----------------------------------------------------------------------------+


+----------------------------------------------------------+------------------------------------------------------------+--------------------------------------------------------------------+-------------------------------------------------------+
+.. figure:: /images/Manual-oversampling-graph-box.jpg     |.. figure:: /images/Manual-oversampling-graph-tent.jpg      |.. figure:: /images/Manual-oversampling-graph-quadratic.jpg         |.. figure:: /images/Manual-oversampling-graph-cubic.jpg+
+                                                          |                                                            |                                                                    |                                                       +
+   Box                                                    |   Tent                                                     |   Quadratic                                                        |   Cubic                                               +
+----------------------------------------------------------+------------------------------------------------------------+--------------------------------------------------------------------+-------------------------------------------------------+
+.. figure:: /images/Manual-oversampling-graph-gaussian.jpg|.. figure:: /images/Manual-oversampling-graph-catmullrom.jpg|.. figure:: /images/Manual-oversampling-graph-mitchell-netravali.jpg                                                        +
+                                                          |                                                            |                                                                                                                            +
+   Gaussian                                               |   Catmull-Rom                                              |   Mitchell-Netravali                                                                                                       +
+----------------------------------------------------------+------------------------------------------------------------+--------------------------------------------------------------------+-------------------------------------------------------+


Filter Size
-----------

Making the filter size value smaller will squeeze the samples more into the center,
and blur the image more. A larger filter size makes the result sharper.
Notice that the last two filters also have a negative part;
this will give an extra sharpening result.


Examples
========


.. figure:: /images/Manual-Part-XI-AA02.jpg
   :width: 630px
   :figwidth: 630px


.. figure:: /images/Manual-osa8_box.jpg
   :width: 630px
   :figwidth: 630px

   AA 8, Box filter


.. figure:: /images/Manual-osa8_tent.jpg
   :width: 630px
   :figwidth: 630px

   AA 8, Tent filter


.. figure:: /images/Manual-osa8_quad.jpg
   :width: 630px
   :figwidth: 630px

   AA 8, Quadratic filter


.. figure:: /images/Manual-osa8_cubic.jpg
   :width: 630px
   :figwidth: 630px

   AA 8, Cubic filter


.. figure:: /images/Manual-osa8_gauss.jpg
   :width: 630px
   :figwidth: 630px

   AA 8, Gaussian filter


.. figure:: /images/Manual-osa8_catrom.jpg
   :width: 630px
   :figwidth: 630px

   AA 8, Catmull-Rom filter


.. figure:: /images/Manual-osa8_mitch.jpg
   :width: 630px
   :figwidth: 630px

   AA 8, Mitchell-Netravali filter


