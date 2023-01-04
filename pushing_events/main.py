"""
UCA example for pushing events
"""
from uniconnapps import connector

uca_client = connector.UcaClient(
  connector_endpoint="uca://xxxxxxx.xxx",
  app_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  client_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  client_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  )

@uca_client.action
def send_sample_events() -> dict[str, str]:
    """push events while executing action"""
    uca_client.event(type="SIMPLE_EVENT_1")
    uca_client.event(type="SIMPLE_EVENT_2")
    uca_client.event(
      type="DATA_EVENT_1",
      properties={"stat_1": 9.0, "stat_2": 9, "status": "OK"}
      )
    uca_client.event(
      type="NESTED_DATA_EVENT",
      properties={
        "stat_1": 9.0,
        "stat_2": 9,
        "status": {"code": 200, "message": "OK"}
      }
      )
    return {"message": "Sample Events sent"}

if __name__ == '__main__':
    #pushing a standalone event on app start
    uca_client.event(type="APP_STARTING")
    uca_client.run_forever()
