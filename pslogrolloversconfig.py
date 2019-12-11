import logging
from logging.handlers import RotatingFileHandler

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
fmt = logging.Formatter(fmt_str)  # what to log?

fh = RotatingFileHandler('messages.log', maxBytes=32, backupCount=5)
fh.setFormatter(fmt)

logger = logging.getLogger('intuit')
logger.setLevel(level=logging.DEBUG)
logger.addHandler(fh)
