import requests
import os
from dotenv import load_dotenv
import json
load_dotenv()


url = 'https://api.devrev.ai/dev-users.self'
# url='https://api.devrev.ai/works.create'
headers = {
    'Authorization': str(os.getenv("api_key"))
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # You can access the response content with response.text
    print(json.loads(response.text))
else:
    print(f'Request failed with status code {response.status_code}')

