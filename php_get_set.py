import sublime, sublime_plugin

class PhpGetSetCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if region.empty():
				selection = self.view.substr(self.view.word(region))
			else:
				selection = self.view.substr(region)
			
			sublime.status_message("Generate getter and setter for %s" % selection);
			self.view.insert(edit, self.view.size() - 2, self.getterAndSetter(selection))

	def getterAndSetter(self, name):
		command = """\n
	public function get%(capitalize_name)s()
	{
		return $this->%(name)s;
	}

	public function set%(capitalize_name)s($%(name)s)
	{
		return $this->%(name)s = $%(name)s;
	}
		""" % {"name" : name, "capitalize_name" : name.capitalize()}
		return command