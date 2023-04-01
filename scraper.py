import requests
import json
from bs4 import BeautifulSoup


def get_element():
    pass

#product_code = input("Podaj kod produktu")
product_code = "100361771"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"

response = requests.get(url)

if response.status_code == requests.codes.ok:
    page_dom = BeautifulSoup(response.text, 'html.parser')
    opinions = page_dom.select("div.js_product-review")
    opinions_all = []
    for opinion in opinions:
        single_opinion = {
            "opinion_id": opinion['data-entry-id'],
            "author": opinion.select_one("span.user-post__author-name").get_text().strip(),
            "recommendation": opinion.select_one("span.user-post__author-recomendation > em").get_text().strip(),
            "score": opinion.select_one("span.user-post__score-count").get_text().strip(),
            "confirmed": opinion.select_one("div.review-pz").get_text().strip(),
            "opinion_date": opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"].strip(),
            "purchase_date ": opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"].strip(),
            "up_votes": opinion.select_one("span[id^='votes-yes']").get_text().strip(),
            "down_votes": opinion.select_one("span[id^='votes-no']").get_text().strip(),
            "content": opinion.select_one("div.user-post__text"),
            "cons": [p.get_text().strip() for p in opinion.select("div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item")],
            "pros": [p.get_text().strip() for p in opinion.select("div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item")]
        }

    

print(json.dumps(single_opinion, indent=4, ensure_ascii=False))

