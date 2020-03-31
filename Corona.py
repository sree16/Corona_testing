import  requests
import  bs4
import pandas as pd
from pandas.io.json import json_normalize

page = requests.get("https://www.worldometers.info/coronavirus/")

soup = bs4.BeautifulSoup(page.text,'lxml')

table = soup.find('table' , id = 'main_table_countries_today')

headers = [heading.text.replace(",Other","") for heading in table.find_all('th')]

table_rows = [row for row in table.find_all('tr')]

results = [{headers[index]:cell.text for index, cell in enumerate(row.find_all("td"))} for row in table_rows ]


Final_output = pd.json_normalize(results);
