import requests
from bs4 import BeautifulSoup

# 出力変数の初期化
company,address,url,amount,employees = "","","","",""

# 該当企業の読み込み（別ファイルで取得した方がいいかも）
r = requests.get("https://doda.jp/DodaFront/View/JobSearchDetail/j_jid__3003824339/-fm__list/-tp__1/-mtmd__0/?from=list_item")

# ページ内容の取得と解析
soup = BeautifulSoup(r.content, "html.parser")

# 企業情報該当テーブルの特定
table = soup.find("table",{"id":"company_profile_table"})
rows = table.findAll("tr")

# 欲しい情報を文字列検索しながら変数に代入
for item in rows:
    if "所在地" in item.text:
        address = item.find("td").text
    if "企業URL" in item.text:
        url = item.find("td").text.strip()
    if "売上高" in item.text:
        amount = item.find("td").text
    if "従業員数" in item.text:
        employees = item.find("td").text

# 企業名取得
company = soup.find(class_ = "job_title").text

# 出力
print("企業名:",company)
print("住所:",address)
print("URL:",url)
print("売り上げ:",amount)
print("従業員数:",employees)