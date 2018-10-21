import requests


def httpreq(url):
    r = requests.get(url)
    return r

try:
    r = httpreq("http://www.yahoo.co.jp")
    print(r.text)
except Exception as e:
    print("issue")
    print(e)

