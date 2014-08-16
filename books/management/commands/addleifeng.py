

from django.core.management.base import BaseCommand, CommandError
from books.models import RSSEntry
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

class Command(BaseCommand):
    help = 'fetch content from leifeng'

    def add_arguments(self, parser):
        # parser.add_argument('source_file', nargs='+', type=str)
        pass

    def handle(self, *args, **options):
        
        url = "http://www.leiphone.com/page/1"
        req = urlopen(url)
        html = req.read()
        soup = BeautifulSoup(html)
        main_div = soup.find('div', 'main')
        entries = main_div.find_all(id=re.compile(r'post-\d+'))
        for entry in entries:
            a_tag = entry.find('h3').a
            
            rss = RSSEntry()
            rss.title = a_tag.text
            rss.link = a_tag['href']
            rss.summary = entry.find('div', 'text_article').find('p').text
            rss.source_site = 'http://www.leiphone.com'
            rss.publication_date = entry['data-posttime']
            
            #read content
            html = urlopen(rss.link).read()
            soup = BeautifulSoup(html)
            content_tag = soup.find('div', 'post_content')
            divs = content_tag.find_all_next('div')
            for div in divs:
                div.decompose()
                
            rss.content = str(content_tag)
            rss.save()