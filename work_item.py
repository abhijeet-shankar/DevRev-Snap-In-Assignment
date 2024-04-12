import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

#loading the api key
devrev_api_key = os.getenv("api_key")


# Define the API endpoint for work creation
url_create = "https://api.devrev.ai/works.create"

# Define the API endpoint for work deletion
url_delete = "https://api.devrev.ai/works.delete"

# Define the API endpoint for getting work details
url_get = "https://api.devrev.ai/works.get"


#payload for getting/deleting the work item
# payload = {
#     "id":"ISS-17"
# }


#payload for creation of the work item
payload={
    "type":"issue",
    "applies_to_part":"PROD-1",
    "owned_by":["DEVU-1"],
    "title":"Sample Issue",
    # "priority":"p0"
}


# Definining the headers
headers = {
    'Authorization': str(os.getenv("api_key")),
    "Content-Type": "application/json"
}

# Making the POST request
response = requests.post(url_create, json=payload, headers=headers)

# # Checking the response for getting the work item details
# if response.status_code == 200:
#     print("Fetching Details..")
#     print("Details:", response.json())


# # Deleting the work item 
# if response.status_code == 200:
#     print("Work Item Deleted")


#CREATING WORK ITEM
if response.status_code == 201:
    print("Work item created successfully.")
    print("Response:", response.json())
else:
    print("Failed to create work item. Status code:", response.status_code)
    print("Error message:", response.text)
