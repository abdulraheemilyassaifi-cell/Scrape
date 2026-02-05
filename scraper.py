import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# ٹارگٹ یو آر ایل (TechCrunch Funding Section)
URL = "https://techcrunch.com/category/venture/"

def scrape_funding_news():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('div', class_='post-block')

    leads = []
    keywords = ['CRM', 'SaaS', 'Sales', 'Customer', 'Marketing']

    for article in articles:
        title = article.find('a', class_='post-block__title__link').text.strip()
        link = article.find('a', class_='post-block__title__link')['href']
        
        # صرف متعلقہ خبریں فلٹر کریں
        if any(word.lower() in title.lower() for word in keywords):
            leads.append([datetime.now().strftime("%Y-%m-%d"), title, link])

    # ڈیٹا کو CSV فائل میں محفوظ کریں
    with open('crm_leads.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(leads)

if __name__ == "__main__":
    scrape_funding_news()
