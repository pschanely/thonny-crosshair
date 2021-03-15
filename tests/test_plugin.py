"""Test the plugin functions both public and private."""
import os
import unittest
import unittest.mock

import thonnycontrib.thonny_crosshair


class TestEnabled(unittest.TestCase):
    def test_enabled_in_editor(self) -> None:
        editor = unittest.mock.Mock()
        # Return just something which is non-None
        editor.get_current_editor.return_value = unittest.mock.Mock()

        workbench = unittest.mock.Mock()
        workbench.get_editor_notebook.return_value = editor

        self.assertTrue(
            thonnycontrib.thonny_crosshair._enabled(workbench=workbench))

    def test_disabled_without_editor(self) -> None:
        workbench = unittest.mock.Mock()
        workbench.get_editor_notebook.return_value.get_current_editor.return_value = \
            None

        self.assertFalse(
            thonnycontrib.thonny_crosshair._enabled(workbench=workbench))


class TestCheck(unittest.TestCase):
    def test_that_error_is_shown_without_editor(self) -> None:
        workbench = unittest.mock.Mock()
        workbench.get_editor_notebook.return_value.get_current_editor.return_value = None

        with unittest.mock.patch("tkinter.messagebox.showerror") as showerror:
            thonnycontrib.thonny_crosshair._execute(
                workbench=workbench,
                command=thonnycontrib.thonny_crosshair._Command.CHECK
            )

            showerror.assert_called_with(
                title="No active editor",
                message=unittest.mock.ANY
            )

    def test_that_error_is_shown_without_filename(self) -> None:
        editor = unittest.mock.Mock()
        editor.get_filename.return_value = None

        workbench = unittest.mock.Mock()
        workbench.get_editor_notebook.return_value.get_current_editor.return_value = \
            editor

        with unittest.mock.patch("tkinter.messagebox.showerror") as showerror:
            thonnycontrib.thonny_crosshair._execute(
                workbench=workbench,
                command=thonnycontrib.thonny_crosshair._Command.CHECK
            )

            showerror.assert_called_with(
                title="No file name",
                message=unittest.mock.ANY
            )

    def test_the_check_command(self) -> None:
        editor = unittest.mock.Mock()
        editor.get_filename.return_value = "some file.py"

        workbench = unittest.mock.Mock()
        workbench.get_editor_notebook.return_value.get_current_editor.return_value = \
            editor

        with unittest.mock.patch("thonny.get_shell") as get_shell:
            shell = unittest.mock.Mock()
            get_shell.return_value = shell

            thonnycontrib.thonny_crosshair._execute(
                workbench=workbench,
                command=thonnycontrib.thonny_crosshair._Command.CHECK
            )

            editor.save_file.assert_called_once()

            shell.text.submit_command.assert_called_with(
                cmd_line='! python -m crosshair check "some file.py"\n',
                tags=unittest.mock.ANY
            )

    def test_the_check_at_command(self) -> None:
        editor = unittest.mock.Mock()
        editor.get_filename.return_value = "some file.py"
        editor.get_code_view.return_value.get_selected_range.return_value.lineno = 1984

        workbench = unittest.mock.Mock()
        workbench.get_editor_notebook.return_value.get_current_editor.return_value = \
            editor

        with unittest.mock.patch("thonny.get_shell") as get_shell:
            shell = unittest.mock.Mock()
            get_shell.return_value = shell

            thonnycontrib.thonny_crosshair._execute(
                workbench=workbench,
                command=thonnycontrib.thonny_crosshair._Command.CHECK_AT
            )

            editor.save_file.assert_called_once()

            shell.text.submit_command.assert_called_with(
                cmd_line='! python -m crosshair check "some file.py:1984"\n',
                tags=unittest.mock.ANY
            )

    def test_the_watch_command(self) -> None:
        editor = unittest.mock.Mock()
        editor.get_filename.return_value = "some file.py"

        workbench = unittest.mock.Mock()
        workbench.get_editor_notebook.return_value.get_current_editor.return_value = \
            editor

        with unittest.mock.patch("thonny.get_shell") as get_shell:
            shell = unittest.mock.Mock()
            get_shell.return_value = shell

            thonnycontrib.thonny_crosshair._execute(
                workbench=workbench,
                command=thonnycontrib.thonny_crosshair._Command.WATCH
            )

            editor.save_file.assert_called_once()

            shell.text.submit_command.assert_called_with(
                cmd_line='! python -m crosshair watch "some file.py"\n',
                tags=unittest.mock.ANY
            )


if __name__ == "__main__":
    unittest.main()
