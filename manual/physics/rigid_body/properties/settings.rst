
********
Settings
********

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Physics --> Rigid Body --> Settings`

.. TODO2.8:
   .. figure:: /images/physics_rigid-body_properties_panel.png

      Default rigid body panel.

Mass
   Specifies how heavy the object is and "weights" irrespective of gravity.
   There are predefined mass presets available with *Calculate Mass*
   in the :menuselection:`Object --> Rigid Body` menu.

   Calculate Mass
      Automatically calculate mass values for rigid body objects based on their volume.
      There are many useful presets available from the menu, listing real-world objects.

      .. note::

         You can also have a *Custom* mass material type,
         which is achieved by setting a custom density value (kg/m\ :sup:`3`).

Dynamic
   Enables/disables rigid body simulation for the object.

Animated
   Allows the rigid body to additionally be controlled by the animation system.
