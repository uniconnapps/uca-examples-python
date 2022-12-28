from config import uca_client
import datetime

@uca_client.action
def get_current_time() -> str:
  return datetime.datetime.now().isoformat()

  