import requests 
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

pixela_username = os.environ['USERNAME']
pixela_token = os.environ['TOKEN']
GRAPH_ID = "walk1"


user_params = {
  "token" : pixela_token,
  "username" : pixela_username,
  "agreeTermsOfService" : "yes",
  "notMinor" : "yes"
}

graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_config = {
  "id" : GRAPH_ID,
  "name" : "Laps Walked",
  "unit" : "Laps",
  "type" : "float",
  "color" : "momiji"
}

headers = {
  "X-USER-TOKEN" : pixela_token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{GRAPH_ID}"

today = datetime.now()


pixel_data = {
  "date" : today.strftime("%Y%m%d"),
  "quantity" : "10",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

date = "20210128"
pixel_update_endpoint  = f"{pixel_creation_endpoint}/{date}"

pixel_update_data = {
  "quantity" : "14"
}

response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
print(response.text)

pixel_deletion_endpoint = pixel_update_endpoint

# response = requests.delete(url=pixel_deletion_endpoint, headers=headers)

