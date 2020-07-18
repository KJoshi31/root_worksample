import sys
from input_validator import argument_validator
from report_engine import ReportEngine


try:
    file_name = sys.argv[1]
    fp = open(file_name)
    contents = fp.read().strip()
except:
    print("please pass in valid file")

command_array = contents.split('\n')

valid = argument_validator(command_array)

if not valid:
    print("input arguments invalid")
else:
    re = ReportEngine()
    re.object_loader(command_array)
    report_data = re.generate_report()
    print(report_data)