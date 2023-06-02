import shutil
import psutil
def check_free_disk(disk):
    du = shutil.disk_usage(disk)
    free = (du.free/du.total)*100
    return free>20
def check_cpu_percent(): 
    usage = psutil.cpu_percent(1)
    return usage
if not check_free_disk("/") or not check_cpu_percent():
    print("ERROR!")
else: 
    print("EVERYTHING IS OK!")