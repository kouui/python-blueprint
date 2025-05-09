"""Usage:
call
```
from risk_based_auth.utils.logger import LogUtil as logging
logger = logging.setup_logger(...)
```
in main.py to setup the logger for the entire project.
and then use
```
from risk_based_auth.utils.logger import LogUtil as logging
logger = logging.get_logger()
logger.info("your log message")
logger.debug("your log message")
logger.error("your log message")
logger.warning("your log message")
```
in your library code to log the messages.
"""

import logging


class LogUtil:
    logger: logging.Logger | None = None
    log_name: str = ""

    ## wrap the logging level for convenience
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    CRITICAL = logging.CRITICAL

    @classmethod
    def _get_logger_name(cls) -> str:
        if cls.log_name:
            return cls.log_name
        from pathlib import Path

        cls.log_name = Path(__file__).parent.parent.name
        return cls.log_name

    @classmethod
    def get_logger(cls, log_name: str | None = None) -> logging.Logger:
        log_name = log_name if log_name is not None else LogUtil._get_logger_name()
        cls.logger = cls.logger if cls.logger is not None else logging.getLogger(log_name)
        return cls.logger

    @classmethod
    def setup_logger(
        cls,
        log_name: str | None = None,
        level: int = logging.DEBUG,
        log_file: str | None = None,
        log_file_level: int = logging.DEBUG,
    ) -> logging.Logger:
        """
        Setup a console/file logger with the specified log name, level and format.
        """
        """ Clear existing handler in root logger"""
        # root_logger = logging.getLogger()
        # [root_logger.removeHandler(h) for h in root_logger.handlers]

        """ customize the logger"""
        logger = logging.getLogger(log_name)
        [logger.removeHandler(h) for h in logger.handlers]
        logger.setLevel(level)

        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter(
            fmt=(
                # "[%(asctime)s][%(name)s][%(levelname)s]"
                "[%(asctime)s][%(levelname)s]"
                # "[%(filename)s][%(funcName)s][line %(lineno)d][pid %(process)d]"
                "[%(filename)s][%(funcName)s][line %(lineno)d]"
                " %(message)s"
            ),
            datefmt="%Y-%m-%d %H:%M:%S",  # .%f
        )
        ch.setFormatter(formatter)

        logger.addHandler(ch)

        """ add file handler """
        if log_file is not None:
            fh = logging.FileHandler(log_file, mode="a", encoding="utf-8")
            fh.setLevel(log_file_level)

            fh.setFormatter(formatter)

            logger.addHandler(fh)

        cls.logger = logger
        logger.info("logger initialized")
        return logger
