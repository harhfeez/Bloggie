from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.
Status = ((0, "Draft"),(1,"Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    like_count = models.IntegerField(default=0)
    status = models.IntegerField(choices=Status, default=0)
    # thumbnail = models.ImageField()

    def approve_comment(self):
        return self.comments.filter(approved_comment=True)

    def publish(self):
        self.status = 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:  # Only generate slug for new objects
            random_int = random.randrange(100000000, 10000000000000000000001) * 2
            splitted_title = self.title.split(" ")
            lower_title_case = "-".join(splitted_title).lower()
            self.slug = lower_title_case + "-" + str(random_int)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

     
    class Meta:
        ordering =['-create_on']