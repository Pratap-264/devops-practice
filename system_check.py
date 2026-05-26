#!/bin/bash
import os
import platform
from datetime import datetime

log_folder = "logs"

if not os.path.exists(log_folder):
    os.makedirs(log_folder)

time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

log_file = f"{log_folder}/system_log_{time_stamp}.txt"

with open(log_file, "w") as file:
    file.write("===== SYSTEM CHECK REPORT =====\n")
    file.write(f"Date & Time: {datetime.now()}\n")
    file.write(f"System: {platform.system()}\n")
    file.write(f"Node Name: {platform.node()}\n")
    file.write(f"Release: {platform.release()}\n")
    file.write(f"Version: {platform.version()}\n")
    file.write(f"Machine: {platform.machine()}\n")
    file.write(f"Processor: {platform.processor()}\n")

print(f"Log saved in {log_file}")
