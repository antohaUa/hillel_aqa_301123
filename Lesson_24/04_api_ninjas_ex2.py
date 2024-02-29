import requests
import json
from ninja_secrets import API_KEY

url = 'https://api.api-ninjas.com/v1/cats'


# abyssinian
# ?name=

def get_cats():
    try:
        headers = {'X-Api-Key': API_KEY}
        params = {'name': 'abyssinian'}
        params2 = {'grooming': 3}
        response = requests.get(url, params=params2, headers=headers)
        response.raise_for_status()
        # print(response.status_code)
        cats_list = response.json()

        for curr_cat in cats_list:
            print(curr_cat["image_link"])
            # with open(f'{curr_cat["name"]}.jpg', 'wb') as cat_fh:
            #     cat_image = requests.get(curr_cat["image_link"])
            #     cat_fh.write(cat_image.content)

        # with open('cats.json', 'wt') as c_fh:
        #     json.dump(cats_dict, c_fh, indent=4)
    except requests.HTTPError as http_err:
        print('[HTTP ERROR BLOCK]')
        print(http_err)
    except requests.exceptions.Timeout:
        print('Timeout error')
    except requests.exceptions.TooManyRedirects:
        print('URL is bad. Too many redirects')
    except requests.exceptions.RequestException as rest_exc:
        print(rest_exc)
    finally:
        print('[THE END]')


if __name__ == '__main__':
    get_cats()
