#imports
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
newrow=[]
for row in csvreader:
    rows.append(row)
file.close()
print(rows)

url = []
#lista
length= len(rows)
print(rows[0][0])
for i in range(length-1):
    #print(i)
    url.append('https://play.google.com/store/apps/details?id=' + rows[i][0])

#requests
nomes=[]
for i in range(length-1):
    try:
        xpathselector = '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/c-wiz[1]/h1/span//text()'
        r = requests.get(url[i])
        tree = html.fromstring(r.content)
        nomes.append(tree.xpath(xpathselector))
        print(nomes[i])
        print(i)
    except:
        nomes.append('')
        print('ERRO')
        print(i)

