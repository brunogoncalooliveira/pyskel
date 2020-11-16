from setuptools import setup, find_packages

# https://www.digitalocean.com/community/tutorials/how-to-package-and-distribute-python-applications

setup(
    name="{{cookiecutter.project_name}}",
    version="0.1",

    description="This is a template description for a new project.",

    author='Bruno Oliveira',
    author_email='xx.xx@gmail.com',

    url='https://github.com/brunogoncalooliveira/pyskel',

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],

    packages=find_packages(exclude=['test*', 'Test*']),

    package_data={
        '': ['README.md', 'LICENSE'],
        '{{cookiecutter.project_name}}': ['config.yaml'],
      },


    scripts=['{{cookiecutter.project_name}}/main.py'],

    entry_points={
          'console_scripts': [
              '{{cookiecutter.project_name}}-cmd1 = {{cookiecutter.project_name}}.main:main',
              '{{cookiecutter.project_name}}-cmd2 = {{cookiecutter.project_name}}.dothings:main',
          ],
      },

    install_requires=[
        'PyYAML==4.2b1',
        'colorama',
      ],
    python_requires = '>=3.6',
)
