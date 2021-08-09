from django.db import models

# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    tool = models.CharField(max_length=30)
    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name + " " + self.last_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    rel_date = models.DateField()
    num_stars = models.IntegerField()

    rating = (
        (1,"Worst"),
        (2,"Bad"),
        (3,"Meh"),
        (4,"Good"),
        (5,"Very Good")
    )
    num_stars = models.IntegerField(choices=rating)

    class Meta:
        ordering = ['-num_stars']


    def __str__(self):
        return self.name +  " (" + str(self.rel_date) + ")"