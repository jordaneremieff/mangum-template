import os
from pathlib import Path

DEBUG = False

LAMBDA_TASK_ROOT: Path = (
    Path(os.environ["LAMBDA_TASK_ROOT"])
    if "LAMBDA_TASK_ROOT" in os.environ
    # For local testing.
    else Path(__file__).resolve().parent.parent
)

LIB_PATH = LAMBDA_TASK_ROOT / "lib"
