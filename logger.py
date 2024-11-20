
import logging

logging.basicConfig(filename="server.log", level=logging.INFO)
logger = logging.getLogger("fastapi")
logger.info("server starting...")
