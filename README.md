# python cookiecutter for a new python project

I developed this project structure so that I am not always doing the same thing ;-)

I tried to use pyprojectbuilder, but after some time I decided to keep it simple and use this approach when I need to create a new python project.
This project its a skeleton of python projects.

# Features

- provides a "standard" python project structure
- provides a setup.py that can be used like "python setup.py sdist bdist_wheel" to create local dists
- provides a folder named data including a png file
- provides two entry points that , after installing the wheel package, installs two exe in windows -> only tried in windows
- provides a clean.bat file that erases the pycache, dist, build and project_name.egg-info folders -> only tried in windows

# Read this first

First, see what Cookiecutter is:
https://cookiecutter.readthedocs.io/en/latest/readme.html


# How to use this project

cookiecutter https://

or download this cookiecutter projet to your hard drive and

cookiecutter path_to_your_cookiecutter

Rename the keywords and start coding.

# After eating the cookiecutter :-)

You get this:
- an app that reads a user config file from %appdata%\{{cookiecutter.project_name}}\config.yaml (overides system config)
- an app that reads a system config file from c:\python3.x\site-packages\{{cookiecutter.project_name}}\config.yaml
- and app that creates two exe after installation of wheel package:
    * {{cookiecutter.project_name}}-cmd1.exe that executes function main of main.py
    * {{cookiecutter.project_name}}-cmd2.exe that executes function main of dothings.oy

Dependencies: PyYAML

## Creating a source package (creates a project_name.tar.gz in dist folder)

python setup.py sdist

## Creating a wheel package (creates a project_name.whl in dist folder)

python setup.py bdist_wheel

## Creating a source package and wheel package

python setup.py sdist bdist_wheel

#### Install and test local source distribution

> python -m venv venv

> source venv/bin/activate

> pip install app.tar.gz
or
> pip install app.whl

The packages will be in installed in venv/lib/python3.x/site-packages/app-package (so will be the code)
The data folder will be in installed in venv/lib/python3.x/site-packages/app-package/data

Uninstall: just delete the venv and your test directory
