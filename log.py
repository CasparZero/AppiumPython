import time


def pass_log(info):
	local_time = time.strftime("%Y:%m:%d %H:%M:%S",time.localtime())
	print("\033[0;32m["+local_time+"] "+info+"\033[0m \n")


def warning_log(info):
	local_time = time.strftime("%Y:%m:%d %H:%M:%S",time.localtime())
	print("\033[0;33m["+local_time+"] "+info+"\033[0m \n")


def error_log(info):
	local_time = time.strftime("%Y:%m:%d %H:%M:%S",time.localtime())
	print("\033[0;31m["+local_time+"] "+info+"\033[0m \n")
