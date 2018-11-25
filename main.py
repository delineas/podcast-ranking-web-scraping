from flask import Flask, render_template
from storage import Storage

app = Flask(__name__)

@app.route("/")
def home():
    ranking = Storage.load_last_file()
    date = Storage.get_date(Storage.last_file())
    return render_template("home.html", ranking=ranking, date=date)

if __name__ == '__main__':
    app.run()