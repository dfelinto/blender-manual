
Random Actuator
===============

Sets a random value into a property of the object


See :doc:`Actuator Common Options <game_engine/logic/actuators/common_options>` for common options.

Special Options:


.. figure:: /images/BGE_Actuator_Random_Bool_Constant.jpg
   :width: 271px
   :figwidth: 271px

   Camera Actuator


**Seed**
Starting seed for random generator (range 1 - 1000)

**Distribution**
Menu of distributions from which to select the random value.
The default entry of Boolean Constant gives either True or False,
which is useful for test purposes.


.. figure:: /images/BGE_Actuator_Random_Float_Neg_Exp.jpg
   :width: 271px
   :figwidth: 271px

   Float Neg. Exp.


:guilabel:`Float Neg. Exp.`
   Values drop off exponentially with the specified half-life time.

   **Property**
      Float property to  receive value
   **Half-Life Time**
      Half-life time (Range 0.00 -10000.00)


.. figure:: /images/BGE_Actuator_Random_Float_Normal.jpg
   :width: 271px
   :figwidth: 271px

   Float Normal


:guilabel:`Float normal`
   Random numbers from a normal distribution.

   **Property**
      Float property to  receive value
   **Mean**
      Mean of normal distribution (Range -10000.00 to +10000.00)
   **SD**
      Standard deviation of normal distribution (Range 0.00 to +10000.00)


.. figure:: /images/BGE_Actuator_Random_Float_Uniform.jpg
   :width: 271px
   :figwidth: 271px

   Float Uniform


:guilabel:`Float uniform`
   Random values selected uniformly between maximum and minimum.

   **Property**
      Float property to  receive value
   **Min**
      Minimum value (Range -10000.00 to +10000.00)
   **Max**
      Maximum value (Range -10000.00 to +10000.00)


.. figure:: /images/BGE_Actuator_Random_Float_Constant.jpg
   :width: 271px
   :figwidth: 271px

   Float Constant


:guilabel:`Float constant`
   Returns a constant value.

   **Property**
      Float property to  receive value
   **Value**
      Value (Range 0.00 to +1.00)


.. figure:: /images/BGE_Actuator_Random_Int_Poisson.jpg
   :width: 271px
   :figwidth: 271px

   Random Integer Poisson


:guilabel:`Int Poisson`
   Random numbers from a Poisson distribution.

   **Property**
      Integer property to  receive value
   **Mean**
      Mean of Poisson distribution (Range 0.01 to +100.00)


.. figure:: /images/BGE_Actuator_Random_Int_Uniform.jpg
   :width: 271px
   :figwidth: 271px

   Random Integer Uniform


:guilabel:`Int uniform`
   Random values selected uniformly between maximum and minimum.

   **Property**
      Integer property to  receive value
   **Min**
      Minimum value (Range -1000 to +1000)
   **Max**
      Maximum value (Range -1000 to +1000)


.. figure:: /images/BGE_Actuator_Random_Int_Constant.jpg
   :width: 271px
   :figwidth: 271px

   Random Integer Constant


:guilabel:`Int constant`
   Returns a constant value.

   **Property**
      Integer property to  receive value
   **Value**
      Value (Range 0.00 to +1.00)


.. figure:: /images/BGE_Actuator_Random_Bool_Bernoulli.jpg
   :width: 271px
   :figwidth: 271px

   Random Bool Bernoulli


:guilabel:`Bool Bernoulli`
   Returns a random distribution with specified ratio of TRUE pulses.

   **Property**
      Boolean property to  receive value
   **Chance**
      Proportion of TRUE responses required.


.. figure:: /images/BGE_Actuator_Random_Bool_Uniform.jpg
   :width: 271px
   :figwidth: 271px

   Random Bool Uniform


:guilabel:`Bool uniform`
   A 50/50 chance of obtaining True/False.

   **Property**
      Boolean property to  receive value


.. figure:: /images/BGE_Actuator_Random_Bool_Constant.jpg
   :width: 271px
   :figwidth: 271px

   Random Bool Constant


:guilabel:`Bool constant`
   Returns a constant value.

   **Property**
      Boolean property to  receive value
   **Value**
      Value (True or False)


