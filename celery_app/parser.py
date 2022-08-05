import requests
import django
from bs4 import BeautifulSoup as bs
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dz11_annotate_aggregate.settings")
django.setup()
from celery_app.models import Author, Quote


def parser_qoutes():
    url = 'https://quotes.toscrape.com'
    NEXT = True
    all_qoutes = []
    while NEXT:
        r = requests.get(url)
        soup = bs(r.text, 'lxml')
        all_qoutes.extend(soup.find_all('div', class_='quote'))
        if not soup.find('li', class_='next'):
            print('parser success')
            NEXT = False
        else:
            url = 'https://quotes.toscrape.com' + soup.find('li', class_='next').a.get('href')


    counter = 0
    for i in all_qoutes:
        qoute = i.find('span', class_='text').text.strip()
        author = i.find('small', class_='author').text.strip()
        url_author = 'https://quotes.toscrape.com' + i.find('a').get('href')
        r = requests.get(url_author)
        soup = bs(r.text, 'lxml')
        born = soup.find('span', class_='author-born-date').text.strip()
        country = soup.find('span', class_='author-born-location').text.strip()
        description = soup.find('div', class_='author-description').text.strip()
        author_obj, created = Author.objects.get_or_create(name=author, born=born, country=country, description=description)
        qoute_obj, created_q = Quote.objects.update_or_create(quote=qoute, author_id=author_obj.id)
        total_qoutes = Quote.objects.count()
        if created_q:
            counter += 1
            if counter == 5:
                print('added 5 qoutes !')
                print('Total qoutes -----', total_qoutes)
                NEXT = False
                break
