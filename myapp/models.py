from django.db import models


# Create your models here.

# Create Categories Model...
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    # this is to show model title on Admin page..
    def __str__(self):
        return self.title


# Create Image Model...
class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    added_date = models.DateTimeField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    # this is to show model title on Admin page..
    def __str__(self):
        return self.title
