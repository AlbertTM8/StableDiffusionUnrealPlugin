import subprocess
import sys
import os
from pathlib import Path
import venv

def create_virtual_environment(path):
    # Ensure the target directory exists
    if not os.path.exists(path):
        os.makedirs(path)
    
    # # Create the virtual environment
    venv.create(path, with_pip=True)  # with_pip=True ensures pip is installed in the venv

# Specify the path where you want the virtual environment to be created
script_dir = Path(__file__).parent.absolute()
parent_dir = script_dir.parent
venv_dir = os.path.join(parent_dir, ".venv")
print(venv_dir)
create_virtual_environment(venv_dir)