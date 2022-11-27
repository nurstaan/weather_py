import sys
from cx_Freeze import setup, Executable


build_exe_options = {"packages": ["os"],
                     "includes": ['tkinter'],
                     "include_files": ['weather_icons', 'app_icon.png']}


base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Weather",
      version="0.0.2",
      description="Weather in cities of the world",
      options={"build_exe": build_exe_options},
      executables=[Executable("main.py", targetName='weather.exe', icon="sunny.ico", base=base)])

