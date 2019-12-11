import logging

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
fmt = logging.Formatter(fmt_str)  # what to log?

sh = logging.StreamHandler()  # where to log?
fh = logging.FileHandler('access.log')  # file stream
sh.setFormatter(fmt)
fh.setFormatter(fmt)

logger = logging.getLogger('intuit')
logger.setLevel(level=logging.DEBUG)
logger.addHandler(fh)
logger.addHandler(sh)
