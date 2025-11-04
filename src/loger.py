import logging
import os
from datetime import datetime

# Log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Logs folder path
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] [ %(levelname)s ] [ %(name)s ] [ line:%(lineno)d ] - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    print("Logging has started")          # Terminal 
    
    logging.info("Logging has started")   # Log file 

# Example test log
logging.info("Logging system successfully configured!")
