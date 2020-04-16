from flask import Flask, render_template
from youtube_api import YoutubeDataApi
from youtube import getStoicData


app = Flask(__name__)

@app.route('/')
def sayHello():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/suggestions')
def suggestions():
    searchData = getStoicData()
    return render_template("suggestions.html", results=searchData)


if __name__ == "__main__":
    app.run(debug=True)