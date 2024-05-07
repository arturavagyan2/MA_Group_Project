import os
import logging
from logging.handlers import RotatingFileHandler


class CustomFormatter(logging.Formatter):
    """
    Custom formatter for informative logging with colored output.
    """
    grey = "\x1b[38;20m"
    violet = "\x1b[38;5;183m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    format = "%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - (%(message)s) - line: %(lineno)d"  # noqa: E501
    datefmt = "%Y-%m-%d %H:%M:%S"
    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: violet + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        """
        Format the log record with colors based on the logging level.

        Parameters:
        ----------
        record : logging.LogRecord
            The log record to format.

        Returns:
        -------
        str
            The formatted log record with ANSI color codes.
        """
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt=self.datefmt)
        return formatter.format(record)


if __name__ == '__main__':
    logger_name = os.path.splitext(os.path.basename(__file__))[0]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)

    fh = RotatingFileHandler(f"{logger_name}.log", maxBytes=10240, backupCount=3)  # noqa: E501
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(CustomFormatter())
    logger.addHandler(fh)

    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
