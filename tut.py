import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 50

if not check_disk_usage("/") or not check_cpu_usage():
    print("System is in danger!")
else:
    print("Everything is fine.")
