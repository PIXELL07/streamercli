import time

# Store: { user: [timestamp, timestamp, ...] }
limits = {}

WINDOW_SECONDS = 10
MAX_MESSAGES = 10

def check_rate(user: str) -> bool:

    now = time.time()
    timestamps = limits.get(user, [])

    # Keep only timestamps within the last WINDOW_SECONDS
    timestamps = [t for t in timestamps if now - t < WINDOW_SECONDS]
    timestamps.append(now)

    limits[user] = timestamps

    return len(timestamps) <= MAX_MESSAGES
