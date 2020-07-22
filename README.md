# Root Worksample

This project is a work-sample written in Python for candidate assessement by Root Insurance Co.
</br>

#### Table of Contents  
1. [Setup](#setup) 
    1. [Software Needed](#software-needed)
    2. [Installation Steps](#Installation-Steps)
2. [Usage](#Usage)  
    1. [Program Execution](#program-execution)
    2. [Test Execution](#test-execution)
3. [Expected Output](#expected-output)
4. [Approach](#approach)
    1. [Files](#Files)

# Setup

## Software Needed: 
- [Python3](https://www.python.org/downloads/): language used 
- [pip (linux)](https://www.tecmint.com/install-pip-in-linux/)
or [pip (windows)](https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip) or [pip (macos)](https://www.poftut.com/how-to-install-pip-on-macos/): python package manager
- [Virtualenv pip package](https://virtualenv.pypa.io/en/latest/): pip package used to create virtual environments for python projects 

## Installation Steps:
The following steps assume that the user has installed Python3 in their respective operating system, as well as pip.

Usage of virtualenv pip package will required to easily set up the virtual environment for this project
```bash
pip install virtualenv
```

After install the virtualenv package globally, create the virtual environment with virtualenv. We will name the virtual environment "env". This may folder may be created anywhere.
```bash
virtualenv env
```

Activate the python virtual environment, "env", we just created. This is for isolating the python packages being installed.
```bash
source env/bin/activate
```

Afterwards, your command line will look similar to the following:
```bash
(env) ...../root_worksample$
```

To verify the virtual environment is activated, enter the following command:
```bash
which python
```
Please verify you receive output as the following:
```bash
...../env/bin/python
```
<a id="req-install"></a>
Afterwards, please use the package manager, pip, to install the packages to run this project once the virtual environment has been activated.

```bash
pip install -r requirements.txt
```

To exit the virtual environment, please type the following command anywhere in the command line
```bash
deactivate
```

# Usage

### Program Execution
Assumption is made that the user passes the file from the command line. The <span>main.py</span> in the app folder is the entry point of the application.
```bash
python3 app/main.py input.txt
```

### Test Execution
In order to run tests for the application, the user is assumed to have the packages from the requirements installed - [command](#req-install). <br>
[Pytest](https://docs.pytest.org/en/stable/) is used for testing.

Please navigate inside the app directory.
```bash
cd app/
```
Tests can be executed with the following command, which is just the invocation of pytest (pytest will discover the tests automatically):
```bash
pytest
```
## Expected Output
This is the expected output after setting up and running the work-sample program:
```
Lauren: 42 miles @ 34 mph
Dan:    39 miles @ 47 mph
Kumi:   0 miles
```

# Approach
The approach or methodology towards this problem was to break down the key pieces/components into modular and reusable pieces of code that could be extended upon if need be. 

## Files
[main.py](https://github.com/KJoshi31/root_worksample/blob/master/app/main.py) is the entrypoint of the program which uses other modules of the application to successfully output the reporting data to the end-user. 

[consts.py](https://github.com/KJoshi31/root_worksample/blob/master/app/consts.py) contains constants used in the application, specifically Driver and Trip representations for determining the command from the input file.

[input_validator.py](https://github.com/KJoshi31/root_worksample/blob/master/app/input_validator.py) takes the contents of the file read by the main file to validate whether the arguments are formatted correctly to be used by the report_engine.py file.

[models.py](https://github.com/KJoshi31/root_worksample/blob/master/app/models.py) houses the classes, Drive and Trip. These classes are reprentations of the drivers and trips that are incoming from the input file. 

[report_engine.py](https://github.com/KJoshi31/root_worksample/blob/master/app/report_engine.py) houses the ReportEngine class which digests the data from the input file by parsing the commands and creating Driver and Trip objects. Afterwards, ReportEngine creates a structure to be used for additional sorting operations, and then is able to output a string representation of the report. 

