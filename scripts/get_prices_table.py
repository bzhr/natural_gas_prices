import requests
from bs4 import BeautifulSoup as bs

daily_prices_url = 'http://www.eia.gov/dnav/ng/hist/rngwhhdD.htm'

s = requests.session()

r = s.get(daily_prices_url)
soup = bs(r.content)
table = soup.find("table", {"summary" : "Henry Hub Natural Gas Spot Price (Dollars per Million Btu)"})
with open("data/html_table.txt", "w") as f:
    f.write(str(table))
    