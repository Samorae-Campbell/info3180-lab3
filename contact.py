#! /usr/bin/env python
import os
from flask import render_template
from flask import Flask
from app import app
import time

@app.route("/contact")
def profile():
  return render_template('contact.html')

def timeinfo():
  now = time.strftime("%c")
  # now = "Time: "+time.strftime("%I:%M:%S")+" "+time.strftime("%A %d/%m/%Y")
  now = "Date: "+time.strftime("%A %d/%b/%Y")
  # name = "Samorae"
  # 12-hr time format -- print (time.strftime("%I:%M:%S"))
  # 12-hr time format -- print (time.strftime("%d/%m/%Y"))
  # return render_template('profile.html', name=name)
  return now

app.run(debug=True,host="0.0.0.0",port=8080)