import time
from datetime import datetime, timezone

def now() -> float:
    return time.time()

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
