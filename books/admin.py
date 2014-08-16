from django.contrib import admin
from books import models


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    ordering = ('-publication_date',)
    fields = ('title', 'authors', 'publisher','publication_date',)
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)

admin.site.register(models.RSSEntry)
admin.site.register(models.Publisher)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author, AuthorAdmin)
