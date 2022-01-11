import requests
from bs4 import BeautifulSoup
from pprint import pprint

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

data = requests.get(
    "https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=9703a62d-b88a-4e30-ae12-90fcafafa3fc&pf_rd_r=9W1DK9D4990BJHF0EAHS&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1",
    headers=headers,
)

soup = BeautifulSoup(data.text, "html.parser")

# table_rows = soup.select('.lister-list > tr')
items = soup.select(".ipc-metadata-list__item")
# ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link
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
pprint(info)
# if "Director" in text and "director" not in info:
#    list_items = item.select(".ipc-metadata-list-item__list-content-item--link")
#    for list_item in list_items:
#        info["director"] = list_item.text
#        print(list_item.text)
# print(info)
# if you want to target a CSS class, use .CSS_CLASS_NAME
# if you want to target HTML tag names, just use the tag name
