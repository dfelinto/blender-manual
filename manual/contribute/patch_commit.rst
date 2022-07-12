.. highlight:: sh

**************
Patch & Commit
**************

.. _contribute-patch_submit:

Submit Patches
==============

The first few times you make changes to the manual,
you will need to submit them as patches for an administrator to review.
This is just to make sure that we maintain a quality user manual,
and that you do not accidentally break anything vital before you get used to the system.

In order to submit a patch, follow this process:

#. Make any changes that you want.
#. Create a patch file by running::

      svn diff > filename.diff

   This creates a simple text file that shows what text was added,
   removed or changed between your working files and the central repository.

   If you have created or deleted files, you will need to run ``svn add /path/to/file``
   or ``svn rm /path/to/file`` before creating the diff. To see a list of affected files, run ``svn status``.
#. `Upload the diff file here <https://developer.blender.org/differential/diff/create/>`__.
   If you do not have an account already,
   you can `register for one <https://developer.blender.org/auth/register/>`__.
#. After submitting the diff, you will be asked to "Create a new Revision"
   before you can add a title and description of your changes.
#. Please check if the Documentation project is assigned in the tag's field in order to notify
   the team of your patch.
   You can also :ref:`contact <contribute-contact>` the team over the mailing list or :ref:`blender-chat`.
#. They will review your patch and let you know about any changes you could make.
   If there is no issue, your patch will be accepted and then committed by the team of your patch.

.. note::

   If your patch includes changes to or additional images,
   simply attach them when you are creating the revision.

Straightforward patches are bound to be accepted very quickly.
Once you get accustomed to making changes and no longer need feedback,
we cut out the middle man and give you direct access to edit the manual.

.. seealso::

   See :doc:`/contribute/release_cycle` for documentation on how to make
   commits to a specific release branch and how to create merge commits.


Commit Directly
===============

Once you are provided with the direct access to edit the manual,
you can start committing directly instead of creating a patch file.
Doing this will submit the change directly to our central repository.

All you need to do now is run::

   svn commit -m "This is what I did"

If you leave out ``-m "message"``, you will be prompted to type the message in a text editor.

Do not forget to always run ``svn update`` before committing.

Then you will be asked for your username and password
(from ``developer.blender.org``) before the change is committed.

.. note::

   Make sure to use your username (case sensitive) and not your email.

Your modified files are uploaded to the central repository for others to work with and continue collaborating.
Commits are tracked in the repositories `Diffusion <https://developer.blender.org/diffusion/BM/>`__.
Soon after your changes become visible in the online manual.


Writing a Good Commit Message
-----------------------------

When making changes to the manual that directly relate to a specific commit (change) in Blender,
it is helpful to make the title of the commit the same as the commit made to Blender.
It is requested that you include the commit hash of the commit made to the Blender source code.

For example, the commit `rBM8473 <https://developer.blender.org/rBM8473>`__
includes a descriptive indicative of the changes made along with the hash ``rBa71d2b260170``.
The hash can be extracted from the URL provided in the Documentation task for a specific upcoming release.

----

Other more general changes do not have to follow the above policy however,
it is still important to make the description clear about what changes you made and why.
It can be helpful to prefix the commit title with a prefix word such as ``Cleanup:`` or ``Fix:``
when you are making general cleanups or fixes respectively.

Writing good commit messages helps administrators keep track of
changes made and ensures all new features are properly documented.
