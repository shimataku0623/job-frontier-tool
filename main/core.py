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
#td = rows[1].find("td")

print(company.text)
# print(rows[1].find("td").text) #住所
# print(rows[-1].find("td").text) #URL
#print(rows[6].find("td").text) #売上
#print(rows[4].find("td").text) #社員数
#企業によって数が違う8がないことも

# print(rows[1].text)
# print("所在地" in rows[1].text)

# 出力変数の初期化
address,url,amount,employees = "","","",""

#合致するか確かめながらそれぞれ値を代入
for item in rows:
    if "所在地" in item.text:
        address = item.find("td").text
    if "企業URL" in item.text:
        url = item.find("td").text
    if "売上高" in item.text:
        amount = item.find("td").text
    if "従業員数" in item.text:
        employees = item.find("td").text

print("住所:",address)
print("URL:",url)
print("売り上げ:",amount)
print("従業員数:",employees)