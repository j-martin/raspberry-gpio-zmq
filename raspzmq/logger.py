import logging


def create(name, log_path="./"):

    log_filename = log_path + name '.log'

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    console_output = logging.StreamHandler()
    console_output.setLevel(logging.DEBUG)

    file_output = logging.FileHandler(log_filename)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_output.setFormatter(formatter)
    console_output.setFormatter(formatter)

    logger.addHandler(console_output)
    logger.addHandler(file_output)

    return logger
