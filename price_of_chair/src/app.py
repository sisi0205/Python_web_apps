import requests
from bs4 import BeautifulSoup

requests = requests.get("https://www.johnlewis.com/house-by-john-lewis-whistler-dining-chair/white/p4843125")
content = requests.content

soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price price--large"})
string_price = element.text.strip() #£99.00
price = float(string_price[1:])

print(price < 200)

# < p
# class ="price price--large" > £99.00
# < / p >
print(requests.content)