
Installing on Linux
===================


Download
--------


You can obtain the latest stable version of Blender for Linux from the
`Blender download page <http://www.blender.org/download/get-blender/>`__
or from your distribution software repository if it provides a Blender package.


Version
-------


Blender for Linux is currently available in 32-bit and 64-bit versions.
Users with a 32-bit version of Linux must download the 32-bit version of Blender. Users with a
64-bit version of Linux can choose to use either the 32-bit or 64-bit version of Blender,
however you will likely notice an increase in performance when using the 64-bit version of
Blender, especially on systems with large amounts of RAM.

To determine whether you have a 32-bit or 64-bit version of Linux, you can either consult your
distributions' documentation or use the ``uname`` command with the ``-m``
option. ``uname`` will print system information and the ``-m`` option will
print the machine hardware name.


- Open a terminal console


- Enter the command ``uname -m``

If you have a 32-bit system, ``uname -m`` will return a value of ``i686``\ .
A 64-bit system will return a value of ``x86_64``\ .


Distribution releases
---------------------


Most major distributions such as Ubuntu, Debian, Open SUSE, Fedora and many others will
provide a build of Blender in their software repository that can be accessed through that
distributions package manager. If your distribution does not do this,
or has not updated their repository to include the latest Blender release,
you can install it yourself with the instructions below.
Note that depending on your distribution, the version available in the software repository may
be outdated compared to the offical release.


Installation
============


First check if your distribution provides the latest Blender version through its package
manager. If it doesn't, download the appropriate version of Blender for Linux from the
`Blender download page <http://www.blender.org/download/get-blender/>`__
and unpack the archive to a location of your choice.

This will create a directory named ``blender-VERSION-linux-glibcVERSION-ARCH``\ ,
where ``VERSION`` is the Blender release version, ``glibcVERSION`` is the
version of glibc required and ``ARCH`` is your computer architecture
(\ ``i686`` or ``x86_64``\ ).
In this directory you will find the ``blender`` binary.

To run Blender,


- Start your `X.Org server <http://www.x.org/wiki/>`__ (if it is not already running)
- Navigate to the Blender directory using a file manager and double click the Blender executable or,
- Open a terminal console, navigate to the Blender directory and execute the command ``./blender``


Installing into <code>/opt</code> or <code>/usr/local</code>
------------------------------------------------------------


You can also install Blender into ``/opt`` or ``/usr/local`` by moving the
Blender directory into one of those locations. If you want to be able to run Blender from any
directory you will also need to update your PATH variable.
Consult your operating system documentation for the recommended method of setting your PATH.


Configuration
=============


Alt+Mouse Conflict
~~~~~~~~~~~~~~~~~~

Many Linux distributions default to
FIXME(Template Unsupported: Shortcut/Keypress;
{{Shortcut/Keypress|alt}}
)
FIXME(Template Unsupported: Shortcut/Mouse;
{{Shortcut/Mouse|lmb}}
) for moving
windows. Since Blender uses Alt+Click it's normally easier to disable this feature or change
the key to Super (Windows Key)

- Ubuntu 11.04: Settings > Window Manger Tweak > Accessibility > Change Window Key to Super
- Ubuntu 12.04 (Unity/Gnome): Command line (effective at next login): gsettings set org.gnome.desktop.wm.preferences mouse-button-modifier 'none'
- Other versions: todo


Compositing Desktop Environments
================================

Many recent Linux distributions enable compositing when hardware support is available. This is
a feature where the graphics card is used to do window drawing and accelerated desktop effects
(for example: drop shadow and window transparency). Notably - Ubuntu Unity,
Gnome Shell and KDE will use compositing.

While many users find this works flawlessly, some graphics cards have buggy drivers which
cause drawing glitches with Blender but work correctly for regular applications which don't
use OpenGL acceleration. Another downside to using hardware accelerated desktop effects is
that the windows you have open share texture memory with Blender's OpenGL display and GPU
rendering.

If you experience these problems they can be avoided by disabling desktop effects or by
switching to a desktop environment that does not use desktop effects such as:


- Unity2D
- Gnome Fallback
- XFCE
- light weight window managers like openbox, jwm, sawfish, icewm... etc.

For details on this topic, see: [http://en.wikipedia.org/wiki/Compositing_window_manager
Wikipedia - Compositing Window Managers]

