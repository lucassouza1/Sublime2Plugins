import sublime, sublime_plugin

class PhpExtractVariableCommand(sublime_plugin.WindowCommand):

	def run(self):
		view = self.window.active_view()
		for region in view.sel():			
			if not region.empty():
				self.current_region = region
				self.selection = view.substr(region)
				self.window.show_input_panel("Extract variable", "", self.prepareVariable, None, None)
			else:
				sublime.status_message("No selection")

	def prepareVariable(self, string):
		view = self.window.active_view()
		edit = view.begin_edit(); view.end_edit(edit)
		region = self.current_region
		view.replace(edit, region, string)
		selection = self.selection
		extracted = "\t\t%s = %s\n" % (string, selection)
		position = view.line(region).begin()
		view.insert(edit, position, extracted)