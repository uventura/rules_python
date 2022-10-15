import requests

def main(url):
    r = requests.get(url)
    return r.status_code
