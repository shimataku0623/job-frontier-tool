import requests
from bs4 import BeautifulSoup
	
#r = requests.get("https://doda.jp/DodaFront/View/JobSearchDetail/j_jid__3003824339/-fm__list/-tp__1/-mtmd__0/?from=list_item")
r = requests.get("https://doda.jp/DodaFront/View/JobSearchDetail/j_jid__3003864701/-fm__list/-tp__1/-mtmd__0/?from=list_item")
	
soup = BeautifulSoup(r.content, "html.parser")
#souphead = BeautifulSoup(r, "html.parser")

#企業名取得
company = soup.find(class_ = "job_title")


#ニュース一覧のテキストのみ抽出
# print(soup.find(id="company_profile_table"))
table = soup.find("table",{"id":"company_profile_table"})
rows = table.findAll("tr")

print(rows[10])