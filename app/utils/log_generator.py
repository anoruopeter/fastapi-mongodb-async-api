import logging
from datetime import datetime
import random

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

messages = [
    "User Login",
    "Order created",
    "Paymant processed",
    "Database connection failed",
    "Disk space low"
]

levels = ["INFO", "WARNING", "ERROR"]


def generate_logs():
    for _ in range(5):

        level = random.choice(levels)
        message = random.choice(messages)

        if level == "INFO":
            logging.info(message)
        
        elif level == "WARNING":
            logging.warning(message)
        
        else:
            logging.error(message)