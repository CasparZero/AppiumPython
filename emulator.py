import time
import multiprocessing
import commands
import os

def launch_emulator(avd_name,default_wait=60):
    launch_avd = lambda emulator_name:commands.getstatusoutput("emulator @{0}".format(emulator_name))
    t = multiprocessing.Process(target = launch_avd,args=(avd_name,))
    # t.daemon = True
    t.start()
    time.sleep(default_wait)


def launch_genymotion(genymotion_name,default_wait=60):
    launch_avd = lambda emulator_name:commands.getstatusoutput("player --vm-name {0}".format(emulator_name))
    t = multiprocessing.Process(target = launch_avd,args=(genymotion_name,))
    # t.daemon = True
    t.start()
    time.sleep(default_wait)


def close_genymotion(genymotion_name):
    os.system("gmtool admin stop {}".format(genymotion_name))



def close_avd():
    os.system("adb emu kill")
