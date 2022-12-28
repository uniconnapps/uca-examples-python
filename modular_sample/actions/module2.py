from config import uca_client
import time

@uca_client.action
def Wow() -> dict[str,str]:
  time.sleep(1)
  return {"message": "Yes its a wow", "status": "Ok" }