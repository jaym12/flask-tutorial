import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.etsy.com/listing/554073851/valentines-day-gift-rose-necklace-rose?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-2&plkey=856e9c0153ef4b3b97e572764d2aca28d7635410:554073851")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "listing-price", "class": "vertical-align-middle"})


#print(soup.prettify())
#print(element.text.strip())

product_price = element.text.strip()
price_without_symbol = product_price[1:]

#print(product_price)
price = (float(price_without_symbol))
#print(price)

product_soup = soup.find("span", {"itemprop": "name"})
product_name = product_soup.text

your_name = input("What's your name? ")
print("Here is a Valentines Day Gift suggestion for you!")
print("Product Info: ")
print(product_name)
print("The product price is {}".format(product_price))
budget = int(input("so, whats your budget? "))
if price < budget:
    print("you can afford this!")
else :
    print("Sorry {}, you can't afford this!".format(your_name))
    real_budget = int(input("Your girlfriend is worth more than that, what's your REAL budget? "))
    print(real_budget)
if price < real_budget:
    print("you can afford this, you're the best!")
else :
    print("Sorry {}, you can't afford this. Dang".format(your_name))

#print(request.content)