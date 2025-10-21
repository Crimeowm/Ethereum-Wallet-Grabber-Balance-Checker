import logging
import sys


class Logger():

    def __init__(self, name='logs', level=logging.DEBUG, FORMATTER=None):
        FORMATTER = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s") if not FORMATTER else FORMATTER
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        fh = logging.FileHandler('%s.log' % name, 'a')
        fh.setFormatter(FORMATTER)
        self.logger.addHandler(fh)

        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(FORMATTER)
        self.logger.addHandler(sh)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)
