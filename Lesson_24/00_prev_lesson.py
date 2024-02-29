import logging

_log = logging.getLogger('DemoLog')


def get_some_ready_status(num):
    _log.info('In get_some_ready_status function')
    if num > 100:
        _log.debug("ready")
        return True
    else:
        _log.debug("Not ready")
        return False


if __name__ == '__main__':
    log_formatter = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    _log.addHandler(console_handler)
    _log.setLevel(logging.INFO)

    assert get_some_ready_status(150)
