import sublime
import sublime_plugin


class CopyWithSpacesCommand(sublime_plugin.TextCommand):
    """
    Copy the selected text to the clipboard, replacing all tab characters with
    spaces based on the tab size in the current view.
    """
    def run(self, edit):
        self.view.run_command("copy")

        tab_size = self.view.settings().get("tab_size", 4)      
        text = sublime.get_clipboard().expandtabs(tab_size)
        sublime.set_clipboard(text)