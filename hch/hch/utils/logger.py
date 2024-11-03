import logging
import colorlog


class Logger():

    def __new__(cls):

        log_format = (
            '%(asctime)s - '
            '%(message)s'
        )

        logger = logging.getLogger()

        bold_seq = '\033[1m'
        colorlog_format = (
            f'{bold_seq} '
            '%(log_color)s '
            f'{log_format}'
        )
        colorlog.basicConfig(format=colorlog_format)
        colorlog.basicConfig(format=colorlog_format)

        logger.setLevel(logging.DEBUG)

        return logger
