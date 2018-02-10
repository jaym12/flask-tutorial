import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.etsy.com/listing/554073851/valentines-day-gift-rose-necklace-rose?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-2&plkey=856e9c0153ef4b3b97e572764d2aca28d7635410:554073851")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "listing-price", "class": "vertical-align-middle"})


#print(soup.prettify())
print(element.text.strip())
#print(request.content)