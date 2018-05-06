from abc import ABC, abstractmethod

class AbstractReportGenerator(ABC):
	@abstractmethod
	def generate(self, report):
		pass

	@abstractmethod
	def write(self, obj):
		pass

	@abstractmethod
	def finalize(self):
		pass
