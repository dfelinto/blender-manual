
..    TODO/Review: {{review|text=simplify?}} .


Spot Buffered Shadows
=====================

.. figure:: /images/25-Manual-Lighting-Shadow-SpotBufShad.jpg
   :width: 310px
   :figwidth: 310px

   Buffer Shadow enabled for a Spot lamp


Spotlights can use either :doc:`Raytraced Shadows <lighting/lamps/spot#raytraced_shadows>` or buffered shadows. Either of the two can provide various extra options.

Raytraced shadows are generally more accurate,
with extra capabilities such as transparent shadows, although they are quite slower to render.

Buffered shadows are more complex to set up and involve more faking, but the speed of rendering is a definite advantage. Nevertheless, it shares with other lamp types common shadows options described in :doc:`Shadows Properties <lighting/shadows/properties>`\ .


Shadow Buffer Types
-------------------

When the :guilabel:`Buffer Shadow` button is activated,
the currently selected :guilabel:`Spot` light generates shadows,
using a "shadow buffer" rather than using raytracing,
and various extra options and buttons appear in the :guilabel:`Shadow` panel.

:guilabel:`Buffer Type`
   There more than one way to generate buffered shadows. The shadow buffer generation type controls which generator to use.
There are four shadow generation types, those being:

   - :guilabel:`Classical`
   - :guilabel:`Classic-Halfway`
   - :guilabel:`Irregular`
   - :guilabel:`Deep`

For more information on the different shadow generation methods see these links:

- `Development Release Logs 2.43: Irregular Shadow Buffer <http://www.blender.org/development/release-logs/blender-243/irregular-shadow-buffer/>`__
- `Blender Nation: Blender Gets Irregular Shadow Buffers <http://www.blendernation.com/2006/10/15/blender-gets-irregular-shadow-buffers/>`__
- `Development Release Logs 2.43: Shadow Buffer Halfway Average <http://www.blender.org/development/release-logs/blender-243/shadow-buffer-halfway-average/>`__


"Classical" and "Classic-Halfway"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/25-Manual-Lighting-Shadow-SpotBufShad.jpg
   :width: 310px
   :figwidth: 310px

   Buffer Shadowset to Classic-Halfway


:guilabel:`Classical`
    A shadow generation which used to be the Blender default and unique method for generation of buffered shadows. It used an older way of generating buffered shadows, but it could have some problems with accuracy of the generated shadows and can be very sensitive to the resolution of the shadow buffer (\ :guilabel:`Shadow Buffer`\ →\ :guilabel:`Size`\ ), different :guilabel:`Bias` values, and all the self-shadowing issues that brings up.

   The :guilabel:`Classical` method of generating shadows is obsolete and is really only still present to allow for backward compatibility with older versions of Blender.  In most other cases you will want to use :guilabel:`Classic-Halfway` instead.

:guilabel:`Classic-Halfway`
    This shadow buffer type is an improved shadow buffering method and is the default option selected in Blender. It works by taking an averaged reading of the first and second nearest Z depth values allowing the :guilabel:`Bias` value to be lowered and yet not suffer as much from self-shadowing issues.

   Not having to increase :guilabel:`Bias` values helps with shadow accuracy, because large :guilabel:`Bias` values can mean small faces can lose their shadows, as well as preventing shadows being overly offset from the larger :guilabel:`Bias` value.

    :guilabel:`Classic-Halfway` doesn't work very well when faces overlap, and biasing problems can happen.

Here are now the options specific to these generation methods:
:guilabel:`Size`
    The :guilabel:`Size` numeric field can have a value from **512** to **10240**\ . :guilabel:`Size` represents the resolution used to create a shadow map. This shadow map is then used to determine where shadows lay within a scene.

    As an example, if you have a :guilabel:`Size` with a value of **1024**\ , you are indicating that the shadow data will be written to a buffer which will have a square resolution of **1024×1024** pixels/samples from the selected spotlight.

    The higher the value of :guilabel:`Size`\ , the higher resolution and accuracy of the resultant shadows, assuming all other properties of the light and scene are the same, although more memory and processing time would be used. The reverse is also true - if the :guilabel:`Size` value is lowered, the resultant shadows can be of lower quality, but would use less memory and take less processing time to calculate.

    As well as the :guilabel:`Size` value affecting the quality of generated shadows, another property of :guilabel:`Spot` lamps that affects the quality of their buffered shadows is the angle of the spotlights lighted area (given in the :guilabel:`Spot Shape` panel's :guilabel:`Size` field).

    As the spot shape :guilabel:`Size` value is increased, the quality of the cast shadows degrades. This happens because when the :guilabel:`Spot` lighted area is made larger (by increasing spot shape :guilabel:`Size`\ ), the shadow buffer area has to be stretched and scaled to fit the size of the new lighted area.

   The :guilabel:`Size` resolution is not altered to compensate for the change in size of the spotlight, so the quality of the shadows degrades. If you want to keep the generated shadows the same quality, as you increase the spot shape :guilabel:`Size` value, you also need to increase the buffer :guilabel:`Size` value.

.. admonition:: The above basically boils down to
   :class: note

    If you have a spotlight that is large you will need to have a larger buffer :guilabel:`Size` to keep the shadows good quality. The reverse is true also - the quality of the generated shadows will usually improve (up to a point) as the :guilabel:`Spot` lamp covers a smaller area.


:guilabel:`Filter Type`
    The :guilabel:`Box`\ , :guilabel:`Tent`\ , and :guilabel:`Gauss` filter types control what filtering algorithm to use to anti-alias the buffered shadows.

    They are closely related to the :guilabel:`Samples` numeric field, as when this setting is set to **1**\ , shadow filtering is disabled, so none of these buttons will have any effect what soever.

   :guilabel:`Box`
       The buffered shadows will be anti-aliased using the "box" filtering method.
       This is the original filter used in Blender.
       It is relatively low quality and is used for low resolution renders, as it produces very sharp anti-aliasing.
       When this filter is used,
       it only takes into account oversampling data which falls within a single pixel,
       and doesn't take into account surrounding pixel samples.
       It is often useful for images which have sharply angled elements and horizontal/vertical lines.

   :guilabel:`Tent`
       The buffered shadows will be anti-aliased using the "tent" filtering method.
       It is a simple filter that gives sharp results, an excellent general purpose filtering method. This filter also takes into account the sample values of neighboring pixels when calculating its final filtering value.

   :guilabel:`Gauss`
       The buffered shadows will be anti-aliased using the "Gaussian" filtering method.
       It produces a very soft/blurry anti-aliasing. As result, this filter is excellent with high resolution renders.

    The :doc:`Anti-Aliasing page <render/options/antialiasing>` in the Render chapter will give more information on the various filtering/distribution methods and their uses.

:guilabel:`Samples`
    The :guilabel:`Samples` numeric field can have a value between **1** and **16**\ . It controls the number of samples taken per pixel when calculating shadow maps.

    The higher this value, the more filtered, smoothed and anti-aliased the shadows cast by the current lamp will be, but the longer they will take to calculate and the more memory they will use. The anti-aliasing method used is determined by having one of the :guilabel:`Box`\ , :guilabel:`Tent` or :guilabel:`Gauss` buttons activated (see above).

    Having a :guilabel:`Samples` value of **1** is similar to turning off anti-aliasing for buffered shadows.

:guilabel:`Soft`
   The :guilabel:`Soft` numeric field can have a value between **1.0** and **100.0**\ . It indicates how wide an area is sampled when doing anti-aliasing on buffered shadows. The larger the :guilabel:`Soft` value, the more graduated/soft the area that is anti-aliased/softened on the edge of generated shadows.

:guilabel:`Sample Buffers`
   The :guilabel:`Sample Buffers` setting can be set to values **1**\ , **4** or **9**\ , and represents the number of shadow buffers that will be used when doing anti-aliasing on buffered shadows.

    This option is used in special cases, like very small objects which move and need to generate really small shadows (such as strands). It appears that normally, pixel width shadows don't anti-alias properly, and that increasing :guilabel:`Buffer Size` doesn't help much.

    So this option allows you to have a sort of extra sample pass, done above the regular one (the one controlled by the :guilabel:`Box`\ /\ :guilabel:`Tent`\ /\ :guilabel:`Gauss`\ , :guilabel:`Samples` and :guilabel:`Soft` settings).

    The default **1** value will disable this option.

    Higher values will produce a smoother anti-aliasing - but be careful: using a :guilabel:`Sample Buffers` of **4** will require four times as much memory and process time, and so on, as Blender will have to compute that number of sample buffers.


"Irregular"
~~~~~~~~~~~

.. figure:: /images/25-Manual-Lighting-Lamps-Spot-Buf-Irregular.jpg
   :width: 313px
   :figwidth: 313px

   Buffer Shadow set to Irregular


:guilabel:`Irregular` shadow method is used to generate sharp/hard shadows that are placed as accurately as raytraced shadows. This method offers very good performance because it can be done as a multi-threaded process.

This method supports transparent shadows. To do so, you will first need to setup the shadow
setting for the object which will receive the transparent shadow. (\ :guilabel:`Material` →
:guilabel:`Shadow` → :guilabel:`Cat Buffer Shadows` and :guilabel:`Buffer Bias`\ )


Deep generation method
~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/25-Manual-Lighting-Lamps-Spot-Buf-Deep.jpg
   :width: 313px
   :figwidth: 313px

   Buffer Shadow set to Deep


:guilabel:`Deep` Shadow buffer supports transparency and better filtering , at the cost of more memory usage and processing time
    :guilabel:`Compress`\ : Deep shadow map compression treshold


Common options
--------------

The following settings are common to all buffered shadow generation method.

:guilabel:`Bias`
    The :guilabel:`Bias` numeric field can have a value between **0.001** and **5.0**\ . :guilabel:`Bias` is used to add a slight offset distance between an object and the shadows cast by it. This is sometimes required because of inaccuracies in the calculation which determines weather an area of an object is in shadow or not.

    Making the :guilabel:`Bias` value smaller results in the distance between the object and its shadow being smaller. If the :guilabel:`Bias` value is too small, an object can get artifacts, which can appear as lines and interference patterns on objects. This problem is usually called "self shadowing", and can usually be fixed by increasing the :guilabel:`Bias` value, which exists for that purpose!

   Other methods for correcting self shadowing include increasing the size of the :guilabel:`Shadow Buffer Size` or using a different buffer shadow calculation method such as :guilabel:`Classic-Halfway` or :guilabel:`Irregular`\ .

    Self shadowing interference tends to affect curved surfaces more than flat ones, meaning that if your scene has a lot of curved surfaces it may be necessary to increase the :guilabel:`Bias` value or :guilabel:`Shadow Buffer Size` value.

    Having overly large :guilabel:`Bias` values not only places shadows further away from their casting objects, but can also cause objects that are very small to not cast any shadow at all. At that point altering :guilabel:`Bias`\ , :guilabel:`Shadow Buffer Size` or :guilabel:`Spot Size` values, among other things, may be required to fix the problem.


.. admonition:: Finer Bias tuning
   :class: note

    You can now refine the :guilabel:`Bias` value independently for each :doc:`Material <materials>`\ , using the :guilabel:`Bias` slider (\ :guilabel:`Material` menu, :guilabel:`Shadow` panel). This value is a factor by which the :guilabel:`Bias` value of each :guilabel:`Spot` buffered shadows lamp is multiplied, each time its light hits an object using this material. The **0.0** and **1.0** values are equivalent - they do not alter the lamp's :guilabel:`Bias` original value.


:guilabel:`Clip Start` & :guilabel:`Clip End`
    When a :guilabel:`Spot` light with buffered shadows is added to a scene, an extra line appears on the :guilabel:`Spot` 3D view representation.

    The start point of the line represents :guilabel:`Clip Start`\ 's value and the end of the line represents :guilabel:`Clip End`\ 's value. :guilabel:`Clip Start` can have a value between **0.1** and **1000.0**\ , and :guilabel:`Clip End`\ , between **1.0** and **5000.0**\ . Both values are represented in Blender Units.

    :guilabel:`Clip Start` indicates the point after which buffered shadows can be present within the :guilabel:`Spot` light area. Any shadow which could be present before this point is ignored and no shadow will be generated.

    :guilabel:`Clip End` indicates the point after which buffered shadows will not be generated within the :guilabel:`Spot` light area. Any shadow which could be present after this point is ignored and no shadow will be generated.

    The area between :guilabel:`Clip Start` and :guilabel:`Clip End` will be capable of having buffered shadows generated.

    Altering the :guilabel:`Clip Start` and :guilabel:`Clip End` values helps in controlling where shadows can be generated. Altering the range between :guilabel:`Clip Start` and :guilabel:`Clip End` can help speed up rendering, save memory and make the resultant shadows more accurate.

    When using a :guilabel:`Spot` lamp with buffered shadows, to maintain or increase quality of generated shadows, it is helpful to adjust the :guilabel:`Clip Start` and :guilabel:`Clip End` such that their values closely bound around the areas which they want to have shadows generated at. Minimizing the range between :guilabel:`Clip Start` and :guilabel:`Clip End`\ , minimizes the area shadows are computed in and therefore helps increase shadow quality in the more restricted area.

:guilabel:`Autoclip Start` & :guilabel:`Autoclip End`
    As well as manually setting :guilabel:`Clip Start` and :guilabel:`Clip End` fields to control when buffered shadows start and end, it is also possible to have Blender pick the best value independently for each :guilabel:`Clip Start` and :guilabel:`Clip End` field.

    Blender does this by looking at where the visible vertices are when viewed from the :guilabel:`Spot` lamp position.


Hints
-----

Any object in Blender can act as a camera in the 3D view. Hence you can select the
:guilabel:`Spot` light and switch to a view from its perspective by pressing
:kbd:`ctrl-pad0`\ .


