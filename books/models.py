from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name
        
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __str__(self):
        return "%s %s"%(self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    
    def __str__(self):
        return self.title
        
class Site(models.Model):
    link = models.URLField()
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='sites/leifeng', null=True)
    #identifier = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
        
        
class RSSEntry(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    link = models.URLField(max_length=200)
    site = models.ForeignKey(Site, null=True)
    content = models.TextField(null=True, blank=True)
    publication_date = models. DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='sites/leifeng', null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-publication_date']
