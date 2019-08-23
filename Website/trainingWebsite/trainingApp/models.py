from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_text = models.CharField(max_length=5000)
    number_of_ratings = models.IntegerField(default=0)
    rating_1 = models.IntegerField(default=0)
    rating_2 = models.IntegerField(default=0)
    rating_3 = models.IntegerField(default=0)
    mean_rating = models.DecimalField(decimal_places=3,max_digits=10)
