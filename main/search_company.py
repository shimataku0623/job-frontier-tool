import time
import requests
from bs4 import BeautifulSoup

# ここで全て（2000件）のidを取得すればいいじゃん
# extendなら、配列が入れ子にならない
# 重複を避けたいならset使えば良さげ
def getidlist():

    # 下記のloop数を特定するための一連の流れは別関数に詰めてもいいかも

    #初期ページ
    target_url = "https://doda.jp/DodaFront/View/JobSearchList.action?pic=0&preBtn=3&ds=1&ar=3&oc=0321M&so=50&tp=1&page=1"
    r = requests.get(target_url)
    # 初期ページ内容の取得と解析
    soup = BeautifulSoup(r.content, "html.parser")
    #全体件数の取得
    search_num = soup.find("span",{"id":"res3"})
    int(search_num.replace(',', ''))
    #loop数の確定
    loop = -(-int(search_num) // 50)


    
    # 企業別ページをcompanyidに詰める
    companyid = soup.findAll("a", class_="btnJob03 _JobListToDetail")
    idlist = list()
    # idlist_dupli = list()

    for id in companyid:
        idlist.append(id.attrs['href'][54:64])

    # idlist = set(idlist_dupli)
    print("idlist:",idlist)
    print()
    return idlist