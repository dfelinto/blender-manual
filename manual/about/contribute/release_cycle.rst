
*************
Release Cycle
*************

A new Blender version is targeted to be released every 3 months.
The actual `release cycle <https://wiki.blender.org/wiki/Process/Release_Cycle>`__ for a specific release is longer,
and overlaps the previous and next release cycle.

.. figure:: /images/about_contribute_release_cycle.png


Branches
========

Work is done in two branches:

- ``blender-v{VERSION}-release`` branch: fixes and other incremental improvements.
- ``master`` branch: documentation for new features and improvements for the release after that.

The ``blender-v{VERSION}-release`` branch will be available for 5 weeks prior to the release date.
At the same time ``master`` will be open for the next release,
giving 2 months to add documentation for new features of the next release, and another month to make improvements.


Bcon Phases
===========

Each Blender version has its own Bcon phase,
indicating which types of changes are allowed to be committed and what writers are focusing on.

That means for example that Blender 2.90 can be in Bcon3 (wrapping up),
while Blender 2.91 is in Bcon1 (new features and changes).

.. list-table::
   :header-rows: 1
   :widths: 5 20 20 50 5

   * - Phase
     - Description
     - Duration
     - Details
     - Branch

   * - Bcon1

     - New features and changes

     - 4-5 weeks

     - The first 5 weeks overlap with the Bcon3 and Bcon4 phases of the previous release,
       Writing focus will be split on fixes for the previous release
       and writing documentation for features already added or likely to be added to Blender.
       This is also the perfect time to make any larger or more disruptive improvements to the manual.

     - ``master``

   * - Bcon2

     - Improve and stabilize

     - 4 weeks

     - Work to improve, optimize and fix bugs in new and existing features.
       All big or disruptive changes must be finished at the end of this stage.

     - ``master``

   * - Bcon3

     - Wrapping up

     - 4 weeks

     - Focus should be on fixes and other incremental improvements.
       All new Blender features should be documented by the end of this stage.

     - ``blender-v{VERSION}-release``

   * - Bcon4

     - Prepare release

     - 1 week

     - Focus should be wrapping up fixes and other incremental improvements.

     - ``blender-v{VERSION}-release``

   * - Bcon5

     - Release

     - 1-2 days

     - The manual is archived on the server and redirects / symlinks are updated.
       See the :ref:`Release Guide <about-contribute-guides-release>` for more information.

     -

   * - Bcon6

     - Long-term release

     - 2 years

     - In case a major error is found in the manual the patch will be committed to the release branch.

     - ``blender-v{VERSION}-release``
