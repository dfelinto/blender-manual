.. _bpy.types.FluidDomainSettings.use_viscosity:

*********
Viscosity
*********

.. _bpy.types.FluidDomainSettings.viscosity_value:

Strength
   The viscosity of the liquid. Higher values result in more viscous fluids.

   .. note::

      A strength value of 0 will still apply some viscosity. Uncheck the 
      :ref:`viscosity flag<bpy.types.FluidDomainSettings.use_viscosity>` to disable the viscosity simulation
      step completely.


   .. list-table:: Rotating liquid inflow with varying viscosities.

      * - .. figure:: /images/physics_fluid_type_domain_liquid_viscosity_0-2.png

             Viscosity of 0.2 (frame 65).

        - .. figure:: /images/physics_fluid_type_domain_liquid_viscosity_0-4.png

             Viscosity of 0.4 (frame 200).
