from django.db import models

class Blog (models.Model):
    title = models.CharField(max_length=100)
    sub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='')

    def __str__ (self):
        return self.title

    def summary (self):
        return self.body[:100]

    def sub_date_short (self):
        return self.sub_date.strftime('%b %e %Y')
