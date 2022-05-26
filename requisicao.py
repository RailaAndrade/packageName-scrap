#imports
from unicodedata import category
import requests
from bs4 import BeautifulSoup
import selenium
from lxml import html
import csv
#leitura do arquivo
file = open("tabela_app_profile_TOP.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []

for row in csvreader:
    rows.append(row)
file.close()
#print(rows)

url = []
#lista
length= len(rows)
#print(rows[0][0])
for i in range(length-1):
    #print(i)
    url.append('https://play.google.com/store/apps/details?id=' + rows[i][0])

#requests

for i in range(length-1):
    try:
        names = '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/c-wiz[1]/h1/span//text()'
        categories='//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/span[2]/a//text()'
        r = requests.get(url[i])
        tree = html.fromstring(r.content)
        print(tree.xpath(names)[0])
        rows[i].append(tree.xpath(names)[0])
        rows[i].append(tree.xpath(categories)[0])
        print(i)
    except:
        rows[i].append('')
        rows[i].append('')
        #print('ERRO')
        print(i)

with open('names.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['package_name', 'freq', 'name', 'category'])
    writer.writerows(rows)
