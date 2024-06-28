import os
import psutil

def list_files(dir_path):
    dir_list = os.listdir(dir_path)
    print(f"Filed and Directories in {dir_path} \n")
    print(dir_list)

def list_system_resource_usage():
    print("*** SYSTEM RESOURCE USAGE ***")
    print(f"CPU Percent: {psutil.cpu_percent()}")
    print(f"Virtual Memory - Percentage of Used RAM: {psutil.virtual_memory().percent}")
    print(f"Virtual Memory - Percentage of Available RAM: {(psutil.virtual_memory().available * 100)/psutil.virtual_memory().total}")
