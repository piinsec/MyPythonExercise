import time
import sys
import os
import requests
from bs4 import BeautifulSoup 
import re
print('===========================================')
print('=                                         =')
print('= "Channel Myanmer" Adult Movies Titles   =')
print('=                                         =')
print('===========================================')
print
test = "Web Scraping Testing by Pyae Phyo Naung"

for i in test:
    time.sleep(0.03)
    sys.stdout.write(i)
print 
for pg in range(1,16):
    url = 'https://channelmyanmar.org/category/adult/page/{}/'.format(pg)
    r = requests.get(url)
    
    print('===========================================')
    print('                Page:'+str(pg)+'           ')
    print('===========================================')
    soup = BeautifulSoup(r.content, 'html.parser')
    title = soup.find_all("div", {"class":"item"})
    for i in title:
        title = i.find('h2').get_text()
        
        print(title)
