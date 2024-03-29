import unreal
import subprocess
from pathlib import Path
import os
import sys 

PYTHON_INTERPRETER_PATH = unreal.get_interpreter_executable_path()
assert Path(PYTHON_INTERPRETER_PATH).exists(), f"Python not found at '{PYTHON_INTERPRETER_PATH}'"
file_path = Path(PYTHON_INTERPRETER_PATH)
parent_dir = file_path.parent
sitepackages = os.path.join(parent_dir, "lib")
sitepackages = os.path.join(sitepackages, "site-packages")
sys.path.append(sitepackages)

print(sitepackages)
def pip_install(packages):
    # dont show window
    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    proc = subprocess.Popen(
        [
            PYTHON_INTERPRETER_PATH, 
            '-m', 'pip', 'install', 
            '--no-warn-script-location', 
            *packages
        ],
        startupinfo = info,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        encoding = "utf-8"
    )

    while proc.poll() is None:
        unreal.log(proc.stdout.readline().strip())
        unreal.log_warning(proc.stderr.readline().strip())

    return proc.poll()

# Put here your required python packages
required = {'Pyside6'}
# installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required

if len(missing) > 0:
    pip_install(missing)
else:
    unreal.log("All python requirements already satisfied")
