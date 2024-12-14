import requests
import psutil
import time
import json

def fetchWinInfo():
      cpu_utilization = psutil.cpu_percent(interval=1)
      ram_information = psutil.virtual_memory()
      ram_utilization = ram_information.percent
      
      winInfo = {
            "cpuPercent" : str(cpu_utilization),
            "ramPercent" : str(ram_utilization),
            "ramInfo" : str(ram_information),
      } 
      
      return winInfo

while True:
      log_api_url = "https://log-api.newrelic.com/log/v1" # For EU : https://log-api.eu.newrelic.com/log/v1
      api_key = "PUT_YOUR_API_KEY"

      headers = {
            'Api-key' : api_key,
            'Content-Type' : 'application/json'
      }

      log_data = {
            "timestamp" : str(int(time.time())),
            "message" : "Windows Information",
            "log" : {
                  "level" : "INFO",
                  "hostname" : "Shayan's PC",
                  "cpu_utilization" : fetchWinInfo()['cpuPercent'],
                  "ram_utilization" : fetchWinInfo()['ramPercent'],
                  "ram_information" : fetchWinInfo()['ramInfo']
            }
      }

      response = requests.post(log_api_url, headers=headers, data = json.dumps(log_data))

      if str(response.status_code)[0] == '2':
            print("SUCCESSFULL")
      else:
            print("ERROR OCCURED")
      
      time.sleep(5)
