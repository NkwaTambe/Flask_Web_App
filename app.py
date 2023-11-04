from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"


#adding new route for json response

@app.route("/api/json")
def json():
   return jsonify({"message": " Hello jude ."})

#adding new route for an html template

@app.route("/html_template")
def template():
   return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080)

