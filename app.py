from flask import Flask, render_template, request
from scrapper import search_incurit, search_work24

app = Flask(__name__)

@app.route("/") # 최초 루트페이지에 대한 설정 / 첫페이지 기본값?
def hello_world():
    return render_template("index.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    print(keyword)
    jobs1 = search_incurit(keyword, 2)
    jobs2 = search_work24(keyword)
    job = jobs1 + jobs2
    print(job)
    return render_template("search.html", jobs=enumerate(job), keyword=keyword, count=len(job))

@app.route("/file")
def file():
    return "file"

if __name__ == '__main__':
    app.run(debug=True)