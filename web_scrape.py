# Frank Anastasia 
# Web scrapping tool using beautiful soup 
# As seen on "Introduction to Web Scraping" by Data Science Dojo

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

# opening connection, grabbing the page 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# Does html parsing 
page_soup = soup(page_html, "html.parser")

# Grabs each product 
containers = page_soup.findAll("div", {"class":"item-container"})

# Loops through each item 
for container in containers:
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	producttitle_container[0].text
