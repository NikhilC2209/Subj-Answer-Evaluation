from flask import Flask, redirect, url_for, request, render_template
from pre_process import ans_dict

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/two",methods=['GET', 'POST'])
def two():
    if request.method=="POST":
        ques = request.form["ques"]
        ans = request.form["ans"]
        # print(ques)
        # print(ans)
        ans_dict(ans)
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)