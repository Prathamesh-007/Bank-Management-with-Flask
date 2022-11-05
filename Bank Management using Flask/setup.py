from cx_Freeze import setup, Executable

# Include the name of all folder or files in your project folder that are nessesary for the project excluding your main flask file.
# If there are multiple files, you can add them into a folder and then specify the folder name.

includefiles = [ 'templates', 'SQL_Control_Functions.py']
includes = [ 'jinja2' , 'jinja2.ext'] 
excludes = ['Tkinter']

setup(
 name='Python Bank App',
 version = '0.1',
 description = 'App using Python and Flask',
 options = {'build_exe':   {'excludes':excludes,'include_files':includefiles, 'includes':includes}},
 executables = [Executable('app.py')]
)