import os
import sys
from pathlib import Path

# This is required for how this project is structured to ensure the app and dependency
# modules available in the execution environment.
LAMBDA_TASK_ROOT = Path(os.environ["LAMBDA_TASK_ROOT"])
sys.path.append(str(LAMBDA_TASK_ROOT / "app"))
sys.path.append(str(LAMBDA_TASK_ROOT / "lib"))


from mangum import Mangum
from app import app

# This represents the value of the lambda handler setting: `lambda_handler.handler`.
handler = Mangum(app)
