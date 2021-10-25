from django.shortcuts import render
from . import models
def articelslist(requests):
    articels = models.articels.objects.all()
    return render(requests , 'articels1/hello.html' , {'articels':articels})





