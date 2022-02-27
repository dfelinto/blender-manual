*************************
PDT Trigonometrical Waves
*************************

The Menu for Trigonometrical Waves

.. figure:: /images/addons_pdt_trig_1.png
   :align: left
   :width: 300px

.. container:: lead

   .. clear
This section of PDT is used to generate Trigonometrical Waves in a selected Object. In order to enable the ``Generate`` button, the use must first select an object using the ``Object Selector`` box.

There are then a number of parameters that need to be set:

* The ``Working Plane`` - this is just a duplicate display of the main PDT ``Working Plane``.
* The ``Wave Form`` - Sine Cosine, or Tangent.
* The number of ``Cycles`` - each cycle is 180 degrees, NOT a full circle, so a value of 1 will result in one peak with a sine wave for example.
* The ``Cycle Length`` - the length in blend file units of one cycle.
* The ``Amplitude`` - the height of the wave.
* Whether to ``Empty`` the target object, set to true this will delete all vertices in the target object.
* The ``Resolution`` - the number of vertices on one cycle.
* If you are generating a ``Tangent`` wave, the maximum amplitude of the wave. Tangent functions range from 0 to infinity over a 90 degree wave, so this limits the extent to which the tangent wave will extend.
* The ``Start Location`` - the point at which the first vertex will appear in Global Coordinates.
* Whether ``Absolute`` values are required. In this context Absolute means greater than 0, so all peaks will be positive.

Here is a "Before" image:

.. figure:: /images/addons_pdt_trig_2.png
   :align: left
   :width: 450px

.. container:: lead

   .. clear
And here is an "After" image:

.. figure:: /images/addons_pdt_trig_3.png
   :align: left
   :width: 450px

.. container:: lead

   .. clear

Here is an example of "Absolute" values using a Sine Wave:

.. figure:: /images/addons_pdt_trig_4.png
   :align: left
   :width: 450px

.. container:: lead

   .. clear

And finally an example of a Tangent Wave limited to a maximum value of 5:

.. figure:: /images/addons_pdt_trig_5.png
   :align: left
   :width: 450px

.. container:: lead

   .. clear
