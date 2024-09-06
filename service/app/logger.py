import logging

# TODO: Move logging to sentry
# TODO: Add levels to logging

def setup_logging(logger_name, log_file='system.log'):
    """
    Sets up logging for a given logger.

    :param logger_name: Name of the logger to be configured.
    :param log_file: Filename for the log file. Defaults to 'system.log'.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Define a custom formatter
    formatter = logging.Formatter(f'{logger_name}: %(asctime)s: %(message)s')

    # Setting the date format as per your requirement
    formatter.datefmt = '%Y-%m-%d %H:%M:%S'

    file_handler.setFormatter(formatter)

    # Clear existing handlers, if any, to avoid duplicate logging
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(file_handler)

    return logger