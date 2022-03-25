from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title