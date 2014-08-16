from django.conf.urls import include, url
from django.contrib import admin
from books.views import list_rss, demo


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/rss/', list_rss),
    url(r'^demo/', demo),
]
