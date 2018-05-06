from .abstract import AbstractOutputBuilder

class NewlineStringBuilder(AbstractOutputBuilder):
	def __init__(self):
		self.lines = []

	def add(self, line):
		self.lines.append(line)

	def done(self):
		return "\n".join(self.lines)
