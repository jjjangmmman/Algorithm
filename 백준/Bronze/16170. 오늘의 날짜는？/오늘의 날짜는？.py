from datetime import datetime, timezone

print(datetime.now(timezone.utc).strftime("%Y\n%m\n%d"))