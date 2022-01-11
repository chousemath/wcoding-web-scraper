import requests
import csv
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

data = requests.get(
    'https://www.imdb.com/chart/top/?ref_=nv_mv_250',
    headers=headers
)

soup = BeautifulSoup(data.text, 'html.parser')

table_rows = soup.select('.lister-list > tr')
# if you want to target a CSS class, use .CSS_CLASS_NAME
# if you want to target HTML tag names, just use the tag name

with open('movies.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['title', 'year', 'rating'])

    for table_row in table_rows:
        title = table_row.select_one('.titleColumn > a').text
        year = table_row.select_one('.titleColumn > span').text
        year = year.replace('(', '')
        year = year.replace(')', '')
        rating = table_row.select_one('.ratingColumn > strong').text
        # print(title, year, rating)
        writer.writerow([title, year, rating])

