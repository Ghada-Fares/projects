import requests
from bs4 import BeautifulSoup
l_link = []
l_name = []
l_befor = []
l_after= []
url="https://www.kabbanifurniture.com/collections/%D8%B1%D9%83%D9%86%D8%A7%D8%AA-g"
page = requests.get(url).content
soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())
##links of all bedrooms
links = soup.find_all('div',{'class':'grid-view_image'})
for link in links:
    l = link.a.attrs['href']
    l = "https://www.kabbanifurniture.com" + l
    l_link.append(l)
#names of all bedrooms
names = soup.find_all('div',{'class':'details'})
for name in names:
    n = name.a.text
    l_name.append(n)
#price of all bedrooms befor discount
b_prices = soup.find_all('div', {'class': 'grid-view-item__meta'})
for b_price in b_prices:
    b = b_price.s.text
    l_befor.append(b)
#price after all bedrooms discount
a_prices = soup.find_all('span', {'class': 'product-price__price product-price__sale'})
for a_price in a_prices:
    a = a_price.text
    l_after.append(a)
#visualize data that were scraped
for i in range(len(l_link)):
    print("the name of rokna : ",l_name[i])
    print("     ")
    print("the link of rokna : ",l_link[i])
    print("     ")
    print("the price before discount of rokna : ",l_befor[i])
    print("     ")
    print("the price after the discount of rokna : ",l_after[i])
    print("     ")
    print("***************************************************")
    print("     ")





