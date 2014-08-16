from django.core.management.base import BaseCommand, CommandError
from books.models import RSSEntry
import feedparser

class Command(BaseCommand):
    help = 'Add feed from source file to database'

    def add_arguments(self, parser):
        # parser.add_argument('source_file', nargs='+', type=str)
        pass

    def handle(self, *args, **options):
        
        url = "http://www.leiphone.com/feed"
        feed = feedparser.parse(url)
        items = feed['items']
        if len(items) == 0:
            print("http error: " + str(feed['bozo_exception']))
            return
            
        for item in items:
            entry = RSSEntry()
            entry.title = item.title
            entry.source_site = url
            entry.summary = item.summary
            #entry.publication_date = item.updated
            entry.link = item.link
            entry.save()