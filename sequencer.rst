

..    TODO/Review: {{review|copy=X}} .


Sequence Editing
================


In addition to modeling and animation, Blender has a fully functional Video Sequence Editor (VSE) as well as an advanced node-based editor that also manipulates a video stream. :doc:`Compositing Nodes <composite_nodes/types>` operate equally well on images or video streams, and can apply detailed image manipulation on the stream.

Operating at a higher conceptual level, and used later in the video production process,
Blender's legacy VSE operates on a set of entire strips at a time, as a chunk of footage.
The many parts of Blender work together in typical work flow fashion:


- Model to construct the objects
- Assign Materials and introduce Lighting to color the objects
- Animate your objects to make them move
- Render layers of video using cameras
- Use Compositing nodes to:
  - Enhance the images by adjusting colors, adding in-scene special effects
  - Layer the images into a composite image sequence (strip)
- Assemble the video strips together to make a movie using the VSE.

The VSE within Blender is a complete video editing system that allows you to combine multiple
video channels and add effects to them.
Its functionality has been inside Blender since the beginning.
Even though it has a limited number of operations,
you can use these to create powerful video edits
(especially when you combine it with the animation power of Blender!) Furthermore,
it is extensible via a plugin system to perform an unlimited number of image manipulations.

Using the VSE, you load multiple video clips and lay them end-to-end (or in some cases,
overlay them),
inserting fades and transitions to link the end of one clip to the beginning of another.
Finally,
add an audio track so you can synchronize the timing of the video sequence to match it.
The result of using the VSE is your finished movie.


 .. admonition:: FFMPEG Support
   :class: note

   Support for exporting an avi/quicktime movie using FFMPEG does work, currently (since 2.44) only within the Linux and Windows builds. With FFMPEG support, you are able to save the audio track with your video.


