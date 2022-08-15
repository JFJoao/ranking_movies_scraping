from time import sleep
from bs4 import BeautifulSoup
import requests

responde = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = responde.text

soup = BeautifulSoup(yc_web_page, "html.parser")
movies = soup.findAll(name="h3", class_="title")

list_names = []

for movie in movies:
    movie_name = movie.get_text()
    list_names.append(movie_name)

print("Top 100 movies ever! ")
print('\n' .join(list_names[::-1]))

sleep(1800)
