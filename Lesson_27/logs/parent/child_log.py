import logging

# Create a child logger
child_logger = logging.getLogger('Main.child')


def child_call():
    child_logger.info('This is child call')
