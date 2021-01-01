from flask import Flask, render_template, request # Flask : @app과 같은 기본적인 프레임워크, render_template : 랜터링하여 따로 탬플릿을 통해 인터페이스 설정request : report의 단어를 뽑기 위해서 

app = Flask("SuperScrapper")

@app.route("/") # @은 데코레이터 요청이 오면 바로 밑에 함수를 통해 꾸며준다.
def home():
	return render_template("potato.html")

@app.route("/<username>") #<> 은 db에서 찾을 때 자주 사용
def contact(username):
	return f"Hello {username} how are you doing"

@app.route("/report")
def report():
	word = request.args.get('word')
	return render_template("reprot.html", searchingBy = word)

app.run(host="127.0.0.1")