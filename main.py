__author__ = "Caspar Fang"
__version__ = "1.0"


import platform
import time
import os
import sys

from log import pass_log, warning_log, error_log
from emulator import launch_emulator, launch_genymotion, close_avd, close_genymotion

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
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', action='store', dest='test_file', help='Set the file of test cases.')
    parser.add_argument('-avd', action='store', dest='emulator_name', help='Set the AVD emulator name.')
    parser.add_argument('-ios', action='store', dest='simulator_name', help='Set the iOS simulator name.')
    parser.add_argument('-genymotion', action='store', dest='genymotion_name', help='Set the genymotion enulator name.')
    parser.add_argument('--version', action='version', version='1.0.0')
    args = parser.parse_args()
    if len(sys.argv)==1:
        os.system("python {0} -h".format(__file__))
        sys.exit(0)

    if args.emulator_name:
        pass_log("Start to launch AVD emulator.")
        launch_emulator(args.emulator_name)
        close_avd()
        pass_log("Close emulator.")

    if args.genymotion_name:
        pass_log("Start to launch AVD emulator.")
        launch_genymotion(args.genymotion_name)
        close_genymotion(args.genymotion_name)
        pass_log("Close emulator.")


if __name__ == '__main__':
    main()
