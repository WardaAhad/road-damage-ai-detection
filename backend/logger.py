"""
=========================================================
AI Road Damage Detection System
Professional Logger

Developer : Warda Ahad
=========================================================
"""


from pathlib import Path
import sys

from loguru import logger


from backend.config import LOG_DIR



# =========================================================
# Log File
# =========================================================

LOG_FILE = Path(LOG_DIR) / "app.log"



# =========================================================
# Remove Default Logger
# =========================================================

logger.remove()



# =========================================================
# Console Logger
# =========================================================

logger.add(

    sys.stdout,

    level="INFO",

    colorize=True,

    format=
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level}</level> | "
    "{message}"

)



# =========================================================
# File Logger
# =========================================================

logger.add(

    LOG_FILE,

    rotation="10 MB",

    retention="30 days",

    compression="zip",

    level="INFO",

    encoding="utf-8",

    enqueue=True,

    backtrace=True,

    diagnose=True,

    format=
    "{time:YYYY-MM-DD HH:mm:ss} | "
    "{level} | "
    "{message}"

)



# =========================================================
# Export Logger
# =========================================================

app_logger = logger