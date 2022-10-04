
*************
GPU Rendering
*************

:abbr:`GPU (Graphics Processing Unit)` rendering makes it possible to use your
graphics card for rendering, instead of the CPU. This can speed up rendering
because modern GPUs are designed to do quite a lot of number crunching.
On the other hand, they also have some limitations in rendering complex scenes, due to more limited memory,
and issues with interactivity when using the same graphics card for display and rendering.

To enable GPU rendering, go into the :menuselection:`Preferences --> System --> Cycles Render Devices`,
and select either *CUDA*, *OptiX*, *HIP*, *oneAPI*, or *Metal*. Next, you must configure each scene to
use GPU rendering in :menuselection:`Properties --> Render --> Device`.


Rendering Technologies
======================

Blender supports different technologies to render on the GPU depending on the particular GPU manufacturer
and operating system.

.. note:: With all GPU rendering technologies, :doc:`/render/shader_nodes/osl` is not supported.


CUDA -- NVIDIA
--------------

:abbr:`CUDA (Compute Unified Device Architecture)` is supported on Windows and Linux and requires a
Nvidia graphics cards with compute capability 3.0 and higher. To make sure your GPU is supported,
see the `list of Nvidia graphics cards <https://developer.nvidia.com/cuda-gpus#compute>`__
with the compute capabilities and supported graphics cards.


.. _render-cycles-gpu-optix:

OptiX -- NVIDIA
---------------

OptiX is supported on Windows and Linux and requires a Nvidia graphics cards with compute capability 5.0 and higher
and a driver version of at least 470. To make sure your GPU is supported,
see the `list of Nvidia graphics cards <https://developer.nvidia.com/cuda-gpus#compute>`__
OptiX works best on RTX graphics cards with hardware ray tracing support (e.g. Turing and above).


HIP -- AMD
----------

:abbr:`HIP (Heterogeneous-compute Interface for Portability)` is supported on Windows and Linux and requires a
AMD graphics card with the Vega, RDNA or newer architecture. Both discrete GPUs and APUs are supported.

Supported GPUs include:

 - Radeon VII
 - Radeon RX Vega Series
 - Radeon RX 5000 Series
 - Radeon RX 6000 Series
 - Radeon Pro WX 9100
 - Radeon Pro W6000 Series

Minimum driver versions:

 - Windows: Radeon Software 21.12.1 or Radeon PRO Software 21.Q4
 - Linux: Radeon Software 22.10 or ROCm 5.1

Please refer to `AMD's website <https://www.amd.com/en/graphics>`__ for more
information about AMD graphics cards and their architectures.

.. note:: The *Clip* extension mode in the :doc:`/render/shader_nodes/textures/image` is not supported.


oneAPI -- Intel
---------------

oneAPI is a computation library that is supported on Windows and Linux and requires a
Intel® Arc™ graphics card with the Xe HPG architecture.

Supported GPUs include:

 - Intel® Arc™ A-Series

Minimum driver versions:

 - Windows: Intel Graphics Driver 30.0.101.3430
 - Linux: OpenCL runtime 22.10.23904

Please refer to `Intel's website <https://www.intel.com/content/www/us/en/products/details/discrete-gpus.html>`__
for more information about Intel graphics cards and their architectures.


Metal -- Apple (macOS)
----------------------

Metal is supported on Apple computers with Apple Silicon or AMD graphics cards. macOS 12.2 is required to use Metal
with Apple Silicon while macOS 12.3 is required to use Metal with AMD graphics cards.

.. note:: :ref:`MNEE caustics <bpy.types.CyclesObjectSettings.is_caustics_caster>` are not supported in Metal.


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
With CUDA, OptiX, HIP and Metal devices, if the GPU memory is full Blender will automatically
try to use system memory. This has a performance impact, but will usually still result in a faster render
than using CPU rendering.


Can multiple GPUs be used for rendering?
----------------------------------------

Yes, go to :menuselection:`Preferences --> System --> Compute Device Panel`, and configure it as you desire.


Would multiple GPUs increase available memory?
----------------------------------------------

Typically, no, each GPU can only access its own memory, however, some GPUs can share their memory.
This is can be enabled with :ref:`Distributed Memory Across Devices <prefs-system-cycles-distributive-memory>`.


What renders faster?
--------------------

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


Error: Out of memory
--------------------

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
