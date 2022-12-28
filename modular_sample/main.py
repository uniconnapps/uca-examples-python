from config import uca_client

if __name__ == '__main__':
  uca_client.auto_load_modules()
  uca_client.run_forever()