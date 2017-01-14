import requests
from bs4 import BeautifulSoup

year=input("enter year")
month=input("enter month")
day=input("enter day")

req_url="http://www.datetime.io/age/"+str(year)+"/"+str(month)+"/"+str(day)

html= (requests.get(req_url)).content
soup=BeautifulSoup(html,"lxml")

print '\n'+soup.h2.text
print soup.p.text
