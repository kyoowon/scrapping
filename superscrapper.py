from flask import Flask, render_template, request, redirect, send_file # Flask : @app과 같은 기본적인 프레임워크, render_template : 랜터링하여 따로 탬플릿을 통해 인터페이스 설정request : report의 단어를 뽑기 위해서 
from saramin import  get_jobs
from save import save_to_file

app = Flask("SuperScrapper")

db = {}

@app.route("/") # @은 데코레이터 요청이 오면 바로 밑에 함수를 통해 꾸며준다.
def home():
	return render_template("potato.html")

@app.route("/report")
def report():
	word = request.args.get('word')
	if word:
		word = word.lower()
		existingJobs = db.get(word)
		if existingJobs:
			jobs = existingJobs
		else:
			jobs = get_jobs()
			db[word] = jobs
	else:
		return redirect("/")
	return render_template("report.html", searchingBy = word, resultsNumber = len(jobs), jobs = jobs)


@app.route("/export")
def export():
	try:
		word = request.args.get('word')
		if not word:
			raise Exception()
		word = word.lower(word)
		jobs = db.get(word)
		if not jobs:
			raise Exception()
		save_to_file(jobs)
		return send_file("jobs.csv")
	except:
		return redirect("/")


app.run(host="127.0.0.1")