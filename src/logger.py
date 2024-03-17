# logging is used to track events that occur in software when it runs
# mostly used during debugging and testing
# it is used to track error or exception or information.

import logging
import os
from datetime import datetime

# Format of "log file" that will be created...
LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y_%H:%M:%S')}.log"

# path of the "log file" in current working directory...
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# create directory name "logs" and add "log files" inside it
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# set up basic configuration for logging in project
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)

if __name__ == '__main__':
    logging.info("Logging has started...")