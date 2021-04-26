import requests
from bs4 import BeautifulSoup

url="https://www.nytimes.com/"
response=requests.get(url)
soup = BeautifulSoup(response.content)
links=soup.find_all("a")

for each_link in links:
    if "https" in each_link.get("href"):
        print("<a href={}{}></a>".format(each_link.get("href"),each_link.text))
        