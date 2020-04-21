import requests
import time
import loop_dif
from bs4 import BeautifulSoup
	
idlist=list()

for i in range(1,5):
    # 取得URL
    url = "https://doda.jp/DodaFront/View/JobSearchList.action?pic=0&preBtn=3&ds=1&ar=3&oc=0321M&so=50&tp=1&page=" + str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # 企業別ページをcompanyidに詰める
    companyid = soup.findAll("a", class_="btnJob03 _JobListToDetail")

    for id in companyid:
        idlist.append(id.attrs['href'][54:64])

    print(i)
    print()
    time.sleep(1)


# idlist = set(idlist_dupli)
print("idlist:",idlist)