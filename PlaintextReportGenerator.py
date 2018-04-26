import DataReport

class PlaintextReportGenerator(DataReport.AbstractReportGenerator):
	def __init__(self):
		self._output_builder = DataReport.LBStringOutputBuilder()

	def generate(self, report):
		self.add_title(report.title)
		self.write_messages(report.messages())
		self.write_sections(report.sections())

		return self.finalize()

	def write(self, line):
		self._output_builder.add(line)
	
	def finalize(self):
		return self._output_builder.done()

	def write_messages(self, messages):
		for m in messages:
			self.add_line(m)

	def write_sections(self, sections):
		for s in sections:
			self.write_section(s)

	def write_section(self, section):
		self.add_subtitle(section.title)
		self.write_subsections(section.subsections())

	def write_subsections(self, subsections):
		for ss in subsections:
			self.write_subsection(ss)

	def write_subsection(self, subsection):
		self.add_header(subsection.title)
		messages = subsection.messages()

		for m in messages:
			self.add_subline(m)

	def add_line(self, line):
		self.write(line)
	
	def add_title(self, title):
		self.add_line("==================================")
		self.add_line(title)
		self.add_line("==================================")
		self.add_line(" ")
	
	def add_subtitle(self, subtitle):
		self.add_line(" ")
		self.add_line("(%s)" % subtitle)
		self.add_line("----------------------------------")
	
	def add_header(self, header):
		self.add_line("%s" % header)
	
	def add_subline(self, subline):
		self.add_line("\t%s" % subline)
	
	def add_namevalue_line(self, name, value):
		self.add_line("%(name)s: %(value)s" % {"name": name, "value": value})

def create():
	return PlaintextReportGenerator()