1. Install Python and Pip
2. Environmental Variables must be set:
	a. Add the python3X folder to SystemVariables -> Path
		1. Select 'path' under system variables and click Edit
		2. New -> paste directory of python folder 
			example: C:\Users\MillsPsych01s\AppData\Local\Programs\Python\Python37
	b. Add/create PYTHONPATH
		1. Under system variables if there is not a PYTHONPATH click create, if there is click edit
		2. paste the same directory from above
	c. RESTART!! changes will not take effect if you do not
3. These packages are nessecary for running the programs, to install them enter the following command into the terminal 
	a. python -m pip install keyboard
	b. python -m pip install pyglet
	c. python -m pip install pynput