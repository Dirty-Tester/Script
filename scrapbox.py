import urllib
import urllib.request, urllib.parse
import json
import datetime
projecturl = "https://scrapbox.io/api/pages/dirty-tester/?limit=1000"

req = urllib.request.Request(projecturl)
res = urllib.request.urlopen(req)
jsonData = json.loads(res.read())

def show_title_list():
    for item in jsonData["pages"]:
        title = item["title"]
        print("[" + title + "]")#コピペでリンクになるようにする。

def load_created_title_list():
    startdate = "2020/07/12"
    enddate = "2020/09/30"
    for item in jsonData["pages"]:
        title = item["title"]
        pagetime = datetime.datetime.fromtimestamp(item["created"])
        created = pagetime.strftime("%Y/%m/%d")
        if enddate > created > startdate:
            print("[" + title + "]")#コピペでリンクになるようにする。

def load_updated_title_list():
    startdate = "2020/07/12"
    enddate = "2020/09/30"
    for item in jsonData["pages"]:
        title = item["title"]
        pagetime = datetime.datetime.fromtimestamp(item["updated"])
        created = pagetime.strftime("%Y/%m/%d")
        if enddate > created > startdate:
            print("[" + title + "]")#コピペでリンクになるようにする。


#load_created_title_list()
#load_updated_title_list()
#show_title_list