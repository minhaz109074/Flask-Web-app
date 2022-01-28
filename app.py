# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:39:09 2022

@author: Minhazul Abedin
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/h1/')
def who():
    return render_template("output.html")



if __name__ == "__main__":
    app.run(debug=True)