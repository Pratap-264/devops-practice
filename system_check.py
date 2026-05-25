import os
from datetime import datetime

# 1. Automatically create a new folder named 'backup_logs'
os.makedirs("backup_logs", exist_ok=True)
print("Step 1: Verified backup_logs folder.")

# Get current timestamp
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("backup_logs/report.txt", "a") as file:
    file.write(f"\n[{current_time}] DevOps Status Report: Systems operational.")

print(f"Step 2: Log added at {current_time}!")
