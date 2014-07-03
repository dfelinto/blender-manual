
Drivers
=======


Drivers
-------


.. figure:: /images/Doc_Animation_Driver_FCurve.jpg

   Graph Editor: Driver example.


Drivers can use properties, numbers, transformations, and scripts,
to control the values of properties.

Using a F-Curve, the driver reads the value of the Driver Value and sets the value of the
selected property it was added to.

So from this example, if the Driver Value is 2.0 the property will be 0.5.

The Driver Value is determined by Driver Variables or a Scripted Expression.

Most the settings for the drivers :doc:`F-Curves <animation/editors/graph/fcurves>` are found in the :doc:`Graph Editor <animation/editors/graph>`\ .


Drivers Panel
-------------


.. figure:: /images/Doc_Animation_Panel_Drivers.jpg

   Graph Editor: Drivers: Drivers Panel.


This panel is located in the :doc:`Graph Editor <animation/editors/graph>` with the mode set to Drivers.

The drivers panel is for setting up *Driver Variables* or a *Scripted Expression* which
will determine the value of the *Driver Value*\ .


Driver Settings
_______________


:guilabel:`Update Dependencies`
   This will force an update for the Driver Value dependencies.

:guilabel:`Remove Driver`
   Removes the driver from the object.

:guilabel:`Type`
   The type of calculation to use on the set of Driver Variables.  (If you only have one driver variable there is no real difference between average, sum, minimum and maximum)

   :guilabel:`Average Value`
      Uses the the average value of the referenced Driver Variables.

   :guilabel:`Sum Values`
      Uses the the sum of the referenced Driver Variables.

   :guilabel:`Scripted Expression`
      Uses a Scripted Expression. See Expr.
      You must write a python expression which performs your own calculations on the Driver Variables.

   :guilabel:`Minimum Value`
      Uses the lowest value from the referenced Driver Variables.

   :guilabel:`Maximum Value`
      Uses the highest value from the referenced Driver Variables.

:guilabel:`Expr`
   Scripted Expression.
   Here you can add real numbers, math operators, math functions, python properties, driver functions.
   See Driver Expression below for some examples.

:guilabel:`Show Debug Info`
   Shows the Driver Value.
   The current value of the variables or scripted expression.

:guilabel:`Add Variable`
   Adds a new Driver Variable.


.. figure:: /images/Doc_Animation_Driver_Single_Property.jpg

   Setup of a Single Property.


.. figure:: /images/Doc_Animation_Driver_Transform_Channel2.jpg

   Transform Channel setup.


.. figure:: /images/Doc_Animation_Driver_Distance.jpg

   Distance setup.


Driver Variables
________________


:guilabel:`Name`
   Name to use for scripted expressions/functions.
   No spaces or dots are allowed and must start with a letter.

:guilabel:`Variable Type`
   The type of variable to use.

   :guilabel:`Single Property`
      Use the value from some RNA property.
      For example, the Ambient shading color from a material.
      First select the type of ID-block, then the ID of the ID-block, then copy and paste an RNA property (Ctrl+V).

      :guilabel:`ID-Type`
         The ID-Block type, example, Key, Image, Object, Material.

      :guilabel:`ID`
         The ID of the ID-Block type, example, Material.001.

      :guilabel:`RNA Path`
         The RNA id name of the property, example, 'ambient' from material shading.

   :guilabel:`Transform Channel`
      Use one of the Transform channels from an object or bone.

      :guilabel:`ID`
         ID of the object, example, Cube, Armature, Camera.

      :guilabel:`Bone`
         ID of the Armature bone, example, Bone, Bone.002, Arma.r.
         This option is for armatures.

      :guilabel:`Type`
         Example, X Location, X Rotation, X Scale.

      :guilabel:`Space`
         World Space, Transform Space, Local Space.

   :guilabel:`Rotational Difference`
      Use the rotational difference between two objects or bones.

   :guilabel:`Distance`
      Use the distance between two objects or bones.

:guilabel:`Value`
   Shows the value of the variable.


Workflow
--------


Adding Drivers
______________


To control a property with a driver, find the property you want to add driver to.


FIXME(Template Unsupported: Shortcut/Mouse;
{{Shortcut/Mouse|rmb}}
) the property and select one of the following options.

:guilabel:`Add Drivers`
    This will add drivers to the set of properties related to the selected one.
    For example, it will add drivers to X, Y, and Z for Rotation.

:guilabel:`Add Single Driver`
    This will add a single driver to the selected property.


.. figure:: /images/Doc_Add_Driver2.jpg

   Add Single Driver.


Transform Driver
________________


This example shows you how rotate a cube mesh by moving another cube left or right in the 3D
view.
First make sure you are in the *Front Orthographic View* :kbd:`Num1`\ ,
:kbd:`Num5`\ .


- In *Object Mode* select then *Duplicate* :kbd:`Shift-D` the default Cube.
-    Move the cube to a new location. You should have two mesh objects, *Cube* and *Cube.001*\ .
- With *Cube.001* selected as the active object, *Add Single Driver* to the *Rotation Y* property.
- Open the *Graph Editor*\ , set the mode to *Drivers*\ .
-    *Show Only Selected* is useful disabled for drivers, marked in green.
- Open the Properties Region :kbd:`N`\ , go to the *Drivers Panel*\ .
-    You may need to select the driver *Y Euler Rotation* :kbd:`LMB` for the *Drivers Panel* to appear.
- Set the driver *Type* to *Sum Values*\ .
- Set the driver variable *var* settings.
-    Set *Type* to *Transform Channel*\ .
-    Set *Ob/Bone ID-block* to *Cube*\ .
-    Set *Transform Type* to *X Location*\ .
-    Set *Transform Space* to *World Space*\ .


.. figure:: /images/Doc_Drivers_TD_Workflow.jpg

   Transform Driver workflow.


Now when you move the *Cube* left or right in the 3D View, *Cube.001* should rotate.


Examples
--------


Some Driver Examples.


Driver Expression
_________________


Here are some examples using the scripted expression Expr to set the Driver Value.


.. figure:: /images/Doc_Animation_Driver_Object_Rotation.jpg

   Object Rotation.


Orbit a point
+++++++++++++


Here two drivers have been added to the Cube, X Location and Y Location.

The scripted expressions are being used to set the object location.

:guilabel:`X Location Expr`
   **0+(sin(frame/8)*4)**
       **(frame/8)**\ : is the current frame of the animation, divided by 8 to slow the orbit down.
       **(sin( )*4)**\ : This returns the sine of (frame/8), then multiplies by 4 for a bigger circle.
       **0+**\ : is used to control the X Location offset of the orbit.
:guilabel:`Y Location Expr`
   **0+(cos(frame/8)*4)**
       **(frame/8)**\ : is the current frame of the animation, divided by 8 to slow the orbit down.
       **(cos( )*4)**\ : This returns the cosine of (frame/8), then multiplies by 4 for a bigger circle.
       **0+**\ : is used to control the Y Location offset of the orbit.

**frame** is the same as bpy.context.scene.frame_current.


Driver Namespace
++++++++++++++++


There is a list of built in driver functions and properties.
These can be displayed via the python console.
::

   >>> bpy.app.driver_namespace['
   __builtins__']
   __doc__']
   __loader__']
   __name__']
   __package__']
   acos']
   acosh']
   asin']
   asinh']
   atan']
   atan2']
   atanh']
   bpy']
   ceil']
   copysign']
   cos']
   cosh']
   ..


This script will add a function to the driver namespace,
which can then be used in the expression **driverFunc(frame)**\ .

::

   import bpy

   def driverFunc(val):

   return val * val    # return val squared

   bpy.app.driver_namespace['driverFunc']
   = driverFunc    # add function to driver_namespace


Shape Key Driver
________________


This example is a Shape Key Driver. The driver was added to the shape key Value.


.. figure:: /images/Doc_Animation_Driver_Shape_Key.jpg
   :width: 400px
   :figwidth: 400px

   Shape Key Driver. Click to enlarge.


This example uses the Armature Bone 'b' Z Rotation to control the Value of a Shape Key.
The bone rotation mode is set to XYZ Euler.

The Driver F-Curve is mapped like so
   Bone Z Rotation 0.0(0.0): Shape Key value 0.0
   Bone Z Rotation -2.09(-120.0): Shape Key value 1.0

This kind of driver can also be setup with the Variable Type Rotational Difference.

See :doc:`Shape Keys <animation/basics/shape_keys>` for more info.


Drivers And Multiple Relative Shape Keys
----------------------------------------


The following screenshots illustrate combining shape keys, bones, and
drivers to make multiple chained relative shape keys sharing a single
root.  While it lacks the convenience of the single Evaluation Time of
an absolute shape key, it allows you to have more complex
relationships between your shape keys.


.. figure:: /images/Driver_For_Multiple_Shape_Keys_Key1.jpg

   Key1 must handle conflicting values from the two


FIXME(TODO: Internal Link;
[[bones]]
)


.. figure:: /images/Driver_For_Multiple_Shape_Keys_Key2A.jpg

   Key2A has different generator coefficients so it


FIXME(TODO: Internal Link;
[[is activated in a different range of the bone's position.]]
)


.. figure:: /images/Driver_For_Multiple_Shape_Keys_Key2B.jpg

   Key2B is the same as Key2A,


FIXME(TODO: Internal Link;
[[but is controlled by the second bone.]]
)


.. figure:: /images/Driver_For_Multiple_Shape_Keys_Retracted.jpg

   when both bones are low,


FIXME(TODO: Internal Link;
[[Key2B and Key2A are deactivated and Key1 is at low influence.]]
)


.. figure:: /images/Driver_For_Multiple_Shape_Keys_Extended.jpg


The Basis shape key has the stacks fully retracted.  Key1 has the base
fully extended.  Key2A has the left stack fully extended.  Key2B has
the right stack fully extended.  Key2A and Key2B are both relative to
Key1 (as you can see in the field in the bottom right of the Shape Keys
panel.

The value of Key1 is bound to the position of bones by a driver with
two variables.  Each variable uses the world Z coordinate of a bone
and uses the maximum value to determine how much the base should be
extended.  The generator polynomial is crafted such that the top of
the dominant stack should line up with the bone for that stack.

The value of Key2A is bound to the position of bone.L .  Its generator
parameters are crafted such that when Key1's value reaches 1, the
value of Key2A starts increasing beyond zero.  In this way the top of
the left stack will move with bone.L (mostly).

The value of Key2B is bound to the position of bone.R .  Its generator
parameters are similar to Key2A so that the top of the right stack
will move with bone.R (mostly).

Since it's quite easy for bone.L and bone.R to be in positions that
indicate conflicting values for Key1 there will be times when the
bones do not line up with the tops of their respective stacks.  If the
driver for Key1 were to use Average or Minimum instead of Maximum to
determine the value of the shape key then "conflicts" between bone.L
and bone.R would be resolved differently.  You will chose according to
the needs of your animation.


Troubleshooting
---------------


Some common problems people may run in to when using drivers.


Scripted Expression
___________________


.. figure:: /images/Doc_Drivers_Auto_Run_B.jpg

   Graph Editor > Properties > Drivers.


.. figure:: /images/Doc_Drivers_Auto_Run_A.jpg

   Info Header.


By default blender will not auto run python scripts.

If using a *Scripted Expression* Driver Type,
you will have to open the file as *Trusted Source*\ ,
or set *Auto Run Python Scripts* in *User Preferences > File > Auto Execution*\ .


.. figure:: /images/Doc_Drivers_Auto_Run_C.jpg

   File Browser.


.. figure:: /images/Doc_Drivers_Auto_Run_D.jpg

   User Preference > File > Auto Execution.


Rotational Properties are Radians
_________________________________


Parts of the User Interface may use different units of measurements for angles, rotation.
In the Graph Editor while working with Drivers, all angles are Radians.


Intra-armature Bone Drivers Can Misbehave
_________________________________________


There is a `well known limitation <https://developer.blender.org/T40301>`__
with drivers on bones that refer to another bone in the same armature.  Their values can be
incorrectly calculated based on the position of the other bone as it was *before* you adjust
the current_frame.  This can lead to obvious shape glitches when the rendering of frames has
a jump in the frame number (either because the .blend file is currently on a different frame
number or because you're skipping already-rendered frames).


See Also
--------


- :doc:`Animation <animation>`
- :doc:`Graph Editor <animation/editors/graph>`
- :doc:`F-Curves <animation/editors/graph/fcurves>`
- :doc:`Extending Blender with python <extensions/python>`\ .


Links
-----


- `Python <http://www.python.org>`__ and its `documentation <http://www.python.org/doc>`__\ .
- `functions.wolfram.com <http://functions.wolfram.com/>`__