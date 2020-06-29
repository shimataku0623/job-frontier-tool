# -*- coding: utf-8 -*-
import time
import requests
from bs4 import BeautifulSoup

def getloop():
    
    #初期ページ
    target_url = "https://doda.jp/DodaFront/View/JobSearchList.action?pic=0&preBtn=3&ds=1&ar=3&oc=0321M&so=50&tp=1&page=1"
    r = requests.get(target_url)
    
    # 初期ページ内容の取得と解析
    soup = BeautifulSoup(r.content, "html.parser")
    
    #全体件数の取得
    search_num = soup.find("span",{"id":"res3"}).text
    int(search_num.replace(',', ''))

    #loop数の確定
    loop = -(-int(search_num) // 50)
    
    return loop