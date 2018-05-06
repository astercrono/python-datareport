class Report(object):
	def __init__(self):
		self._title = ""
		self._messages = []
		self._sections = []

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, title):
		self._title = title

	def add_message(self, message):
		self._messages.append(message)

	def add_messages(self, messages):
		self._messages.extend(messages)

	def messages(self):
		return self._messages

	def add_section(self, section):
		return self._sections.append(section)

	def add_sections(self, sections):
		return self._sections.extend(sections)

	def sections(self):
		return self._sections

class ReportSection(object):
	def __init__(self):
		self._title = ""
		self._subsections = []

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, title):
		self._title = title

	def add_subsection(self, subsection):
		self._subsections.append(subsection)

	def add_subsections(self, subsections):
		self._subsections.extend(subsections)

	def subsections(self):
		return self._subsections

class ReportSubSection(object):
	def __init__(self):
		self._title = ""
		self._messages = []

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, title):
		self._title = title

	def add_message(self, message):
		self._messages.append(message)

	def add_messages(self, messages):
		self._messages.extend(messages)

	def messages(self):
		return self._messages
