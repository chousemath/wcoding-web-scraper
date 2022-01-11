import requests

data = requests.post(
    "http://192.168.2.112:5000/movie",
    json={
        "movie_url": "https://www.imdb.com/title/tt0167260/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=9703a62d-b88a-4e30-ae12-90fcafafa3fc&pf_rd_r=9W1DK9D4990BJHF0EAHS&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_7"
    },
)

print(data.text)
