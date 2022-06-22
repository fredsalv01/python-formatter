import pandas as pd
import json
import os
from dotenv import load_dotenv
import requests
load_dotenv()
plates_data = pd.read_csv("ORBITEC_SIMPLIROUTE.csv")

arr = []
for plate in plates_data.Dispositivo:
    arr.append(plate)

print(arr)

URL = os.getenv('SIMPLIROUTE_URL')
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token ' + os.getenv('TOKEN')
}

response = None
try:
  response = requests.get(URL, headers=headers)
  
  if response.status_code == 200:
    print(response.json())
    print("Success")
  else:
    print("Error")
    print(response.json())
except Exception as e:
  print(e)
  print("Error")