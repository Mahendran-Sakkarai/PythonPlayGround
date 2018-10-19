[Source][4]

**Steps to convert .py to .exe in Python 3.6**

 1. Install [Python 3.6][1].
 2. Install cx_Freeze, (open your command prompt and type `pip install cx_Freeze`.
 4. Install idna, (open your command prompt and type `pip install idna`.
 5. Write a `.py` program named `myfirstprog.py`.
 6. Create a new python file named `setup.py` on the current directory of your script.
 7. In the `setup.py`, code below and save it.
 8. With shift pressed right click on the same directory, so you are able to open a command prompt window.
 9. In the prompt, type `python setup.py build`
 10. If your script is error free, then there will be no problem on creating application. 
 11. Check the newly created folder `build`. It has another folder in it. Within that folder you can find your application. Run it. Make yourself happy.

See the original script in my [blog][3].

**setup.py:**

<!-- language: lang-py -->

    from cx_Freeze import setup, Executable
    
    base = None    
    
    executables = [Executable("myfirstprog.py", base=base)]
    
    packages = ["idna"]
    options = {
        'build_exe': {    
            'packages':packages,
        },    
    }
    
    setup(
        name = "<any name>",
        options = options,
        version = "<any number>",
        description = '<any description>',
        executables = executables
    )

EDIT:
 
- be sure that instead of `myfirstprog.py` you should put your `.py`extension file name as created in **step 4**;
- you should include each `import`ed package in your `.py` into `packages` list (ex: `packages = ["idna", "os","sys"]`)
- `any name, any number, any description` in `setup.py` file should not remain the same, you should change it accordingly (ex:`name = "<first_ever>", version = "0.11", description = ''` )
- the `import`ed packages must be installed before you start **step 8**.
 
  [1]: https://www.python.org/downloads/ "Python"
  [2]: https://drive.google.com/file/d/0B3e4ErQeXruDSmFYV2poSGhJY1k/view
  [3]: https://regilanj.wordpress.com/2017/06/07/py-to-exe-in-python-3-6-1/
  [4]: https://stackoverflow.com/a/44433442/3049065