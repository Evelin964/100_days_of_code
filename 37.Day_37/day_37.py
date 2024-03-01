"""This is project day 37 from 100 days of code in Python by Angela Yu on Udemy
This is a project to create a habbit tracker using the pixela API
    """
    
from datetime import datetime
import requests

USER_NAME = "yourusernamehere"
TOKEN = "yourtokenhere"
GRAPH_ID = "yourgraphidhere"

pixela_endpoint = "https://pixe.la/v1/users"

see_graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1.html" #
post_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}" #.

#-----------------Create a user-----------------#
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"   
}


response = requests.post(url=pixela_endpoint, json=user_params,timeout=12)
print(response.text)

#-----------------Create a graph-----------------#
graph_params = {
    "id": GRAPH_ID,
    "name": "Km logged",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_response = requests.post(url=graph_endpoint, json=graph_params,timeout=10,headers=headers)
print(graph_response.text)


print(see_graph_endpoint)


today_date = datetime.now().strftime("%Y%m%d")
post_params = {
    "date": today_date,
    "quantity": "4.6"
}


post_pixel = requests.post(url=post_pixel_endpoint, json=post_params,timeout=10,headers=headers)
print(post_pixel.text)


#-----------------Update a pixel-----------------#




update_pixel_url = f"{post_pixel_endpoint}/{today_date}"
update_params = {
    'quantity': '0.0'  
}

update_pixel = requests.put(url=update_pixel_url, json=update_params,timeout=10,headers=headers)
print(update_pixel.text)

#-----------------Delete a pixel-----------------#
delete_pixel_url = update_pixel_url
print(delete_pixel_url)

delete_pixel = requests.delete(url=delete_pixel_url,timeout=10,headers=headers)
print(delete_pixel.text)

auto_pixel_params = {
    "date": today_date,
    "quantity": input("How many km did you run today?: ")
}

post_pixel = requests.post(url=post_pixel_endpoint, json=auto_pixel_params,timeout=10,headers=headers)
print(post_pixel.text)
