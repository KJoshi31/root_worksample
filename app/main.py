import sys
from input_validator import argument_validator
from report_engine import ReportEngine

"""
    main.py is the entrypoint for the project.
    outputs data after consumed by the report engine. 
"""

try:
    file_name = sys.argv[1]
    fp = open(file_name)
    contents = fp.read().strip()
except:
    raise Exception('unable to open file')

valid = argument_validator(contents)

if not valid:
    print("input argument(s) invalid")
else:
    command_array = contents.split('\n')
    re = ReportEngine()
    re.object_loader(command_array)
    report_data = re.generate_report()
    print(report_data)
