# https://www.w3schools.com/tags/ref_urlencode.ASP

from urllib.parse import quote

url_part = "something with spaces & and other characters!"

encoded_url_part = quote(url_part)
base_url = 'https://example.com/api/'
full_url = base_url + encoded_url_part
print(full_url)


