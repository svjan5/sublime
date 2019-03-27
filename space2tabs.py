import sublime, sublime_plugin

class ConvertSpacesToTabs(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command('unexpand_tabs', {"set_translate_tabs": False})