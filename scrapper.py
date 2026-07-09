import requests
from bs4 import BeautifulSoup

keyword = "python"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"
r = requests.get(url) #r은 변수
# print(r.text)
soup = BeautifulSoup(r.text, "html.parser")
result = soup.find_all("li", class_="c_col")
print(len(result))