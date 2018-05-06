from abc import ABC, abstractmethod

class AbstractOutputBuilder(ABC):
	@abstractmethod
	def add(self, obj):
		pass

	@abstractmethod
	def done(self):
		pass
