from flask import Flask, render_template, request, send_file, redirect
from scrapper import search_incurit, search_work24
from file import save_to_csv

app = Flask(__name__)

db={}

@app.route("/") # 최초 루트페이지에 대한 설정 / 첫페이지 기본값?
def hello_world():
    return render_template("index.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    
    if keyword =="":
        return redirect("/")
    
    if keyword in db:
        jobs = db[keyword]

    else:
        jobs1 = search_incurit(keyword, 2)
        db[keyword] = jobs
        jobs2 = search_work24(keyword)
        job = jobs1 + jobs2
        return render_template("search.html", jobs=enumerate(job), keyword=keyword, count=len(job))

@app.route("/file")
def file():
    keyword = request.args.get("keyword")

    if keyword == "":
        return redirect("/")
    
    if keyword in db:
        jobs = db[keyword]
    
    else:
        jobs = search_incurit(keyword, 2)
        save_to_csv(jobs)
        return send_file("./downloads.csv", as_attachment=True)



if __name__ == '__main__':
    app.run()