from django.db import models

# Create your models here.

class News(models.Model):
    author = models.CharField(max_length = 50)
    title = models.CharField(max_length = 100)
    date = models.DateField()
    article = models.TextField()

    def __str__(self):
        return self.title

    def seeArticle(self):
        return self.article[:10] + "..."
    