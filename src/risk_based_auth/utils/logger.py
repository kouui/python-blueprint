"""Usage:
call setup_logger() in main.py to setup the root logger
in your main script for the entire project.
and then use
import logging
logging.info("your log message")
logging.debug("your log message")
logging.error("your log message")
logging.warning("your log message")
in your library code to log the messages.
"""

import logging


def setup_logger(
    # log_name: str = "secioss_anomaly_detection",
    level: int = logging.DEBUG,
    log_file: str | None = None,
    log_file_level: int = logging.DEBUG,
):
    """
    Setup a console logger with the specified log name and level.
    """
    """ Clear existing handler in root logger"""
    root_logger = logging.getLogger()
    [root_logger.removeHandler(h) for h in root_logger.handlers]

    """ customize the logger"""
    # logger = logging.getLogger(log_name)
    logger = logging.getLogger()
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

    return None
