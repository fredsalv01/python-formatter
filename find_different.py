from dotenv import load_dotenv
import pandas as pd, os, requests

load_dotenv()

TOKEN = os.getenv('TOKEN')
URL = os.getenv('SIMPLIROUTE_URL')
PLATES_DATA = pd.read_csv(os.getenv('PLATES_DATA'))

plates_list = []
response_list = []
plates_not_in_response = []

for plate in PLATES_DATA.Dispositivo:
    plates_list.append(plate.replace('-', '').upper())

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Token {TOKEN}'
}

try:
    request = requests.get(URL, headers=headers)

    if request.status_code == 200:
        raw_data = request.json()

        for item in raw_data:
            response_list.append(item['reference_id'])
except Exception as e:
    print("Error")
    print(e)

for plate in plates_list:
    if plate not in response_list:
        plates_not_in_response.append(plate)

print(f'Plates list from csv: {plates_list}')
print(f'Plates list from response: {response_list}')
print(f'Plates in csv that not appear in response: {plates_not_in_response}')
