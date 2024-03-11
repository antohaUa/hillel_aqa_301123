import logging

_log = logging.getLogger('Main')

try:
    raise ValueError('Error')
except (ValueError, PermissionError, AssertionError) as g_err:
    _log.info(g_err)
