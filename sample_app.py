from flask import Flask

app = Flask(__name__)

@app.route("/sample")
def hello_world():
    res = {
        "Message":"Hello World!!!"
    }

    return res
if __name__ == "__main__":
    app.run(port=int("3000"),debug=True)
