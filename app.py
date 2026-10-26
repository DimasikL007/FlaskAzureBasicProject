from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/compare")
def compare():
    return render_template("compare.html")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.errorhandler(404)
def page_not_found(error):
    # Зберігаємо правильний HTTP-код помилки.
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run()
