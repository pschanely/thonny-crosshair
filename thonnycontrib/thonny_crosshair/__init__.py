"""Automatically test Python code using CrossHair in Thonny."""
import enum
import subprocess
import tkinter.messagebox

import thonny
import thonny.workbench

name = "thonny-crosshair"  # pylint: disable=invalid-name

# From: https://github.com/Franccisco/thonny-black-code-format/blob/master/thonnycontrib/thonny_black_format/__init__.py
# Temporary fix: this function comes from thonny.running, but importing that
# module may conflict with outdated Thonny installations from some Linux
# repositories.
_console_allocated = False  # pylint: disable=invalid-name


def _enabled(workbench: thonny.workbench.Workbench) -> bool:
    """Check whether the commands should be enabled."""
    editor = workbench.get_editor_notebook().get_current_editor()

    if editor is None:
        return False

    # Allow the user to run the command even if the file name has not been specified.
    # This will cause an error to be shown to the user, but also inform her that
    # the file needs to be saved.
    # Otherwise, the user is in the dark why the file can not be checked.
    return True


class _Command(enum.Enum):
    CHECK = "check"
    CHECK_AT = "check_at"
    WATCH = "watch"


def _execute(workbench: thonny.workbench.Workbench, command: _Command) -> None:
    """
    Execute the CrossHair command.

    Depending on the ``command``, different checks are performed (*e.g.*,
    whole file, single function, watch & check *etc.*).
    """
    editor = workbench.get_editor_notebook().get_current_editor()

    if editor is None:
        tkinter.messagebox.showerror(
            title="No active editor",
            message="No file is currently edited. "
            "Hence CrossHair check can not be performed.",
        )
        return

    filename = editor.get_filename()
    if filename is None:
        tkinter.messagebox.showerror(
            title="No file name",
            message="The current file has not been saved and does not have a name so "
            "it can not be checked with CrossHair. "
            "Please save the file first.",
        )
        return

    editor.save_file()

    if command == _Command.CHECK:
        cmd = ["!", "python", "-m", "crosshair", "check", filename]
    elif command == _Command.CHECK_AT:
        selection = editor.get_code_view().get_selected_range()
        cmd = [
            "!",
            "python",
            "-m",
            "crosshair",
            "check",
            f"{filename}:{selection.lineno}",
        ]
    elif command == _Command.WATCH:
        cmd = ["!", "python", "-m", "crosshair", "watch", filename]
    else:
        raise NotImplementedError(f"Unhandled command: {command}")

    cmd_line = subprocess.list2cmdline(cmd)

    thonny.get_shell().text.submit_command(cmd_line=cmd_line + "\n", tags=("magic",))

    return


def _load_plugin(workbench: thonny.workbench.Workbench) -> None:
    """Add the plug-in commands to the workbench."""
    workbench.add_command(
        command_id="crosshair.check",
        menu_name="tools",
        command_label="Check the current file with CrossHair",
        handler=lambda: _execute(workbench=workbench, command=_Command.CHECK),
        tester=lambda: _enabled(workbench=workbench),
    )

    workbench.add_command(
        command_id="crosshair.check_at",
        menu_name="tools",
        command_label="Check the function under the caret with CrossHair",
        handler=lambda: _execute(workbench=workbench, command=_Command.CHECK_AT),
        tester=lambda: _enabled(workbench=workbench),
    )

    workbench.add_command(
        command_id="crosshair.watch",
        menu_name="tools",
        command_label="Check the current file with CrossHair continuously",
        handler=lambda: _execute(workbench=workbench, command=_Command.WATCH),
        tester=lambda: _enabled(workbench=workbench),
    )


if thonny.get_workbench() is not None:
    _load_plugin(workbench=thonny.get_workbench())
