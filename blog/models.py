from django.db import models
from django.utils import timezone

class Post(models.Model):
#this line defines our model - it is an object
#class is a special keyword that indicates we are defining an object
#Post is the name of the model - can give it any name
#Reminder: Always start class name with an uppercase letter.
#models.Model means Post is a Django Model, so Django
##knows it should be saved in the database.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#models.ForeignKey is a link to another model.
    title=models.CharField(max_length=200)
#This is how you define text with a limited number of characters
    text=models.TextField()
#This is for long text without a limit - for things like blog posts.
    created_date=models.DateTimeField(
        default=timezone.now)
    published_date=models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    #Remember to indent your methods (def) inside your class!

    def __str__(self):
        return self.title

# Create your models here.
