import logging

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
logging.basicConfig(level=logging.WARNING, format=fmt_str, filename='error.log')

logging.debug('debug messages')
logging.info('confirmation notes')
logging.warning('warnings messages')
# logging.error('an error information')
logging.critical('panic errors')
