import urllib
import urllib.request, urllib.parse
import json
import datetime

import pandas as pd

projecturl = "https://scrapbox.io/api/pages/dirty-tester/?limit=1000"

req = urllib.request.Request(projecturl)
res = urllib.request.urlopen(req)
jsonData = json.loads(res.read())


if __name__ == "__main__":
    scrap_data = pd.json_normalize(jsonData, record_path='pages')
    scrap_bool1 = (scrap_data["user.id"] == '5c8d0988d52c3100174cd0d2')
    scrap_bool2 = (scrap_data["user.id"] == '5e744f3760095e0017e4ec9c')
    scrap_bool3 = (scrap_data["user.id"] == '5e74530b2e5c97001785d3a6')
    print(str("Created by Yamashita == ") + str(scrap_bool1.sum()))
    print(str("Created by Inoue     == ") + str(scrap_bool2.sum()))
    print(str("Created by Yamaguchi == ") + str(scrap_bool3.sum()))
