import sys
import os
from logging import DEBUG, Formatter, StreamHandler, getLogger

def setup_logger():
    logger = getLogger(__name__)
    logger.setLevel(DEBUG)

    handler = StreamHandler(sys.stdout)
    level = "INFO" if os.environ.get("GENERATOR_LOG_LEVEL") else "DEBUG"
    handler.setLevel(level)

    formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    handler.setFormatter(formatter)
    logger.addHandler(handler)

setup_logger()



