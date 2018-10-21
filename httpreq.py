from test import httpreq
import json

r = httpreq("https://api.github.com/repos/tjtjtjtj/go-images/branches")
with open("jsontest",mode="w") as fp:
    fp.write(r.text)
print(r.text)
