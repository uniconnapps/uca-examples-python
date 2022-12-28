from uniconnapps import connector

uca_client = connector.UcaClient(
  connector_endpoint="uca://xxxxxxx.xxx",
  app_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  client_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  client_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  )

@uca_client.action
def addition(a:float, b: float) -> float:
  return a + b

@uca_client.action
def subtraction(a:float, b: float) -> float:
  return a - b

@uca_client.action
def multiplication(a:float, b: float) -> float:
  return a * b

@uca_client.action
def division(a:float, b: float) -> float:
  return a / b

if __name__ == '__main__':
  uca_client.run_forever()