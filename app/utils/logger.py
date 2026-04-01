import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger("streamercli")

def log(msg: str):
    logger.info(msg)

def log_error(msg: str):
    logger.error(msg)
