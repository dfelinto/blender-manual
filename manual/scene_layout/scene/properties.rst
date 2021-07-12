
****************
Scene Properties
****************

.. _bpy.types.Scene.camera:
.. _bpy.types.Scene.background_set:
.. _bpy.types.Scene.active_clip:

Scene
=====

.. reference::

   :Panel:     :menuselection:`Properties --> Scene --> Scene`

.. _scene-camera:

Camera
   Used to select which camera is used as the active camera.
   You can also set the active camera in the 3D Viewport with :kbd:`Ctrl-Numpad0`.

.. _scene-background-set:

Background Scene
   Allows you to use a scene as a background,
   this is typically useful when you want to focus on animating the foreground for example,
   without background elements getting in the way.

   This scene can have its own animation, physics simulations, etc,
   but you will have to select it from the *Scene* data-block menu, if you want to edit any of its contents.

   Sets can themselves have a background set (they're recursively included).
   So you can always make additions to existing scenes by using them as a background
   to a newly created scene where your additions are made.

   .. tip::

      This can also be used in combination with :ref:`Linking to a Scene <bpy.ops.object.make_links_scene>`,
      where one blend-file contains the environment, which can be reused in many places.

.. _scene-active-clip:

Active Clip
   Active movie clip for constraints and viewport display.


.. _data-scenes-props-units:
.. _bpy.types.UnitSettings:

Units
=====

.. reference::

   :Panel:     :menuselection:`Properties --> Scene --> Units`

Unit System
   None
      Use units that have with no relation to the real world,
      practically this is the same as *Metric* just without unit names.
   Metric
      Use the metric unit system in this scene.
   Imperial
      Use the imperial unit system in this scene.

Unit Scale
   Scale factor to use when converting between internal units and values displayed in the user interface.
   This can be changed when modeling at microscopic or astronomical scales.

   .. note::

      This only influences the values displayed in the user interface
      and not how things behave internally. For example, physics simulations
      don't take the unit scale into account.

Separate Units
   When using *Metric* or *Imperial*, display properties as multiple values.
   For example, ``2.285m`` will become ``2m 28.5cm``.

Rotation
   Degrees
      Use degrees for angles in the user interface.
   Radians
      Use radians for angles in the user interface.

Length
   Adaptive
      The unit used for a specific value depends on the magnitude of the value.
      For example, some values might be displayed as ``23cm`` while others are
      displayed as ``10km``.
   Meters/Centimeters/Feet/...
      A fixed unit that will be used for all lengths in the user interface.

Mass
   See *Length*.

Time
   See *Length*.

Temperature
   See *Length*.

.. Normally we would avoid documenting long lists of values
   however, this is not displayed anywhere else.

.. list-table:: Imperial Length Units
   :header-rows: 1
   :stub-columns: 1

   * - Full Name
     - Short Name(s)
     - Scale of a Meter
   * - thou
     - ``mil``
     - 0.0000254
   * - inch
     - ``"``, ``in``
     - 0.0254
   * - foot, feet
     - ``'``, ``ft``
     - 0.3048
   * - yard
     - ``yd``
     - 0.9144
   * - chain
     - ``ch``
     - 20.1168
   * - furlong
     - ``fur``
     - 201.168
   * - mile
     - ``mi``, ``m``
     - 1609.344

.. list-table:: Metric Length Units
   :header-rows: 1
   :stub-columns: 1

   * - Full Name
     - Short Name(s)
     - Scale of a Meter
   * - micrometer
     - ``um``
     - 0.000001
   * - millimeter
     - ``mm``
     - 0.001
   * - centimeter
     - ``cm``
     - 0.01
   * - decimeter
     - ``dm``
     - 0.1
   * - meter
     - ``m``
     - 1.0
   * - dekameter
     - ``dam``
     - 10.0
   * - hectometer
     - ``hm``
     - 100.0
   * - kilometer
     - ``km``
     - 1000.0


Gravity
=======

.. reference::

   :Panel:     :menuselection:`Properties --> Scene --> Gravity`

Options to control global gravity used for physics effects.

See the :doc:`Physics chapter </physics/forces/gravity>` for more information.


Keying Sets
===========

.. reference::

   :Panel:     :menuselection:`Properties --> Scene --> Keying Sets`

See :doc:`/animation/keyframes/keying_sets`.


.. _data-scenes-audio:
.. _bpy.types.Scene.audio_volume:
.. _bpy.types.Scene.audio_distance_model:
.. _bpy.types.Scene.audio_doppler_speed:
.. _bpy.types.Scene.audio_doppler_factor:

Audio
=====

.. reference::

   :Panel:     :menuselection:`Properties --> Scene --> Audio`

Options to control global audio settings.
To control how sounds is played back from within Blender, see the audio settings
in the :ref:`Preferences <prefs-system-sound>`.

Volume
   Volume for the scene.

Distance Model
   Changes how the sound attenuation is calculated based on the distance.
   Most physically correct is the *Inverse* model,
   but it's also possible to choose a linear and an exponential falloff.
   The clamped modes limit the volume to be lower than 100% (1.0),
   that means if the distance is smaller than the reference distance, the volume is always 100%.
   For an exact description of each option
   see the `OpenAL documentation <https://www.openal.org/documentation/>`__.
Doppler Speed
   Speed of the sound for the Doppler effect calculations.
   The typical value is 343.3 m/s in air, in water for example this value is around 1560 m/s.
Doppler Factor
   Controls how strong the Doppler effect is.
   You can exaggerate or attenuate the change of pitch, but physically correct is a factor of 1.0.

.. _bpy.ops.sound.bake_animation:

Update Animation Cache
   Updates the audio animation cache. This is useful if you start noticing artifact in the audio.


Rigid Body World
================

.. reference::

   :Panel:     :menuselection:`Properties --> Scene --> Rigid Body World`

The *Rigid Body World* is a group of rigid body objects,
which holds settings that apply to all rigid bodies in this simulation.

See :doc:`Rigid Body World </physics/rigid_body/world>` for more information.
