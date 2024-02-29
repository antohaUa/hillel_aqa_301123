import requests
import json
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

# GET + parameters
# img_src
# mars_photo1.jpg

response = requests.get(url, params=params)
curr_dict = response.json()
# with open('data.json', 'wt') as dj_fh:
#     json.dump(curr_dict, dj_fh, indent=4)

for idx, curr_img_dict in enumerate(curr_dict.get('photos', []), start=1):
    #print(curr_img_dict['img_src'])
    with open(f'mars_photo{idx}.jpg', 'wb') as img_fh:
        resp_img = requests.get(curr_img_dict['img_src'])
        img_fh.write(resp_img.content)


