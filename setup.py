from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [], include_files = ["logo.png", "logo-text.png", "splash.png"])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

buildOptions = {
	"include_msvcr": True
}


executables = [
    Executable('main.py', base=base, targetName = 'Caves and Cheese.exe')
]

setup(name='Caves and Cheese',
      version = '0.1',
      description = 'DnD-derived tabletop game stat-keeper',
      options = dict(build_exe = buildOptions),
      executables = executables)
