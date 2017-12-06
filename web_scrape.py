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

# The file to write scraped up stuff to 
filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

# Loops through each item 
for container in containers:
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	print("brand: " + brand)
	print("product_name: " + product_name)
	print("shipping: " + shipping) 
	#print()

	f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

# If you dont close file you cant open the file 
f.close()
