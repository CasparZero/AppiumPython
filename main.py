__author__ = "Caspar Fang"
__version__ = "0.1"


import platform
import time
import os
import sys
from log import pass_log, warning_log, error_log


def check_environment():
    # Get system type
    system_type = platform.system()
    if system_type == "Darwin":
        pass_log("System type: Mac OS")
    elif system_type == "Linux":
        pass_log("System type: Linux OS")
    elif system_type == "Windows":
        pass_log("System type: Windows OS")
    else:
        pass_log("System type: Other OS({0})".format(system_type))
    # Get python version
    python_version = platform.python_version()
    pass_log("Python versin:{0}".format(python_version))
    # Get Appium version
    appium_verion = os.popen("appium -v").read()
    pass_log("Appium Version: {0}".format(appium_verion))


def run_testcases():
	if len(sys.argv) == 1:
		warning_log("No test cases for run.") 
	elif len(sys.argv) == 2:
		pass_log("Running python main.py {0}".format(sys.argv[1]))
		os.system("python {0}".format(sys.argv[1]))
		pass_log("Run end")
		
	else:
		error_log("You need use it as $python main.py test.py")
		

def main():
    check_environment()
    run_testcases()
if __name__ == '__main__':
    main()
