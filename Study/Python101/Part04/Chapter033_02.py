import urllib.request
import urllib.parse
import webbrowser

data = urllib.parse.urlencode({'q': 'Python'})
url = 'http://duckduckgo.com/html/'
full_url = url + '?' + data
response = urllib.request.urlopen(full_url)
with open("D:\git\Study_Python\Python101\Part04\data\\Chapter033_results.html", "wb") as f:
    f.write(response.read())

webbrowser.open("D:\git\Study_Python\Python101\Part04\data\\Chapter033_results.html")
