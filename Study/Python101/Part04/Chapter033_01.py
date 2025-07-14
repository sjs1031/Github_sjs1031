# The requests package

import requests

r = requests.get("http://www.google.com")

print(dir(r))

print(r.headers)
print(r.content)