import time
import search_company
import requests
from bs4 import BeautifulSoup

# 該当企業の読み込み（別ファイルで取得した方がいいかも）ここも含めてループに組み込む
# 重複を避けたいならset使えば良さげ
idlist = search_company.getidlist()


for id_num in idlist:

    # 出力変数の初期化
    company,address,url,amount,employees = "","","","",""

    ur = "https://doda.jp/DodaFront/View/JobSearchDetail/j_jid__" + id_num + "/-tab__jd/-fm__jobdetail/-mpsc_sid__10/"
    r = requests.get(ur)

    # ページ内容の取得と解析
    soup = BeautifulSoup(r.content, "html.parser")

    # 企業名取得
    company = soup.find(class_ = "job_title").text.strip()

    # 企業情報該当テーブルの特定
    table_tr = soup.find("table",{"id":"company_profile_table"})
    table_dl = soup.find("div",class_="modDetail04")

    # 表の形式がtableの形の場合
    if table_tr:
        rows = table_tr.findAll("tr")
        # 欲しい情報を文字列検索しながら変数に代入
        for item in rows:
            if "所在地" in item.text:
                address = item.find("td").text.strip()
            if "企業URL" in item.text:
                url = item.find("td").text.strip()
            if "売上高" in item.text:
                amount = item.find("td").text.strip()
            if "従業員数" in item.text:
                employees = item.find("td").text.strip()

    # 表の形式がdlの形の場合
    if table_dl:
        rows = table_dl.findAll("dl")
        for item in rows:
            if "所在地" in item.text:
                address = item.find("dd").text.strip()
            if "企業URL" in item.text:
                url = item.find("dd").text.strip()
            if "売上高" in item.text:
                amount = item.find("dd").text.strip()
            if "従業員数" in item.text:
                employees = item.find("dd").text.strip()

    # 出力
    print("企業名:",company)
    print("住所:",address)
    print("URL:",url)
    print("売り上げ:",amount)
    print("従業員数:",employees)
    print()
    time.sleep(2)
