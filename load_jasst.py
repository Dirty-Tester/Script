import requests
from bs4 import BeautifulSoup

target_url = "http://www.jasst.jp/symposium/jasst20kansai/timetable.html"
rgt = requests.get(target_url)
soup = BeautifulSoup(rgt.content, "html.parser")

for element in soup.find_all("h4"):
    print(element.text)


#print(soup)
"""
for element in soup.find_all(class_="Name"):
    print(element.text)
#print(soup.find("Session"))
"""