from django.db import models

# Create your models here.
class articels(models.Model):
    titel = models.CharField(max_length=100)
    body = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titel
    def mahodit(self):
        return self.body[0:50] + ' ....'
    

