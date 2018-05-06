from context import datareport
from datareport.generator import PlaintextReportGenerator
from datareport.models import Report, ReportSection, ReportSubSection
from datareport.builder import NewlineStringBuilder

def mockup_report_model():
	report_title = "Test Report"
	report_message_1 = "report test message"
	section_title = "Test Section"
	subsection_title = "Test SubSection"
	subsection_message_1 = "subsection test message"
	subsection_message_2 = "subsection test message"

	report = Report()
	report.title = report_title
	report.add_message(report_message_1)

	section = ReportSection()
	section.title = section_title

	subsection = ReportSubSection()
	subsection.title = subsection_title
	subsection.add_message(subsection_message_1)
	subsection.add_message(subsection_message_2)

	section.add_subsection(subsection)
	report.add_section(section)

	builder = NewlineStringBuilder()
	builder.add("==================================")
	builder.add(report_title)
	builder.add("==================================")
	builder.add(" ")
	builder.add(report_message_1)
	builder.add(" ")
	builder.add("({})".format(section_title))
	builder.add("----------------------------------")
	builder.add(subsection_title)
	builder.add("\t{}".format(subsection_message_1))
	builder.add("\t{}".format(subsection_message_2))

	return {"report": report, "expected": builder.done()}

def test_generation():
	builder = NewlineStringBuilder()
	generator = PlaintextReportGenerator(builder)

	model = mockup_report_model()
	report = model.get("report")
	expected = model.get("expected")

	actual = generator.generate(report)
	assert actual == expected
