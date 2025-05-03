import os
import logging
from logging.handlers import RotatingFileHandler

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logger = logging.getLogger("github_utils")
logger.setLevel(LOG_LEVEL)

ch = logging.StreamHandler()
ch.setLevel(LOG_LEVEL)
fh = RotatingFileHandler(os.getenv("LOG_FILE", "github_utils.log"), maxBytes=5_242_880, backupCount=3)
fh.setLevel(LOG_LEVEL)

formatter = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d — %(message)s"
)
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)