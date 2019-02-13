import os
import json 
from flask import Flask, render_template

app = Flask(__name__)

"""
Routing: Allows us to switch between views using URLs 
create another template and another route
use Jinja templating

"""
@app.route('/')
def index():
    return render_template("index.html")

"""
set data on the server side and get it to come through to the client
"""
@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company_data=data)
   

@app.route('/contact')
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route('/carees.html')
def carees():
    return render_template("carees.html", page_title="Carees")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
debug=True)