import time
import requests
from bs4 import BeautifulSoup

# ここで全て（2000件）のidを取得すればいいじゃん
def getidlist():
    target_url = "https://doda.jp/DodaFront/View/JobSearchList.action?pic=0&preBtn=3&ds=1&oc=0321M&so=50&tp=1&page=1"
    r = requests.get(target_url)

    # 検索ページ内容の取得と解析
    soup = BeautifulSoup(r.content, "html.parser")

    # 企業別ページをcompanyidに詰める
    companyid = soup.findAll("a", class_="btnJob03 _JobListToDetail")
    idlist = list()

    for id in companyid:
        idlist.append(id.attrs['href'][54:64])

    return idlist