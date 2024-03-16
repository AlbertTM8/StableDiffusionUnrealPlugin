import subprocess
import sys
import os
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyside6"])
    print("Successfully installed PySide6.")
except subprocess.CalledProcessError as e:
    print(f"Failed to install PySide6: {e}")