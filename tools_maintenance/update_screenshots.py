#!/usr/bin/env python3
"""
******************
Update Screenshots
******************

This utility is intended to update screenshots, currently it covers:

- Preferences (preferences_section_*.png).

Once this command has finished, review:

   manual_images_preview.html

If the images are acceptable, run:

   mv manual_images_preview/* manual/images/


Example Usage
=============

   env BLENDER_BIN=/src/blender/blender.bin ./tools_maintenance/update_screenshots.py
"""


import sys
import os
if "bpy" not in sys.modules:
    import subprocess
    import tempfile

    blender = os.environ.get("BLENDER_BIN", "blender")

    command = [
        blender,
        "--factory-startup",
        "-noaudio",
        # Note: opening preferences requires window focus.
        # ideally we could work around this.
        # "--no-window-focus",
        "--no-native-pixels",
        # For preferences this wont matter, for other screen-shots it may.
        # Size is odd, this is based on the screenshot in the manual.
        "--window-geometry", "0", "0", "1442", "767",
        "--enable-event-simulate",
        "--python", __file__,
    ]

    env = os.environ.copy()

    # Needed to avoid reading "recent-files.txt" & "bookmarks.txt"
    # as well as helpfully auto-saving the preferences.
    with tempfile.TemporaryDirectory() as temp_home:
        env["HOME"] = temp_home

        subprocess.run(
            command,
            env=env,
        )
    sys.exit(0)

# -----------
# Setup Paths

ROOT_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))

IMAGE_DIR_FINAL = os.path.join(ROOT_DIR, "manual", "images")
IMAGE_DIR_PREVIEW = os.path.join(ROOT_DIR, "manual_images_preview")

if not os.path.exists(IMAGE_DIR_PREVIEW):
    os.mkdir(IMAGE_DIR_PREVIEW)


# -------------
# Other Globals

# Workaround for previews not being generated instantly.
# Wait for this many ticks before taking a screenshot.
SCREENSHOT_WAIT_TICKS = 4

# ----------------------------------------------------------------------
# Blender Defaults

def setup_default_preferences(preferences):
    """ Set preferences useful for automation.
    """
    preferences.view.show_splash = False
    preferences.view.smooth_view = 0
    # preferences.view.use_quit_dialog = False
    preferences.filepaths.use_auto_save_temporary_files = False

    bpy.app.use_userpref_skip_save_on_exit = False



import bpy


# ----------------------------------------------------------------------
# Blender Timer Wrapper

def run_iter_from_timer(event_iter):
    i = iter(event_iter)

    def event_step():
        ret = next(i, Ellipsis)
        if ret is Ellipsis:
            return None
        return 0.0

    bpy.app.timers.register(event_step, first_interval=0.0)


# ----------------------------------------------------------------------
# Blender Helpers

def window_tap_key(*, window, type, unicode=None):
    kw = {}
    if unicode is not None:
        kw["unicode"] = unicode
    yield
    window.event_simulate(type=type, value='PRESS', **kw)
    yield
    window.event_simulate(type=type, value='RELEASE')
    yield


def window_type_keys(*, window, text):
    yield
    for c in text:
        if c == ' ':
            c_upper = 'SPACE'
        else:
            c_upper = c.upper()
        yield
        yield from window_tap_key(window=window, type=c_upper, unicode=c)
        yield
    yield


def window_run_operator_from_search(*, window, operator_name):
    yield
    yield from window_tap_key(window=window, type='F3')
    yield
    yield from window_type_keys(window=window, text=operator_name)
    yield from window_tap_key(window=window, type='RET')
    yield


def window_screenshot_to_filepath(*, window, filepath):
    for _ in range(SCREENSHOT_WAIT_TICKS):
        yield

    bpy.ops.screen.screenshot(
        {"window": window},
        filepath=filepath,
    )
    yield


# ----------------------------------------------------------------------
# Screenshot Helpers

def crop(filepath, size_dst):
    import imbuf

    ibuf = imbuf.load(filepath)
    size_src = ibuf.size
    min = (
        (size_src[0] // 2) - (size_dst[0] // 2) - 1,
        (size_src[1] // 2) - (size_dst[1] // 2) - 1,
    )
    max = (
        min[0] + size_dst[0],
        min[1] + size_dst[1],
    )
    ibuf.crop(min=min, max=max)
    imbuf.write(ibuf, filepath)


# ----------------------------------------------------------------------
# Screenshot Startup

def screenshot_startup(window):
    from bpy import context

    filepath = os.path.join(
        IMAGE_DIR_PREVIEW,
        "interface_window-system_introduction_default-startup.png",
    )

    yield from window_screenshot_to_filepath(
        window=window,
        filepath=filepath,
    )


# ----------------------------------------------------------------------
# Screenshot Splash

def screenshot_splash_screen(window):
    from bpy import context

    # Needed otherwise userpref.blend is an empty file.
    filepath_userpref = os.path.join(
        os.environ["HOME"],
        ".config",
        "blender",
        "{:d}.{:d}".format(*bpy.app.version[:2]),
        "config",
        "userpref.blend",
    )

    os.makedirs(os.path.dirname(filepath_userpref), exist_ok=True)
    with open(filepath_userpref, 'wb') as fh:
        pass

    filepath = os.path.join(
        IMAGE_DIR_PREVIEW,
        "interface_splash_current.png"
    )

    yield from window_run_operator_from_search(
        window=window,
        operator_name="splash screen",
    )

    yield from window_screenshot_to_filepath(
        window=window,
        filepath=filepath,
    )

    os.unlink(filepath_userpref)

    yield from window_tap_key(window=window, type='ESC')

    crop(filepath, [520, 487])


# ----------------------------------------------------------------------
# Screenshot Preferences

def screenshot_preferences(window):
    from bpy import context

    prefs = context.preferences

    # We can't open preferences from a timer, use the shortcut.
    # bpy.ops.screen.userpref_show({"window": window, "screen": window.screen}, 'INVOKE_DEFAULT')
    yield from window_tap_key(window=window, type='F4')
    yield from window_tap_key(window=window, type='P')

    prefs_window = next(iter([w for w in context.window_manager.windows if w.screen.is_temporary]))
    area = prefs_window.screen.areas[0]

    prefs_sections = tuple(
        e.identifier
        for e in prefs.rna_type.properties["active_section"].enum_items
    )

    for section in prefs_sections:
        filepath = os.path.join(
            IMAGE_DIR_PREVIEW,
            "editors_preferences_section_" + section.lower().replace("_", "-") + ".png",
        )
        if section == 'EXPERIMENTAL':
          prefs.view.show_developer_ui = True

        setattr(prefs, "active_section", section)

        yield from window_screenshot_to_filepath(window=prefs_window, filepath=filepath)

        if section == 'EXPERIMENTAL':
          prefs.view.show_developer_ui = False

    bpy.ops.wm.window_close({"window": prefs_window})

    # import IPython
    # IPython.embed()


# ----------------------------------------------------------------------
# Generate HTML
#
# Run this after all other operations.

def generate_preview_html():
    with open(os.path.join(ROOT_DIR, "manual_images_preview.html"), 'w', encoding='utf-8') as fh:
        fw = fh.write
        fw('<!DOCTYPE html>\n')
        fw('<html>\n')
        fw('<body>\n')

        fw('<table style="table-layout: fixed;width: 100%;" border="1">\n')
        fw('  <tr>\n')
        fw('    <td><h1>Old Images</h1></td>\n')
        fw('    <td><h1>New Images</h1></td>\n')
        fw('  </tr>\n')

        for filename in os.listdir(IMAGE_DIR_PREVIEW):

            file_old = os.path.relpath(os.path.join(IMAGE_DIR_FINAL, filename), ROOT_DIR)
            file_new = os.path.relpath(os.path.join(IMAGE_DIR_PREVIEW, filename), ROOT_DIR)

            fw('  <tr>\n')
            fw('    <td><img src="{:s}" style="width: 100%"></td>\n'.format(file_old))
            fw('    <td><img src="{:s}" style="width: 100%"></td>\n'.format(file_new))
            fw('  </tr>\n')

        fw('</table>\n')

        fw('</body>\n')
        fw('</html>\n')


def screenshot_all(window):
    from bpy import context

    yield
    yield from screenshot_startup(window)
    yield from screenshot_splash_screen(window)
    yield from screenshot_preferences(window)

    bpy.app.use_event_simulate = False

    # Finally
    generate_preview_html()

    yield
    print(__doc__)
    sys.exit(0)


def main():
    from bpy import context

    setup_default_preferences(context.preferences)

    run_iter_from_timer(screenshot_all(context.window))


if __name__ == "__main__":
    main()
