from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}


@app.route("/")
def serve_home_page():
    return "<h1>Hello there</h1>"


@app.route("/about")
def serve_about_page():
    return """
    <h1>Joseph Choi</h1>
    <hr/>
    <p>phone: 01068613003</p>
    <p>email: joseph@hosepjasdf.com</p>
    <hr/>
    """


@app.route("/movie", methods=["POST"])
def get_movie_data():
    movie_url = request.form["movie_url"]
    data = requests.get(
        movie_url,
        headers=headers,
    )

    soup = BeautifulSoup(data.text, "html.parser")
    items = soup.select(".ipc-metadata-list__item")
    info = {}
    for item in items:
        text = item.text
        if "Director" in text:
            director = item.select_one("a").text
            info["director"] = director
        elif "Writers" in text:
            writers = item.select("a")
            writer_names = []
            for writer in writers:
                writer_names.append(writer.text)
            info["writers"] = writer_names
        elif "Stars" in text:
            stars = item.select("a")
            star_names = []
            for star in stars:
                star_name = star.text
                if star_name != "" and star_name != "Stars":
                    star_names.append(star_name)
            info["stars"] = star_names
    return info


app.run("0.0.0.0", port=5000, debug=True)
