import feedparser
from feeder import get_feed
import sqlite3 as lite

urls = get_feed()

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		link = request.form.get('link')
		title = request.form.get('title')
		con = lite.connect('read.db')
		with con:
			cur = con.cursor()
			cur.execute("INSERT INTO Read(title, link) VALUES(?, ?)", (title, link))
		return render_template('index.html', urls=urls)
	else:
		return render_template('index.html', urls=urls)

@app.route('/read', methods=["POST", "GET"])
def read():
	if request.method == 'POST':
		title = request.form.get('title')
		con = lite.connect('read.db')
		with con:
			cur = con.cursor()
			cur.execute("DELETE FROM Read WHERE title=?", (title,))
			cur.execute("SELECT * FROM Read")
			read_list = cur.fetchall()
		return render_template('read.html', read_list=read_list)
	else:
		con = lite.connect('read.db')
		with con:
			cur = con.cursor()
			cur.execute("SELECT * FROM Read")
			read_list = cur.fetchall()
		return render_template('read.html', read_list=read_list)