import os
import subprocess

ROOT_FOLDER = os.getcwd()
IGNORE_MD_FILES = ["README.md"]

total_tils = 0

for root, dirs, files in os.walk(ROOT_FOLDER):
    for file in files:
        if file.endswith('.md') and file not in IGNORE_MD_FILES:
            total_tils += 1


print("Total TILs: " + str(total_tils))

til_string = "_" + str(total_tils) + " TILs and counting..._"
subprocess.run("pbcopy", universal_newlines=True, input=til_string)
print("\"" + til_string + "\" copied to clipboard.")
