import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://goodinfo.tw/tw/ShowK_Chart.asp?STOCK_ID=0050"
data={'trade_date':[],
      'opening_price':[],
      'high':[],
      'low':[],
      'closing_price':[]
      }
# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table containing the data (assuming there is one)
    table = soup.select('table#tblPriceDetail tr#row')
    
    print(table)
    for i in range(1,100):
        table = soup.select('table#tblPriceDetail tr#row{}'.format(i))
        for j in table:
            j = j.select('td')
            data['trade_date'].append(j[0].get_text())
            data['opening_price'].append(j[1].get_text())
            data['high'].append(j[2].get_text())
            data['low'].append(j[3].get_text())
            data['closing_price'].append(j[4].get_text())
            # print(j)
                # print(i.get_text())

else:
    print("Failed to fetch the webpage. Status code:", response.status_code)
print(data)