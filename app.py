from flask import Flask, render_template, request, send_file, redirect
from scrapper import search_incruit, search_work24
from file import save_to_csv

app = Flask(__name__)

db={

}

page = 2

@app.route("/") 
def hello_world():
    return render_template("index.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    
    if keyword =="":
        return redirect("/")
    
    # if keyword in db:
    #     jobs = db[keyword]

    else:
        incruit = search_incruit(keyword, page)
        work24 = search_work24(keyword, page)
        # jobs = jobs1 + jobs2
        # db[keyword] = jobs
        
        
        return render_template("search.html", jobs1=enumerate(incruit), jobs2=enumerate(work24), keyword=keyword, count=len(incruit) + len(work24))

@app.route("/file")
def download_csv():

    keyword = request.args.get("keyword")
    incruit = search_incruit(keyword, page)
    work24 = search_work24(keyword, page)
    jobs = incruit + work24
    save_to_csv(jobs)

    return send_file("./downloads.csv", as_attachment=True)


if __name__ == '__main__':
    app.run()



# def file():
#     keyword = request.args.get("keyword")

#     if keyword == "":
#         return redirect("/")
    
#     if keyword in db:
#         jobs = db[keyword]
    
#     else:
#         jobs = search_incurit(keyword, 2)
#         save_to_csv(jobs)
#         return send_file("./downloads.csv", as_attachment=True)



