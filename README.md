**Overview**

This is a minimal library for producing reports. 

Build up a Report model and then hand it off to a ReportGenerator to create the report. 

**Prerequisites**

 - python3
 - pip
 - virtualenv
 
 **Building**
 
 ```bash
 make
 ```
 
**Usage**
 
Import the required classes:

```python
from datareport.generator import PlaintextReportGenerator
from datareport.models import Report, ReportSection, ReportSubSection
from datareport.builder import NewlineStringBuilder
```
 
Build up the report model:

```python
def create_report_model():
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
  
  return report
```

Create a new builder and hand it off to a new generator. NewlineStringBuilder is a good option for plaintext reports:
```python
builder = NewlineStringBuilder()
generator = PlaintextReportGenerator(builder)
````

Now generate the report:

```python
report = create_report_model()
output = generator.generate(report)
print(output)
```
 
 **Notes**
 
 Currently, the only type of report generator is plaintext.  
