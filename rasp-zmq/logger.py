import logging

logger = logging.getLogger('GPIO')
logger.setLevel(logging.DEBUG)

console_output = logging.StreamHandler()
console_output.setLevel(logging.DEBUG)

file_output = logging.FileHandler(config['log_path'])
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_output.setFormatter(formatter)
console_output.setFormatter(formatter)

logger.addHandler(console_output)
logger.addHandler(file_output)
