from typing import List
from dotenv import load_dotenv
import pandas as pd, json, os, requests

load_dotenv()

TOKEN = os.getenv('TOKEN')
URL = os.getenv('SIMPLIROUTE_URL')
PLATES_DATA = pd.read_csv("ORBITEC_SIMPLIROUTE.csv")

arr = []

for plate in PLATES_DATA.Dispositivo:
    arr.append(plate)

print(arr)

headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Token {TOKEN}'
}

# response = None

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
