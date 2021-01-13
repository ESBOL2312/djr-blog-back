from django.db import models

# Create your models here.
class author(models.Model):
    full_name = models.CharField(max_length = 100)
    def __str__(self):
        return self.full_name
class category(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class article(models.Model):
    author = models.ForeignKey(author, related_name = 'author_name', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'blog-img')
    created = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 100)
    text = models.TextField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

