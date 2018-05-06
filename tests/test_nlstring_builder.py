from context import datareport

def test_builder():
	builder = datareport.builder.NewlineStringBuilder()
	builder.add("hello")
	builder.add("world")

	expected = "hello\nworld"
	assert expected == builder.done()
