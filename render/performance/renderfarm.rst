
..    TODO/Review: {{review|copy=X}} .


Distributed Render Farm
***********************

There are several levels of CPU allocation that you can use to decrease overall render time by
applying more brainpower to the task.


Multi-Threading
===============

First, if you have a multi-core CPU, you can increase the number of threads,
and Blender will use that number of CPUs to compute the render.


Frame Ranges
============

Second, if you have a local area network with available PCs,
you can split the work up by frames. For example, if you want to render a 200 frame animation,
and have 5 PCs of roughly equal processing power,
you can allocate PC#1 to produce frames 1-40, PC#2 to frames 41-80, and so on.
If one PC is slower than the others, simply allocate fewer frames to that PC.
To do LAN renders, map the folder containing the .blend file
(in which you should have packed your external data, like the textures, ...)
as a shareable drive. Start Blender on each PC and open the .blend file.
Change the Start and End frame counts on that PC, but do not save the .blend file.
Start Rendering. If you use relative paths for your output pathspec,
the rendered frames will be placed on the host PC.


Collaborative Rendering
=======================

Third, you can do WAN rendering,
which is where you email or fileshare or Verse-share the .blend file (with packed data!)
across the Internet, and use anyone's PC to perform some of the rendering.
They would in turn email you the finished frames as they are done.
If you have reliable friends, this is a way for you to work together.


Remote Renderfarms
==================

Fourth, you can use a render farm service. These services, like `BURP <http://burp.boinc.dk/>`__,
are run by an organization. You email them your file,
and then they distribute it out across their PCs for rendering.
BURP is mentioned because it is free,
and is a service that uses fellow BlenderHead PCs with BOINC-type background processing.
Other services are paid subscription or pay-as-you-go services.