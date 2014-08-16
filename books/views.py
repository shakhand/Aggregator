from django.shortcuts import render, render_to_response
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book, RSSEntry
    
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        if books:
            return render_to_response('books/search_results.html',
                {'books': books, 'query': q})
        else:
            return render_to_response('books/search_form.html', {'infomation':'No books matched your search criteria'})
    else:
        return render_to_response('books/search_form.html', {'infomation':'Please submit a search term.'})
        
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(  cd['subject'],
                        # cd['message'],
                        # cd.get('email', 'noreply@example.com'),
                        # ['hurricane_200@163.com'],)
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm()
    return render_to_response('books/contact_form.html', {'form':form})
    
def list_rss(request):
    entries = RSSEntry.objects.all()
    return render_to_response('books/rsslist.html', {'rss_entries': entries})
    #return HttpResponse("Hello World")
        
def demo(request):
    entries = RSSEntry.objects.all()
    return render_to_response('books/demo.html', {'rss_entries': entries})
    
def greet(person_name, gretting):
    message = "%s %s" % (grettting, person_name)
    return HttpResponse(message)