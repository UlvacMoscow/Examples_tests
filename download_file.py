import requests
import json


# url = 'http://www.picshare.ru/uploads/181203/8225pX0ruZ.jpg'
#url = 'https://www.expedia.com/Larnaca-Hotels-Adams-Beach-Hotel.h660276.Hotel-Information#gallery-thumbnails-content'
# url = 'http://httpbin.org/'
#url = 'http://zastavok.net/anime/46205-devushka_soldat_vintovka_anime_strelba.html'

# print( requests.request('get', url).headers )
#response = requests.get(url)

# with open('img.jpeg', 'wb') as file:
#     file.write(response.content)


import requests

url = "http://www.picshare.ru/"

payload = "adams03.jpg"
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "160ebb15-7f35-44ce-808e-48e455c0453f"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response)
