from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap
import SesSozcuk as sessozcuk


app = Flask(__name__)
Bootstrap(app)


@app.route("/",methods = ("GET","POST"))
def index(): 
    if request.method == "POST":
       
        ses2text = sessozcuk.recognizer()

        if request.form.get("text"):
            prevyazi = request.form.get("text")
        else:
            prevyazi = ""
    
        return render_template("index.html", message = prevyazi + ses2text)
    else:
        return render_template("index.html")
 

if __name__=="__main__":
    app.run(debug = True)
