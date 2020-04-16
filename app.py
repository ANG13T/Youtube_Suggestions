from flask import Flask, render_template
from youtube_api import YoutubeDataApi
from youtube import getVideoData


app = Flask(__name__)

@app.route('/')
def sayHello():
    return render_template("index.html")

# @app.route('/about')
# def about():
#     return render_template("about.html")

@app.route('/suggestions')
def about():
    return render_template("suggestions.html")

@app.route('/stocism')
def suggestions():
    searchData = getVideoData('stocism')
    return render_template("videoLayout.html", results=searchData, title="Stocism")

@app.route('/philosophy')
def philosuggestions():
    searchData = getVideoData('philosophy')
    return render_template("videoLayout.html", results=searchData, title="Philosophy")

@app.route('/motivation')
def motivsuggestions():
    searchData = getVideoData('motivation')
    return render_template("videoLayout.html", results=searchData, title="Motivation")

@app.route('/inspiration')
def insipsuggestions():
    searchData = getVideoData('inspirational')
    return render_template("videoLayout.html", results=searchData, title="Inspirational")

@app.route('/productivity')
def producsuggestions():
    searchData = getVideoData('productivity')
    return render_template("videoLayout.html", results=searchData, title="Productivity")

@app.route('/business')
def businesssuggestions():
    searchData = getVideoData('business')
    return render_template("videoLayout.html", results=searchData, title="Business")


if __name__ == "__main__":
    app.run(debug=True)