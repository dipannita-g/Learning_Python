import requests
from datetime import date, timedelta

USERNAME = "example"
TOKEN = "exampleexample"
HEADERS = {"X-USER-TOKEN": TOKEN}
GRAPH_ID = "graph1"
TODAY = date.today().strftime("%Y%m%d")
YESTERDAY = (date.today() - timedelta(days = 1)).strftime("%Y%m%d")

#______________________________________CREATE USER____________________________________________________#
#_______________________________Needs to be done only once____________________________________________#

pixela_endpoint = "https://pixe.la/v1/users"
pixela_params = {"token": TOKEN,
          "USERNAME": USERNAME,
          "agreeTermsOfService": "yes",
          "notMinor": "yes",
          }
create_user_response = requests.post(url=pixela_endpoint, json=pixela_params)
print(create_user_response.text)

#______________________________________CREATE A GRAPH____________________________________________________#
#______________________________Needs to be done only once per habit______________________________________#

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {"id" : GRAPH_ID,
                "name": "Reading Graph",
                "unit": "Pages",
                "type": "float",
                "color": "momiji"
                }
create_graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
print(create_graph_response.text)

#________________________________________POST A PIXEL____________________________________________________#
#___________________________________Needs to be done everyday____________________________________________#

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_params = {"date": TODAY,
                "quantity": input("How many pages did you read today? "),
                }
create_pixel_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=HEADERS)
print(create_pixel_response.text)

#______________________________________UPDATE A PIXEL____________________________________________________#
#______________________________Needs to be done only when required_______________________________________#

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{YESTERDAY}"
update_pixel_params = {"quantity": "40",
                }
update_pixel_response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=HEADERS)
print(update_pixel_response.text)

#_______________________________________DELETE A PIXEL____________________________________________________#
#______________________________Needs to be done only when required________________________________________#

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

delete_pixel_response = requests.delete(delete_pixel_endpoint, headers=HEADERS)
print(delete_pixel_response.text)
