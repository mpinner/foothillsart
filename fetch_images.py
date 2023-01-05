import requests
import sys, os

def saveimage(url, filename, path):
    response = requests.get(url)
    destination = os.path.join(path, filename) 
    open(destination, "wb").write(response.content)
