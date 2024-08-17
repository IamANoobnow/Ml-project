'''This code sets up a system to record logs in your Python application.
The logs are saved in a file that has a name based on the exact date and time when the program starts running.
These logs will be stored in a "logs" folder within the current working directory.
The logs will include important information like when the log was made, what line of code created it, the severity of the log (INFO, ERROR, etc.), and the actual message.
This helps in tracking what your program is doing, making it easier to understand and fix issues when they arise.
This logging setup is a foundational piece in any robust Python application, as it enables developers to monitor and diagnose issues effectively.'''
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)