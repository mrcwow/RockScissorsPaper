import sys
import cx_Freeze
from cx_Freeze import setup, Executable
build_exe_options = {"packages": ["os", "tkinter", "random"]}



base = "Win32GUI"


setup(

    name = "RSP",
    version = "1.0",
    description = "byDK",
    executables = [Executable("RPS.py", base=base, icon='RPSnew.ico', shortcutName='RSP', shortcutDir='DesktopFolder')]
)




