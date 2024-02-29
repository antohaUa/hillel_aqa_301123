import requests
import urllib.parse

url = 'http://127.0.0.1:8080'
image_name = 'mars_photo_1.jpg'

with open(image_name, 'rb') as fh:
    files = {'image': fh}
    response = requests.post(f'{url}/upload', files=files)
    print(response.status_code)
    print(response.text)
#
headers = {'Content-Type': 'text'}
encoded_part = urllib.parse.quote(image_name)
print(encoded_part)
response = requests.get(f'{url}/image/{encoded_part}', headers=headers)
print(response.status_code)
print(response.text)

response = requests.delete(f'{url}/delete/{encoded_part}')
print(response.status_code)
print(response.text)


#
#
