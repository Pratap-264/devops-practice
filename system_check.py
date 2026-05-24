import os

# 1
os.makedirs("backup_logs", exist_ok=True)
print("Step 1: Created the backup_logs folder successfully!")

# 2
with open("backup_logs/report.txt", "w") as file:
    file.write("DevOps Status Report: All systems running fine on Ubuntu!")

print("Step 2: Generated report.txt inside the folder!")
