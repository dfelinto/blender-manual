
*************
GPU Rendering
*************

:abbr:`GPU (Graphics Processing Unit)` rendering makes it possible to use your
graphics card for rendering, instead of the CPU. This can speed up rendering
because modern GPUs are designed to do quite a lot of number crunching.
On the other hand, they also have some limitations in rendering complex scenes, due to more limited memory,
and issues with interactivity when using the same graphics card for display and rendering.

To enable GPU rendering, go into the :menuselection:`Preferences --> System --> Cycles Render Devices`,
and select either *CUDA* or *OptiX*. Next, you must configure each scene to use GPU rendering in
:menuselection:`Properties --> Render --> Device`.

.. note::

   GPU rendering is only supported on Windows and Linux; macOS is currently not supported.


Supported Hardware
==================

Blender supports different technologies to render on the GPU depending on the particular GPU manufacture.


Nvidia
------

:abbr:`CUDA (Compute Unified Device Architecture)` and OptiX are supported
for GPU rendering with Nvidia graphics cards.


CUDA
^^^^

CUDA requires graphics cards with compute capability 3.0 and higher.
To make sure your GPU is supported,
see the `list of Nvidia graphics cards <https://developer.nvidia.com/cuda-gpus#compute>`__
with the compute capabilities and supported graphics cards.

.. note:: Open Shading Language is not supported.


.. _render-cycles-gpu-optix:

OptiX
^^^^^

OptiX requires graphics cards with compute capability 5.0 and higher.
To make sure your GPU is supported,
see the `list of Nvidia graphics cards <https://developer.nvidia.com/cuda-gpus#compute>`__
OptiX works best on RTX graphics cards with hardware ray tracing support (e.g. Turing and above).

.. note:: Open Shading Language is not supported.


Frequently Asked Questions
==========================

Why is Blender unresponsive during rendering?
---------------------------------------------

While a graphics card is rendering, it cannot redraw the user interface, which makes Blender unresponsive.
We attempt to avoid this problem by giving back control over to the GPU as often as possible,
but a completely smooth interaction cannot be guaranteed, especially on heavy scenes.
This is a limitation of graphics cards for which no true solution exists,
though we might be able to improve this somewhat in the future.

If possible, it is best to install more than one GPU,
using one for display and the other(s) for rendering.


Why does a scene that renders on the CPU not render on the GPU?
---------------------------------------------------------------

There may be multiple causes,
but the most common one is that there is not enough memory on your graphics card.
Typically, the GPU can only use the amount of memory that is on the GPU
(see `Would multiple GPUs increase available memory?`_ for more information).
This is usually much smaller than the amount of system memory the CPU can access.
With CUDA and OptiX devices, if the GPU memory is full Blender will automatically try to use system memory.
This has a performance impact, but will usually still result in a faster render than using CPU rendering.


Can multiple GPUs be used for rendering?
----------------------------------------

Yes, go to :menuselection:`Preferences --> System --> Compute Device Panel`, and configure it as you desire.


Would multiple GPUs increase available memory?
----------------------------------------------

Typically, no, each GPU can only access its own memory, however, some GPUs can share their memory.
This is can be enabled with :ref:`Distributed Memory Across Devices <prefs-system-cycles-distributive-memory>`.


What renders faster?
----------------------------------------------------------

This varies depending on the hardware used. Different technologies also have different compute times
depending on the scene tested. For the most up to date information on the performance of different devices,
browse the `Blender Open Data <https://opendata.blender.org/>`__ resource.


Error Messages
==============

In case of problems, be sure to install the official graphics drivers from the GPU manufacturers website,
or through the package manager on Linux.


Unsupported GNU version
-----------------------

On Linux, depending on your GCC version you might get this error.
See the `Nvidia CUDA Installation Guide for Linux
<https://docs.nvidia.com/cuda/archive/10.2/cuda-installation-guide-linux/index.html>`__
for a list of supported GCC versions. There are two possible solutions to this error:

Use an alternate compiler
   If you have an older GCC installed that is compatible with the installed CUDA toolkit version,
   then you can use it instead of the default compiler.
   This is done by setting the ``CYCLES_CUDA_EXTRA_CFLAGS`` environment variable when starting Blender.

   Launch Blender from the command line as follows:

   .. code-block:: sh

      CYCLES_CUDA_EXTRA_CFLAGS="-ccbin gcc-x.x" blender

   (Substitute the name or path of the compatible GCC compiler).

Remove compatibility checks
   If the above is unsuccessful, delete the following line in
   ``/usr/local/cuda/include/host_config.h``:

   .. code-block:: c

      #error -- unsupported GNU version! gcc x.x and up are not supported!

   This will allow Cycles to successfully compile the CUDA rendering kernel the first time it
   attempts to use your GPU for rendering. Once the kernel is built successfully, you can
   launch Blender as you normally would and the CUDA kernel will still be used for rendering.


CUDA Error: Kernel compilation failed
-------------------------------------

This error may happen if you have a new Nvidia graphics card that is not yet supported by
the Blender version and CUDA toolkit you have installed.
In this case Blender may try to dynamically build a kernel for your graphics card and fail.

In this case you can:

#. Check if the latest Blender version
   (official or `experimental builds <https://builder.blender.org/download/>`__)
   supports your graphics card.
#. If you build Blender yourself, try to download and install a newer CUDA developer toolkit.

Normally users do not need to install the CUDA toolkit as Blender comes with precompiled kernels.


CUDA Error: Out of memory
-------------------------

This usually means there is not enough memory to store the scene for use by the GPU.

.. note::

   One way to reduce memory usage is by using smaller resolution textures.
   For example, 8k, 4k, 2k, and 1k image textures take up respectively 256MB, 64MB, 16MB and 4MB of memory.


The Nvidia OpenGL driver lost connection with the display driver
----------------------------------------------------------------

If a GPU is used for both display and rendering,
Windows has a limit on the time the GPU can do render computations.
If you have a particularly heavy scene, Cycles can take up too much GPU time.
Reducing Tile Size in the Performance panel may alleviate the issue,
but the only real solution is to use separate graphics cards for display and rendering.

Another solution can be to increase the time-out,
although this will make the user interface less responsive when rendering heavy scenes.
`Learn More Here <https://docs.microsoft.com/en-us/windows-hardware/drivers/display/timeout-detection-and-recovery>`__.


CUDA error: Unknown error in cuCtxSynchronize()
-----------------------------------------------

An unknown error can have many causes, but one possibility is that it is a time-out.
See the above answer for solutions.
