import requests
from bs4 import BeautifulSoup
	
#r = requests.get("https://doda.jp/DodaFront/View/JobSearchDetail/j_jid__3003824339/-fm__list/-tp__1/-mtmd__0/?from=list_item")
r = requests.get("https://doda.jp/DodaFront/View/JobSearchDetail/j_jid__3003993874/-tab__jd/-fm__jobdetail/-mpsc_sid__10/-tp__1/")
	
soup = BeautifulSoup(r.content, "html.parser")
#souphead = BeautifulSoup(r, "html.parser")

#企業名取得
company = soup.find(class_ = "job_title")


#ニュース一覧のテキストのみ抽出
# print(soup.find(id="company_profile_table"))
table = soup.find("table",{"id":"company_profile_tablea"})
rows = table.findAll("tr")

#if '' in table.text:
print(rows)