'''
This is a scrip that will be used in the setup.py as an entry point.
Instantiate all your classes here.
'''
import argparse
import sys
import os
import logging
from pprint import pprint

if sys.argv[0] == 'main.py':
    import project
else:
    from {{cookiecutter.project_name}} import project


def parse_input_args(argv):
    ''' Parses command line arguments '''

    parser = argparse.ArgumentParser(description=
            "Description of the app that will be displayed when the script is executed.")
    parser.add_argument('--test', help="Test the app.", dest="test",
                        action='store_true', required=False)


def execute_script(input_args):
    parsed_args = parse_input_args(input_args)
    pprint(parsed_args)

    classObject = project.Config()
    logging.info('Starting...')
    logging.info('Ending...')

def main():
    # Entry point to the app. Call in test method
    execute_script(sys.argv[1:])


if __name__ == "__main__":
    main()