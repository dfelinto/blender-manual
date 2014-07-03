


Licensing of Blender Games
==========================


The licensing of games created for distribution using the Blender Game Engine and the
Standalone Player is complicated by Blender's status as open-source software.
This page aims to describe the problems, and present some possible solutions.

Blender is distributed as open-source software distributed and owned by the Blender Foundation
under the GNU General Public License (GPL).    In brief,
while the Blender system itself is available to everyone,
you own anything that you make using Blender (scripts, texture, rendered artwork etc.).
See http://www.blender.org/education-help/faq/gpl-for-artists/ for further details.


Standalone Player License
-------------------------

Unfortunately, this does not extend to games or other artwork distributed to run under the
Blender Standalone Player.  To distribute your game you need to create an executable
(run time). What it does is take your Blender .blend file and put it "inside" the Standalone
Player - a stripped-down version of Blender containing only the functions corresponding to the
Blender Game Engine.
The resulting executable file falls into the category of "derivatives" of the original program
(i.e. a hybrid of your file with the Standalone Player itself),
and therefore must be licensed as GPL.


Distributing Games
------------------

There are four possible solutions to the problem of how to distribute your game with suitable
license protection:
      1) Do not protect your Blender Game by license. Are you really sure that you need to license it? Remember the old adage "Imitation is the sincerest form of flattery".

      2) Pretend that there is no problem. It is very, very unlikely that the Blender Foundation will ever prosecute anyone for distributing a game that is based on the BGE.

      3) Make use of  an external system for running Blender games: e.g. BPPlayer or Gamekit (but these are not fully tested).

      4) Use the Game Actuator, which enables a basic .blend game file to start.   By making a basic file which contains an "Always" sensor to run, and allowing this to activate a  "Game" actuator to load and run  the full content of your game, this gets round the problem.   Your main file is now "outside" the  Standalone Player, so that it need not be open to GPL and is therefore  "legally protected".  Although your game is not fully protected with this system, it affords a similar level of protection to that used in most other distributed games. The fact that others can access your .blend file does not mean that it can be used for purposes not covered by the license you want.

(Acknowledgements: This page is based on information contained in the blog file of Dalai Felinto).


