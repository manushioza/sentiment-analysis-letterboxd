import requests, csv
from bs4 import BeautifulSoup

url = "https://letterboxd.com/film/spider-man-no-way-home/reviews/by/activity/page/"
page_counter = 1

while True:
    res = requests.get(url + str(page_counter))
    if res.status_code == 200:
        content = res.content
        soup = BeautifulSoup(content, "html.parser").find_all(class_="hidden-spoilers expanded-text")
        with open('no_way_home_reviews.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            for r in soup:
                writer.writerow([r.text])
        f.close()
        page_counter+=1
    else:
        print(res)
        break