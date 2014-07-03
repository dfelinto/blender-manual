

About this manual
=================


This manual is a mediawiki implementation that is written by a world-wide collaboration of volunteer
FIXME(Link Type Unsupported: dev;
[[Dev:Ref/Release_Notes/Source_code/Contributors|authors]]
). It is updated daily, and this is the English version. Other language versions are translated, generally, from this English source for the convenience of our world-wide audience. It is constantly out of date, thanks to the tireless work of some 50 or more volunteer developers, working from around the world on this code base. However, it is the constructive goal to provide you with the best possible professional documentation on this incredible package.

To assist you in the best and most efficient way possible,
this manual is organized according to the creative process generally followed by 3D artists,
with appropriate stops along the way to let you know how to navigate your way in this strange
territory with a new and deceptively complex software package.
If you read the manual linearly, you will follow the path most artists use in both learning
Blender *and* developing fully animated productions:


- Getting to know Blender = Intro, Navigating in 3d, scene mgt
- Models = Modeling, Modifiers
- Lighting
- Shading = Materials, Textures, Painting, Worlds & Backgrounds
- Animation = Basics, Characters, Advanced, Effects & Physical Sim
- Rendering = Rendering, Compositing, Video Seq Edit
- Beyond Blender = Extending Blender


Audience
========


This manual is written for a very broad audience,
to answer the question "I want to *do something*\ ; how do I do it using Blender?" all the way
to "what is the latest change in the way to sculpt a mesh?"

This manual is a worldwide collaborative effort using time donated to the cause.
While there may be some lag between key features being implemented and their documentation,
we do strive to keep it as up-to-date as possible.
We try to keep it narrowly focused on what you, the end user, need to know,
and not digress too far off topic, as in discussing the meaning of life.

There are
FIXME(TODO: Internal Link;
[[Main Page|other Blender wiki books]]
) that delve deeper into other topics and present Blender from different viewpoints, such as the Tutorials, the Reference Manual, the software itself, and its scripting language. So, if a question is not answered for you in this User Manual, please search the other
FIXME(TODO: Internal Link;
[[Main Page|Blender wiki books]]
).


Learning CG and Blender
=======================


.. figure:: /images/Manual-Introduction-Learning.jpg
   :width: 400px
   :figwidth: 400px


Getting to know Blender and learning Computer Graphics (CG) are two different topics.
Learning what a computer model is,
and then learning how to develop one in Blender are two different things to learn.
Learning good lighting techniques,
and then learning about the different kinds of lamps in Blender are two different topics.
The first, or conceptual understanding,
is learned by taking secondary and college courses in art and media,
by reading books available from the library or bookstore on art and computer graphics,
and by trial and error. Even though a book or article may use a different package
(like Max or Maya) as its tool, it may still be valuable because it conveys the concept.

Once you have the conceptual knowledge, you can easily learn Blender
(or any other CG package). Learning both at the same time is difficult,
since you are dealing with two issues.
The reason for writing this is to make you aware of this dilemma,
and how this manual attempts to address both topics in one wiki book. The conceptual knowledge
is usually addressed in a short paragraph or two at the beginning of a topic or chapter,
that explains the topic and provides a workflow, or process, for accomplishing the task.
The rest of the manual section addresses the specific capabilities and features of Blender.
The user manual cannot give you the full conceptual knowledge - that comes from reading books,
magazines, tutorials and sometimes a lifetime of effort.
You can use Blender to produce a full-length feature film,
but reading this manual and using Blender won't make you another Steven Spielberg!

At a very high level, using Blender can be thought of as knowing how to accomplish imagery
within three dimensions of activity:


- Integration - rendering computer graphics, working with real-world video, or mixing the two (CGI and VFX)
- Animation - posing and making things change shape, either manually or using simulation
- Duration - producing a still image, a short video, a minute-long commercial, a ten minute indie short, or a full-length feature film.

Skills, like navigating in 3D space, modeling, lighting, shading, compositing,
and so forth are needed to be productive in any given area within the space.
Proficiency in a skill makes you productive.
Tools within Blender have applicability within the space as well. For example,
the video sequence editor (VSE) has very little to do with the skill of animation,
but is deeply applicable along the Duration and Integration scales.
From a skills-learning integration perspective,
it is interesting to note that the animation curve, called an Ipo curve,
is used in the VSE to animate effects strips.

At the corners/intersections is where most people's interest's lie at any given time;
a sort of destination, if you will. For example,
there are many talented artists that produce Static-Still-CG images. Tony Mullen's book
*Introducing Character Animation With Blender* addresses using CG models deformed by
Armatures and shapes to produce a one-minute animation. Using Blender fluids in a TV
production/commercial is at the Shape/Sim-Integrated-Minute intersection.
Elephants Dream and Big Buck Bunny is a bubble at the Armature-CG-Indie space. Therefore,
depending on what you want to do,
various tools and topics within Blender will be of more or less interest to you.

A fourth dimension is Game Design,
because it takes all of this knowledge and wraps Gaming around it as well.
A game not only has a one-minute cinematic in it, but it also has actual game play,
story line programming, etc. -- which may explain why it is so hard to make a game;
you have to understand all this stuff before you actually can construct a game. Therefore,
this Manual does not address using the Game Engine; that is a whole 'nother wiki book.

