from cx_Freeze import setup, Executable

base = None    

executables = [Executable("myecho.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "myecho",
    options = options,
    version = "1.0",
    description = 'Just an echo',
    executables = executables
)