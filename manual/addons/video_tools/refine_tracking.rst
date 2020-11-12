
************************
Refine Tracking Solution
************************

When solving for camera motion, narrowing down the solve error by hand can be a really frustrating task.
Setting the track weight according to the reprojection error solve this issue for camera motion tracking.
This add-on automatically sets the weight of all tracks according to the error in a single click.

Basically this allow you to choose the wanted solution error and get it within a single click,
even with poor tracks (stemming from for example the automatic detected feature).

It is perfectly suited for automatically tracked movies, with many tracks (motion flow like solving).
Even a bad track may have a good influence with the correct weight.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Video Tools then Refine tracking solution to enable the script.


Usage
=====

#. Start to solve your motion as usually.
#. Choose your target solution error, e.g: 0.3.
#. Refine your camera motion path solution.


.. admonition:: Reference
   :class: refbox

   :Category:  Video Tools
   :Description: Refine motion solution by setting track weight according to reprojection error.
   :Location: :menuselection:`Clip Editor --> Tools --> Solve --> Refine Solution`
   :File: space_clip_editor_refine_solution.py
   :Author: Stephen Leger
   :Note: This add-on is bundled with Blender.
