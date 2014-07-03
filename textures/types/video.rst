


Video Textures
==============


.. figure:: /images/Doc-26-Manual-Textures-Video-Example.jpg
   :width: 700px
   :figwidth: 700px

   Video texture


**Video textures** are a some kind of :doc:`Image <textures/types/image>` textures and based on movie file or sequence of successive numbered separate images. They are added in the same way that image textures are.


Options
-------


Image
~~~~~


.. figure:: /images/Doc-26-Manual-Textures-Video-Imagepanel.jpg
   :width: 400px
   :figwidth: 400px

   Image panel for video texture


:guilabel:`Source`
    For video texture the kind of source file to use is
   :guilabel:`Movie`
       See about supported :doc:`Movie <data_system/files/formats#movie_formats>` formats.
   :guilabel:`Image Sequence`
      See about supported :doc:`Image <data_system/files/formats#image_formats>` formats.
      To load image sequence in any of the supported image file formats first click on the first frame and then Accept.
      Then change the Source to Image Sequence, and enter the ending frame number of this sequence.

More about loading source file for video texture see :doc:`here <textures/types/image#settings>`\ .

:guilabel:`Fields`
    Work with field images. Video frames consist of two different images (fields) that are merged.  This option ensures that when :guilabel:`Fields` are rendered, the correct field of the image is used in the correct field of the rendering.

   :guilabel:`Upper First`
       Order of video fields - upper field first.
   :guilabel:`Lower First`
       Order of video fields - lower field first.
   :guilabel:`Fields`
       Number of fields per rendered frame.  Used with Fields and interlaced video, it says whether each image has both odd and even, or just one.

:guilabel:`Frames`
    Number of frames/images in the movie or sequence to use
:guilabel:`Start`
    Global starting frame of the sequence/movie
:guilabel:`Offset`
    Offset the number of the frame to use in the animation. What frame number inside the movie/sequence to start grabbing.

:guilabel:`Match Movie Length`
    This button set image's user's length to the one of selected movie/sequence.

:guilabel:`Auto Refresh`
    Automatically refresh images on frame changes
:guilabel:`Cyclic`
    When the video ends, it will loop around the to the start and begin playing again.

For :guilabel:`Movie` source:
:guilabel:`Use Alpha`
    Use the alpha channel information from the image or make image fully opaque

   :guilabel:`Straight`
       Transparent RGB and alpha pixels are unmodified.
   :guilabel:`Premultiplied`
       Transparent RGB pixels of an image are multiplied by the image's alpha value.


About input color space for video texture see :doc:`here <textures/types/image>`\ .

About video sampling for video texture see :doc:`here <textures/types/image#image_sampling>`\ .

About video mapping for video texture see :doc:`here <textures/types/image#image_mapping>`\ .

