import requests
from bs4 import BeautifulSoup


def search_incurit(keyword):
    url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"
    r = requests.get(url) #r은 변수
    # print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    lis = soup.find_all("li", class_="c_col")

    jobs = []

    for li in lis:
        company = li.find("a", class_="cpname").text
        title = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text
        location = li.find("div", class_="cl_md").find_all("span")[0].text
        link = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").get("href")
        
        job_data = {
            "company": company,
            "title": title,
            "location": location,
            "link":link
        }

        jobs.append(job_data)

    return(jobs)