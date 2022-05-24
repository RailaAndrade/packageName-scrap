import sys
from xml.dom.minidom import Document
from selenium import webdriver
import time
import csv
from threading import Thread, Barrier
from queue import Queue


file = open("tabela_app_profile_TOP.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
newrow=[]


for row in csvreader:
    rows.append(row)

file.close()
length= len(rows)


concurrent = 5
s=1

def doWork():
  
    while True:
        url = q.get()
  
        crawl(url)
        q.task_done()
        

def crawl(myurl):
    driver = webdriver.Chrome(executable_path = r'/chromedriver')
    driver.get(myurl)
    try:
        name = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/c-wiz[1]/h1/span').get_attribute("innerHTML")
        category= driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/span[2]/a').get_attribute("innerHTML")
        newrow.append({"name":name, "category":category})
    except: 

        newrow.append({"name":'' ,"category":''})
        pass

    driver.close()

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:

    for x in range(length-1):
        lin= 'https://play.google.com/store/apps/details?id='+rows[x][0]
        q.put(lin.strip())
    q.join()
 
except KeyboardInterrupt:
    pass


document =[[]]

for m in range(length-1):


    if newrow[m]["name"]:
        rows[m].append(newrow[m]["name"])

    if newrow[m]["category"]: 
        rows[m].append(newrow[m]["category"])




with open('names.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['package_name', 'freq', 'name', 'category'])
    writer.writerows(rows)




