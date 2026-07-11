import requests

from bs4 import BeautifulSoup

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}

def search_incruit(keyword, page = 1):
    
    incruit_jobs = []
    
    for i in range(page):
        page = 30 * i
        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}"
        r = requests.get(url, headers = headers) #r은 변수
        # print(r.text)
        soup = BeautifulSoup(r.text, "html.parser")
        lis = soup.find_all("li", class_="c_col")

        
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

            incruit_jobs.append(job_data)
    
    return incruit_jobs

# if __name__ == "__main__":
#     result = search_incurit("간호사", 2)
#     print(result)
#     print(len(result))


def search_work24(keyword, page):
    
    work24_jobs = []

    for i in range(1, page+ 1 ):
        url =f"https://www.work24.go.kr/cm/f/c/0100/selectUnifySearch.do?topQuerySearchArea=tb_workinfo&topQueryData={keyword}&startCount={i}"
        # url = f"https://www.work24.go.kr/cm/f/c/0100/selectUnifySearch.do?topQuerySearchArea=all&topQueryData={keyword}"
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        lis = soup.find("ul", class_="srch_list_default").find_all("li")

        for li in lis:
            company = li.find("strong", class_="b1_sb").text
            title = li.find("a", class_="btn_txt").text.strip()
            location = li.find("div", class_="vline_group").find_all("span")[4].text.strip()
            link = li.find("dd").find("a").get("href")

            job_data = {
                "company": company,
                "title": title,
                "location": location,
                "link":link
            }

            work24_jobs.append(job_data)
        
    return work24_jobs




# def search_work24(keyword):
    
#     jobs = []
#     for i in range(page):
#         page = 30 * i  
#         url = f"https://www.work24.go.kr/cm/f/c/0100/selectUnifySearch.do?topQuerySearchArea=tb_workinfo&topQueryData={keyword}
#         r = requests.get(url,headers=headers)
#         soup = BeautifulSoup(r.text, "html.parser")
#         lis = soup.find("ul", class_="srch_list_default").find_all("li")

#         for li in lis:
#             company = li.find("dl", class_= "dl_list").find("strong", class_="b1_sb").text
#             title = li.find("a", class_="btn_txt").text.strip()
#             # title = " ".join(title_tag.text.split())
#             location = li.find("div", class_="vline_group").find_all("span")[4].text.strip()
#             # location = li.find("div", class_="item").find_all("span")[0].text
#             link = li.find("dd").find("a").get("href")
#             # link = "http://www.work24.go.kr/" + li.find("dl", class_="dl_list").find("a").get("href")

#             job_data = {
#                 "company": company,
#                 "title": title,
#                 "location": location,
#                 "link":link
#             }

#         jobs.append(job_data)
    
#     return(jobs)

