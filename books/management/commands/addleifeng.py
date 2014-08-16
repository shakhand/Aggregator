from django.core.files.base import ContentFile
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from books.models import RSSEntry, Site
from urllib.request import urlopen, pathname2url
from bs4 import BeautifulSoup
import re
import uuid

import re
from urllib import parse

def iriToUri(iri):
    items = list(parse.urlsplit(iri))
    i = 0
    for item in items:
        items[i] = parse.quote(item)
        i += 1
    return parse.urlunsplit(items)


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
            rss.site = Site.objects.get(link = 'http://www.leiphone.com/')
            rss.publication_date = entry['data-posttime']
            
            #load image
            img_link = entry.find('div', 'text_img').find('img')['src']
            self.stdout.write(iriToUri(img_link))
            img_content = urlopen(iriToUri(img_link)).read()
            file_name = uuid.uuid4().hex
            content = ContentFile(img_content)
            rss.image.save(file_name, content)
            
            #read content(
            html = urlopen(rss.link).read()
            soup = BeautifulSoup(html)
            content_tag = soup.find('div', 'post_content')
            if not content_tag:
                continue
                
            divs = content_tag.find_all_next('div')
            for div in divs:
                div.decompose()
                
            rss.content = str(content_tag)
            rss.save()