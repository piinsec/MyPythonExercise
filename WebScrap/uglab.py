import requests
from bs4 import BeautifulSoup

for uid in range(500):
    url = 'http://uglab.rf.gd/data.php?id={}'.format(uid)
    r = requests.get(url, headers={'Cookie' : '__test=bc5e3d81d3d9a1d1b45da32dd0ace355; PHPSESSID=08172727d957ede1fa2399e2fe6bf972'})
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.get_text(separator=" ").split()
    print(data)
    