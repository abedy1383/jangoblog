from django.shortcuts import render , HttpResponse

def abuot(requests):
    # return HttpResponse('ha im abolfazl')
    return render(requests , 'index-abuot.html')

def home(requests):
    return render(requests , 'index-home.html')