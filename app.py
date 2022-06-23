from typing import List
from dotenv import load_dotenv
import pandas as pd, json, os, requests

load_dotenv()

TOKEN = os.getenv('TOKEN')
URL = os.getenv('SIMPLIROUTE_URL')
PLATES_DATA = pd.read_csv(os.getenv('PLATES_DATA'))

plates = []
formatted_plates = []
plates_list = []

for plate in PLATES_DATA.Dispositivo:
    plates.append(plate)
    formatted_plates.append(plate.replace('-', '').upper())

    plates_list.append({
        'plate': plate,
        'formatted_plate': plate.replace('-', '').upper()
    })

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Token {TOKEN}'
}

plates_response = []

try:
    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        raw_data = response.json()

        for item in raw_data:
            for plate in plates_list:
                if plate['formatted_plate'] == item['reference_id']:
                    plates_response.append({
                        'orbitec_plate': plate['plate'],
                        'simpliroute_id': item['id'],
                        'simpliroute_name': item['name'],
                        'simpliroute_reference_id': item['reference_id']
                    })

        with open('plates_response.json', 'w') as f:
            json.dump(plates_response, f)

    else:
        print("Error")
        print(response.json())
except Exception as e:
    print(e)
    print("Error")
