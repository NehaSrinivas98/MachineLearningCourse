import logging
import os
from datetime import datetime
LOG_FILE_NAME = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # create the logs folder if it does not exist
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE_NAME)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    force=True,
)

logger = logging.getLogger(__name__)