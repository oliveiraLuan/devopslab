from flask import Flask

#Simple Flask app
app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
