import logging
import os

# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("AutonomousAgent")
logger.setLevel(logging.INFO)

# Avoid duplicate handlers when FastAPI reloads
if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler("logs/agent.log")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)