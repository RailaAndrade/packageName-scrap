#imports
from unicodedata import category
import requests
from bs4 import BeautifulSoup
import selenium
from lxml import html
import csv
from threading import Thread, Barrier
from queue import Queue
import time
import timeit
#leitura do arquivo

inicio = timeit.default_timer()
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
#print(rows[0][0])
for i in range(length-1):
    #print(i)
    url.append('https://play.google.com/store/apps/details?id=' + rows[i][0])

#requests
concurrent = 5
s=1
def doWork():
    
    while True:
        url = q.get()
        crawl(url)
        q.task_done()
     


def crawl(myurl):
    try:
        names = '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[1]/div/div/c-wiz/div[2]/div[1]/div/h1/span//text()'     
        r = requests.get(myurl)
        tree = html.fromstring(r.content)
        newrow.append({"name":tree.xpath(names)[0]})
        print(tree.xpath(names)[0])
    except:
        newrow.append({"name":''})
        print('ERRO')
        pass
       


q = Queue(concurrent * 2)

for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:

    for x in range(length-1):
        lin= url[x]
        q.put(lin.strip())
    q.join()
 
except KeyboardInterrupt:
    pass


print("writing")
for m in range(length-1):
    if newrow[m]["name"]:
        rows[m].append(newrow[m]["name"])


with open('names.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['package_name', 'freq', 'name'])
    writer.writerows(rows)

fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))