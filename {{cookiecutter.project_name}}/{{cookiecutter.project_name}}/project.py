import logging.config
import os
import yaml
import sys
import logging
import logging.handlers
import colorama

if sys.argv[0] == 'main.py':
    import project
else:
    from {{cookiecutter.project_name}} import project

colorama.init()


def root():
    return os.path.dirname(__file__)


# Logging formatter supporting colored output
class LogFormatter(logging.Formatter):
    COLOR_CODES = {
        logging.CRITICAL: "\033[1;35m",  # bright/bold magenta
        logging.ERROR: "\033[1;31m",  # bright/bold red
        logging.WARNING: "\033[1;33m",  # bright/bold yellow
        logging.INFO: "\033[0;37m",  # white / light gray
        logging.DEBUG: "\033[1;30m"  # bright/bold black / dark gray
    }

    RESET_CODE = "\033[0m"

    def __init__(self, color, *args, **kwargs):
        super(LogFormatter, self).__init__(*args, **kwargs)
        self.color = color

    def format(self, record, *args, **kwargs):
        if (self.color == True and record.levelno in self.COLOR_CODES):
            record.color_on = self.COLOR_CODES[record.levelno]
            record.color_off = self.RESET_CODE
        else:
            record.color_on = ""
            record.color_off = ""
        return super(LogFormatter, self).format(record, *args, **kwargs)


def addLogHandler(logger, conf):
    level = conf['level'].upper()
    formatter = conf['formatter']

    if conf['class'] == 'logging.StreamHandler':
        console_log_output = conf['output']
        logColor = conf['color']

        # print(f'console_log_output: {console_log_output}')
        # print(f'logColor          : {logColor}')

        console_log_output = console_log_output.lower()
        if (console_log_output == "stdout"):
            console_log_output = sys.stdout
        elif (console_log_output == "stderr"):
            console_log_output = sys.stderr
        else:
            print("Failed to set console output: invalid output: '%s'" % console_log_output)
            exit(1)
        myhandler = logging.StreamHandler(console_log_output)


    else:
        logColor = False
        filename = conf['filename']
        backupCount = conf['backupCount']
        sizePerFile = conf['sizePerFile']

        # Create log file handler
        try:
            myhandler = logging.handlers.RotatingFileHandler(
                filename, maxBytes=(sizePerFile * 1024 * 1024), backupCount=backupCount
            )

        except Exception as exception:
            print("Failed to set up log file: %s" % str(exception))
            return False

    # Set log file log level
    try:
        myhandler.setLevel(level)  # only accepts uppercase level names
    except:
        print("Failed to set log file log level: invalid level: '%s'" % level)
        return False

    myformatter = LogFormatter(fmt=formatter, color=logColor)
    myhandler.setFormatter(myformatter)
    logger.addHandler(myhandler)


class Config():

    # def __init__(self, config_file):
    def __init__(self):

        self.config = self.load_config()

        logger = logging.getLogger()

        # Set global log level to 'debug' (required for handler levels to work)
        logger.setLevel(logging.DEBUG)
        logger.handlers = []
        # logger.propagate = False

        for i in self.config['logging']['root']['handlers']:
            addLogHandler(logger, self.config['logging']['handlers'][i])

    """
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value
    """

    # def load_config(self, config_file):
    def load_config(self):
        system_config_file = f"{project.root()}{os.sep}config.yaml"
        user_config_file = f"{os.getenv('APPDATA')}{os.sep}{{cookiecutter.project_name}}{os.sep}config.yaml"
        config_file = ''

        if os.path.isfile(user_config_file) and os.access(user_config_file, os.R_OK):
            config_file = user_config_file
        else:
            if os.path.isfile(system_config_file) and os.access(system_config_file, os.R_OK):
                logging.warning(f'No user config file in {user_config_file} was found!')
                logging.warning(f'Using system config file "{system_config_file}"')
                config_file = system_config_file
            else:
                logging.error(f'No system config file in {system_config_file} was found!')
                exit()

        try:
            with open(config_file, 'r') as stream:
                config = yaml.load(stream)

        except yaml.YAMLError as e:
            logging.error("Could not load configuration file. Error: {}".format(e))
            exit(1)
        except FileNotFoundError as e:
            logging.error('Configuration file full path: {}'.format(os.path.abspath(config_file)))
            logging.error("Configuration file {} could not be found. Error: {}".format(config_file, e))
            exit(1)
        except Exception as msg:
            logging.error("Error while loading configuration file {}. Error: {}".format(config_file))
            exit(1)

        logging.info("Configuration file was successfully loaded. File name: {}".format(config_file))

        return config

